from tkinter import *
import pypyodbc as odbc
from threading import *
import pandas as pd

class Root(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title('Agenda')
        self.root.geometry('1000x730')
        self.root.config(bg='#d8d8d8')
        self.connect_sql()

        self.root.mainloop()
    
    def connect_sql(self):
        def sub_connect_sql():
            self.connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-5S5FFP6;#UID=;PWD=;DATABASE=provas'
            try:
                self.connection_server = odbc.connect(self.connection_string)
                self.connection = self.connection_server
                self.cursor = self.connection_server.cursor()
                print('Connection - Ok')
                self.main()
            except odbc.Error as error:                     
                print(error)

        Thread(target=sub_connect_sql).start()

    def main(self):
        self.query = '''
            SELECT materia, data_prova, conteudo
            FROM prova
            '''
        self.table = pd.read_sql_query(self.query, self.connection)
        self.provas = list(self.table['materia'])
        self.data = list(self.table['data_prova'])
        self.conteudo = list(self.table['conteudo'])
        
        self.testtitle = Label(
            self.root,
            text = 'Prova',
            bg='#d8d8d8',
            font = ('Arial', 13, 'bold')
        ).grid(row = 0, column = 3)

        self.datetitle = Label(
            self.root,
            text = 'Data',
            bg='#d8d8d8',
            font = ('Arial', 13, 'bold')
        ).grid(row = 0, column = 4)

        self.titleconteudo = Label(
            self.root,
            text = 'Conteúdo',
            bg='#d8d8d8',
            font = ('Arial', 13, 'bold')
        ).grid(row = 0, column = 5)

        self.tests_prova = Listbox(
            self.root,
            width = 30,
            font = ('Arial', 13)
        )
        self.tests_prova.grid(row = 1, column= 3, padx = 30)

        self.tests_data = Listbox(
            self.root,
            width = 10,
            font = ('Arial', 13)
        )
        self.tests_data.grid(row = 1, column= 4)

        self.tests_conteudo = Listbox(
            self.root,
            width = 40,
            font = ('Arial', 13)
        )
        self.tests_conteudo.grid(row = 1, column= 5)
        

        for prova in self.provas:
            self.tests_prova.insert(END, prova)
        for data in self.data:
            self.tests_data.insert(END, data)
        for conteudo in self.conteudo:
            self.tests_conteudo.insert(END, conteudo)
Root()