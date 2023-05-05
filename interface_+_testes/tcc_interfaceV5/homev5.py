# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeV5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import test_unit as test_unit_
from Cria_testeV5 import Ui_MainWindow_cria_teste
testev = 10
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os
from datetime import datetime
import time
from datetime import datetime
#def mudarprogressBar( self, time_):
 #       self.progressBar.setProperty("value", time_)

def adiciona_linha_xml(new_linha):
        
        xmlfile = 'linha.xml'
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        var = ET.SubElement(root, 'var')
        var.text = str(new_linha)
        tree.write(open('linha.xml', 'wb'))
def remove_linha_xml(new_linha):
        xmlfile = 'linha.xml'
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        for elm in root:
                value = elm.text
                if value == str(new_linha):
                        root.remove(elm)
        tree.write(open('linha.xml', 'wb'))
class Ui_MainWindow(object):
    def openWindow_cria_teste(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_cria_teste()
        self.ui.setupUi(self.window)
        self.window.show()    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 567)
        MainWindow.setStyleSheet(
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #232430;\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: #232430,0.0;\n"
"    color: #c1c1c1;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #ff9c2b;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #ff9c2b;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #38394e;\n"
"    color: #c1c1c1;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #4a4c68;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabWidget::pane \n"
"{ \n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    left: 5px; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    color: #c1c1c1;\n"
"    min-width: 1px;\n"
"    padding-left: 25px;\n"
"    margin-left:-22px;\n"
"    height: 28px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    color: #c1c1c1;\n"
"    font-weight: bold;\n"
"    height: 28px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!first \n"
"{\n"
"    margin-left: -20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    color: #DDD;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"    background-color: #232430,0.0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    \n"
"    background-color: rgb(175, 175, 175);\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_TITULO = QtWidgets.QLabel(self.frame_5)
        self.label_TITULO.setGeometry(QtCore.QRect(60, 0, 361, 45))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_TITULO.setFont(font)
        self.label_TITULO.setStyleSheet("color:rgba(30,80,159,255);\n"
"font: 16pt \"Impact\";\n"
"")
        self.label_TITULO.setObjectName("label_TITULO")
        self.Button_home = QtWidgets.QPushButton(self.frame_5)
        self.Button_home.setGeometry(QtCore.QRect(0, 0, 50, 45))
        self.Button_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_home.setStyleSheet("background-color: rgba(217,217,215,255);\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"")
        self.Button_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("homenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_home.setIcon(icon)
        self.Button_home.setIconSize(QtCore.QSize(64, 50))
        self.Button_home.setObjectName("Button_home")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(50, 0, 731, 51))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("fundo.jpg"))
        self.label_16.setObjectName("label_16")
        self.label_16.raise_()
        self.label_TITULO.raise_()
        self.Button_home.raise_()
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_esquedo = QtWidgets.QFrame(self.frame_2)
        self.menu_esquedo.setMinimumSize(QtCore.QSize(50, 0))
        self.menu_esquedo.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menu_esquedo.setStyleSheet("background-color: rgba(217,217,215,255);")
        self.menu_esquedo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_esquedo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_esquedo.setObjectName("menu_esquedo")
        self.Button_INFO = QtWidgets.QPushButton(self.menu_esquedo)
        self.Button_INFO.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.Button_INFO.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"")
        self.Button_INFO.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_INFO.setIcon(icon1)
        self.Button_INFO.setIconSize(QtCore.QSize(67, 50))
        self.Button_INFO.setAutoRepeatDelay(0)
        self.Button_INFO.setAutoDefault(False)
        self.Button_INFO.setObjectName("Button_INFO")
        self.horizontalLayout.addWidget(self.menu_esquedo)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_fundo = QtWidgets.QLabel(self.frame_4)
        self.label_fundo.setGeometry(QtCore.QRect(-4, -20, 711, 551))
        self.label_fundo.setText("")
        self.label_fundo.setPixmap(QtGui.QPixmap("fundo.jpg"))
        self.label_fundo.setObjectName("label_fundo")
        self.Button_Criar_teste = QtWidgets.QPushButton(self.frame_4, clicked= lambda: self.openWindow_cria_teste())
        self.Button_Criar_teste.setGeometry(QtCore.QRect(40, 320, 86, 25))
        self.Button_Criar_teste.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"border-radius: 5px;\n"
"    background-color: rgb(140, 140, 140);\n"
"}")
        self.Button_Criar_teste.setObjectName("Button_Criar_teste")
        self.label_lista_de_testes = QtWidgets.QLabel(self.frame_4)
        self.label_lista_de_testes.setGeometry(QtCore.QRect(30, 50, 191, 16))
        self.label_lista_de_testes.setMaximumSize(QtCore.QSize(276, 39))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_lista_de_testes.setFont(font)
        self.label_lista_de_testes.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_lista_de_testes.setObjectName("label_lista_de_testes")
        self.label_SubTITULO = QtWidgets.QLabel(self.frame_4)
        self.label_SubTITULO.setGeometry(QtCore.QRect(15, -10, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_SubTITULO.setFont(font)
        self.label_SubTITULO.setStyleSheet("color:rgba(146,146,146,255);\n"
"font: 13pt \"Impact\";\n"
"")
        self.label_SubTITULO.setObjectName("label_SubTITULO")
        self.Button_deletar_teste = QtWidgets.QPushButton(self.frame_4)
        self.Button_deletar_teste.setGeometry(QtCore.QRect(170, 320, 111, 25))
        self.Button_deletar_teste.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(180, 12, 0);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 29, 0);\n"
"border-radius: 5px;\n"
"}")
        self.Button_deletar_teste.setObjectName("Button_deletar_teste")
        self.Button_executar_teste = QtWidgets.QPushButton(self.frame_4)
        self.Button_executar_teste.setGeometry(QtCore.QRect(320, 320, 111, 25))
        self.Button_executar_teste.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 108, 0);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(49, 167, 17);\n"
