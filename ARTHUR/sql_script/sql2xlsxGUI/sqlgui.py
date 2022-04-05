from multiprocessing.dummy import connection
import tkinter as tk
from threading import *
import pypyodbc as odbc
import os
from datetime import datetime
import time
import pandas as pd
import subprocess
import sys

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('sql2xlsx')
        self.geometry('1000x730')
        self.config(bg='#d8d8d8')

        #driver
        self.l_driver = tk.Label(self, text='DRIVER', bg='#d8d8d8')
        self.l_driver.grid(row=0, column=0)
        self.e_driver = tk.Entry(self, width=30)
        self.e_driver.grid(row=0, column=1, padx=20, pady=5)

        #server
        self.l_server = tk.Label(self, text='SERVER', bg='#d8d8d8')
        self.l_server.grid(row=1, column=0)
        self.e_server = tk.Entry(self, width=30)
        self.e_server.grid(row=1, column=1, padx=20, pady=5)

        #database
        self.l_database = tk.Label(self, text='DATABASE', bg='#d8d8d8')
        self.l_database.grid(row=2, column=0)
        self.e_database = tk.Entry(self, width=30)
        self.e_database.grid(row=2, column=1, padx=20, pady=5)

        #uid
        self.l_uid = tk.Label(self, text='UID', bg='#d8d8d8')
        self.l_uid.grid(row=3, column=0)
        self.e_uid = tk.Entry(self, width=30)
        self.e_uid.grid(row=3, column=1, pady=5)

        #password
        self.l_psw = tk.Label(self, text='PASSWORD', bg='#d8d8d8')
        self.l_psw.grid(row=4, column=0)
        self.e_psw = tk.Entry(self, width=30)
        self.e_psw.grid(row=4, column=1, pady=5)

        #submit_button
        self.submit1 = tk.Button(self, text="Connect", command=self.on_button)
        self.submit1.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        #connection text
        self.connection_text = tk.Label(self, text='', fg='green', bg='#d8d8d8')
        self.connection_text.grid(row=6, column=0, columnspan=2)

        #querry
        self.l_querry = tk.Label(self, text='QUERRY', bg='#d8d8d8')
        self.l_querry.grid(row=9, column=0)
        self.e_querry = tk.Text(self, height=25, width=33, bd=3,)
        self.e_querry.grid(row=10, column=0, columnspan=2)
        self.e_querry.insert('1.0', f'remember: in table place \n(from [tabel]) use [tabel.]\nex: select * from [tabel]\nerase it before writing the querry.')

        #tabels
        self.l_tabel = tk.Label(self, text='TABEL', bg='#d8d8d8')
        self.l_tabel.grid(row=8, column=0)
        self.e_tabel = tk.Entry(self, width=30)
        self.e_tabel.grid(row=8, column=1, padx=20, pady=10)

        #submit button
        self.submit1 = tk.Button(self, text="Consult", command=self.on_button2)
        self.submit1.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        #text 
        self.connection_text2 = tk.Label(self, text='', fg='green', bg='#d8d8d8')
        self.connection_text2.grid(row=11, column=3, columnspan=2)

        self.connection_text = tk.Label(self, text='Not connected', fg='red', bg='#d8d8d8')
        self.connection_text.grid(row=6, column=0, columnspan=2)
        
        #result
        self.querry_resulttxt = tk.Label(self, text='RESULT:', bg='#d8d8d8')
        self.querry_resulttxt.grid(row=0, column=2)
        self.querry_result = tk.Text(self, height=40, bd=3)
        self.querry_result.place(x=295, y=32)
        self.querry_result.insert('1.0', f'')
        #variables
        App.connection = 'none'
        App.app2 = 0

    def on_button(self):
        def sub_on_button():
            self.step = 1
            self.database = self.e_database.get()
            self.database = self.database.replace(' ', '')
            self.databases = self.database.split(',')
            
            for x in range(len(self.databases)):
                self.globalcounter = x+1
            self.connection_info = f'''
                DRIVER={{{self.e_driver.get()}}};
                SERVER={self.e_server.get()};
                DATABASE={self.databases[0]};
                Trust_Connection=yes;
                UID={self.e_uid.get()};
                PWD={self.e_psw.get()};
                            '''
            self.connection_text.config(fg = 'green')
            self.connection_text.config(text = 'Connecting...')
            try:
                #connection line
                connection_server = odbc.connect(self.connection_info)
                App.connection = connection_server
                self.connection_text.config(text = 'Connected.') 
            except odbc.Error as error:                     
                value = str(error)
                self.connection_text.config(fg = 'red')
                self.connection_text.config(text = f'Connection failed. Check ./logs.')
                directory_exist = os.path.exists(f'./logs')
                if directory_exist == False:
                    os.makedirs('./logs')
                with open('./logs/logs.txt', 'w') as log:
                    log.write(f'{str(datetime.today())}: {value}')
        Thread(target=sub_on_button).start()


    def on_button2(self):
        def sub_on_button2():
            if self.step == 1:
                self.connection_text2.config(text = 'Consulting...')  
                self.tabel = self.e_tabel.get()
                self.tabel = self.tabel.replace(' ', '')
                self.tabels = self.tabel.split(',')

                self.successcounter = 0
                skipped = 0
                for i in range(len(self.tabels)):
                    try:
                        self.querry = self.e_querry.get("1.0",'end-1c')
                        self.querry = self.querry.replace('[tabel]', self.tabels[i])

                        self.final_result = 0
                        if self.tabels[-1] == self.tabels[i]:
                            self.final_result = 1
                        
                        pd.set_option('display.max_rows', None)
                        self.table = pd.read_sql_query(self.querry, App.connection)
                        self.querry_result.delete('1.0', tk.END)
                        self.querry_result.insert('1.0', f'{self.table}') 

                        directory_exist = os.path.exists(f'./results')
                        if directory_exist == False:
                            os.makedirs(f'./results')
                        with open(f'./results/data.txt', 'a') as sqlinfo:
                            config = f'\n\n{self.table}'
                            characters = ', '
                            for x in range(len(characters)):
                                tabels_formated = self.tabels[i].replace(characters[x], '')
                            sqlinfo.write(f'\n\nDatabase: {tabels_formated}\nResult:\n{config}')
                        if self.final_result == 1:
                            with open(f'./results/data.txt', 'a') as sqlinfo:
                                date = str(datetime.today())
                                sqlinfo.write(f'\n\n\nGenerated at: {date}\nDeveloper: https://github.com/tucokk')
                        self.table.to_csv(f'./results/{self.tabels[i]}.csv')
                        self.table.to_excel(f'./results/{self.tabels[i]}.xlsx')
                        self.complete = True
                    except:
                        skipped += 1
                        pass
                if self.complete == True:
                    self.dir_path = os.path.dirname(os.path.realpath(__file__))
                    self.connection_text2.config(text = f'Consult complete. {skipped} skipped. - Check {self.dir_path}')
            
            
        Thread(target=sub_on_button2).start() 

window = App()
window.mainloop()