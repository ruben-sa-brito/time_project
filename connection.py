import sqlite3
from datetime import datetime


class WorkHours:
    def __init__(self):
        self.conn = sqlite3.connect('project_data.db')
        self.cursor = self.conn.cursor()
        self.valor_hora = 0

    def inserir(self, nome_funcionario, hora_inicio, hora_fim, valor_hora):
        

        hora1 = datetime.strptime(hora_inicio, '%H:%M')
        hora2 = datetime.strptime(hora_fim, '%H:%M')
        valor_trabalho = hora2 - hora1
        total_horas = str(hora2 - hora1)
        valor_trabalho = valor_trabalho.seconds*(int(valor_hora))/3600


        consulta = 'INSERT OR IGNORE INTO project_data (nome_funcionario, valor_trabalho, total_horas) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nome_funcionario, valor_trabalho, total_horas))
        self.conn.commit()


    def adicionar(self, hora_inicio, hora_fim, valor_hora, id):
        hora1 = datetime.strptime(hora_inicio, '%H:%M')
        hora2 = datetime.strptime(hora_fim, '%H:%M')
        valor_trabalho = hora2 - hora1
        total_horas = hora2 - hora1
        temp = 'SELECT total_horas FROM project_data WHERE id = ?'
        self.cursor.execute(temp, (id, ))
        for a in self.cursor.fetchone():
            temp = a
        
        temp = datetime.strptime(a[:-3], '%H:%M')
        temp = str(total_horas + temp)
        
        valor_trabalho = valor_trabalho.seconds*(int(valor_hora))/3600
        consulta = 'UPDATE OR IGNORE project_data SET valor_trabalho = valor_trabalho + ?, total_horas = ? WHERE id = ?'
        self.cursor.execute(consulta, (valor_trabalho, temp[11:], id, ))
        self.conn.commit()

    def excluir(self, id):
        temp = 'SELECT total_horas FROM project_data WHERE id = ?'
        consulta = 'DELETE FROM project_data WHERE id = ?'
        self.cursor.execute(temp, (id, ))
        c =0
        for a in self.cursor.fetchall():
            c = 1
           
        if c == 0:
            return '1'

        self.cursor.execute(consulta, (id, ))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM project_data')

        return self.cursor.fetchall()

    def buscar(self, valor):
        consulta = 'SELECT * FROM project_data WHERE nome_funcionario LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%', ))
        return self.cursor.fetchall()
                    

   


   
    
