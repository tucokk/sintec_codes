import textwrap
import pypyodbc as odbc
import tkinter as tk
from threading import *
import time
import os
from datetime import datetime
    
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('sql2xlsx')
        self.geometry('290x190')
        #driver
        self.l_driver = tk.Label(self, text='DRIVER', justify='left')
        self.l_driver.grid(row=0, column=0)
        self.e_driver = tk.Entry(self, width=30)
        self.e_driver.grid(row=0, column=1, padx=20)

        #server
        self.l_server = tk.Label(self, text='SERVER', justify='left')
        self.l_server.grid(row=1, column=0)
        self.e_server = tk.Entry(self, width=30)
        self.e_server.grid(row=1, column=1, padx=20)

        #database
        self.l_database = tk.Label(self, text='DATABASE', justify='left')
        self.l_database.grid(row=2, column=0)
        self.e_database = tk.Entry(self, width=30)
        self.e_database.grid(row=2, column=1, padx=20)

        #uid
        self.l_uid = tk.Label(self, text='UID', justify='left')
        self.l_uid.grid(row=3, column=0)
        self.e_uid = tk.Entry(self, width=30)
        self.e_uid.grid(row=3, column=1)

        #password
        self.l_psw = tk.Label(self, text='PASSWORD', justify='left')
        self.l_psw.grid(row=4, column=0)
        self.e_psw = tk.Entry(self, width=30)
        self.e_psw.grid(row=4, column=1)

        #submit_button
        self.submit1 = tk.Button(self, text="Connect", command=Thread(target=self.on_button).start)
        self.submit1.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        #connection text
        self.connection_text = tk.Label(self, text='', fg='green')
        self.connection_text.grid(row=6, column=0, columnspan=2)

        #variables
        App.connection = 'none'
        App.app2 = 0

    def on_button(self):
        self.connection_info = f'''
            DRIVER={{{self.e_driver.get()}}};
            SERVER={self.e_server.get()};
            DATABASE={self.e_database.get()};
            Trust_Connection=yes;
            UID={self.e_uid.get()};
            PWD={self.e_psw.get()};
                        '''
        self.connection_text.config(text = 'Connecting...')
        
        try:
            #connection line
            connection_server = odbc.connect(self.connection_info)
            App.connection = connection_server
            self.connection_text.config(text = 'Connected.')  

            #geometry
            self.geometry('400x700')

            #querry 
            self.l_querry = tk.Label(self, text='QUERRY', justify='left')
            self.l_querry.grid(row=8, column=0)
            self.e_querry = tk.Text(self, height=25, width=30, justify='center')
            self.e_querry.grid(row=9, column=0, padx=20)

            #tabels
            self.l_tabel = tk.Label(self, text='TABEL', justify='left')
            self.l_tabel.grid(row=10, column=0)
            self.e_tabel = tk.Entry(self, width=30)
            self.e_tabel.grid(row=10, column=1, padx=20)

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
        
class NewWindow(tk.Tk):
    def __init__(self):
            print('a')
window1 = App()
window1.mainloop()
                        

