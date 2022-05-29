from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog

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
        main_main_cape_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/cape.jpg')
        main_main_cape_img = main_main_cape_img.resize((220, 300))
        self.main_main_cape_img = ImageTk.PhotoImage(main_main_cape_img)

        main_dir_img = Image.open(r'C:\Users\arthu\Desktop\MINIBUILDERGH3\_img/dir.png')
        main_dir_img = main_dir_img.resize((25, 20))
        self.main_dir_img = ImageTk.PhotoImage(main_dir_img)

        # Create control variables
        self.art_preset = tk.IntVar()
        self.music_preset = tk.StringVar()
        self.configs1 = tk.BooleanVar()
        self.configs2 = tk.BooleanVar()
        self.configs3 = tk.BooleanVar()

        #Program Version
        self.program_version = 'v. alfa0.01'

        # Create widgets
        self.main_main_window()

    def main_main_window(self):
        print(self.art_preset.get())
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
        

        self.teste = ttk.Label(self, text = self.art_preset.get())
        self.teste.pack()

        # Main_image Change Button Frame
        self.main_main_image_btn = tk.Button(
            self.main_sub_main_image_frame, text = 'Change', image = self.main_dir_img,
            background = '#333333', border = 3, relief=tk.FLAT, 
            state = (tk.DISABLED if self.art_preset.get() == 0 else tk.NORMAL), 
            command = lambda: self.search_cover_image()
        )
        self.main_main_image_btn.grid(row = 0, column = 1, padx = (10, 5))

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
            variable = self.art_preset, command = lambda: self.main_main_image_btn.config(state = tk.DISABLED)
        )
        self.main_art_info_radio1.grid(row = 1, column = 0, pady = (10, 0), sticky = tk.W)

        self.main_art_info_radio2 = ttk.Radiobutton(
            self.main_art_info_frame, text = 'Just the Cover', value = 1, 
            variable = self.art_preset, command = lambda: self.main_main_image_btn.config(state = tk.NORMAL)
        )
        self.main_art_info_radio2.grid(row = 2, column = 0, pady = (10, 0), sticky = tk.W)

        self.main_art_info_radio3 = ttk.Radiobutton(
            self.main_art_info_frame, text = 'Modify', value = 2, 
            variable = self.art_preset, command = lambda: self.main_main_image_btn.config(state = tk.NORMAL)
        )
        self.main_art_info_radio3.grid(row = 3, column = 0, pady = (10, 0), sticky = tk.W)

        # Art_Info Button
        self.main_art_info_btn = ttk.Button(
            self.main_art_info_frame, text = 'Explore',
            command = lambda: self.images_main_root()
        )
        self.main_art_info_btn.grid(row = 4, column = 0, pady = (17, 0))


if __name__ == "__main__":
    App().mainloop()