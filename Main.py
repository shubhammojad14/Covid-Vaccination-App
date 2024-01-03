from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import hashlib



# Add database
mypass = "root"
mydatabase="db"

con = pymysql.connect(user="root",password='Shubham@14',database='covid19')
cur = con.cursor()

#***********************Registration Window *************
def registration(): 
    
    global Info1,Info2,Info3,Info4,Info5,Canvas1,con,cur,Table,root
    
    root = Tk()
    root.title("Registeration")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")
     
    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
           
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Person Details", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
        
    # aadhar no.
    lb1 = Label(labelFrame,text="Aadhar No        : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Person Name
    lb2 = Label(labelFrame,text="Person Name      : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Date of Birth
    lb3 = Label(labelFrame,text="Date of Birth    : ", bg='black', fg='white',font=('Courier',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Phone No.
    lb4 = Label(labelFrame,text="Phone No.        : ", bg='black', fg='white',font=('Courier',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Address
    lb4 = Label(labelFrame,text="Address          : ", bg='black', fg='white',font=('Courier',15))
    lb4.place(relx=0.05,rely=0.80, relheight=0.08)
        
    Info5 = Entry(labelFrame)
    Info5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#d1ccc0', fg='black',font=('Courier',15),command=personregistration)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Exit",bg='#f7f1e3', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

def personregistration():
    #variables
    pid = StringVar()
    name = StringVar()
    dob = StringVar()
    phone = StringVar()
    add = StringVar()
    #get informtaion
    pid = "{}".format(Info1.get())
    name = "{}".format(Info2.get())
    dob = "{}".format(Info3.get())
    phone = "{}".format(Info4.get())
    add = "{}".format(Info5.get())
    
    insertdata = (pid,name,dob,phone,add)
    print(insertdata)
    try:
        cur.execute("""INSERT INTO register (aadhar,r_name,dob,phone_no,r_address) VALUES """+ str(insertdata))
        con.commit()
        messagebox.showinfo('Thank You',"person added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database") 
    
    root.destroy()

#***********************Person Login Window**************
def personlogin_verification():
    
    global aadhar,dob,ad
    aadhar = If1.get()
    dob = If2.get()

    sql = "select * from register where aadhar = %s and dob = %s"
    cur.execute(sql,[(aadhar),(dob)])
    results = cur.fetchall()
    if results:#login successful
        for i in results:
            messagebox.showinfo("Login","Login Successful !")
            persond()
            break
    else:#login failed
        messagebox.showerror(title="Invalid Message",message="Invalid Username or Password")

    root.destroy()

def personlogin():
    global If1,If2,Canvas1,con,cur,Table,root

    If1 = StringVar()  
    
    root = Tk()
    root.title("person login")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")


    

    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#188075")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Person Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Aadhar No       : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2)
        
    If1 = Entry(labelFrame,font=('Courier',13))
    If1.place(relx=0.3,rely=0.2, relwidth=0.62,relheight=0.08)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Date of Birth   : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.4)
        
    If2 = Entry(labelFrame,font=('Courier',13))
    If2.place(relx=0.3,rely=0.4, relwidth=0.62,relheight=0.08)
    
    
    #Issue Button
    issueBtn = Button(root,text="Login",bg='#d1ccc0', fg='black',font=('Courier',15),command=personlogin_verification)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Exit",bg='#aaa69d', fg='black',font=('Courier',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
   
#*********************Person Window ******************
def persond():
    root = Tk()
    root.title("person details")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

   
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    #view of main window

    headingLabel = Label(headingFrame1, text="Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Personal details",bg='black', fg='white',font=('Courier',15), command=View1)#displayperson
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Vaccine Details",bg='black', fg='white',font=('Courier',15), command=View2)#vaccine
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="Incoming vaccine",bg='black', fg='white',font=('Courier',15), command=View7)#coming vaccine
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    issueBtn = Button(root,text="Exit",bg='black', fg='white',font=('Courier',15),command=root.destroy)
    issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)

#Person Details 
def View1(): 

    global personid

    root = Tk()
    root.title("person details")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("700x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.11)
        
    headingLabel = Label(headingFrame1, text="View person details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)

    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=persond)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    y = 0.25
            
    Label(labelFrame, text="%-15s%-15s%-15s%-20s%-10s"%('Aadhar No','Person Name','Date Of Birth','Phone No','Address'),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-------------------------------------------------------------------------------------------------------------------------------------"
    "--------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
        
    personid = str(aadhar)
    print(personid)
    
    reg = "select * from register where aadhar = "+personid
    try:
        cur.execute(reg)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-15s%-15s%-15s%-20s%-10s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
        persond()
        
       
    root.mainloop()

#Vaccine Chart
def View2(): 
    
    root = Tk()
    root.title("Vaccine details")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "vaccine" 
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Vaccine Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-20s%-20s%-20s%-20s"%('Vaccine Id','Vaccine Name','No of Dose','Next Dose'),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------"
    "--------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    vaccine = "select * from "+Table
    try:
        cur.execute(vaccine)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch data from database")
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#incoming Vaccine
def View7(): 
    
    root = Tk()
    root.title("Incoming vaccine")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "comingv"
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Incoming Vaccine", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-5s%-15s%-15s%-15s%-20s%-20s"%('Id','Vaccine Name','No Of Vaccine','Date','Location','Address'),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------------"
    "--------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    getdetails = "select * from "+Table
    try:
        cur.execute(getdetails)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-5s%-15s%-15s%-15s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


#*******************Admin login Window***************************
def adminlogin_verification2():

    global aadhar2,dob2
    aadhar2 = If5.get()
    dob2 = If6.get()
    sql = "select * from admin where aadhar_no = %s and dob = %s"
    cur.execute(sql,[(aadhar2),(dob2)])
    results = cur.fetchall()
    if results:
        for i in results:
            messagebox.showinfo("Login","Login Successful !")
            admin()
            break
    else:
        messagebox.showerror(title="Invalid Message",message="Invalid Username or Password")
    
    root.destroy()

def adminlogin(): 
    
    global If5,If6,Canvas1,con,cur,Table,root,aadhar2,dob2
    
    root = Tk()
    root.title("admin login")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")


    

    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#188075")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Admin Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Aadhar No       : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2)
        
    If5 = Entry(labelFrame,font=('Courier',13))
    If5.place(relx=0.3,rely=0.2, relwidth=0.62,relheight=0.08)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Date of Birth   : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.4)
        
    If6 = Entry(labelFrame,font=('Courier',13))
    If6.place(relx=0.3,rely=0.4, relwidth=0.62,relheight=0.08)
    
    
    #Issue Button
    issueBtn = Button(root,text="Login",bg='#d1ccc0', fg='black',font=('Courier',15),command=adminlogin_verification2)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Exit",bg='#aaa69d', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

#*****************Admin Window *********************
def admin():
    root = Tk()
    root.title("admin")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#4C7EF4")
    Canvas1.pack(expand=True,fill=BOTH)
   

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    #view of main window

    headingLabel = Label(headingFrame1, text="Admin ", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Admin detais",bg='black', fg='white', command=View5)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Update person",bg='black', fg='white', command=updateperson)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="Registration Details",bg='black', fg='white', command=regdetails)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Vaccine",bg='black', fg='white', command=view8)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    #btn4 = Button(root,text="Non-vaccinated",bg='black', fg='white', command=View4)
    #btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    issueBtn = Button(root,text="Exit",bg='black', fg='white',command=root.destroy)
    issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
#Admin Details  / upadte person  / registration Detsils  / vaccine    
# admin details 
def View5():
    global add2

    root = Tk()
    root.title("covid19")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "register"

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Admin details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=admin)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    y = 0.25   
    
    
    Label(labelFrame, text="%-20s%-30s%-20s%-10s"%('Aadhar No.','Date of Birth','Admin Name','Address'),bg='black',fg='white',font=('Courier',10)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------------------------------------------------------"
    "----------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    adminid = str(aadhar2)
    register = "select * from admin where aadhar_no = "+adminid
    try:
        cur.execute(register)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-20s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white',font=('Courier',10)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
       
    root.mainloop()

#********************  update person   ************
def updateperson():
    
    root = Tk()
    root.title("person update")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#4C7EF4")
    Canvas1.pack(expand=True,fill=BOTH)
   

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    #view of main window

    headingLabel = Label(headingFrame1, text="Update Person", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Person",bg='black', fg='white',font=('Courier',15), command=addperson)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Person Vaccine Update",bg='black', fg='white',font=('Courier',15),command=update)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="Delete Person",bg='black', fg='white',font=('Courier',15),command=delete)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    """btn4 = Button(root,text="vaccinated",bg='black', fg='white', command=View6)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Non-vaccinated",bg='black', fg='white', command=View4)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)"""

    issueBtn = Button(root,text="Back",bg='black', fg='white',command=admin)
    issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

# Add Person
def addperson(): 
    
    global Info1,Info2,Info3,Info4,Info5,Canvas1,con,cur,Table,root
    
    root = Tk()
    root.title("Registeration")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")
     
    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
           
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Person Details", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
        
    # aadhar no.
    lb1 = Label(labelFrame,text="Aadhar No        : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    Info1 = Entry(labelFrame)
    Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Person Name
    lb2 = Label(labelFrame,text="Person Name      : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    Info2 = Entry(labelFrame)
    Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Date of Birth
    lb3 = Label(labelFrame,text="Date of Birth    : ", bg='black', fg='white',font=('Courier',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Info3 = Entry(labelFrame)
    Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Phone No.
    lb4 = Label(labelFrame,text="Phone No.        : ", bg='black', fg='white',font=('Courier',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Info4 = Entry(labelFrame)
    Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Address
    lb4 = Label(labelFrame,text="Address          : ", bg='black', fg='white',font=('Courier',15))
    lb4.place(relx=0.05,rely=0.80, relheight=0.08)
        
    Info5 = Entry(labelFrame)
    Info5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#d1ccc0', fg='black',font=('Courier',15),command=addpersonregistration)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
def addpersonregistration():
    #variables
    pid = StringVar()
    name = StringVar()
    dob = StringVar()
    phone = StringVar()
    add = StringVar()
    #get informtaion
    pid = "{}".format(Info1.get())
    name = "{}".format(Info2.get())
    dob = "{}".format(Info3.get())
    phone = "{}".format(Info4.get())
    add = "{}".format(Info5.get())
    
    insertdata = (pid,name,dob,phone,add)
    print(insertdata)
    try:
        cur.execute("""INSERT INTO register (aadhar,r_name,dob,phone_no,r_address) VALUES """+ str(insertdata))
        con.commit()
        messagebox.showinfo('Thank You',"Person added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database") 
    
    root.destroy()

# Update Person vaccinated
def updateinsert():
    #variables
    aadhar = StringVar()
    v_name = StringVar()
    dose1 = StringVar()
    dose2= StringVar()
    #get informtaion
    aadhar = "{}".format(Ifo1.get())
    v_name = "{}".format(Ifo2.get())
    dose1 = "{}".format(Ifo3.get())
    dose2 = "{}".format(Ifo4.get())
    
    
    insertdata = (aadhar,v_name,dose1,dose2)
    print(insertdata)
    try:
        cur.execute("""INSERT INTO vaccinated(aadhar,v_name,dose1,dose2) VALUES """+ str(insertdata))
        con.commit()
        messagebox.showinfo('Success',"Records added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    


    root.destroy()
def update(): 
    
    global Ifo1,Ifo2,Ifo3,Ifo4,Ifo5,Canvas1,con,cur,Table,root,vlist,v
    
    root = Tk()
    root.title("covid19")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    # Add database 
    mypass = "root"
    mydatabase="db"

    con = pymysql.connect(user="root",password='Shubham@14',database='covid19')
    cur = con.cursor()

   
    # Enter Table Names here
    Table = "vaccinated" #Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update Person Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # aadhar no.
    lb1 = Label(labelFrame,text="Aadhar No. : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    Ifo1 = Entry(labelFrame)
    Ifo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # vaccine Name
    lb2 = Label(labelFrame,text="Vaccine Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)

    #vaccine list
    vlist = ['covain','covisheid','sputnik','etc']
    v = StringVar()

    droplist = ttk.Combobox(root,values=['covain','covisheid','sputnik','etc'])
    droplist.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)    
    """Ifo2 = Entry(labelFrame)
    Ifo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)"""
        
    # Dose1
    lb3 = Label(labelFrame,text="Dose 1 : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    Ifo3 = Entry(labelFrame)
    Ifo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # dose2
    lb4 = Label(labelFrame,text="Dose 2 ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    Ifo4 = Entry(labelFrame)
    Ifo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=updateinsert)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

#  Delete Person
def delete_verify():
    
    global pd1,pd2
        
    pd1 = d1.get()
    pd2 = d2.get()
    sql2 = "delete from register where aadhar ="+ str(pd1) +" and dob = '" + str(pd2)+"'"
    try:
        cur.execute(sql2)
        con.commit()
        messagebox.showinfo("Person Delete","Delete Succesfully !")
        
    except:
        messagebox.showerror(title="Invalid Message",message="Invalid Username or Password")
    print(sql2)
    updateperson()
    root.destroy()
def delete(): 
    
    global d1,d2,Canvas1,con,cur,Table,root,aadhar22,dob22
    
    root = Tk()
    root.title("delete person")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")


    

    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#188075")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Enter Person Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Aadhar No       : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2)
        
    d1 = Entry(labelFrame,font=('Courier',13))
    d1.place(relx=0.3,rely=0.2, relwidth=0.62,relheight=0.08)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Date of Birth   : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.4)
        
    d2 = Entry(labelFrame,font=('Courier',13))
    d2.place(relx=0.3,rely=0.4, relwidth=0.62,relheight=0.08)
    
    
    #Issue Button
    issueBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',font=('Courier',15),command=delete_verify)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Back",bg='#aaa69d', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


#********************** Registration Details **********
def regdetails():
    root = Tk()
    root.title("person update")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#4C7EF4")
    Canvas1.pack(expand=True,fill=BOTH)
   

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    #view of main window

    headingLabel = Label(headingFrame1, text="Registration Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Total Registered",bg='black', fg='white',font=('Courier',15), command=View3)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Vaccinated",bg='black', fg='white',font=('Courier',15),command=View6)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="Non Vaccinated",bg='black', fg='white',font=('Courier',15),command=View4)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    """btn4 = Button(root,text="vaccinated",bg='black', fg='white', command=View6)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Non-vaccinated",bg='black', fg='white', command=View4)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)"""

    issueBtn = Button(root,text="Back",bg='black', fg='white',command=admin)
    issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
#Total Person Registeration    
def View3(): 
    
    root = Tk()
    root.title("registered")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "register"
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Total registered", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-15s%-15s%-20s%-20s%-10s"%('Aadhar No','Person Name','Date Of Birth','Phone No','Address'),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-------------------------------------------------------------------------------------------------------------------------------------"
    "--------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
        
    getdetails = "select * from "+Table
    try:
        cur.execute(getdetails)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-15s%-15s%-20s%-20s%-10s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=regdetails)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#Total vaccinated    
def View6(): 
    
    root = Tk()
    root.title("covid19")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "vaccinated"
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Total vaccinated", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-20s%-20s%-20s%-20s%-20s"%('Vaccine Id','Aadhar No.','Vaccine Name','Dose 1','Dose 2',),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------"
    "-------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
        
    register = "select * from "+Table
    try:
        cur.execute(register)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-20s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=regdetails)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

#  Non Vaccinated 
def View4(): 
    
    root = Tk()
    root.title("covid19")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")

    Table = "register"
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Non Vaccinated details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=regdetails)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    y = 0.25
    
    
    Label(labelFrame, text="%-15s%-20s%-20s%-20s%-20s"%('Aadhar No.','Name','Date of Birth','Phone','Address'),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="------------------------------------------------------------------------------------------------------------------------------------"
    "---------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

    nonreg = "select * from register where aadhar not in(select aadhar from vaccinated);"
    try:
        cur.execute(nonreg)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-15s%-20s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white',font=('Courier',15)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=regdetails)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


#***************  Vaccine details  *******************
def view8():
    
    root = Tk()
    root.title("person update")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#4C7EF4")
    Canvas1.pack(expand=True,fill=BOTH)
   

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    #view of main window

    headingLabel = Label(headingFrame1, text="Update Vaccine", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Vaccine",bg='black', fg='white',font=('Courier',15), command=addvaccine)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Delete Vaccine",bg='black', fg='white',font=('Courier',15),command=delvaccine)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="Incoming Vaccine ",bg='black', fg='white',font=('Courier',15),command=invaccine)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    """btn4 = Button(root,text="vaccinated",bg='black', fg='white', command=View6)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Non-vaccinated",bg='black', fg='white', command=View4)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)"""

    issueBtn = Button(root,text="Back",bg='black', fg='white',command=admin)
    issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()


# Update vaccine chart
def addvaccineinsert():
    #variables
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    #get informtaion
    v1 = "{}".format(av1.get())
    v2 = "{}".format(av2.get())
    v3 = "{}".format(av3.get())
    v4 = "{}".format(av4.get())
  
    
    insertdata = (v1,v2,v3,v4)
    print(insertdata)
    try:
        cur.execute("""INSERT INTO vaccine(ID,v_name,dose,D1_Difference_D2) VALUES """+ str(insertdata))
        con.commit()
        messagebox.showinfo('Success',"Records Updated successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
        view8()
    root.destroy()
def addvaccine(): 
    global av1,av2,av3,av4
    
    root = Tk()
    root.title("covid19")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")

    

   
    # Enter Table Names here
    Table = "vaccine" #Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update Vaccine Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # aadhar no.
    lb1 = Label(labelFrame,text="Vaccine Id :", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    av1 = Entry(labelFrame)
    av1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # vaccine Name
    lb2 = Label(labelFrame,text="Vaccine Name  :", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)

    av2 = Entry(labelFrame)
    av2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Dose1
    lb3 = Label(labelFrame,text="No of Dose : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    av3 = Entry(labelFrame)
    av3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # dose2
    lb4 = Label(labelFrame,text="Difference (Days) :", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    av4 = Entry(labelFrame)
    av4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="Update",bg='#d1ccc0', fg='black',command=addvaccineinsert)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=view8)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

# delete vaccine
# 
def delete_vaccine():
    
    global pd11,pd21
        
    pd11 = d11.get()
    pd21 = d21.get()
    sql21 = "delete from vaccine where ID ="+ str(pd11) +" and v_name = '" + str(pd21)+"'"
    try:
        cur.execute(sql21)
        con.commit()
        messagebox.showinfo("Person Delete","Delete Succesfully !")
        
    except:
        messagebox.showerror(title="Invalid Message",message="Invalid Username or Password")
    print(sql2)
    updateperson()
    root.destroy()
def delvaccine(): 
    
    global d11,d21,Canvas1,con,cur,Table,root,aadhar22,dob22
    
    root = Tk()
    root.title("delete vaccine chart")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x500")


    

    # Enter Table Names here
    Table = "register" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#188075")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Enter Vaccine Details", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Vaccine Id       : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.2)
        
    d11 = Entry(labelFrame,font=('Courier',13))
    d11.place(relx=0.3,rely=0.2, relwidth=0.62,relheight=0.08)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Vaccine Name : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.4)
        
    d21 = Entry(labelFrame,font=('Courier',13))
    d21.place(relx=0.3,rely=0.4, relwidth=0.62,relheight=0.08)
    
    
    #Issue Button
    issueBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',font=('Courier',15),command=delete_vaccine)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Back",bg='#aaa69d', fg='black',font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Update Incoming Vaccine
def invaccineinsert():
    global s1,s2,s3,s4,s5,s6
    #variables
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4= StringVar()
    s5 = StringVar()
    s6 = StringVar()
    #get informtaion
    s1 = "{}".format(iv1.get())
    s2 = "{}".format(iv2.get())
    s3 = "{}".format(iv3.get())
    s4 = "{}".format(iv4.get())
    s5 = "{}".format(iv5.get())
    s6 = "{}".format(iv6.get())
    
    
    insertdata2 = (s1,s2,s3,s4,s5,s6)
    print(insertdata2)
    try:
        cur.execute("""INSERT INTO comingv(c_id,vaccine_name,no_of_vaccine,coming_date,area,place) VALUES """+ str(insertdata2))
        con.commit()
        messagebox.showinfo('Success',"Records Updated successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
        invaccine()
    
    root.destroy()
def invaccine(): 
    
    global iv1,iv2,iv3,iv4,iv5,iv6,root,Table,con,cur
    
    root = Tk()
    root.title("Registeration")
    root.minsize(width=400,height=400)
    root.attributes('-fullscreen', True)
    #root.geometry("600x600")
        
    # Enter Table Names here
    Table = "comingv" #Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
            
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Incoming Vaccine Details", bg='black', fg='white', font=('Courier',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
        
    # aadhar no.
    lb1 = Label(labelFrame,text="Id : ", bg='black', fg='white',font=('Courier',15))
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    iv1= Entry(labelFrame)
    iv1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08)
        
    # Person Name
    lb2 = Label(labelFrame,text="Vaccine Name      : ", bg='black', fg='white',font=('Courier',15))
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    iv2 = Entry(labelFrame)
    iv2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)
        
    # Date of Birth
    lb3 = Label(labelFrame,text="No Of Vaccine :",bg='black', fg='white',font=('Courier',15))
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
        
    iv3 = Entry(labelFrame)
    iv3.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)
        
    # Phone No.
    lb4 = Label(labelFrame,text="Date      : ", bg='black', fg='white',font=('Courier',15))
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    iv4 = Entry(labelFrame)
    iv4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

    # Address
    lb5 = Label(labelFrame,text="Location          : ", bg='black', fg='white',font=('Courier',15))
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
        
    iv5 = Entry(labelFrame)
    iv5.place(relx=0.3,rely=0.70, relwidth=0.62, relheight=0.08)

    # Address
    lb6 = Label(labelFrame,text="Area         : ", bg='black', fg='white',font=('Courier',15))
    lb6.place(relx=0.05,rely=0.85, relheight=0.08)
        
    iv6 = Entry(labelFrame)
    iv6.place(relx=0.3,rely=0.85, relwidth=0.62, relheight=0.08)

    #Submit Button
    SubmitBtn = Button(root,text="Update",bg='#d1ccc0', fg='black',font=('Courier',15),command=invaccineinsert)
    SubmitBtn.place(relx=0.28,rely=0.86, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Back",bg='#f7f1e3', fg='black',font=('Courier',15), command=view8)
    quitBtn.place(relx=0.53,rely=0.86, relwidth=0.18,relheight=0.08)

    root.mainloop()

#****************** Main Window **************
root = Tk()
root.title("covid19 system")
root.minsize(width=400,height=400)
root.attributes('-fullscreen', True)
#root.geometry("1500x750")

# Take n greater than 0.25 and less than 5
same=True
n=0.30

# Adding a background image
background_image =Image.open("F:\Final Projects Imp\Covid19 Vaccination System\person.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n)
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(750,300,anchor= CENTER,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

#view of main window

headingLabel = Label(headingFrame1, text="Welcome to \n Covid-19 Vaccine System", bg='black', fg='white', font=('Courier',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Registration",bg='black', fg='white', command=registration)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
   
btn2 = Button(root,text="Admin Login",bg='black', fg='white', command=adminlogin)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Person Login",bg='black', fg='white', command=personlogin)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

issueBtn = Button(root,text="Exit",bg='black', fg='white',command=root.destroy)
issueBtn.place(relx=0.41,rely=0.9, relwidth=0.18,relheight=0.08)


root.mainloop()