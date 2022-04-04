import textwrap
from pyparsing import col
import pypyodbc as odbc
import tkinter as tk
from threading import *
import time
import os
from datetime import datetime
import pandas as pd
    
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('sql2xlsx')
        self.geometry('290x190')
        self.config(bg='#d8d8d8')
        #driver
        self.l_driver = tk.Label(self, text='DRIVER', bg='#d8d8d8')
        self.l_driver.grid(row=0, column=0)
        self.e_driver = tk.Entry(self, width=30)
        self.e_driver.grid(row=0, column=1, padx=20)
        

        #server
        self.l_server = tk.Label(self, text='SERVER', bg='#d8d8d8')
        self.l_server.grid(row=1, column=0)
        self.e_server = tk.Entry(self, width=30)
        self.e_server.grid(row=1, column=1, padx=20)

        #database
        self.l_database = tk.Label(self, text='DATABASE', bg='#d8d8d8')
        self.l_database.grid(row=2, column=0)
        self.e_database = tk.Entry(self, width=30)
        self.e_database.grid(row=2, column=1, padx=20)

        #uid
        self.l_uid = tk.Label(self, text='UID', bg='#d8d8d8')
        self.l_uid.grid(row=3, column=0)
        self.e_uid = tk.Entry(self, width=30)
        self.e_uid.grid(row=3, column=1)

        #password
        self.l_psw = tk.Label(self, text='PASSWORD', bg='#d8d8d8')
        self.l_psw.grid(row=4, column=0)
        self.e_psw = tk.Entry(self, width=30)
        self.e_psw.grid(row=4, column=1)

        #submit_button
        self.submit1 = tk.Button(self, text="Connect", command=Thread(target=self.on_button).start)
        self.submit1.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        #connection text
        self.connection_text = tk.Label(self, text='', fg='green', bg='#d8d8d8')
        self.connection_text.grid(row=6, column=0, columnspan=2)

        #variables
        App.connection = 'none'
        App.app2 = 0

    def on_button(self):
        self.database = self.e_database.get()
        self.database = self.database.replace(' ', '')
        self.databases = self.database.split(',')
        for x in range(len(self.databases)):
            self.globalcounter = x
            self.connection_info = f'''
                DRIVER={{{self.e_driver.get()}}};
                SERVER={self.e_server.get()};
                DATABASE={self.e_database.get()};
                Trust_Connection=yes;
                UID={self.e_uid.get()};
                PWD={self.databases[x]};
                            '''
            print(self.connection_info)
        self.connection_text.config(text = 'Connecting...')
        
        try:
            #connection line
            connection_server = odbc.connect(self.connection_info)
            App.connection = connection_server
            self.connection_text.config(text = 'Connected.')  

            #geometry
            self.geometry('290x710')

            #querry 
            self.l_querry = tk.Label(self, text='QUERRY', bg='#d8d8d8')
            self.l_querry.grid(row=8, column=0)
            self.e_querry = tk.Text(self, height=25, width=32)
            self.e_querry.grid(row=9, column=0, columnspan=2)

            #tabels
            self.l_tabel = tk.Label(self, text='TABEL', bg='#d8d8d8')
            self.l_tabel.grid(row=10, column=0)
            self.e_tabel = tk.Entry(self, width=30)
            self.e_tabel.grid(row=10, column=1, padx=20, pady=10)

            #submit button
            self.submit1 = tk.Button(self, text="Consult", command=Thread(target=self.on_button2).start)
            self.submit1.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

            #consult text 2
            self.connection_text2 = tk.Label(self, text='', fg='green', bg='#d8d8d8')
            self.connection_text2.grid(row=12, column=0, columnspan=2)

        except odbc.Error as error:                     
            value = str(error)
            self.connection_text.config(fg = 'red')
            self.connection_text.config(text = f'Connection failed.\nCheck ./logs.')
            directory_exist = os.path.exists(f'./logs')
            if directory_exist == False:
                os.makedirs('./logs')
            with open('./logs/logs.txt', 'w') as log:
                log.write(f'{str(datetime.today())}: {value}')
            time.sleep(5)
            self.destroy()
        
    def on_button2(self):
          
        #calling the start of connecting process
            self.connection_text2.config(text = 'Consulting...')  
            self.tabel = self.e_tabel.get()
            self.tabel = self.tabel.replace(' ', '')
            self.tabels = self.tabel.split(',')
            
            self.successcounter = 0
            for i in range(len(self.tabels)):
                self.querry = self.e_querry.get("1.0",'end-1c')
                self.querry = self.querry.replace('[tabel]', self.tabels[i])

                self.final_result = 0
                if self.tabels[-1] == self.tabels[i]:
                    self.final_result = 1
                
                pd.set_option('display.max_rows', None)
                self.table = pd.read_sql_query(self.querry, App.connection)
                self.connection_text2.config(text = 'Consult complete.')
                print(self.table)
                #geometry
                self.geometry('1000x730')

                #result
                self.querry_resulttxt = tk.Label(self, text='RESULT:', bg='#d8d8d8')
                self.querry_resulttxt.grid(row=0, column=3)
                self.querry_result = tk.Text(self, height=40, bd=3, )
                self.querry_result.place(x=295, y=20)
                self.querry_result.insert('1.0', f'{self.table}')


                #consult text 3
                self.connection_text3 = tk.Label(self, text='Files generated. Check ./results', fg='green', bg='#d8d8d8')
                self.connection_text3.grid(row=12, column=3, columnspan=2)



window1 = App()
window1.mainloop()
                        

