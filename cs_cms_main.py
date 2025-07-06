import os
from subprocess import call
import sys
from PIL import ImageTk,Image
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import mysql.connector
import tkinter as tk

root = Tk()
root.title("Contact List")
width = 800
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/1.5) - (width/1.5)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.state('zoomed')
root.resizable(0, 0)

def MainCallBack():
    os.system('python cs_cms_project_final.py')
    
def Close():
    root.destroy()
#==========================IMAGE=========================================    
image1 = tk.PhotoImage(file='name.png')
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (w, h))
Image_path=os.environ['TEMP']+"name.png"

#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width = 500, bg='white')
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100,bg='white')
MidLeft = Frame(Mid, highlightbackground = "black", 
                         highlightthickness = 2, bd=0)
MidLeft.pack(side=LEFT, pady=10)
MidRight = Frame(Mid, width=100,bg='white')
MidRight = Frame(Mid, highlightbackground = "white", 
                         highlightthickness = 2, bd=0)
MidRight.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(MidRight, width=370,bg='white',highlightbackground = "black", highlightthickness = 0, bd=0)
MidLeftPadding.pack(side=LEFT)

#============================LABELS======================================
lbl_title = Label(Top, text="VIEW CONTACT MANAGEMENT SYSTEM? Press Enter/Exit Button", font=('verdana', 16), width=500)
lbl_title.pack(fill=X)

#==========================IMAGE=========================================
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_enter = Button(MidLeft, text="ENTER", height =  1,width = 10, fg = 'black', bg = 'SlateBlue4',font = (("verdana"),22), command=MainCallBack)
btn_enter.pack(side=LEFT)

btn_exit = Button(MidRight, text="EXIT", height =  1,width = 10, fg = 'black', bg = 'brown3',font = (("verdana"),22),command=Close)
btn_exit.pack(side=RIGHT)

#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()

