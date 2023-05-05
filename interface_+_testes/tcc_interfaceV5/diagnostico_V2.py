# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telanova2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 567)
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
"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"    background-color: #232430;\n"
"    color: #c1c1c1;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #41424e;\n"
"    color: #c1c1c1;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #232430;\n"
"    border: 1px solid #37384d;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator{\n"
"    background-color: #1d1d28;\n"
"    border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator:checked{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"    background-color: #1d1d28;\n"
"\n"
"}\n"
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
        self.Button_home.setStyleSheet("\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"")
        self.Button_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("img1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_LISTATESTES_Diagnostico = QtWidgets.QLabel(self.frame_4)
        self.label_LISTATESTES_Diagnostico.setGeometry(QtCore.QRect(20, 30, 276, 39))
        self.label_LISTATESTES_Diagnostico.setMaximumSize(QtCore.QSize(276, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_LISTATESTES_Diagnostico.setFont(font)
        self.label_LISTATESTES_Diagnostico.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_LISTATESTES_Diagnostico.setObjectName("label_LISTATESTES_Diagnostico")
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 641, 381))
        self.groupBox.setStyleSheet("background-color: #232430,0.0;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_acao_nome = QtWidgets.QLabel(self.groupBox)
        self.label_acao_nome.setGeometry(QtCore.QRect(22, 20, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_acao_nome.setFont(font)
        self.label_acao_nome.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_acao_nome.setObjectName("label_acao_nome")
        self.label_inicio_duracao = QtWidgets.QLabel(self.groupBox)
        self.label_inicio_duracao.setGeometry(QtCore.QRect(180, 20, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_inicio_duracao.setFont(font)
        self.label_inicio_duracao.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_inicio_duracao.setObjectName("label_inicio_duracao")
        self.label_fim = QtWidgets.QLabel(self.groupBox)
        self.label_fim.setGeometry(QtCore.QRect(350, 20, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_fim.setFont(font)
        self.label_fim.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_fim.setObjectName("label_fim")
        self.label_status = QtWidgets.QLabel(self.groupBox)
        self.label_status.setGeometry(QtCore.QRect(500, 20, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color:rgba(30,80,159,255);\n"
"")
        self.label_status.setObjectName("label_status")
        self.Button_Detalhes1 = QtWidgets.QPushButton(self.groupBox)
        self.Button_Detalhes1.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.Button_Detalhes1.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(217,217,215,255);\n"
"border-radius: 10px;\n"
"}")
        self.Button_Detalhes1.setObjectName("Button_Detalhes1")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.verticalScrollBar.setGeometry(QtCore.QRect(620, 10, 20, 361))
        self.verticalScrollBar.setStyleSheet("")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.Button_Detalhes2 = QtWidgets.QPushButton(self.groupBox)
        self.Button_Detalhes2.setGeometry(QtCore.QRect(20, 120, 81, 31))
        self.Button_Detalhes2.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(217,217,215,255);\n"
"border-radius: 10px;\n"
"}")
        self.Button_Detalhes2.setObjectName("Button_Detalhes2")
        self.Button_Detalhes3 = QtWidgets.QPushButton(self.groupBox)
        self.Button_Detalhes3.setGeometry(QtCore.QRect(20, 170, 81, 31))
        self.Button_Detalhes3.setStyleSheet("\n"
"QPushButton::pressed\n"
"{\n"
"    \n"
"    background-color: rgb(112, 112, 112);\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgba(217,217,215,255);\n"
"border-radius: 10px;\n"
"}")
        self.Button_Detalhes3.setObjectName("Button_Detalhes3")
        self.label_data1_inicio = QtWidgets.QLabel(self.groupBox)
        self.label_data1_inicio.setGeometry(QtCore.QRect(150, 80, 111, 16))
        self.label_data1_inicio.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data1_inicio.setObjectName("label_data1_inicio")
        self.label_data2_inicio = QtWidgets.QLabel(self.groupBox)
        self.label_data2_inicio.setGeometry(QtCore.QRect(150, 130, 111, 16))
        self.label_data2_inicio.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data2_inicio.setObjectName("label_data2_inicio")
        self.label_data3_inicio = QtWidgets.QLabel(self.groupBox)
        self.label_data3_inicio.setGeometry(QtCore.QRect(150, 180, 111, 16))
        self.label_data3_inicio.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data3_inicio.setObjectName("label_data3_inicio")
        self.label_data1_fim = QtWidgets.QLabel(self.groupBox)
        self.label_data1_fim.setGeometry(QtCore.QRect(320, 80, 121, 16))
        self.label_data1_fim.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data1_fim.setObjectName("label_data1_fim")
        self.label_data2_fim = QtWidgets.QLabel(self.groupBox)
        self.label_data2_fim.setGeometry(QtCore.QRect(320, 130, 121, 16))
        self.label_data2_fim.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data2_fim.setObjectName("label_data2_fim")
        self.label_data3_fim = QtWidgets.QLabel(self.groupBox)
        self.label_data3_fim.setGeometry(QtCore.QRect(320, 180, 121, 16))
        self.label_data3_fim.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_data3_fim.setObjectName("label_data3_fim")
        self.label_PASS = QtWidgets.QLabel(self.groupBox)
        self.label_PASS.setGeometry(QtCore.QRect(490, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_PASS.setFont(font)
        self.label_PASS.setStyleSheet("    background-color: rgb(0, 170, 0);\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"border-radius: 10px;")
        self.label_PASS.setObjectName("label_PASS")
        self.label_PASS2 = QtWidgets.QLabel(self.groupBox)
        self.label_PASS2.setGeometry(QtCore.QRect(490, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_PASS2.setFont(font)
        self.label_PASS2.setStyleSheet("    background-color: rgb(0, 170, 0);\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"border-radius: 10px;")
        self.label_PASS2.setObjectName("label_PASS2")
        self.label_FAILED = QtWidgets.QLabel(self.groupBox)
        self.label_FAILED.setGeometry(QtCore.QRect(490, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_FAILED.setFont(font)
        self.label_FAILED.setStyleSheet("    \n"
"background-color: rgb(255, 0, 0);\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"border-radius: 10px;")
        self.label_FAILED.setObjectName("label_FAILED")
        self.label_fundo = QtWidgets.QLabel(self.frame_4)
        self.label_fundo.setGeometry(QtCore.QRect(-4, -20, 711, 551))
        self.label_fundo.setText("")
        self.label_fundo.setPixmap(QtGui.QPixmap("fundo.jpg"))
        self.label_fundo.setObjectName("label_fundo")
        self.label_SubTITULO = QtWidgets.QLabel(self.frame_4)
        self.label_SubTITULO.setGeometry(QtCore.QRect(15, -10, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_SubTITULO.setFont(font)
        self.label_SubTITULO.setStyleSheet("color:rgba(146,146,146,255);\n"
"font: 14pt \"Impact\";\n"
"")
        self.label_SubTITULO.setObjectName("label_SubTITULO")
        self.label_fundo.raise_()
        self.label_LISTATESTES_Diagnostico.raise_()
        self.groupBox.raise_()
        self.label_SubTITULO.raise_()
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_TITULO.setText(_translate("MainWindow", " TESTE UNITÁRIO  EM LADDER"))
        self.label_LISTATESTES_Diagnostico.setText(_translate("MainWindow", "Lista de Testes/Diagnóstico da lista"))
        self.label_acao_nome.setText(_translate("MainWindow", "Ação/Nome"))
        self.label_inicio_duracao.setText(_translate("MainWindow", "Início \n"
"Duração"))
        self.label_fim.setText(_translate("MainWindow", "Fim"))
        self.label_status.setText(_translate("MainWindow", "Status"))
        self.Button_Detalhes1.setText(_translate("MainWindow", "Detalhes"))
        self.Button_Detalhes2.setText(_translate("MainWindow", "Detalhes"))
        self.Button_Detalhes3.setText(_translate("MainWindow", "Detalhes"))
        self.label_data1_inicio.setText(_translate("MainWindow", "07/05/2022 - 1:24:33 PM"))
        self.label_data2_inicio.setText(_translate("MainWindow", "07/05/2022 - 1:24:33 PM"))
        self.label_data3_inicio.setText(_translate("MainWindow", "07/05/2022 - 1:24:33 PM"))
        self.label_data1_fim.setText(_translate("MainWindow", "07/05/2022 - 1:25:33 PM"))
        self.label_data2_fim.setText(_translate("MainWindow", "07/05/2022 - 1:25:33 PM"))
        self.label_data3_fim.setText(_translate("MainWindow", "07/05/2022 - 1:25:33 PM"))
        self.label_PASS.setText(_translate("MainWindow", "PASSED"))
        self.label_PASS2.setText(_translate("MainWindow", "PASSED"))
        self.label_FAILED.setText(_translate("MainWindow", "FAILED"))
        self.label_SubTITULO.setText(_translate("MainWindow", "Utilizando OPC UA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

