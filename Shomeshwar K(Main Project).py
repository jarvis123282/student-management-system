from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    windows = Tk()
    app = login_window(windows)
    windows.mainloop()


class login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")
        
        
        self.bg = ImageTk.PhotoImage(file=r"F:\New folder (7)\bike.jpeg")
        label1 = Label(self.root,image=self.bg)
        label1.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame = Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1 = Image.open(r"F:\New folder (7)\logo1.png")
        img1 = img1.resize((100,100),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        label2 = Label(image = self.photoimage1,bg="white",borderwidth=0)
        label2.place(x=730,y=175,width=100,height=100)
        
        get_str = Label(frame,text="Get Started",font=("Times New Roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
        
        ##label##
        username = lab1 =Label(frame,text="Username",font=("Times New Roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)
        
        self.txt_user = StringVar()
        self.txtuser = ttk.Entry(frame,textvariable=self.txt_user,font=("Times New Roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password = lab1 = Label(frame,text="Password",font=("Times New Roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)
        
        self.txt_pass = StringVar()
        self.txtpass = ttk.Entry(frame,textvariable=self.txt_pass,font=("Times New Roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        
        ####icon image####
        img2 = Image.open(r"F:\New folder (7)\logo1.png")
        img2 = img2.resize((25,25),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        label2 = Label(image = self.photoimage2,bg="white",borderwidth=0)
        label2.place(x=650,y=323,width=25,height=25)
        
        img3 = Image.open(r"F:\New folder (7)\pngegg.png")
        img3 = img3.resize((25,25),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        label2 = Label(image = self.photoimage3,bg="white",borderwidth=0)
        label2.place(x=650,y=395,width=25,height=25)
        
        #login button
        loginbutton = Button(frame,command=self.login,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,fg="red",bg="white",
                             activeforeground="red",activebackground="white")
        loginbutton.place(x=110,y=300,width=120,height=35)
        
        #new register button
        newregisterbutton = Button(frame,text="New User Register",command=self.regwin,font=("Times New Roman",10,"bold"),borderwidth=0,fg="black",bg="white",
                             activeforeground="white",activebackground="white")
        newregisterbutton.place(x=15,y=350,width=160)
        
        #forgot password
        frpassbutton = Button(frame,text="Forgot Password",command=self.forgot_pass,font=("Times New Roman",10,"bold"),borderwidth=0,fg="black",bg="white",
                             activeforeground="white",activebackground="white")
        frpassbutton.place(x=10,y=370,width=160)
    
    def regwin(self):
        self.new_win = Toplevel(self.root)
        self.app = register_window(self.new_win)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="shom" and self.txtpass.get()=="1234":
            messagebox.showinfo("Successful","Welcome to my blogspot")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM register WHERE Email=%s AND Password=%s",(self.txt_user.get(),
                                                                                      self.txt_pass.get()))
            
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("Confirmation","Access only Admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Student(self.new_window)
                else:
                    if not open_main:
                        return 
                       
            
            mydb.commit()
            mydb.close()
    
    def reset_pass(self):
        if self.var_secans.get()=="" or self.var_secqu.get()=="" or self.txt_npassentry.get()=="":
            messagebox.showerror("Error","Enter all Field")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
            mycursor = mydb.cursor()
            qry2 = "SELECT * FROM register WHERE Email=%s AND SecurityQuestion=%s AND SecurityAnswer=%s"
            val2 = (self.txt_user.get(),self.var_secqu.get(),self.var_secans.get(),)
            mycursor.execute(qry2,val2)
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter the Security Answer")
            else:
                qry3 = "UPDATE register SET Password=%s WHERE Email=%s"
                val3 = (self.txt_npassentry.get(),self.txt_user.get())
                mycursor.execute(qry3,val3)
                
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Success"," Password successfully changed")
                
            
            
    def forgot_pass(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Enter the Username")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
            mycursor = mydb.cursor()
            qry1 = "SELECT * FROM register WHERE Email=%s"
            val1 = (self.txt_user.get(),)
            mycursor.execute(qry1,val1)
            row1 = mycursor.fetchone()
            if row1==None:
                messagebox.showerror("Error","Enter a valid Username")
            else:
                self.root2 = Toplevel(self.root)
                self.root2.title("Forgot Password")
                self.root2.geometry("320x400+620+250")
                self.root2.resizable(0,0)
                
                label_1 = Label(self.root2,text="Forgot password",font=("Times New Roman",20,"bold"))
                label_1.pack()
                
                self.var_secqu = StringVar()
                self.var_secans = StringVar()
                
                securityqn = Label(self.root2,text="Security Question",font=("Times New Roman",15,"bold"),bg="white")
                securityqn.pack(pady=10)
                
                
                self.comsec = ttk.Combobox(self.root2,textvariable=self.var_secqu,font=("Times New Roman",15),state="readonly")
                self.comsec["values"]=("Select","Your Birth Place","Your Favourite Book","Your Favourite Sports")
                self.comsec.pack(pady=10)
                self.comsec.current(0)
        
                securityans = Label(self.root2,text="Security Answer",font=("Times New Roman",15,"bold"),bg="white")
                securityans.pack(pady=10)
                
                self.txt_secansentry = ttk.Entry(self.root2,textvariable=self.var_secans,font=("Times New Roman",15))
                self.txt_secansentry.pack(pady=10)
                
                newpass = Label(self.root2,text="New Password",font=("Times New Roman",15,"bold"),bg="white")
                newpass.pack(pady=10)
                
                self.txt_npassentry = StringVar()
                self.txt_newpass = ttk.Entry(self.root2,textvariable=self.txt_npassentry,font=("Times New Roman",15))
                self.txt_newpass.pack(pady=10)
                
                resetbutton = Button(self.root2,text="RESET",command=self.reset_pass,font=("Times New Roman",15),borderwidth=5)
                resetbutton.pack(pady=10)
                
                mydb.commit()
                mydb.close()
        
            
            
            
    
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
        
        self.comsec = ttk.Combobox(frame,textvariable=self.var_secqu,font=("Times New Roman",15),state="readonly")
        self.comsec["values"]=("Select","Your Birth Place","Your Favourite Book","Your Favourite Sports")
        self.comsec.place(x=50,y=270,width=250)
        self.comsec.current(0)
        
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
            
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1530x790+0+0")
        
        ##variables##
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_rollno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phoneno = StringVar()
        self.var_add = StringVar()
        self.var_doa = StringVar()
        
        img = Image.open(r"F:\New folder (7)\word.jpg")
        img = img.resize((540,160),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        self.label1 = Label(self.root,image=self.photoimg,cursor="hand2")
        self.label1.place(x=0,y=0,width=540,height=160)
        
        img1 = Image.open(r"F:\New folder (7)\word1.jpg")
        img1 = img1.resize((540,160),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.label2 = Label(self.root,image=self.photoimg1,cursor="hand2")
        self.label2.place(x=540,y=0,width=540,height=160)
        
        img2 = Image.open(r"F:\New folder (7)\word3.jpg")
        img2 = img2.resize((540,160),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.label3 = Label(self.root,image=self.photoimg2,cursor="hand2")
        self.label3.place(x=1080,y=0,width=540,height=160)
        
        ##Title##
        lbl_title = Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("Times New Roman",37,"bold"),bg="white",fg="blue")
        lbl_title.place(x=0,y=160,width=1530,height=50)
        
        ##bgframe##
        bg_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bg_frame.place(x=15,y=215,width=1500,height=560)
        
        ##leftframe##
        left_frame = LabelFrame(bg_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Times New Roman",13,"bold"),bg="white",fg="red")
        left_frame.place(x=10,y=10,width=660,height=540)
        
        img3 = Image.open(r"F:\New folder (7)\unversity.jfif")
        img3 = img3.resize((640,120),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.label4 = Label(left_frame,image=self.photoimg3,cursor="hand2")
        self.label4.place(x=5,y=0,width=640,height=120)
        
        left_frame1 = LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text="Course Information",font=("Times New Roman",13,"bold"),bg="white",fg="red")
        left_frame1.place(x=5,y=120,width=640,height=115)
        
        ##leftframe1 labels##
        #department#
        lbl_dept = Label(left_frame1,text="Department",font=("Times New Roman",12,"bold"),bg="white")
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)
        
        com_dept = ttk.Combobox(left_frame1,textvariable=self.var_dept,font=("Times New Roman",12),width=17,state="readonly")
        com_dept["values"] = ("Select Department","Civil","CSE","ECE","EEE","Mech","Maths","Physics","Chemistry")
        com_dept.current(0)
        com_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #courses#
        lbl_course = Label(left_frame1,text="Courses",font=("Times New Roman",12,"bold"),bg="white")
        lbl_course.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        com_course = ttk.Combobox(left_frame1,textvariable=self.var_course,font=("Times New Roman",12),width=17,state="readonly")
        com_course["values"] = ("Select Courses","BE","ME","BSc","MSc","MCA")
        com_course.current(0)
        com_course.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year#
        lbl_year = Label(left_frame1,text="Year",font=("Times New Roman",12,"bold"),bg="white")
        lbl_year.grid(row=1,column=0,padx=2,pady=10,sticky=W)
            
        com_year = ttk.Combobox(left_frame1,textvariable=self.var_year,font=("Times New Roman",12),width=17,state="readonly")
        com_year["values"] = ("Select Year","2014-2018","2015-2019","2016-2020","2017-2021","2018-2022",
                              "2019-2023")
        com_year.current(0)
        com_year.grid(row=1,column=1,padx=2,sticky=W)
        
        #semester#
        lbl_semester = Label(left_frame1,text="Semester",font=("Times New Roman",12,"bold"),bg="white")
        lbl_semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        
        com_semester = ttk.Combobox(left_frame1,textvariable=self.var_sem,font=("Times New Roman",12),width=17,state="readonly")
        com_semester["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        com_semester.current(0)
        com_semester.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        left_frame2 = LabelFrame(left_frame,bd=4,relief=RIDGE,padx=2,text="Class Information",font=("Times New Roman",13,"bold"),bg="white",fg="red")
        left_frame2.place(x=5,y=235,width=640,height=235)
        
        ##leftframe2 labels##
        #id#
        lbl_id = Label(left_frame2,text="Students Id:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_id.grid(row=0,column=0,padx=2,pady=7,sticky=W)
        
        id_entry = ttk.Entry(left_frame2,textvariable=self.var_id,font=("Times New Roman",12),width=22)
        id_entry.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        
        #name#
        lbl_name = Label(left_frame2,text="Students Name:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_nameentry = ttk.Entry(left_frame2,textvariable=self.var_name,font=("Times New Roman",12),width=22)
        txt_nameentry.grid(row=0,column=3,padx=2,pady=7)
        
        #division#
        lbl_division = Label(left_frame2,text="Class Division:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_division.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        com_txt_div = ttk.Combobox(left_frame2,textvariable=self.var_div,font=("Times New Roman",12),width=18,state="readonly")
        com_txt_div["values"] = ("Select Division","A","B","C","D")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        #rollno#
        lbl_rollno = Label(left_frame2,text="Roll No:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_rollno.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        
        txt_rollno = ttk.Entry(left_frame2,textvariable=self.var_rollno,font=("Times New Roman",12),width=22)
        txt_rollno.grid(row=1,column=3,padx=2,pady=7)
        
        #gender#
        lbl_gender = Label(left_frame2,text="Gender:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_gender.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        com_txt_gen = ttk.Combobox(left_frame2,textvariable=self.var_gender,font=("Times New Roman",12),width=18,state="readonly")
        com_txt_gen["values"] = ("Select Gender","Male","Female","Others")
        com_txt_gen.current(0)
        com_txt_gen.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        
        #dob#
        lbl_dob = Label(left_frame2,text="DOB:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_dob.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        
        txt_dob = ttk.Entry(left_frame2,textvariable=self.var_dob,font=("Times New Roman",12),width=22)
        txt_dob.grid(row=2,column=3,padx=2,pady=7)
        
        #email#
        lbl_email = Label(left_frame2,text="Email:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_email.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        txt_email = ttk.Entry(left_frame2,textvariable=self.var_email,font=("Times New Roman",12),width=22)
        txt_email.grid(row=3,column=1,padx=2,pady=7)
        
        #phoneno#
        lbl_phoneno = Label(left_frame2,text="Phone No:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_phoneno.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        
        txt_phoneno = ttk.Entry(left_frame2,textvariable=self.var_phoneno,font=("Times New Roman",12),width=22)
        txt_phoneno.grid(row=3,column=3,padx=2,pady=7)
        
        #address#
        lbl_address = Label(left_frame2,text="Address:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_address.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        txt_address = ttk.Entry(left_frame2,textvariable=self.var_add,font=("Times New Roman",12),width=22)
        txt_address.grid(row=4,column=1,padx=2,pady=7)
        
        #doa#
        lbl_doa = Label(left_frame2,text="Addmission Date:",font=("Times New Roman",12,"bold"),bg="white")
        lbl_doa.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        txt_doa = ttk.Entry(left_frame2,textvariable=self.var_doa,font=("Times New Roman",12),width=22)
        txt_doa.grid(row=4,column=3,padx=2,pady=7)
        
        ##buttonframe##
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=475,width=640,height=35)
        
        btn_add = Button(btn_frame,text="Save",command=self.add_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_add.grid(row=0,column=1,padx=1)
        
        btn_update = Button(btn_frame,text="Update",command=self.update_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_update.grid(row=0,column=2,padx=1)
        
        btn_delete = Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_delete.grid(row=0,column=3,padx=1)
        
        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_reset.grid(row=0,column=4,padx=1)
        
        ##rightframe##
        right_frame = LabelFrame(bg_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Times New Roman",13,"bold"),bg="white",fg="red")
        right_frame.place(x=680,y=10,width=800,height=540)
        
        image1 = Image.open(r"F:\New folder (7)\additional.jpg")
        image1 = image1.resize((780,200),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(image1)
        self.label5 = Label(right_frame,image=self.photoimage1,cursor="hand2")
        self.label5.place(x=5,y=0,width=780,height=200)
        
        search_frame = LabelFrame(right_frame,bd=4,relief=RIDGE,padx=2,text="Search Information",font=("Times New Roman",13,"bold"),bg="white",fg="red")
        search_frame.place(x=5,y=200,width=780,height=70)
        
        search_by = Label(search_frame,text="Search by:",font=("Times New Roman",12,"bold"),bg="white")
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("Times New Roman",12),width=18,state="readonly")
        com_txt_search["values"] = ("Select Option","RollNo","PhoneNo","StudentId")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)
        
        self.txt_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.txt_search,font=("Times New Roman",12),width=22)
        txt_search.grid(row=0,column=2,padx=5)
        
        btn_search = Button(search_frame,text="Search",command=self.search_data,width=15,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)
        
        btn_showall = Button(search_frame,text="Show all",command=self.fetch_data,width=15,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        btn_showall.grid(row=0,column=4,padx=5)
        
        ##show details frame and scroll bar##
        table_frame = Frame(right_frame,bd=4,relief=RIDGE)
        table_frame.place(x=5,y=260,width=780,height=250)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=("Dept","Course","Year","Sem","Id","Name","Div","RollNo","Gender","DOB","Email","PhoneNo","Address","Addm Date"),xscrollcommand=scroll_x.get,yscrollcommand=scroll_y.get)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Students Id")
        self.student_table.heading("Name",text="Students Name")
        self.student_table.heading("Div",text="Divison")
        self.student_table.heading("RollNo",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Addm Date",text="Addmission Date")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("Dept",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Addm Date",width=100)
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if(self.var_dept.get()=="" or self.var_email.get()=="" or self.var_id.get()==""):
            messagebox.showerror("Error","Enter all the Field")
        else:
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dept.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_rollno.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phoneno.get(),
                                                                                                        self.var_add.get(),
                                                                                                        self.var_doa.get()))
                mydb.commit()
                self.fetch_data()
                mydb.close()
                messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #fetch function#
    def fetch_data(self):
        mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM student")
        data = mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            mydb.commit()
        mydb.close()
    
    #get cursor#
    def get_cursor(self,event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        
        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_rollno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9]) 
        self.var_email.set(data[10])
        self.var_phoneno.set(data[11])
        self.var_add.set(data[12])
        self.var_doa.set(data[13])
    
                                                         
    #update data##
    def update_data(self):
        if(self.var_dept.get()=="" or self.var_email.get()=="" or self.var_id.get()==""):
            messagebox.showerror("Error","Enter all the Field")
        else:
            try:
                update=messagebox.askyesno("Updation","Do u want to update",parent=self.root)
                if update>0:
                    mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
                    mycursor = mydb.cursor()
                    mycursor.execute("UPDATE student SET Dept=%s,Course=%s,Year=%s,Semester=%s,StudentName=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,EmailId=%s,PhoneNo=%s,Address=%s,AddmissionDate=%s WHERE StudentId=%s",
                                     (self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_name.get(),self.var_div.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phoneno.get(),self.var_add.get(),self.var_doa.get(),self.var_id.get()))
                
                else:
                    if not update:
                        return
                mydb.commit()
                self.fetch_data()
                mydb.close()
                
                messagebox.showinfo("Successfull","Updation Succesfull")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
   
   #Delete##
    def delete_data(self):
        if (self.var_id.get()==""):
            messagebox.showerror("Error","Enter all the field",parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Deletion","Are you sure to delete this student information",parent=self.root)
                if Delete>0:
                    mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
                    mycursor = mydb.cursor()
                    sql = "DELETE FROM student WHERE StudentId=%s"
                    value = (self.var_id.get(),)
                    mycursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                mydb.commit()
                self.fetch_data()
                mydb.close()
                
                messagebox.showinfo("Successful","Student information deleted",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
     ##reset data##        
    def reset_data(self):        
            self.var_dept.set("Select Department")
            self.var_course.set("Select Courses")
            self.var_year.set("Select Year")
            self.var_sem.set("Select Semester")
            self.var_id.set("")
            self.var_name.set("")
            self.var_div.set("Select Division")
            self.var_rollno.set("")
            self.var_gender.set("Select Gender")
            self.var_dob.set("") 
            self.var_email.set("")
            self.var_phoneno.set("")
            self.var_add.set("")
            self.var_doa.set("")
    
        
    ##search data##
    def search_data(self):
        if self.var_com_search.get()=="" or self.txt_search.get()=="":
            messagebox.showerror("Error","Select one Option",parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM student where " +str(self.
                    var_com_search.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                data = mycursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    mydb.commit()
                mydb.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
              
if __name__ == "__main__":
    main()
    
