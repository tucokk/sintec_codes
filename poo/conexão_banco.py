import pypyodbc as odbc
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from threading import *

class Root:
    def __init__(self):
        self.root = Tk()
        self.root.title('Conexão ao Banco de Dados SQL')
        self.root.geometry('1000x730')
        self.root.config(bg='#d8d8d8')
        self.connection_database()
        
        self.root.mainloop()

    def connection_database(self):
        def sub_connection_database():
            self.connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-5S5FFP6;#UID=;PWD=;DATABASE=financeiro'
            try:
                self.connection_server = odbc.connect(self.connection_string)
                self.connection = self.connection_server
                print('Connection - Ok')
                self.loading_text.config(text = '', background='#d8d8d8')
                self.selection_names()
            except odbc.Error as error:                     
                print(error)
                self.loading_text.config(text = 'Connection Failed.')
        self.loading_text = Label(
            self.root,
            text = 'Connecting Database. Please wait.'
        )
        self.loading_text.pack()
        Thread(target=sub_connection_database).start()

    def selection_names(self):
        query = '''
        SELECT *
        FROM colaborador
        '''
        table = pd.read_sql_query(query, self.connection)
        name = list(table['nome'])
        cpf = list(table['cpf'])

        names_combobox = Combobox(
            self.root,
            values = name,
            width = 30,
            state = "readonly"
        )
        names_combobox.set('Selecione:')
        names_combobox.pack()

        cpfs_combobox = Combobox(
            self.root,
            values = cpf,
            width = 30,
            state = "readonly"
        )
        cpfs_combobox.set('Selecione:')
        cpfs_combobox.pack()

Root()