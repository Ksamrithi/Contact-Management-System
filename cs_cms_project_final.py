from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import mysql.connector
import tkinter as tk
from tkinter.font import nametofont


root = Tk()
root.title("Contact List")
width = 800
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/1.5) - (width/1.5)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="gray11")
root.state('zoomed')


#============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()

#============================METHODS=====================================

def Database():
    conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS member (mem_id INTEGER NOT NULL  PRIMARY KEY AUTO_INCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT)")
    cursor.execute("SELECT * FROM member ORDER BY 'lastname' ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        
    else:
        tree.delete(*tree.get_children())
        conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
        cursor = conn.cursor()
        query = ("INSERT INTO member (firstname, lastname, gender, age, address, contact) VALUES(%s, %s, %s, %s, %s, %s)")
        val = (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()))
        cursor.execute(query, val)
        conn.commit()
        cursor.execute("SELECT * FROM member ORDER BY 'lastname' ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
    NewWindow.destroy()
        
def UpdateData():
 
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to update this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']        

            tree.delete(curItem)
            conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
            cursor = conn.cursor()   
            query = ("UPDATE member SET firstname = %s, lastname = %s, gender = %s, age = %s, address = %s, contact = %s WHERE mem_id = %s" )
            val = (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()),str(selecteditem[0]))
            cursor.execute(query, val)
            conn.commit()
            result = tkMessageBox.showinfo('', 'Updated Successfully!', icon="info")
            cursor.execute("SELECT * FROM member WHERE `mem_id` = %d" % selecteditem[0])
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            FIRSTNAME.set("")
            LASTNAME.set("")
            GENDER.set("")
            AGE.set("")
            ADDRESS.set("")
            CONTACT.set("")
    NewWindow.destroy()


            
def ViewData():
    
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
            cursor = conn.cursor()
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM member ORDER BY 'lastname' ASC")            
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            
            

def SearchData():
    
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
            cursor = conn.cursor()
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM member WHERE FIRSTNAME LIKE '%" + str(FIRSTNAME.get()) + "%'")            
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            NewWindow.destroy()

         
 
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = mysql.connector.connect(host ="localhost",port='3305',user ="root",passwd ="",database="sam")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM member WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            result = tkMessageBox.showinfo('', 'Deleted Successfully!', icon="info")
            cursor.close()
            conn.close()
def Close():
    root.destroy()
    
def AddNewWindow():#add new
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, 250, y))


    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 18)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 18)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Contacts", font=('verdana', 22), bg="chocolate2",  width = 400)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('arial', 18))
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name", font=('arial', 18))
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 18))
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 18))
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 18))
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact Number", font=('arial', 18))
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, width=55, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, width=55, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  width=55, font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  width=55, font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  width=55, font=('arial', 14))
    contact.grid(row=5, column=1)
    

    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", height =  1,width = 10, fg = 'black', font = (("verdana"),20), command=SubmitData,bg='grey')
    btn_addcon.grid(row=6, columnspan=2, pady=10)
    
def AddNewWindow2():#search
    global NewWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    FIRSTNAME.set("")
        
    NewWindow = Toplevel()
    NewWindow.title("Contact List Search")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, 250, y))
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 18)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 18)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Searching Existing Contacts", font=('verdana', 22), bg="dark red",  width = 400)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('arial', 18))
    lbl_firstname.grid(row=0, sticky=W)
    
    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, width=55, font=('arial', 14))
    firstname.grid(row=0, column=1)
    
    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Search", height =  1,width = 10, fg = 'black', font = (("verdana"),20), command=SearchData,bg="grey")
    btn_addcon.grid(row=6, columnspan=2, pady=10)
   
    
   
