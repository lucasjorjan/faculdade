from opcua import Client
from xml.dom import minidom
import py
import time
import pytest
import Tags
import OPC as server
import homev5 as homeV5_
from importlib import reload
from classe import teste
reload(Tags)

from datetime import datetime
import xml.etree.ElementTree as ET

xmlfile = 'output.xml'
tree = ET.parse(xmlfile)
root = tree.getroot()

tam = len(root)
testcase=[tam+1]
input=[tam]
expected=[tam]
    
vet_input = []
vet_output=[]
n_output=[]
n_input=[]
id=[]
nome_teste=[]

#///////////////////Initialize///////////////////
 
tag_struct= Tags.MotorTestTags
varpath=  Tags.MotorTestpath
varpathton=  Tags.MotorTestpathton

#client = Client("opc.tcp://DESKTOP-N34O1IR:4840") 
client = Client("opc.tcp://192.168.100.72:4840") 

#root = client.get_root_node()
#cond = root.get_child(["0:Types", "0:EventTypes", "0:BaseEventType", "0:ConditionType"])
#cond.call_method("0:ConditionRefresh", ua.Variant(sub.subscription_id, ua.VariantType.UInt32))

reset_tag=tag_struct[0]
#reset_coil=tag_struct[4]
delay_time=0.05
delay_time_timer=10

#///////////////////////////////////////////////////    
#conexão inicial
def test_init_prg():
    server.OPC_Connect(client)
   # server.end_test(client,tag_struct,varpath, reset_tag)
    pytest.skip("término da comunicação")

for value in root.findall("./test-case"):
  nome_teste.append(value.attrib["name"])
linhas= []
xmlfile_ = 'linha.xml'
tree_ = ET.parse(xmlfile_)
root_ = tree_.getroot()
for elm in root_:
  value_ = elm.text
  numero_linha = value_
  if numero_linha != None:
    linhas.append(numero_linha)
#for i in range(len(linhas)):
#    @pytest.mark.parametrize("n_linha", (linhas[i]))


params = []
for i in range(len(linhas)):
    params.append(linhas[i])
@pytest.mark.parametrize("n_linha", (params))

def teste_xml(n_linha):
    tam_entrada=1
    tam_saida=1
    objects=server.getvar(client)
    for value in root.findall("./test-case"):
      id_ = int(value.attrib["id"])
      if id_ == int(n_linha) +1:          
        #id_ = id_ +1
        vet_input = []
        # tam_entrada recebe o número de entradas desse teste
        for entrada in root.findall("./test-case[@id='"+str(id_)+"']/input"): 
            tam_entrada=len(entrada)
        # é acicionado no for os valores de cada variável, nome e tempo
        #for entrada in root.findall("./test-case[@id='"+id_+"']/input/var"): 
        #   print("valor:",entrada.attrib)
        for type_tag in root.findall("./test-case[@id='"+str(id_)+"']/input/var"): 
            value = type_tag.get('value')
            name = type_tag.get('name')
            obj_time = type_tag.get('time')
            if(obj_time == None):
                obj_time= 0
            vet_input.append(teste(name,value,obj_time,nome_teste[id_-1]))
        for i in range(tam_entrada):
          server.write_opc_var(objects,varpath, vet_input[i].name, eval(vet_input[i].value))
          time.sleep(int(vet_input[i].time))
        vet_input.clear()
        # tam_saida recebe o número de saidas desse teste
        for saida in root.findall("./test-case[@id='"+str(id_)+"']/expected"): 
            tam_saida=len(saida)
        for type_tag in root.findall("./test-case[@id='"+str(id_)+"']/expected/var"): 
            value = type_tag.get('value')
            name = type_tag.get('name')
            obj_time = type_tag.get('time')
            if(obj_time == None):
                obj_time= 0
            vet_output.append(teste(name,value,obj_time,nome_teste[id_-1]))
        for elm in root.findall("./test-case[@id='"+str(id_)+"']/last_time/var"):
                now = str(datetime.now())
                elm.attrib= {'name' : 'tempo' , 'value' : now}   
        for j in range(tam_saida):
          print("name ",j,": " ,vet_output[j].name)
          data = server.read_opc_var(objects, varpath,vet_output[j].name)
          expected = eval(vet_output[j].value)
          time.sleep(int(vet_output[j].time))
          if (data == expected):
              print("teste ", id_ ," - ", nome_teste[id_ -1], " ok!")
              for elm_ in root.findall("./test-case[@id='"+str(id_)+"']/last_result/var"):
                elm_.attrib= {'name' : 'True' , 'value' : "1" }
                tree.write('output.xml')
              for elm in root.findall("./test-case[@id='"+str(id_)+"']/result/var"):
                value = elm.get('value')
                name = elm.get('name')
                value_ = int(value)
                if name == "True" :
                    value_ = value_ + 1
                    elm.attrib= {'name' : 'True' , 'value' : str(value_) }
                    tree.write('output.xml')
                    
          else:
              for elm_ in root.findall("./test-case[@id='"+str(id_)+"']/last_result/var"):
                elm_.attrib= {'name' : 'False' , 'value' : "1" }
                tree.write('output.xml')
              for elm in root.findall("./test-case[@id='"+str(id_)+"']/result/var"):
                value = elm.get('value')
                name = elm.get('name')
                value_ = int(value)
                if name == "False" :
                    value_ = value_ + 1
                    elm.attrib= {'name' : 'False' , 'value' : str(value_) }
              print("teste ", id_ ," - ", nome_teste[id_ -1], " falhou")
              print("saida", vet_output[j].name, " foi =" , data)
              print("saida esperada para ", vet_output[j].name, "era=" , expected)
              tree.write('output.xml')
          assert data == expected
        vet_output.clear()



"""
#Teste motor fechando
def test_motor_fechando():
    
    objects=server.getvar(client)
  
    
    server.write_opc_var(objects,varpath, tag_struct[0], False)
    server.write_opc_var(objects,varpath, tag_struct[4], True)
    time.sleep(delay_time_timer) # 10 segundos do timer para ai começar a fechar a porta


    server.write_opc_var(objects,varpath, tag_struct[1], False)
    data=server.read_opc_var(objects, varpath,tag_struct[2])
    assert data==1

#Teste motor abrindo

def test_motor_abrindo():
    
    objects=server.getvar(client)
    print('teste')
  
    #server.write_opc_var(objects,varpath, vet_input[0].name, eval(vet_input[0].value))
    server.write_opc_var(objects,varpath, tag_struct[0], True)
    server.write_opc_var(objects,varpath, tag_struct[1], False)
    time.sleep(delay_time)
    server.write_opc_var(objects,varpath, tag_struct[2], False)
    time.sleep(delay_time)
    data=server.read_opc_var(objects, varpath,tag_struct[3])
    assert data==1

"""

#fim da conexão
def test_u_disconnect():
    server.OPC_Disconnect(client)
    pytest.skip("término da comunicação")
