# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cria_testeV5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_cria_teste(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 569)
        MainWindow.setMaximumSize(QtCore.QSize(753, 569))
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
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
"    color: #c1c1c1;\n"
"    border-color: #000000;\n"
"    background-color: #232430,0.0;\n"
"\n"
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
"QPushButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
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
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #56576c;\n"
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
        self.label_TITULO.setGeometry(QtCore.QRect(80, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_TITULO.setFont(font)
        self.label_TITULO.setStyleSheet("color:rgba(30,80,159,255);\n"
"font: 12pt \"Impact\";\n"
"")
        self.label_TITULO.setObjectName("label_TITULO")
        self.Button_home = QtWidgets.QPushButton(self.frame_5)
        self.Button_home.setGeometry(QtCore.QRect(0, 0, 50, 45))
        self.Button_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_home.setStyleSheet("\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(204,204,204,255);\n"
"color: rgba(30,80,159,255);\n"
"border-radius: 10px;\n"
"    border-color: rgb(65, 65, 255);\n"
"\n"
"}\n"
"")
        self.Button_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("homenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_home.setIcon(icon)
        self.Button_home.setIconSize(QtCore.QSize(64, 50))
        self.Button_home.setObjectName("Button_home")
        self.label_43 = QtWidgets.QLabel(self.frame_5)
        self.label_43.setGeometry(QtCore.QRect(50, 0, 711, 51))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("fundo.jpg"))
        self.label_43.setObjectName("label_43")
        self.label_SubTITULO = QtWidgets.QLabel(self.frame_5)
        self.label_SubTITULO.setGeometry(QtCore.QRect(85, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_SubTITULO.setFont(font)
        self.label_SubTITULO.setStyleSheet("color:rgba(146,146,146,255);\n"
"font: 12pt \"Impact\";\n"
"")
        self.label_SubTITULO.setObjectName("label_SubTITULO")
        self.label_43.raise_()
        self.label_TITULO.raise_()
        self.Button_home.raise_()
        self.label_SubTITULO.raise_()
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
        self.Button_INFO.setGeometry(QtCore.QRect(0, 10, 50, 50))
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
        self.label_fundo.setGeometry(QtCore.QRect(0, 0, 711, 571))
        self.label_fundo.setText("")
        self.label_fundo.setPixmap(QtGui.QPixmap("fundo.jpg"))
        self.label_fundo.setObjectName("label_fundo")
        self.label_adicionar = QtWidgets.QPushButton(self.frame_4)
        self.label_adicionar.setGeometry(QtCore.QRect(30, 430, 311, 23))
        self.label_adicionar.setStyleSheet("\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(204,204,204,255);\n"
"color: rgba(30,80,159,255);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.label_adicionar.setObjectName("label_adicionar")
        self.label_nome_teste_2 = QtWidgets.QLabel(self.frame_4)
        self.label_nome_teste_2.setGeometry(QtCore.QRect(30, 240, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome_teste_2.setFont(font)
        self.label_nome_teste_2.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_nome_teste_2.setObjectName("label_nome_teste_2")
        self.label_nome_teste_3 = QtWidgets.QLabel(self.frame_4)
        self.label_nome_teste_3.setGeometry(QtCore.QRect(30, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome_teste_3.setFont(font)
        self.label_nome_teste_3.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_nome_teste_3.setObjectName("label_nome_teste_3")
        self.lineEdit_tempo = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_tempo.setGeometry(QtCore.QRect(300, 370, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_tempo.setFont(font)
        self.lineEdit_tempo.setStyleSheet("background-color: rgba(204,204,204,255);\n"
"color: rgb(11, 11, 11);")
        self.lineEdit_tempo.setObjectName("lineEdit_tempo")
        self.label_selecionar_tempo_execucao = QtWidgets.QLabel(self.frame_4)
        self.label_selecionar_tempo_execucao.setGeometry(QtCore.QRect(30, 370, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_selecionar_tempo_execucao.setFont(font)
        self.label_selecionar_tempo_execucao.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_selecionar_tempo_execucao.setObjectName("label_selecionar_tempo_execucao")
        self.lineEdit_nome_teste = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_nome_teste.setGeometry(QtCore.QRect(240, 310, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_nome_teste.setFont(font)
        self.lineEdit_nome_teste.setStyleSheet("background-color: rgba(204,204,204,255);\n"
"color: rgb(12, 12, 12);")
        self.lineEdit_nome_teste.setObjectName("lineEdit_nome_teste")
        self.comboBox_Entrada_Saida_2 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Entrada_Saida_2.setGeometry(QtCore.QRect(240, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.comboBox_Entrada_Saida_2.setFont(font)
        self.comboBox_Entrada_Saida_2.setStyleSheet("QComboBox {\n"
"\n"
"\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    box-shadow: transparent;\n"
"    padding: 4px 4px 4px 4px;\n"
"    background-color: rgb(195, 195, 195);\n"
"}")
        self.comboBox_Entrada_Saida_2.setObjectName("comboBox_Entrada_Saida_2")
        self.comboBox_Entrada_Saida_2.addItem("")
        self.comboBox_Entrada_Saida_2.addItem("")
        self.comboBox_Entrada_Saida_2.addItem("")
        self.comboBox_Entrada_Saida_2.addItem("")
        self.label_Entrada_Saida = QtWidgets.QLabel(self.frame_4)
        self.label_Entrada_Saida.setGeometry(QtCore.QRect(30, 180, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_Entrada_Saida.setFont(font)
        self.label_Entrada_Saida.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_Entrada_Saida.setObjectName("label_Entrada_Saida")
        self.comboBox_Entrada_Saida = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_Entrada_Saida.setGeometry(QtCore.QRect(240, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.comboBox_Entrada_Saida.setFont(font)
        self.comboBox_Entrada_Saida.setStyleSheet("QComboBox {\n"
"\n"
"\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    box-shadow: transparent;\n"
"    padding: 4px 4px 4px 4px;\n"
"    background-color: rgb(195, 195, 195);\n"
"}")
        self.comboBox_Entrada_Saida.setObjectName("comboBox_Entrada_Saida")
        self.comboBox_Entrada_Saida.addItem("")
        self.comboBox_Entrada_Saida.addItem("")
        self.lineEdit_nome_teste_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_nome_teste_2.setGeometry(QtCore.QRect(240, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_nome_teste_2.setFont(font)
        self.lineEdit_nome_teste_2.setStyleSheet("background-color: rgba(204,204,204,255);\n"
"color: rgb(12, 12, 12);")
        self.lineEdit_nome_teste_2.setObjectName("lineEdit_nome_teste_2")
        self.label_escolher_aplicacao = QtWidgets.QLabel(self.frame_4)
        self.label_escolher_aplicacao.setGeometry(QtCore.QRect(30, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_escolher_aplicacao.setFont(font)
        self.label_escolher_aplicacao.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_escolher_aplicacao.setObjectName("label_escolher_aplicacao")
        self.label_TITULO_2 = QtWidgets.QLabel(self.frame_4)
        self.label_TITULO_2.setGeometry(QtCore.QRect(30, 30, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_TITULO_2.setFont(font)
        self.label_TITULO_2.setStyleSheet("color:rgba(30,80,159,255);\n"
"font: 14pt \"Impact\";\n"
"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_TITULO_2.setObjectName("label_TITULO_2")
        self.label_escolher_aplicacao_2 = QtWidgets.QLabel(self.frame_4)
        self.label_escolher_aplicacao_2.setGeometry(QtCore.QRect(30, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_escolher_aplicacao_2.setFont(font)
        self.label_escolher_aplicacao_2.setStyleSheet("color: rgba(30,80,159,255);")
        self.label_escolher_aplicacao_2.setObjectName("label_escolher_aplicacao_2")
        self.lineEdit_nome_teste_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_nome_teste_3.setGeometry(QtCore.QRect(240, 130, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_nome_teste_3.setFont(font)
        self.lineEdit_nome_teste_3.setStyleSheet("background-color: rgba(204,204,204,255);\n"
"color: rgb(12, 12, 12);")
        self.lineEdit_nome_teste_3.setObjectName("lineEdit_nome_teste_3")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_TITULO.setText(_translate("MainWindow", " TESTE UNITÁRIO  EM LADDER"))
        self.label_SubTITULO.setText(_translate("MainWindow", "Utilizando OPC UA"))
        self.label_adicionar.setText(_translate("MainWindow", "+ Adicionar"))
        self.label_nome_teste_2.setText(_translate("MainWindow", "Tipo de variável"))
        self.label_nome_teste_3.setText(_translate("MainWindow", "Valor de variável"))
        self.lineEdit_tempo.setText(_translate("MainWindow", "Tempo (Segundos)"))
        self.label_selecionar_tempo_execucao.setText(_translate("MainWindow", "Selecionar tempo de execução:"))
        self.lineEdit_nome_teste.setText(_translate("MainWindow", "1 (TRUE) // 0 (FALSE)"))
        self.comboBox_Entrada_Saida_2.setItemText(0, _translate("MainWindow", "Bolean"))
        self.comboBox_Entrada_Saida_2.setItemText(1, _translate("MainWindow", "Int"))
        self.comboBox_Entrada_Saida_2.setItemText(2, _translate("MainWindow", "Float"))
        self.comboBox_Entrada_Saida_2.setItemText(3, _translate("MainWindow", "New Item"))
        self.label_Entrada_Saida.setText(_translate("MainWindow", "Entrada/Saída:"))
        self.comboBox_Entrada_Saida.setItemText(0, _translate("MainWindow", "Entrada"))
        self.comboBox_Entrada_Saida.setItemText(1, _translate("MainWindow", "Saída"))
        self.label_escolher_aplicacao.setText(_translate("MainWindow", "Nome Teste:"))
        self.label_TITULO_2.setText(_translate("MainWindow", "•  CRIAÇÃO DE TESTES UNITÁRIOS"))
        self.label_escolher_aplicacao_2.setText(_translate("MainWindow", "Nome Variável:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_cria_teste()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

