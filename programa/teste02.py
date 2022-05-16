import tkinter as tk 
   
  

   
window = tk.Tk() 
window.geometry("250x200") 
   
SVBar = tk.Scrollbar(window) 
SVBar.pack (side = tk.RIGHT,  
            fill = "y") 
   
SHBar = tk.Scrollbar(window,  
                     orient = tk.HORIZONTAL) 
SHBar.pack (side = tk.BOTTOM,  
            fill = "x") 
   
lb = tk.Listbox(window)
  
lb.pack(expand = 0, fill = tk.BOTH) 
   
lb.insert(tk.END, (i for i in range(100))) 
lb.insert(tk.END, (i for i in range(100))) 
   
SHBar.config(command = TBox.xview) 
SVBar.config(command = TBox.yview) 
   
window.mainloop() 