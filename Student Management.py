from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        com_txt_search["values"] = ("Select Option","Roll No","Phone No","Id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)
        
        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.var_search,font=("Times New Roman",12),width=22)
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
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Select all Option",parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost",user="root",password="Shomi@01",database="infodata")
                mycursor = mydb.cursor()
                
                data = mycursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    mydb.commit()
                mydb.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
            
            
         
        
        
if __name__ == "__main__" :
    root = Tk()
    obj = Student(root)
    root.mainloop()
