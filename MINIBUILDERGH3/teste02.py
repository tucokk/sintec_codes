from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('minibuildergh3')
        self.geometry('600x750')
        self.iconbitmap(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img\icon.ico')
        self.resizable(False, False)
        
        # Set the Theme
        self.tk.call("source", r"C:\Users\arthu\Desktop\programa\Forest-ttk-theme-master\forest-dark.tcl")
        ttk.Style().theme_use('forest-dark')

        # Root-Window List

        # Load Images
        main_main_cape_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/cape.jpg').resize((220, 300))
        self.main_main_cape_img = ImageTk.PhotoImage(main_main_cape_img)

        main_dir_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/dir.png').resize((25, 20))
        self.main_dir_img = ImageTk.PhotoImage(main_dir_img)

        menu_minibuildergh3_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/minibuildergh3.png').resize((150, 150))
        self.menu_minibuildergh3_img = ImageTk.PhotoImage(menu_minibuildergh3_img)

        menu_harpy_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/harpy.png').resize((150, 150))
        self.menu_harpy_img = ImageTk.PhotoImage(menu_harpy_img)

        # Create control variables
        self.art_preset = tk.IntVar()
        self.music_preset = tk.BooleanVar()
        self.configs1 = tk.BooleanVar()
        self.configs2 = tk.BooleanVar()
        self.configs3 = tk.BooleanVar()

        #Program Version
        self.program_version = 'v. alfa0.01'

        # Create widgets
        self.main_main_window()

    def main_main_window(self):
        def change_art_state():
            if self.art_preset.get() == 0:
                self.main_main_image_btn.configure(state = tk.DISABLED)
                self.main_art_info_btn.configure(text = 'Blocked', command = '')
            elif self.art_preset.get() == 1:
                self.main_main_image_btn.configure(state = tk.NORMAL)
                self.main_art_info_btn.configure(text = 'Blocked', command = '')
            elif self.art_preset.get() == 2:
                self.main_main_image_btn.configure(state = tk.NORMAL)
                self.main_art_info_btn.configure(text = 'Explore', command = lambda: self.images_main_root())

        def search_cover_image():
            try:
                f_types = [('PNG Files', '*.png'), ('JPEG Files', '*.jpg')]
                filename = filedialog.askopenfilename(filetypes = f_types)
                img = Image.open(filename)
                img = img.resize((220, 300))
                img = ImageTk.PhotoImage(img)
                self.main_main_image_cape.image = img
                self.main_main_image_cape['image'] = img
                self.main_main_cape_img = img
            except:
                pass
            
        # Menu
        self.menu = tk.Menu(self, tearoff = 0)
        self.config(menu = self.menu)
        self.menu.add_command(label="Information", command = self.information_menu) 

        # Main Frame
        self.main_main_frame = ttk.Frame(
            self, padding = (10, 10)
        )
        self.main_main_frame.pack()

        # --- Session 1 ---

        # Main_Image Frame
        self.main_main_image_frame = ttk.Labelframe(
            self.main_main_frame, text = 'Cover',
            labelanchor= tk.N 
        )
        self.main_main_image_frame.grid(row = 0, column = 0, sticky = tk.NW, padx = (0, 15), rowspan = 2)

        # Main_Image Cape
        self.main_main_image_cape = tk.Label(
            self.main_main_image_frame, image = self.main_main_cape_img, relief = 'solid', border = 3
        )
        self.main_main_image_cape.grid(row = 0, column = 0, columnspan = 2)

        # Sub Main_Image Frame
        self.main_sub_main_image_frame = ttk.Frame(
            self.main_main_image_frame, padding = (3, 3)
        )
        self.main_sub_main_image_frame.grid(row = 1, column = 0, sticky = tk.NW, pady = 0, columnspan = 2)

        # Main_Image Change Txt
        self.main_main_image_txt = ttk.Label(
            self.main_sub_main_image_frame, text = '        Replace', font = ('Helvetica', 13, 'bold'),
            width = 20, anchor=tk.N
        )
        self.main_main_image_txt.grid(row = 0, column = 0, pady = 0)
        
        # Main_image Change Button Frame
        self.main_main_image_btn = tk.Button(
            self.main_sub_main_image_frame, text = 'Change', image = self.main_dir_img,
            background = '#333333', border = 3, relief=tk.FLAT, 
            state = tk.DISABLED, 
            command = search_cover_image
        )
        self.main_main_image_btn.grid(row = 0, column = 1, padx = (10, 5))

        # --- Session 2 ---

        # Main_Info Frame
        self.main_main_info_frame = ttk.Labelframe(
            self.main_main_frame, text = 'Main Info', padding = (10, 23)
        )
        self.main_main_info_frame.grid(row = 0, column = 1, sticky = tk.NE)

        # Main_Info Name Txt
        self.main_main_info_name_txt = ttk.Label(
            self.main_main_info_frame, text = 'Mod-Name',
            font = ('Helvetica', 9, 'bold')
        )
        self.main_main_info_name_txt.grid(row = 0, column = 0, padx = (0, 10), sticky = tk.W)

        # Main_Info Name Entry
        self.main_main_info_name_entry = ttk.Entry(
            self.main_main_info_frame, width = 30
        )
        self.main_main_info_name_entry.grid(row = 0, column = 1, pady = (0, 5))

        # Main_Info Creator Txt
        self.main_main_info_creator_txt = ttk.Label(
            self.main_main_info_frame, text = 'Creator',
            font = ('Helvetica', 13, 'bold')
        )
        self.main_main_info_creator_txt.grid(row = 1, column = 0, padx = (0, 10), sticky = tk.W)

        # Main_Info Creator Entry
        self.main_main_info_creator_entry = ttk.Entry(
            self.main_main_info_frame, width = 30
        )
        self.main_main_info_creator_entry.grid(row = 1, column = 1, pady = (0, 5))

        # Main_Info Year Txt
        self.main_main_info_year_txt = ttk.Label(
            self.main_main_info_frame, text = 'Year',
            font = ('Helvetica', 13, 'bold')
        )
        self.main_main_info_year_txt.grid(row = 2, column = 0, padx = (0, 10), sticky = tk.W)

        # Main_Info Creator Entry
        self.main_main_info_year_entry = ttk.Entry(
            self.main_main_info_frame, width = 30
        )
        self.main_main_info_year_entry.grid(row = 2, column = 1)

        # --- Session 3 ---

        # Art_Info Frame
        self.main_art_info_frame = ttk.Labelframe(
            self.main_main_frame, text = 'Art Info', padding = (10, 10)
        )
        self.main_art_info_frame.grid(row = 1, column = 1, sticky = tk.NE)

        # Art_Info Txt
        self.main_art_info_txt = ttk.Label(
            self.main_art_info_frame, text = 'Select the Art Preset', 
            font = ('Helvetica', 15, 'bold'), width = 27
        )
        self.main_art_info_txt.grid(row = 0, column = 0)

        # Art_Info Radiobuttons
        self.main_art_info_radio1 = ttk.Radiobutton(
            self.main_art_info_frame, text = 'No Modifying', value = 0, 
            variable = self.art_preset, command = change_art_state
        )
        self.main_art_info_radio1.grid(row = 1, column = 0, pady = (10, 0), sticky = tk.W)

        self.main_art_info_radio2 = ttk.Radiobutton(
            self.main_art_info_frame, text = 'Just the Cover', value = 1, 
            variable = self.art_preset, command = change_art_state
        )
        self.main_art_info_radio2.grid(row = 2, column = 0, pady = (10, 0), sticky = tk.W)

        self.main_art_info_radio3 = ttk.Radiobutton(
            self.main_art_info_frame, text = 'Modify', value = 2, 
            variable = self.art_preset, command = change_art_state
        )
        self.main_art_info_radio3.grid(row = 3, column = 0, pady = (10, 0), sticky = tk.W)

        # Art_Info Button
        self.main_art_info_btn = ttk.Button(
            self.main_art_info_frame, text = 'Blocked'
        )
        self.main_art_info_btn.grid(row = 4, column = 0, pady = (17, 0))

        # --- Session 4 ---

        # Config Frame
        self.main_config_frame = ttk.Labelframe(
            self.main_main_frame, text = 'Configurations', padding = (12, 10),
            labelanchor= tk.N
        )
        self.main_config_frame.grid(row = 1, column = 0, sticky = tk.W, pady=(190, 0))

        # Config Txt
        self.main_config_txt = ttk.Label(
            self.main_config_frame, text = 'Select the Desired\nConfig Presets', 
            font = ('Helvetica', 12, 'bold')
        )
        self.main_config_txt.grid(row = 0, column = 0, sticky = tk.W, pady = (0, 5))

        # Config Checkbuttons
        self.main_config_checkbutton1 = ttk.Checkbutton(
            self.main_config_frame, text = 'Download Original Game-Copy\nAutomatically',
            onvalue = True, offvalue = False, variable = self.configs1
        )
        self.main_config_checkbutton1.grid(row = 1, column = 0, sticky = tk.W)

        self.main_config_checkbutton2 = ttk.Checkbutton(
            self.main_config_frame, text = 'Auto Extract Charts From\nOriginal Game-Copy',
            onvalue = True, offvalue = False, variable = self.configs2
        )
        self.main_config_checkbutton2.grid(row = 2, column = 0, sticky = tk.W)

        self.main_config_checkbutton3 = ttk.Checkbutton(
            self.main_config_frame, text = 'Auto Generate .ISO File in\nOutput',
            onvalue = True, offvalue = False, variable = self.configs3
        )
        self.main_config_checkbutton3.grid(row = 3, column = 0, sticky = tk.W, pady = (0, 36))


        # --- Session 5 ---

        # Music_Info Frame
        self.main_music_info_frame = ttk.Labelframe(
            self.main_main_frame, text = 'Music Info', padding = (10, 10)
        )
        self.main_music_info_frame.grid(row = 1, column = 1, sticky = tk.NE, pady = (235, 0))

        # Music_Info Txt
        self.main_music_info_txt = ttk.Label(
            self.main_music_info_frame, text = 'Select the Music Preset', 
            font = ('Helvetica', 15, 'bold'), width = 27
        )
        self.main_music_info_txt.grid(row = 0, column = 0, sticky = tk.W, pady = (0, 5))
        
        # Music_Info Radiobuttons   
        self.main_music_info_radio1 = ttk.Radiobutton(
            self.main_music_info_frame, text = 'No Modifying', value = False, 
            variable = self.music_preset
        )
        self.main_music_info_radio1.grid(row = 1, column = 0, pady = (10, 0), sticky = tk.W)

        self.main_music_info_radio2 = ttk.Radiobutton(
            self.main_music_info_frame, text = 'Modifying', value = True, 
            variable = self.music_preset
        )
        self.main_music_info_radio2.grid(row = 2, column = 0, pady = (10, 0), sticky = tk.W)

        # Music_Info Button
        self.main_music_info_btn = ttk.Button(
            self.main_music_info_frame, text = 'Explore',
            command = lambda: tk.messagebox.showwarning("WARNING", "This Session is on Development")
        )
        self.main_music_info_btn.grid(row = 3, column = 0, pady = (17, 0))

        # Main Buttons Frame
        self.main_main_buttons_frame = ttk.Frame(
            self, padding = (10, 10)
        )
        self.main_main_buttons_frame.pack()

        # Exit Button
        self.main_main_button_exit = ttk.Button(
            self.main_main_buttons_frame, text = 'Exit', width = 15,
            command = lambda: exit()
        )
        self.main_main_button_exit.grid(row = 0, column = 0, pady = (30, 0))

        # Resume Button
        self.main_main_button_resume = ttk.Button(
            self.main_main_buttons_frame, text = 'Resume', width = 15,
            command = lambda: tk.messagebox.showwarning("WARNING", "This Session is on Development")
        )
        self.main_main_button_resume.grid(row = 0, column = 1, pady = (30, 0), padx = (100, 0))

        # Mod Button
        self.main_main_button_mod = ttk.Button(
            self.main_main_buttons_frame, text = 'Build', width = 20, style="Accent.TButton",
            command = lambda: tk.messagebox.showwarning("WARNING", "This Session is on Development")
        )
        self.main_main_button_mod.grid(row = 0, column = 2, pady = (30, 0), padx = (20, 0))
        
        # Program Version
        self.main_main_button_version = ttk.Label(
            self.main_main_buttons_frame, text = f'minibuildergh3 {self.program_version}', 
            font = ('Helvetica', 9)
        )
        self.main_main_button_version.grid(row = 1, column = 0, columnspan = 3, pady = (25, 0))
        
    def images_main_root(self):
        
        tk.messagebox.showwarning("WARNING", "This Session is on Development")
        # -------------------------------

        # Load Images


        # -------------------------------

        # New Window Config

    def information_menu(self):
        self.menu_toplevel = tk.Toplevel()
        self.menu_toplevel.geometry('600x400')

        self.menu_main_frame = ttk.Frame(
            self.menu_toplevel, width = 270, height = 270
        )
        self.menu_main_frame.pack(pady = 10)

        self.menu_image = tk.Label(
            self.menu_main_frame, image = self.menu_minibuildergh3_img
        )
        self.menu_image.grid(row = 0, column = 0, pady = (50, 30), padx = (50, 0))

        self.menu_image2 = tk.Label(
            self.menu_main_frame, image = self.menu_harpy_img
        )
        self.menu_image2.grid(row = 0, column = 1, pady = (50, 30))

        self.menu_text = tk.Label(
            self.menu_main_frame, text = "This program was developed by HARPY™ with the objective of making it easy to mod\n Guitar Hero III: Legends of Rock for PS2.\nWe do not take responsability for creations generated using it.", 
            font = ('Arial', 9, 'bold')
        )
        self.menu_text.grid(row = 1, column = 0, columnspan = 3, pady = (0, 35))

        self.menu_program_version = ttk.Label(
            self.menu_toplevel, text = f'minibuildergh3 {self.program_version}', 
            font = ('Helvetica', 9)
        )
        self.menu_program_version.pack()


if __name__ == "__main__":
    App().mainloop()
