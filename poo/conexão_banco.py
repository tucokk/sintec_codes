import pypyodbc as odbc
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar,DateEntry
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
                self.cursor = self.connection_server.cursor()
                print('Connection - Ok')
                self.loading_text.config(text = '', background='#d8d8d8')
                self.select_action()
            except odbc.Error as error:                     
                print(error)
                self.loading_text.config(text = 'Connection Failed.')
        self.loading_text = Label(
            self.root,
            text = 'Connecting Database. Please wait.'
        )
        self.loading_text.pack()
        Thread(target=sub_connection_database).start()

    def select_action(self):
        self.text = Label(
            self.root,
            text = 'Select the desire option'
        )
        self.text.pack()

        self.select = Button(
            self.root, 
            text = 'Select',
            command = self.selection,
            width=30
        )
        self.select.pack(pady = 50)

        self.insert = Button(
            self.root, 
            text = 'Insert',
            command = self.insertion,
            width=30
        )
        self.insert.pack(pady = 50)

    def insertion(self):
        def insert():
            name = str(self.name.get().upper())
            cpf = str(self.cpf.get())
            email = str(self.email.get())
            tel = str(self.tel.get())
            sex = str(self.sex.get())
            date = str(self.date.get_date()).replace('-', '')
            country = str(self.country.get().upper())

            result = Label(
                    self.root,
                    text = '',
                    background = '#d8d8d8'
                )
            result.pack()
            try:
                query = f'''
                INSERT INTO colaborador values ('{name}', '{cpf}', '{email}', '{tel}', '{sex}', '{date}', '{country}')
                '''
                self.cursor.execute(query)
                self.connection_server.commit()
                query = '''
                SELECT *
                FROM colaborador
                '''
                table = pd.read_sql_query(query, self.connection)
                result.config(text='Complete sucessfully.')
            except:
                result.config(text='Failed.')

        self.name = Entry(
            self.root,
            width = 50
        )
        self.name.insert(0,'Name')
        self.name.pack()

        self.cpf = Entry(
            self.root,
            width = 50
        )
        self.cpf.insert(0,'CPF')
        self.cpf.pack()

        self.email = Entry(
            self.root,
            width = 50
        )
        self.email.insert(0,'E-mail')
        self.email.pack()

        self.tel = Entry(
            self.root,
            width = 50
        )
        self.tel.insert(0,'Telephone')
        self.tel.pack()

        self.sex = Combobox(
            self.root,
            values = ['M', 'F', 'O'],
            width = 47,
            state = "readonly"
        )
        self.sex.set('Sex:')
        self.sex.pack()

        self.date = DateEntry(
            self.root,
            width = 47
        )
        
        self.date.pack()

        self.country = Entry(
            self.root,
            width = 50
        )
        self.country.pack()
        self.country.insert(0,'Country')
        self.country.pack()

        self.insertbutton = Button(
            self.root,
            text = 'Insert',
            width=30,
            command = insert
        )
        self.insertbutton.pack()

    def selection(self):
        query = '''
        SELECT *
        FROM colaborador
        '''
        table = pd.read_sql_query(query, self.connection)
        name = list(table['nome'])
        cpf = list(table['cpf'])
        tel = list(table['telefone'])

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

        tels_combobox = Combobox(
            self.root,
            values = tel,
            width = 30,
            state = "readonly"
        )
        tels_combobox.set('Selecione:')
        tels_combobox.pack()

Root()