from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
class register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Form")
        self.root.geometry("1600x900+0+0")
        
        ##textvariable##
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contno = StringVar()
        self.var_email = StringVar()
        self.var_secqu = StringVar()
        self.var_secans = StringVar()
        self.var_passw = StringVar()
        self.var_cofpass = StringVar()
        
        ##bg image##
        self.bg = ImageTk.PhotoImage(file=r"F:\New folder (7)\1600900.jpg")
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        ##inner left image##
        self.bg1 = ImageTk.PhotoImage(file=r"F:\New folder (7)\business_solutions-1-470x550.png")
        inleft_lbl = Label(self.root,image=self.bg1)
        inleft_lbl.place(x=50,y=100,width=470,height=550)
        
        #frame design and header label#
        frame = Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl = Label(frame,text="REGISTER HERE",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #label and entry#
        ###row1###
        firstname = Label(frame,text="First Name",font=("Times New Roman",15,"bold"),bg="white")
        firstname.place(x=50,y=100)
        
        frnaentry = ttk.Entry(frame,textvariable=self.var_fname,font=("Times New Roman",15))
        frnaentry.place(x=50,y=130,width=250)
        
        lastname = Label(frame,text="Last Name",font=("Times New Roman",15,"bold"),bg="white")
        lastname.place(x=370,y=100)
        
        self.txt_lnnaentry = ttk.Entry(frame,textvariable=self.var_lname,font=("Times New Roman",15))
        self.txt_lnnaentry.place(x=370,y=130,width=250)
        
        ##row2##
        contactno = Label(frame,text="Contact No",font=("Times New Roman",15,"bold"),bg="white")
        contactno.place(x=50,y=170)
        
        self.txt_conentry = ttk.Entry(frame,textvariable=self.var_contno,font=("Times New Roman",15))
        self.txt_conentry.place(x=50,y=200,width=250)
        
        emailid = Label(frame,text="Email Id",font=("Times New Roman",15,"bold"),bg="white")
        emailid.place(x=370,y=170)
        
        self.txt_emidentry = ttk.Entry(frame,textvariable=self.var_email,font=("Times New Roman",15))
        self.txt_emidentry.place(x=370,y=200,width=250)
        
        ##row3##
        securityqn = Label(frame,text="Security Question",font=("Times New Roman",15,"bold"),bg="white")
        securityqn.place(x=50,y=240)
        
        self.var_secqn = ttk.Combobox(frame,textvariable=self.var_secqu,font=("Times New Roman",15),state="readonly")
        self.var_secqn["values"]=("Select","Your Birth Place","Your Favourite Book","Your Favourite Sports")
        self.var_secqn.place(x=50,y=270,width=250)
        self.var_secqn.current(0)
        
        securityans = Label(frame,text="Security Answer",font=("Times New Roman",15,"bold"),bg="white")
        securityans.place(x=370,y=240)
        
        self.txt_secansentry = ttk.Entry(frame,textvariable=self.var_secans,font=("Times New Roman",15))
        self.txt_secansentry.place(x=370,y=270,width=250)
        
        ##row4##
        password = Label(frame,text="Password",font=("Times New Roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
        
        self.txt_passentry = ttk.Entry(frame,textvariable=self.var_passw,font=("Times New Roman",15))
        self.txt_passentry.place(x=50,y=340,width=250)
        
        confirmpass = Label(frame,text="Confirm Password",font=("Times New Roman",15,"bold"),bg="white")
        confirmpass.place(x=370,y=310)
        
        self.txt_conpassentry = ttk.Entry(frame,textvariable=self.var_cofpass,font=("Times New Roman",15))
        self.txt_conpassentry.place(x=370,y=340,width=250)
        
        ##checkbutton##
        self.var_check = IntVar()
        checkbut = Checkbutton(frame,variable=self.var_check,text="I Agree to the 'Terms & Condition'",font=("Times New Roman",13),bg="white",onvalue=1,offvalue=0)
        checkbut.place(x=50,y=380)
        
        ##register and login button##
        img = Image.open(r"F:\New folder (7)\images (4).jpeg")
        img = img.resize((200,50),Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        regbut = Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2",font=("Times New Roman",15,"bold"),bg="white",activebackground="white")
        regbut.place(x=10,y=420,width=300)
        
        img1 = Image.open(r"F:\New folder (7)\images (5).jpeg")
        img1 = img1.resize((200,50),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        logbut = Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("Times New Roman",15,"bold"),bg="white",activebackground="white")
        logbut.place(x=330,y=420,width=300)
   
   ##Function Declaration##
    def register(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secqu.get()=="Select":
            messagebox.showerror("Error","All Field Required")
        elif self.var_passw.get()!= self.var_cofpass.get():
            messagebox.showerror("Invalid","Entered Password and Confirm Password should be same!")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Agree to Term and Condition")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
            mycursor = mydb.cursor()
            query = "SELECT * FROM register WHERE Email = %s"
            values = (self.var_email.get(),)
            mycursor.execute(query,values)
            row = mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists")
            else:
                mycursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contno.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_secqu.get(),
                                                                                     self.var_secans.get(),
                                                                                     self.var_passw.get()))
            
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Success","Register completed") 


if __name__=="__main__" :
    root = Tk()
    app = register_window(root)
    root.mainloop()