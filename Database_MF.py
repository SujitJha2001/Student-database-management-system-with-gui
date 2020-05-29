from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Management System')
        self.root.config(bg='cadet blue')

        l1=Label(self.root,text='Student Management System',font=('Times new roman',40,'bold'),
                 fg='cadet blue',bg='white',bd=10,relief=GROOVE)
        l1.pack(side=TOP,fill=X)

        frame1=Frame(self.root,relief=RIDGE,bg='crimson')
        frame1.place(x=50,y=95,height=640,width=460)

        frame2=Frame(self.root,relief=RIDGE,bg='crimson')
        frame2.place(x=550,y=95,height=640,width=700)

        #//////// ALL VARIABLES\\\\\\\#

        self.Name_var=StringVar()
        self.Roll_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
                

        #//////////////////////////// COMPONENTS OF LEFT FRAME i.e. 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        frame1_Title=Label(frame1,text='Manage Student',font=('Times new roman',20,'bold'),
                 bd=10,fg='white',bg='crimson')
        frame1_Title.grid(row=0,columnspan=2,pady=20)


        roll=Label(frame1,text='Roll No.',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        roll.grid(row=1,column=0,padx=20,pady=10,sticky='w')
        roll_entry=Entry(frame1,textvariable=self.Roll_var,font=('Times new roman',15,'bold'),bd=2,relief=GROOVE)
        roll_entry.grid(row=1,column=1,padx=20,pady=10,sticky='w')


        Name=Label(frame1,text='Name',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        Name.grid(row=2,column=0,padx=20,pady=10,sticky='w')
        Name_entry=Entry(frame1,textvariable=self.Name_var,font=('Times new roman',15,'bold'),bd=2,relief=GROOVE)
        Name_entry.grid(row=2,column=1,padx=20,pady=10,sticky='w')


        Email=Label(frame1,text='Email',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        Email.grid(row=3,column=0,padx=20,pady=10,sticky='w')
        Email_entry=Entry(frame1,textvariable=self.Email_var,font=('Times new roman',15,'bold'),bd=2,relief=GROOVE)
        Email_entry.grid(row=3,column=1,padx=20,pady=10,sticky='w')


        Gender=Label(frame1,text='Gender',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        Gender.grid(row=4,column=0,padx=20,pady=10,sticky='w')
        Gender_entry=ttk.Combobox(frame1,textvariable=self.Gender_var,font=('Times new roman',12,'bold'),state='readonly')
        Gender_entry['values']=("Male","Female","Others")
        Gender_entry.grid(row=4,column=1,padx=20,pady=10,sticky='w')


        Contact=Label(frame1,text='Contact',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        Contact.grid(row=5,column=0,padx=20,pady=10,sticky='w')
        Contact_entry=Entry(frame1,textvariable=self.Contact_var,font=('Times new roman',15,'bold'),bd=2,relief=GROOVE)
        Contact_entry.grid(row=5,column=1,padx=20,pady=10,sticky='w')


        DOB=Label(frame1,text='D.O.B',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        DOB.grid(row=6,column=0,padx=20,pady=10,sticky='w')
        DOB_entry=Entry(frame1,textvariable=self.DOB_var,font=('Times new roman',15,'bold'),bd=2,relief=GROOVE)
        DOB_entry.grid(row=6,column=1,padx=20,pady=10,sticky='w')


        Address=Label(frame1,text='Address',font=('Times new roman',20,'bold'),
                 fg='white',bg='crimson')
        Address.grid(row=7,column=0,padx=20,pady=10,sticky='w')
        self.Address_entry=Text(frame1,font=('',10),width=30,height=4)
        self.Address_entry.grid(row=7,column=1,padx=20,pady=10,sticky='w')

        #BUTTONS of frame1

        frame1_buttons=Frame(frame1,bg='white',bd=4,relief=RIDGE)
        frame1_buttons.place(x=20,y=565,height=55,width=418)
        
        b1=Button(frame1_buttons,text='Add',command=self.add_students,font=('Times new roman',15,'bold'),width=7,bg='cadet blue',fg='white')
        b1.grid(row=0,column=0,padx=5,pady=5)
        b2=Button(frame1_buttons,text='Update',command=self.update_data,font=('Times new roman',15,'bold'),width=7,bg='cadet blue',fg='white')
        b2.grid(row=0,column=1,padx=4,pady=5)
        b3=Button(frame1_buttons,text='Delete',command=self.delete_data,font=('Times new roman',15,'bold'),width=7,bg='cadet blue',fg='white')
        b3.grid(row=0,column=2,padx=4,pady=5)
        b4=Button(frame1_buttons,text='Clear',command=self.clear,font=('Times new roman',15,'bold'),width=7,bg='cadet blue',fg='white')
        b4.grid(row=0,column=3,padx=4,pady=5)
        #//////////////////////////// STYLING OF LEFT FRAME ENDS i.e. 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

        #//////////////////////////// COMPONENTS OF RIGHT FRAME i.e. 2 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
        frame3=Frame(self.root,relief=RIDGE,bg='crimson')
        frame3.place(x=560,y=110,height=50,width=680)

        Search=Label(frame3,text='Search by',font=('Times new roman',18,'bold'),
                 fg='white',bg='crimson')
        Search.grid(row=0,column=0,padx=20,pady=10,sticky='w')

        Search_combination=ttk.Combobox(frame3,textvariable=self.search_by,font=('Times new roman',12,'bold'),width=10,state='readonly')
        Search_combination['values']=("Roll","Name","Contact")
        Search_combination.grid(row=0,column=1,padx=20,pady=10,sticky='w')

        Search_entry=Entry(frame3,textvariable=self.search_txt,font=('Times new roman',12,'bold'),bd=2,relief=GROOVE)
        Search_entry.grid(row=0,column=2,padx=20,pady=10,sticky='w')
        #BUTTONS of frame2 
        b5=Button(frame3,text='Search',command=self.search_data,font=('Times new roman',15,'bold'),width=6,bg='white',fg='cadet blue')
        b5.grid(row=0,column=3,padx=5,pady=5)
        b6=Button(frame3,text='Show All',command=self.fetch_data,font=('Times new roman',15,'bold'),width=6,bg='white',fg='cadet blue')
        b6.grid(row=0,column=4,padx=5,pady=5)

        #List of the frame2
        frame4=Frame(frame2,bg='white',bd=4,relief=RIDGE)
        frame4.place(x=10,y=70,width=680,height=550)

        scroll_x=Scrollbar(frame4,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame4,orient=VERTICAL)

        self.Student_Table=ttk.Treeview(frame4,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        self.Student_Table.heading("Roll",text="Roll No.")
        self.Student_Table.heading("Name",text="Name")
        self.Student_Table.heading("Email",text="Email")
        self.Student_Table.heading("Gender",text="Gender")
        self.Student_Table.heading("Contact",text="Contact")
        self.Student_Table.heading("DOB",text="D.O.B")
        self.Student_Table.heading("Address",text="Address")
        self.Student_Table['show']='headings'

        self.Student_Table.column("Roll",width=100)
        self.Student_Table.column("Name",width=100)
        self.Student_Table.column("Email",width=100)
        self.Student_Table.column("Gender",width=100)
        self.Student_Table.column("Contact",width=100)
        self.Student_Table.column("DOB",width=100)
        self.Student_Table.column("Address",width=150)
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
######################################################################################################
#if str(type(t))=="<class 'int'>":
#	print("yes")
                                        ##BACKEND CODE##

    def add_students(self):
        """Set up a connection with the database."""
        con = sqlite3.connect("stm.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "
                        "students (roll_no integer PRIMARY KEY, "
                                "name text, "
                                "email text, "
                                "gender text, "
                                "contact text, "
                                "dob text, "
                                "address text)")

        """Insert entry into database."""
        if self.Roll_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Address_entry.get('1.0',END)=="":
            messagebox.showerror("Error","All Fields are required!!!")
        
        else:
            try:
                cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                                     (self.Roll_var.get(),
                                      self.Name_var.get(),
                                      self.Email_var.get(),
                                      self.Gender_var.get(),
                                      self.Contact_var.get(),
                                      self.DOB_var.get(),
                                      self.Address_entry.get('1.0',END)))
        
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been added!!!")
            except:
                messagebox.showerror("Error","Roll Number should be of type integer and unique!!!")

    def fetch_data(self):
        con = sqlite3.connect("stm.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
                con.commit()
        else:
            self.Student_Table.delete(*self.Student_Table.get_children())
            con.commit()
            
        con.close()

    def clear(self):
        self.Roll_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.Address_entry.delete('1.0',END)
        
    def get_cursor(self,ev):
        cursor_row=self.Student_Table.focus()
        contents=self.Student_Table.item(cursor_row)
        row=contents['values']
        self.Roll_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.Address_entry.delete('1.0',END)
        self.Address_entry.insert(END,row[6])
    def update_data(self):
        if self.Roll_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.Address_entry.get('1.0',END)=="":
            messagebox.showerror("Error","All Fields are required!!!")
        else:
            con = sqlite3.connect("stm.db")
            cur = con.cursor()
            cur.execute("UPDATE students "
                        "SET name = ?, "
                        "email = ?, "
                        "gender = ?, "
                        "contact = ?, "
                        "dob = ?, "
                        "address = ? "
                        "WHERE roll_no = ?",  
                        (self.Name_var.get(),
                         self.Email_var.get(),
                         self.Gender_var.get(),
                         self.Contact_var.get(),
                         self.DOB_var.get(),
                         self.Address_entry.get('1.0',END),
                         self.Roll_var.get()))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

    def delete_data(self):
        if self.Roll_var.get()=="":
            messagebox.showerror("Error","*No record has been selected")    
        else:
            con = sqlite3.connect("stm.db")
            cur = con.cursor()
            cur.execute("DELETE FROM students WHERE roll_no=?",(self.Roll_var.get(),))
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()

    def search_data(self):
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("Error","All Fields are required!!!\nFill in the Search by Entry")    
        else:
            con = sqlite3.connect("stm.db")
            cur = con.cursor()
            
            if str(self.search_by.get())=="Roll":
                cur.execute("SELECT * FROM students WHERE roll_no = ?",(self.search_txt.get(),))

            elif str(self.search_by.get())=="Name":
                cur.execute("SELECT * FROM students WHERE name = ?",(self.search_txt.get(),))

            elif str(self.search_by.get())=="Contact":
                cur.execute("SELECT * FROM students WHERE contact = ?",(self.search_txt.get(),))
                
            
            rows = cur.fetchall()
            if len(rows)!=0:
                self.Student_Table.delete(*self.Student_Table.get_children())
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                    con.commit()
            con.close()

        

#####################################################################################################
root=Tk()
root.iconbitmap(r'Database2.ico')

obj=Student(root)

root.mainloop()
