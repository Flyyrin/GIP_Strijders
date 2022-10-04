from fileinput import filename
from createArticle import createArticle
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = Tk()
window.tk.call('tk', 'scaling', 2.0)
window.title("GIP Strijders blog aanmaken")
variable = StringVar(window)
OPTIONS = ["Rafael Lemmen","Michael van Walderveen"]
variable.set(OPTIONS[0])

def callback():
    titelV = str(titel.get("1.0","end"))
    textV = str(text.get("1.0","end"))
    catV = str(cat.get())
    authorV = str(option_Menu.get())
    filePath = str(fotoLabel.cget("text"))
    if titelV and textV and catV and authorV:
        if createArticle(catV, titelV, authorV, textV, filePath):
            messagebox.showinfo("Melding", "Blog is geplaats, vergeet niet te pushen!")
            window.quit()
    else:
        messagebox.showerror("Error", "Velden niet ingevuld!")

def foto():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Kies een foto", filetypes=[('Image Files', ('*jpeg', "*jpg", "*png"))])
    fotoLabel.configure(text=filename)
      

Label(window, text="Titel: ").pack()
titel = Text(window, height=1)
titel.pack()
Label(window, text=" ").pack()
Label(window, text="Catagory: ").pack()
cat = Entry(window)
cat.pack()
Label(window, text=" ").pack()
Label(window, text="Schrijver: ").pack()
option_Menu = StringVar(window)
author = OptionMenu(window,option_Menu, *OPTIONS)
author.pack()
Label(window, text=" ").pack()
fotoLabel = Label(window, text="Foto:")
fotoLabel.pack()
Button(window, text="Upload foto", width=10, command=foto).pack()
Label(window, text=" ").pack()
Label(window, text="Inhoud: ").pack()
text = Text(window, height=20)
text.pack()
Label(window, text=" ").pack()
Label(window, text=" ").pack()
Button(window, text="Post", width=10, command=callback).pack()

window.mainloop()