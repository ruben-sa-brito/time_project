
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 2, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.btnList = QtWidgets.QPushButton(self.centralwidget)
        self.btnList.setObjectName("btnList")
        self.gridLayout.addWidget(self.btnList, 4, 8, 1, 1)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout.addWidget(self.btnUpdate, 3, 8, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.inputID = QtWidgets.QLineEdit(self.centralwidget)
        self.inputID.setObjectName("inputID")
        self.gridLayout.addWidget(self.inputID, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)
        self.inputName = QtWidgets.QLineEdit(self.centralwidget)
        self.inputName.setObjectName("inputName")
        self.gridLayout.addWidget(self.inputName, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setObjectName("btnRegister")
        self.gridLayout.addWidget(self.btnRegister, 1, 8, 1, 1)
        self.inputInit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputInit.setObjectName("inputInit")
        self.gridLayout.addWidget(self.inputInit, 1, 3, 1, 1)
        self.inputInitA = QtWidgets.QLineEdit(self.centralwidget)
        self.inputInitA.setObjectName("inputInitA")
        self.gridLayout.addWidget(self.inputInitA, 3, 3, 1, 1)
        self.inputEnd = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEnd.setObjectName("inputEnd")
        self.gridLayout.addWidget(self.inputEnd, 1, 5, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 5, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 6, 1, 1)
        self.inputNamep = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNamep.setObjectName("inputNamep")
        self.gridLayout.addWidget(self.inputNamep, 2, 7, 1, 1)
        self.inputValue = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValue.setObjectName("inputValue")
        self.gridLayout.addWidget(self.inputValue, 1, 7, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 9)
        self.inputEndA = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEndA.setObjectName("inputEndA")
        self.gridLayout.addWidget(self.inputEndA, 3, 5, 1, 1)
        self.inputValue2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValue2.setObjectName("inputValue2")
        self.gridLayout.addWidget(self.inputValue2, 3, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 6, 1, 1)
        self.inputIdD = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIdD.setObjectName("inputIdD")
        self.gridLayout.addWidget(self.inputIdD, 5, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionPesquisar = QtWidgets.QAction(MainWindow)
        self.actionPesquisar.setObjectName("actionPesquisar")
        self.actionAtualizar = QtWidgets.QAction(MainWindow)
        self.actionAtualizar.setObjectName("actionAtualizar")
        self.actionListar_Todos = QtWidgets.QAction(MainWindow)
        self.actionListar_Todos.setObjectName("actionListar_Todos")
        self.actionExcluir = QtWidgets.QAction(MainWindow)
        self.actionExcluir.setObjectName("actionExcluir")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "  Fim:"))
        self.btnSearch.setText(_translate("MainWindow", "Pesquisar"))
        self.label_2.setText(_translate("MainWindow", "Inicio:"))
        self.btnList.setText(_translate("MainWindow", "Listar Todos"))
        self.btnUpdate.setText(_translate("MainWindow", "Atualizar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "   Fim:"))
        self.label_5.setText(_translate("MainWindow", "     Id:"))
        self.label_6.setText(_translate("MainWindow", "Inicio:"))
        self.btnRegister.setText(_translate("MainWindow", "Cadastrar"))
        self.btnDelete.setText(_translate("MainWindow", "Deletar"))
        self.label_4.setText(_translate("MainWindow", "Nome:"))
        self.label_9.setText(_translate("MainWindow", "Valor:"))
        self.label_10.setText(_translate("MainWindow", "Valor:"))
        self.label_8.setText(_translate("MainWindow", "     Id:"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionPesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.actionAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.actionListar_Todos.setText(_translate("MainWindow", "Listar Todos"))
        self.actionExcluir.setText(_translate("MainWindow", "Excluir"))