def AddNewWindow1():#update
    global NewWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:     
        FIRSTNAME.set(selecteditem[1])
        LASTNAME.set(selecteditem[2])
        GENDER.set(selecteditem[3])
        AGE.set(selecteditem[4])
        ADDRESS.set(selecteditem[5])
        CONTACT.set(selecteditem[6])
    
    
        NewWindow = Toplevel()
        NewWindow.title("Contact List")
        width = 800
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.resizable(0, 0)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, 250, y))
        
        #===================FRAMES==============================
        FormTitle = Frame(NewWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(NewWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm,bg="grey")
        Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 18)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 18)).pack(side=LEFT)
        
        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Updating Existing Contacts", font=('verdana', 22), bg="DarkGoldenrod1",  width = 400)
        lbl_title.pack(fill=X)
        lbl_firstname = Label(ContactForm, text="First Name", font=('arial', 18))
        lbl_firstname.grid(row=0, sticky=W)
        lbl_lastname = Label(ContactForm, text="Last Name", font=('arial', 18))
        lbl_lastname.grid(row=1, sticky=W)
        lbl_gender = Label(ContactForm, text="Gender", font=('arial', 18))
        lbl_gender.grid(row=2, sticky=W)
        lbl_age = Label(ContactForm, text="Age", font=('arial', 18))
        lbl_age.grid(row=3, sticky=W)
        lbl_address = Label(ContactForm, text="Address", font=('arial', 18))
        lbl_address.grid(row=4, sticky=W)
        lbl_contact = Label(ContactForm, text="Contact Number", font=('arial', 18))
        lbl_contact.grid(row=5, sticky=W)

        #===================ENTRY===============================

        firstname = Entry(ContactForm, textvariable=FIRSTNAME, width=55,font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = Entry(ContactForm, textvariable=LASTNAME, width=55,font=('arial', 14))
        lastname.grid(row=1, column=1)
        RadioGroup.grid(row=2, column=1)
        age = Entry(ContactForm, textvariable=AGE, width=55, font=('arial', 14))
        age.grid(row=3, column=1)
        address = Entry(ContactForm, textvariable=ADDRESS, width=55,  font=('arial', 14))
        address.grid(row=4, column=1)
        contact = Entry(ContactForm, textvariable=CONTACT,  width=55, font=('arial', 14))
        contact.grid(row=5, column=1)
        

        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save", height =  1,width = 10, fg = 'black', font = (("verdana"),20),command=UpdateData,bg="grey")
        btn_addcon.grid(row=6, columnspan=2, pady=10)


   
    
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,bg='gray11')
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100,bg='gray11')
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370,bg='gray11')
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100,bg='gray11')
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="CONTACT MANAGEMENT SYSTEM", font=('verdana', 24), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================

btn_add = Button(MidLeft, text="+ ADD NEW", height =  1, width = 10, fg = 'black', bg = 'lime green',font = (("verdana"),22), command=AddNewWindow)
btn_add.pack()



btn_update = Button(Mid, text="UPDATE", height =  1,width = 10, fg = 'black', bg = 'RoyalBlue1',font = (("verdana"),22), command=AddNewWindow1)
btn_update.pack(side=RIGHT)

btn_exit = Button(MidRight, text="EXIT", height =  1,width = 10, fg = 'black', bg = 'red',font = (("verdana"),22), command=Close)
btn_exit.pack(side=RIGHT)


btn_view = Button(MidRight, text="VIEW ALL", height =  1,width = 10, fg = 'black', bg = 'aquamarine1',font = (("verdana"),22), command=ViewData)
btn_view.pack(side=RIGHT)

btn_search = Button(MidRight, text="SEARCH", height =  1,width = 10, fg = 'black', bg = 'brown',font = (("verdana"),22), command=AddNewWindow2)
btn_search.pack(side=RIGHT)

btn_delete = Button(MidRight, text="DELETE", height =  1,width = 10, fg = 'black', bg = 'goldenrod1',font = (("verdana"),22), command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W,)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=10)
tree.column('#1', stretch=NO, minwidth=0, width=150)
tree.column('#2', stretch=NO, minwidth=0, width=150)
tree.column('#3', stretch=NO, minwidth=0, width=210)
tree.column('#4', stretch=NO, minwidth=0, width=180)
tree.column('#5', stretch=NO, minwidth=0, width=170)
tree.column('#6', stretch=NO, minwidth=0, width=350)
tree.column('#7', stretch=NO, minwidth=0, width=210)
style = ttk.Style()
style.configure("Treeview.Heading", font = (("verdana"),18))
style.configure("Treeview", highlightthickness=1, bd=1, font=('arial', 14))
tree.pack()


#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()