"border-radius: 5px;\n"
"    border-bottom-color: rgb(11, 11, 11);\n"
"\n"
"}")
        self.Button_executar_teste.setObjectName("Button_executar_teste")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 550, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("QTableWidget { \n"
"  background-color: rgba(217,217,215,255);\n"
"  gridline-color:  rgb(229, 229, 229);\n"
"    gridline-color: #fffff8;\n"
"   border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgba(217,217,215,255);\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    \n"
"    background-color: rgb(140, 140, 140);\n"
"    padding: 4px;\n"
"    font-size: 9pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(55)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(37)
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setGeometry(QtCore.QRect(40, 400, 391, 23))
        self.progressBar.setStyleSheet("border-radius: 5px;\n"
"\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_teste_sendo_executado = QtWidgets.QLabel(self.frame_4)
        self.label_teste_sendo_executado.setGeometry(QtCore.QRect(470, 400, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_teste_sendo_executado.setFont(font)
        self.label_teste_sendo_executado.setStyleSheet("color: rgb(11, 11, 11);\n"
"border-radius: 5px;\n"
"")
        self.label_teste_sendo_executado.setObjectName("label_teste_sendo_executado")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.prencher_tabela()
    def prencher_tabela(self):
        xmlfile = 'output.xml'
        tree_ = ET.parse(xmlfile)
        root_ = tree_.getroot()
        cont= 0
        value_true=1
        value_false=0
        nome_teste=[]
        numero_testes=0
        porcentagem=0
        for value in root_.findall("./test-case"):
                nome_teste.append(value.attrib["name"])
                numero_testes=numero_testes+1
        for elm in root_.findall("./test-case/last_result/var"):
                name = elm.get('name')
                self.tableWidget.setItem(cont, 2, QtWidgets.QTableWidgetItem(name)) 
                cont=cont+1
        cont=0
        for elm in root_.findall("./test-case/last_time/var"):
                value = elm.get('value')
                self.tableWidget.setItem(cont, 3, QtWidgets.QTableWidgetItem(value)) 
                cont=cont+1
        for i in range(numero_testes):
                for elm in root_.findall("./test-case[@id='"+str(i+1)+"']/result/var"):
                        value = elm.get('value')
                        name = elm.get('name')
                        value_ = float(value)
                        if name == "True" :
                          value_true = value_ 
                        if name == "False" :
                          value_false = value_ 
                if value_true != "0" :
                        porcentagem = (value_true)/float(value_true+ value_false)
                        porcentagem = round(porcentagem, 5)
                        porcentagem = str(100*porcentagem) + ' %'
                        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(porcentagem)) 
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(nome_teste[i]))  
                
    def teste_linha(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_teste_sendo_executado.setText(_translate("MainWindow", "testes executados"))
        self.progressBar.setProperty("value", 50)
        os.system('python3 -m pytest  ')
        self.progressBar.setProperty("value", 100)
        self.prencher_tabela()
    def teste_barra(self):
        start = time.time()
        x=25
        if start == 1:
                self.progressBar.setProperty("value", x)
                x=x+25
        self.progressBar.setProperty("value", 100)
        _translate = QtCore.QCoreApplication.translate
    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
                linha = ix.row()
                coluna = ix.column()
                xmlfile = 'output.xml'
                adiciona_linha_xml(ix.row())
        for ix in deselected.indexes():
                linha = ix.row()
                remove_linha_xml(ix.row())
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_TITULO.setText(_translate("MainWindow", " TESTE UNITÁRIO  EM LADDER"))
        self.Button_Criar_teste.setText(_translate("MainWindow", "Criar Teste +"))
        self.label_lista_de_testes.setText(_translate("MainWindow", "Lista de Testes"))
        self.label_SubTITULO.setText(_translate("MainWindow", "Utilizando OPC UA"))
        self.Button_deletar_teste.setText(_translate("MainWindow", "Deletar Teste -"))
        self.Button_executar_teste.setText(_translate("MainWindow", "Executar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Taxa de acerto"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Resultado último teste"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Último teste"))
        self.label_teste_sendo_executado.setText(_translate("MainWindow", "Nenhum teste selecionado"))

        self.Button_executar_teste.clicked.connect(self.teste_linha)
        #self.Button_executar_teste.clicked.connect(self.teste_barra)
        
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        
    
        
import sys


def main():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        ret = app.exec_()
        # código que roda quando a aplicação fechar, onde é limpo todas linhas de teste no xml
        xmlfile = 'linha.xml'
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for i in range(len(root)):
                root.remove(root[0])
        tree.write(open('linha.xml', 'wb'))
        sys.exit(ret)
        
        #sys.exit(app.exec_())
        
if __name__ == '__main__':
   main()