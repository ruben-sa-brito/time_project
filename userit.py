import sys
from connection import WorkHours
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Interaction(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.conexao = WorkHours()
        self.textEdit.setDisabled(True)
        self.btnRegister.clicked.connect(lambda: self.cadastroUser())
        self.btnUpdate.clicked.connect(lambda: self.attUser())
        self.btnSearch.clicked.connect(lambda: self.fucSearch())
        self.btnList.clicked.connect(lambda: self.listAll())
        self.btnDelete.clicked.connect(lambda: self.callExe())
        
    
    def cadastroUser(self):
        
        try:
            self.conexao.inserir(self.inputName.text(), self.inputInit.text(), self.inputEnd.text(), self.inputValue.text())
            self.textEdit.setText('Cadastro realizado com sucesso')
            self.inputName.setText(''), self.inputInit.setText(''), self.inputEnd.setText(''), self.inputValue.setText('') 
        except:
            self.textEdit.setText("algo deu errado, tente novamente")

    def attUser(self):

        try:
            self.conexao.adicionar(self.inputInitA.text(), self.inputEndA.text(), self.inputValue2.text(), self.inputID.text())
            self.textEdit.setText('Atualizado!')
            self.inputName.setText(''), self.inputInitA.setText(''), self.inputEndA.setText(''), self.inputValue2.setText('')        
        except:
            self.textEdit.setText("algo deu errado, tente novamente") 

    def fucSearch(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Valor total: ', 4:'Total de horas trabalhadas: '}
        controle = 1
        for linha in self.conexao.buscar(self.inputNamep.text()):
            for dado in linha:
               if controle == 4:
                    texto += form[controle] +  str(dado)  + '\n---------------------------\n\n'  
               else:
                    texto += form[controle] +  str(dado) + '\n'
               controle +=1  

        self.textEdit.setText(texto)
        self.inputNamep.setText('')

    def listAll(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Valor total: ', 4:'Total de horas trabalhadas: '}
        controle = 1
        for linha in self.conexao.listar():
            for dado in linha:
               if controle == 4:
                    texto += form[controle] +  str(dado)  + '\n---------------------------\n\n'  
               else:
                    texto += form[controle] +  str(dado) + '\n'
               controle +=1
            controle = 1     

        self.textEdit.setText(texto) 

    def callExe(self):
         
        if self.conexao.excluir(int(self.inputIdD.text())) == '1':
            self.textEdit.setText('Algo deu errado, tente novamente')
            self.inputIdD.setText('')
        else:
            self.textEdit.setText('Deletado com sucesso!')
            self.inputIdD.setText('')


            
        
             



    

        

    
        

if __name__ =='__main__':

    
    qt = QApplication(sys.argv)
    novo = Interaction()
    
    novo.show()
    qt.exec_()
    
    
   

