import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Root-Window List
        self.roots = list()

        # Load Images
        self.new_user_img = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\novo_usuario.png')
        self.info_user_img = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\info_usuario.png')
        self.config_img = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\config.png')
        self.database_img = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\banco_de_dados.png')
        self.export_success = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\exportS.png')
        self.export_fail = tk.PhotoImage(file=r'C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\_img\exportF.png')

        # Create control variables
        self.export_status = False
        self.version = 'Beta 1.02'
        self.counter_checkboxes = 0
        self.value_1 = ''
        self.value_2 = ''
        self.value_3 = ''
        self.value_4 = ''
        self.value_5 = ''
        self.value_6 = ''
        self.value_7 = ''
        self.value_8 = ''
        self.value_9 = ''
        self.value_10 = ''
        self.value_11 = ''
        self.value_12 = ''
        self.value_13 = ''
        self.value_14 = ''

        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Buttons
        self.options_frame = ttk.Frame(self, padding=(20, 10))
        self.options_frame.pack(pady = 50)

        # Create a Frame for the New User Button
        self.new_user_frame = ttk.LabelFrame(self.options_frame, text="New User", padding=(10))
        self.new_user_frame.grid(
            row=0, column=0, padx=(20, 20), pady=(20, 10)
        )
        self.new_user = tk.Button (
                self.new_user_frame, text = 'New User', image = self.new_user_img,
                background = '#333333', border = 0, command = lambda: self.change_window(1)
            )
        self.new_user.grid(row = 0, column = 0, pady = 5, padx = 30)

        # Create a Frame for the Database Button
        self.database_frame = ttk.LabelFrame(self.options_frame, text="Database", padding=(10))
        self.database_frame.grid(
            row=0, column=1, padx=(20, 20), pady=(20, 10)
        )
        self.database = tk.Button (
                self.database_frame, text = 'Database', image = self.database_img,
                background = '#333333', border = 0, command = lambda: self.change_window(2)
            )
        self.database.grid(row = 0, column = 0, pady = 5, padx = 30)

        # Create a Frame for the User Information Button
        self.user_info_frame = ttk.LabelFrame(self.options_frame, text="User Information", padding=(10))
        self.user_info_frame.grid(
            row=1, column=0, padx=(20, 20), pady=(20, 10)
        )
        self.user_info = tk.Button (
                self.user_info_frame, text = 'User Information', image = self.info_user_img,
                background = '#333333', border = 0, command = lambda: self.change_window(3)
            )
        self.user_info.grid(row = 0, column = 0, pady = 5, padx = 30)

        # Create a Frame for the User Configurations Button
        self.config = ttk.LabelFrame(self.options_frame, text="Configurations", padding=(10))
        self.config.grid(
            row=1, column=1, padx=(20, 20), pady=(20, 10)
        )
        self.configs = tk.Button (
                self.config, text = 'Configurations', image = self.config_img,
                background = '#333333', border = 0, command = lambda: self.change_window(4)
            )
        self.configs.grid(row = 0, column = 0, pady = 5, padx = 30)

        # Separator
        self.separator = ttk.Separator(self.options_frame, orient='horizontal')
        self.separator.grid(row = 2, column = 0, columnspan=3, padx = (20, 20), pady = 10, sticky = "ew")

        # Version Label
        self.program_version = ttk.Label(
            self.options_frame, text = f'Version: {self.version}'
        ).grid(row = 3, column = 0, columnspan = 3, pady = 5)

    def change_window(self, value):
        if value == 1:
            self.options_frame.destroy()
            tk.messagebox.showwarning("WARNING", "This Session is on Development")
            self.setup_widgets()
        elif value == 2:
            self.options_frame.destroy()
            tk.messagebox.showwarning("WARNING", "This Session is on Development")
            self.setup_widgets()
        elif value == 3:
            self.options_frame.destroy()
            self.user_info_page()
        elif value == 4:
            self.options_frame.destroy()
            tk.messagebox.showwarning("WARNING", "This Session is on Development")
            self.setup_widgets()
        elif value == 6:
            self.user_info_main_frame.destroy()
            self.counter_checkboxes = 0
            self.sub_user_info_page()
        elif value == 7:
            self.sub_user_info_main_frame.destroy()
            self.user_info_page()
        elif value == 8:
            self.sub_user_info_main_frame.destroy()
            self.user_info_export()
        elif value == 9:
            self.export_info_main_frame.destroy()
            self.user_info_page()
        elif value == 5:
            self.counter_checkboxes = 0
            for i in self.roots:
                try:
                    i.destroy()
                except:
                    pass
            self.setup_widgets()

    def user_info_page(self):
        def change_checkboxes():
            if self.counter_checkboxes == 0:
                self.counter_checkboxes = 1
                for item in self.checkbox_list:
                    if item.state(['selected']) == False:
                        item.invoke() 
            elif self.counter_checkboxes == 1:
                self.counter_checkboxes = 0
                for item in self.checkbox_list:
                    if item.state(['selected']) == True:
                        pass
                    item.invoke()

        def update_listbox(data):
            self.user_listbox.delete(0, tk.END)
            for item in data: 
                self.user_listbox.insert(tk.END, item)
                
        def fillout(e):
            self.user_entry.delete(0, tk.END)
            self.user_entry.insert(0, self.user_listbox.get(tk.ACTIVE))

        def checktype(e):
            typed = self.user_entry.get()
            if type == '':
                data = self.names
            else:
                data = list()
                for item in self.names:
                    if typed.lower() in item.lower():
                        data.append(item)
            update_listbox(data)

        def clearbox(e):
            self.user_entry.delete(0, tk.END)
            self.user_entry.config(font = ('Arial', 14, 'bold'))
            self.user_listbox.place(x = 97, y = 40)

        def unselectlistbox(e):
            self.user_listbox.place(x = 500, y = 500)
            
        #Create Main frame
        self.user_info_main_frame = ttk.Frame(self)
        self.user_info_main_frame.pack(pady = 50)
        self.roots.append(self.user_info_main_frame)
        # Create a Frame for the Header 
        self.user_header_frame = ttk.Frame(self.user_info_main_frame, padding=(20, 10))
        self.user_header_frame.grid(
            row=0, column=0, padx=40, pady=20
        )

        #  Create a Frame for the Image 
        self.user_header_img_frame = ttk.Labelframe(self.user_header_frame, padding=(20, 10), text='')
        self.user_header_img_frame.grid(
            row=0, column=0
        )
        self.image = tk.Label(
            self.user_header_img_frame, image = self.info_user_img,
            width = 160, height = 180
        )
        self.image.grid(row = 0, column = 0, rowspan = 2)

        # Create a Frame for the Info
        self.user_header_info_frame = ttk.Frame(self.user_header_frame, padding=(20, 10))
        self.user_header_info_frame.grid(
            row=0, column=1, padx = 30
        )

        # Create a Frame for User
        self.header_user_frame = ttk.Frame(self.user_header_info_frame, padding=(20, 60))
        self.header_user_frame.grid(
            row=0, column=0
        )
        # User 
        self.user_text = ttk.Label(
            self.header_user_frame, text = 'User:', font = ('Arial', 20)
        ).grid(row = 0, column = 0)

        # User Entry
        self.user_entry = ttk.Entry(
            self.header_user_frame, width = 30,
            font = ('Arial', 14))
        self.user_entry.grid(row = 0, column = 1, padx = 30)
        self.user_entry.insert(0, 'Digite seu nome')
        # User Listbox
        self.user_listbox = tk.Listbox(
            self.header_user_frame, width = 49, height = 3
        )
        self.names = ['ARTHUR LUFT RIBEIRO', 'ARTHUR ROIAL', 'EDUARDO MARMENTIN', 'EDUARDO NERES', 'JOAO VICTOR GHELLERE SOARES', 'BRUNA CARVALHO DA SILVA', 'VIVIANE CARAVALHO DA SILVA', 'ANA PAULA COMIN ROSIN']

        update_listbox(self.names)

        self.user_listbox.bind('<<ListboxSelect>>', fillout)
        self.user_listbox.bind('<Leave>', unselectlistbox)
        self.user_entry.bind('<FocusIn>', clearbox)
        self.user_entry.bind('<KeyRelease>', checktype)
        
        #  Create a Frame for the Checkboxes
        self.user_header_check_frame = ttk.Labelframe(self.user_info_main_frame, padding=(20, 10), text='Filtros')
        self.user_header_check_frame.grid(
            row=1, column=0, sticky = tk.W, padx = 60
        )

        #Checkboxes
        self.check1 = ttk.Checkbutton(
            self.user_header_check_frame, text='Nome', variable = self.value_1, onvalue = 'nome'
        )
        self.check1.grid(row = 0, column = 0, sticky = tk.W)
        self.check2 = ttk.Checkbutton(
            self.user_header_check_frame, text='CPF', variable = self.value_2, onvalue = 'cpf'
        )
        self.check2.grid(row = 0, column = 1, padx = 40, sticky = tk.W)
        self.check3 = ttk.Checkbutton(
            self.user_header_check_frame, text='RG', variable = self.value_3, onvalue = 'rg'
        )
        self.check3.grid(row = 1, column = 0, sticky = tk.W)
        self.check4 = ttk.Checkbutton(
            self.user_header_check_frame, text='Estado Civil', variable = self.value_4, onvalue = 'estado_civil'
        )
        self.check4.grid(row = 1, column = 1, padx = 40, sticky = tk.W)
        self.check5 = ttk.Checkbutton(
            self.user_header_check_frame, text='Tipo de Pessoa', variable = self.value_5, onvalue = 'tipo'
        )
        self.check5.grid(row = 2, column = 0, sticky = tk.W)
        self.check6 = ttk.Checkbutton(
            self.user_header_check_frame, text='UF', variable = self.value_5, onvalue = 'uf'
        )
        self.check6.grid(row = 2, column = 1, padx = 40, sticky = tk.W)
        self.check7 = ttk.Checkbutton(
            self.user_header_check_frame, text='Cidade', variable = self.value_5, onvalue = 'cidade'
        )
        self.check7.grid(row = 3, column = 0, padx = (0, 40), sticky = tk.W)
        self.check8 = ttk.Checkbutton(
            self.user_header_check_frame, text='CEP', variable = self.value_5, onvalue = 'cep'
        )
        self.check8.grid(row = 3, column = 1, padx = 40, sticky = tk.W)
        self.check9 = ttk.Checkbutton(
            self.user_header_check_frame, text='Bairro', variable = self.value_5, onvalue = 'bairro'
        )
        self.check9.grid(row = 4, column = 0, sticky = tk.W)
        self.check10 = ttk.Checkbutton(
            self.user_header_check_frame, text='Endereço', variable = self.value_5, onvalue = 'endereco'
        )
        self.check10.grid(row = 4, column = 1, padx = 40, sticky = tk.W)
        self.check11 = ttk.Checkbutton(
            self.user_header_check_frame, text='Número', variable = self.value_5, onvalue = 'numero'
        )
        self.check11.grid(row = 5, column = 0, sticky = tk.W)
        self.check12 = ttk.Checkbutton(
            self.user_header_check_frame, text='Complemento', variable = self.value_5, onvalue = 'complemento'
        )
        self.check12.grid(row = 5, column = 1, padx = 40, sticky = tk.W)
        self.check13 = ttk.Checkbutton(
            self.user_header_check_frame, text='Telefone', variable = self.value_5, onvalue = 'telefone'
        )
        self.check13.grid(row = 6, column = 0, sticky = tk.W)
        self.check14 = ttk.Checkbutton(
            self.user_header_check_frame, text='E-mail', variable = self.value_5, onvalue = 'email'
        )
        self.check14.grid(row = 6, column = 1, padx = 40, sticky = tk.W)

        self.checkbox_list = [
            self.check1, self.check2, self.check3, self.check4, self.check5,
            self.check6, self.check7, self.check8, self.check9, self.check10,
            self.check11, self.check12, self.check13, self.check14
        ]

        #  Create a Frame for the Buttons
        self.user_buttons_frame = ttk.Frame(self.user_info_main_frame, padding=(20, 10))
        self.user_buttons_frame.grid(
            row=2, column=0, sticky = tk.W, padx = 40, pady = 60
        )

        # Back Button
        self.backbutton = ttk.Button(
            self.user_buttons_frame, text = 'Back', width = 20, command = lambda: self.change_window(5)
        )
        self.backbutton.grid(row = 0, column = 0, columnspan = 2)

        # All Filters Button
        self.allfilterson = ttk.Checkbutton(
            self.user_buttons_frame, text="All filters on", style="Toggle.TButton", width = 20,
            command = change_checkboxes
        )
        self.allfilterson.grid(row=0, column=4, padx= (250, 0), sticky="nsew")

        # Go Button
        self.gobutton = ttk.Checkbutton(
            self.user_buttons_frame, text="Go", style="Accent.TButton", width = 20,
            command = lambda: self.change_window(6)
        )
        self.gobutton.grid(row=0, column=5, padx= (20, 0), sticky="nsew")

    def sub_user_info_page(self):
        #Create Main frame
        self.sub_user_info_main_frame = ttk.Frame(self)
        self.sub_user_info_main_frame.pack(pady = 50)
        self.roots.append(self.sub_user_info_main_frame)
        # Create a Frame for the Header 
        self.sub_user_header_frame = ttk.Frame(self.sub_user_info_main_frame, padding=(20, 10))
        self.sub_user_header_frame.grid(
            row=0, column=0, padx=40, pady=20
        )

        #  Create a Frame for the Image 
        self.sub_user_header_img_frame = ttk.Labelframe(self.sub_user_header_frame, padding=(20, 10), text='')
        self.sub_user_header_img_frame.grid(
            row=0, column=0
        )
        # Image
        self.image = tk.Label(
            self.sub_user_header_img_frame, image = self.info_user_img,
            width = 160, height = 180
        )
        self.image.grid(row = 0, column = 0, rowspan = 2)

        # Create a Frame for the Info
        self.sub_user_header_info_frame = ttk.Frame(self.sub_user_header_frame, padding=(20, 10))
        self.sub_user_header_info_frame.grid(
            row=0, column=1, padx = 42
        )

        # Create a Frame for User
        self.sub_header_user_frame = ttk.Frame(self.sub_user_header_info_frame, padding=(20, 10))
        self.sub_header_user_frame.grid(
            row=0, column=0
        )

        # User 
        self.user_text2 = ttk.Label(
            self.sub_header_user_frame, text = 'Nome:', font = ('Arial', 17)
        ).grid(row = 0, column = 0)

        # User Name
        self.user_name = ttk.Entry(
            self.sub_header_user_frame, width = 22,
            font = ('Arial', 20)
        )
        self.user_name.grid(row = 0, column = 1, padx = 30, columnspan = 2)
        self.user_name.insert(0, 'ARTHUR LUFT RIBEIRO')
        self.user_name.configure(state='disabled')

        # CPF
        self.user_text3 = ttk.Label(
            self.sub_header_user_frame, text = 'CPF:', font = ('Arial', 17)
        )
        self.user_text3.grid(row = 1, column = 0, sticky = tk.W, pady = 10)

        # User CPF
        self.user_cpf = ttk.Entry(
            self.sub_header_user_frame, width = 15, 
            font = ('Arial', 17)
        )
        self.user_cpf.grid(row = 1, column = 1, sticky = tk.W, padx = (30, 0))
        self.user_cpf.insert(0, '038.448.680-93')
        self.user_cpf.configure(state='disabled')

        # RG
        self.user_text4 = ttk.Label(
            self.sub_header_user_frame, text = 'RG:', font = ('Arial', 17)
        )
        self.user_text4.grid(row = 2, column = 0, sticky = tk.W)
        # User RG
        self.user_rg = ttk.Entry(
            self.sub_header_user_frame, width = 15, 
            font = ('Arial', 17)
        )
        self.user_rg.grid(row = 2, column = 1, sticky = tk.W, padx = (30, 0))
        self.user_rg.insert(0, '20.200.866-6')
        self.user_rg.configure(state='disabled')

        #  Create a Frame for Infos
        self.sub_user_header_info_frame = ttk.Frame(self.sub_user_info_main_frame, padding=(20, 10))
        self.sub_user_header_info_frame.grid(
            row=1, column=0, sticky = tk.W, padx = 60
        )

        # Estado Civil
        self.user_text5 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Estado Civil:', font = ('Arial', 14)
        )
        self.user_text5.grid(row = 0, column = 0, sticky = tk.W)
        # User Estado Civil
        self.user_estado_civil = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_estado_civil.grid(row = 0, column = 1, sticky = tk.W, padx = (30, 0))
        self.user_estado_civil.insert(0, 'Solteiro')
        self.user_estado_civil.configure(state='disabled')

        # Tipo
        self.user_text6 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Tipo de Pessoa:', font = ('Arial', 14)
        )
        self.user_text6.grid(row = 1, column = 0, sticky = tk.W)
        # User tipo
        self.user_tipo = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_tipo.grid(row = 1, column = 1, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_tipo.insert(0, 'Física')
        self.user_tipo.configure(state='disabled')

        # UF
        self.user_text7 = ttk.Label(
            self.sub_user_header_info_frame, text = 'UF:', font = ('Arial', 14)
        )
        self.user_text7.grid(row = 2, column = 0, sticky = tk.W)
        # User UF
        self.user_uf = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_uf.grid(row = 2, column = 1, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_uf.insert(0, 'PR')
        self.user_uf.configure(state='disabled')

        # Cidade
        self.user_text8 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Cidade:', font = ('Arial', 14)
        )
        self.user_text8.grid(row = 3, column = 0, sticky = tk.W)
        # User Cidade
        self.user_cidade = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_cidade.grid(row = 3, column = 1, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_cidade.insert(0, 'Medianeira')
        self.user_cidade.configure(state='disabled')

        # CEP
        self.user_text9 = ttk.Label(
            self.sub_user_header_info_frame, text = 'CEP:', font = ('Arial', 14)
        )
        self.user_text9.grid(row = 2, column = 2, sticky = tk.W, padx = (30, 0))
        # User CEP
        self.user_cep = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_cep.grid(row = 2, column = 3, sticky = tk.W, padx = (30, 0))
        self.user_cep.insert(0, '85.884-000')
        self.user_cep.configure(state='disabled')

        # Bairro
        self.user_text10 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Bairro:', font = ('Arial', 14)
        )
        self.user_text10.grid(row = 3, column = 2, sticky = tk.W, padx = (30, 0))
        # User Bairro
        self.user_bairro = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_bairro.grid(row = 3, column = 3, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_bairro.insert(0, 'CIDADE ALTA')
        self.user_bairro.configure(state='disabled')
        
        # Endereço
        self.user_text11 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Endereço:', font = ('Arial', 14)
        )
        self.user_text11.grid(row = 4, column = 2, sticky = tk.W, padx = (30, 0))
        # User Endereço
        self.user_endereco = ttk.Entry(
            self.sub_user_header_info_frame,
            font = ('Arial', 13), width = 40
        )
        self.user_endereco.grid(row = 4, column = 3, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_endereco.insert(0, 'AVENIDA LAGOA VERMELHA, 2487')
        self.user_endereco.configure(state='disabled')

        # Complemento
        self.user_text14 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Complemento:', font = ('Arial', 14)
        )
        self.user_text14.grid(row = 4, column = 0, sticky = tk.W)
        # User Complemento
        self.user_complemento = ttk.Entry(
            self.sub_user_header_info_frame,
            font = ('Arial', 13), width = 20
        )
        self.user_complemento.grid(row = 4, column = 1, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_complemento.insert(0, 'APARTAMENTO 02')
        self.user_complemento.configure(state='disabled')

        # Telefone
        self.user_text12 = ttk.Label(
            self.sub_user_header_info_frame, text = 'Telefone:', font = ('Arial', 14)
        )
        self.user_text12.grid(row = 5, column = 0, sticky = tk.W)
        # User Telefone
        self.user_tel = ttk.Entry(
            self.sub_user_header_info_frame, width = 15, 
            font = ('Arial', 13)
        )
        self.user_tel.grid(row = 5, column = 1, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_tel.insert(0, '45999979955')
        self.user_tel.configure(state='disabled')

        # Email
        self.user_text13 = ttk.Label(
            self.sub_user_header_info_frame, text = 'E-mail:', font = ('Arial', 14)
        )
        self.user_text13.grid(row = 5, column = 2, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        # User Email
        self.user_email = ttk.Entry(
            self.sub_user_header_info_frame, width = 40, 
            font = ('Arial', 13)
        )
        self.user_email.grid(row = 5, column = 3, sticky = tk.W, padx = (30, 0), pady = (5, 0))
        self.user_email.insert(0, 'arthurluftribeiro@gmail.com')
        self.user_email.configure(state='disabled')

        #  Create a Frame for the Buttons
        self.user_buttons_frame = ttk.Frame(self.sub_user_info_main_frame, padding=(20, 10))
        self.user_buttons_frame.grid(
            row=2, column=0, sticky = tk.W, padx = 40, pady = 60
        )

        # Back Button
        self.sub_backbutton = ttk.Button(
            self.user_buttons_frame, text = 'Back', width = 20, command = lambda: self.change_window(7)
        )
        self.sub_backbutton.grid(row = 0, column = 0, columnspan = 2)


        # Export Button
        self.sub_exportbutton = ttk.Checkbutton(
            self.user_buttons_frame, text="Export", style="Accent.TButton", width = 20,
            command = lambda: self.change_window(8)
        )
        self.sub_exportbutton.grid(row=0, column=4, padx= (550, 0), sticky="nsew")
    def user_info_export(self):
        #Create Main frame
        self.export_info_main_frame = ttk.Frame(self)
        self.export_info_main_frame.pack(pady = 50)
        self.roots.append(self.export_info_main_frame)

        # Main Label
        self.export_image = ttk.Label(self.export_info_main_frame, 
        image = (self.export_success if self.export_status == True else self.export_fail), width = 50)
        self.export_image.grid(row = 0, column = 0, padx = (330), pady = (150, 0))

        self.export_text = ttk.Label(self.export_info_main_frame,
        text = ('Export Complete Successfully' if self.export_status == True else 'Export Failed'), font = ('Arial', 20))
        self.export_text.grid(row = 1, column = 0, pady = 40)

        # Back button
        self.export_backbutton = ttk.Button(
            self.export_info_main_frame, text = 'Back', width = 20, style="Accent.TButton", 
            command = lambda: self.change_window(9)
        )
        self.export_backbutton.grid(row = 2, column = 0, columnspan = 2)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Database')
    
    # Simply set the theme
    root.tk.call("source", r"C:\Users\Usuario\Documents\GitHub\sintec_codes\programa\Azure-ttk-theme-main\azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.geometry("2100x900")
    root.state('zoomed')

    root.mainloop()
