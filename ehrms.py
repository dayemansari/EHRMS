# Employee Management System for PYCODEPRO.com

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
#from tkcalendar import Calendar
import os
import sys
import qrcode
import datetime
from datetime import date
from datetime import time

from datetime import datetime

def login_func(parent,controller):
        global uid
        global pw

        a=uid.get()
        b=pw.get()

        import mysql.connector as A1

        con1=A1.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur1=con1.cursor()

        if a=='' and b=='':
                c=messagebox.showerror('Empty Field','Fill the Empty Field')

                sys.exit()


        elif len(a)>0 and len(b)>0:

                query='select post,name from login where (id,pw)=(%s,%s)'
                val=(a,b)

                cur1.execute(query,val)

                res1=cur1.fetchall()

                try:

                        global x

                        ab=res1[0]
                        post_a=ab[0]
                        name_a=ab[1]

                        for x in res1:
                                messagebox.showinfo('Welcome',('Welcome',x))

                                import mysql.connector as D1
                                cond1=D1.connect(host='localhost',user='root',password='dayem',database='pycode')
                                curd1=cond1.cursor()

                                queryd1='INSERT INTO ATTENDANCE (ID,LOGINDATE,LOGINTIME) VALUES (%s,%s,%s)'

                                today = date.today()

                                now = datetime.now()

                                current_time = now.strftime("%H:%M:%S")
                                
                                valued1=(a,today,current_time)

                                curd1.execute(queryd1,valued1)
                                cond1.commit()

                except:
                        messagebox.showinfo('Not Found','Employee Not Found Try Again')
                        sys.exit()

                        

class tkinterApp(tk.Tk):
        def __init__(self,*args,**kwargs):
                tk.Tk.__init__(self,*args,**kwargs)
                self.geometry('300x600+480+50')
                self.configure(bg='white')
                self.title('Employee Management System')
                container=Frame(self)
                container.pack(side="right",fill="both",expand=True)

                container.grid_rowconfigure(0,weight=1)
                container.grid_columnconfigure(0,weight=1)

                self.frames={}

                for F in (main_screen,request_qr,your_details,attendance,change_password,projects,qr_generator_frame,submitted_projects,assigned_or_assign,assign_project_frame,login,main_menu,register,view_expense_frame,other_expense_frame,dept,get_details,logout,leave,app_leave,expense,apply_expense,view_expense,view_leave_frame,your_leave_frame,other_leave_frame):
                        

                        
                        global img
                        frame=F(container,self)
                        frame.configure(bg='white',borderwidth=1)

                        self.frames[F]=frame
                        copyright_label=Label(self,text='Developed By PyCodePro.com',bg='white',fg='blue',borderwidth=1,relief='solid')
                        copyright_label.place(x=0,y=581)
                        frame.grid(row=0,column=0,sticky="nsew")

                        

                self.show_frame(main_screen)

        def show_frame(self,cont):
                frame=self.frames[cont]
                frame.tkraise()

class main_screen(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                
                global img
                global tkimage
                global img2alpha
                img = Image.open('logo.png')
                img = img.resize((400, 400))
                tkimage = ImageTk.PhotoImage(img)
                img2alpha=Label(self, image=tkimage).place(x=-53,y=0)
                tmp_label=Label(self,text='Welcome To PycodePro.com',fg='#000080',bg='white',bd=2,font=("Times New Roman", 14),relief='groove').place(x=35,y=20)
                login_btn=Button(self,text='Login',fg='blue',bg='white',relief='groove',command=lambda:controller.show_frame(login),font=12).place(x=20,y=350)

                register_btn=Button(self,text='Register as New Employee',fg='blue',bg='white',relief='groove',font=12,command=lambda:controller.show_frame(register)).place(x=85,y=350)
                
def profile_picture_func(parent):

        ppuid=uid.get()
        print(ppuid)

        import mysql.connector as sqlpro

        connection=sqlpro.connect(host='localhost',user='root',password='dayem',database='pycode')
        cursorsql=connection.cursor()

        query_sql='SELECT UID,NAME,POST,DEPARTMENT FROM DEPARTMENT WHERE UID = (%s)'
        value_sql=ppuid,

        cursorsql.execute(query_sql,value_sql)

        sql_records=cursorsql.fetchall()

        for x_sql in sql_records:

                id_in_sql=x_sql[0]
                name_in_sql=x_sql[1]
                post_in_sql=x_sql[2]
                dept_in_sql=x_sql[3]

                id_print=Label(parent,text=(id_in_sql),bg='white',fg='red',font='helvetica 10 bold').place(x=135,y=10)
                name_print=Label(parent,text=name_in_sql,bg='white',fg='red',font='helvetica 10 bold').place(x=135,y=30)
                post_print=Label(parent,text=post_in_sql,bg='white',fg='red',font='helvetica 10 bold').place(x=135,y=50)
                dept_print=Label(parent,text=dept_in_sql,bg='white',fg='red',font='helvetica 10 bold').place(x=135,y=70)



        
        
       
class login(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)


                global uid
                global pw

                uid=StringVar()
                pw=StringVar()


                id_lbl=Label(self,text='User ID :',fg='white',bg='#7AD7F0',relief='groove',font=("sans serif","12","bold italic"),width=9).place(x=20,y=40)
                pw_lbl=Label(self,text='Password :',fg='white',bg='#7AD7F0',relief='groove',font=("sans serif","12","bold italic"),width=9).place(x=20,y=80)

                id_entry=Entry(self,textvariable=uid,borderwidth=2,relief='groove',font=12,width=15).place(x=130,y=40)
                pw_entry=Entry(self,textvariable=pw,borderwidth=2,relief='groove',show='•',font=12,width=15).place(x=130,y=80)
                
                global submit_btn
                #global forgot_id_pw
                #forgot_id_pw=Button(self,text='Forgot ID & PW',relief='groove',bg='#0F0C08',fg='white',font=("sans serif","12","bold italic")).place(x=100,y=160)

                submit_btn=Button(self,text='Submit',relief='groove',bg='#0F0C08',fg='white',font=("sans serif","12","bold italic"),command=lambda:(login_func(self,controller),controller.show_frame(main_menu),profile_picture_func(parent))).place(x=100,y=130)#3CB043
                
                goback_btn=Button(self,text='← Go Back',relief='groove',fg='red',bg='white',command=lambda:controller.show_frame(main_screen)).place(x=25,y=360)

class main_menu(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                #dashboard with photo and name and post

                global profilepic
                global profileimage
                global img2profile
                profilepic = Image.open('profile.png')
                profilepic = profilepic.resize((100, 100))
                profileimage = ImageTk.PhotoImage(profilepic)
                img2profile=Label(self, image=profileimage).place(x=20,y=0)

                
                #tmp_btn=Button(self,text='Temporary Button',bg='white',fg='red',relief='groove').place(x=20,y=20)
                #attendence
                atd_btn=Button(self,text='Attendance',fg='white',command=lambda:controller.show_frame(attendance),bg='#3DED47',font='helvetica 14 bold',width=8,height=3,relief='groove').place(x=40,y=120)
                #Department Details
                dept_btn=Button(self,text='Department Details',fg='white',bg='#AAAAAA',font='helvetica 14 bold',width=8,height=3,relief='groove',wraplength=120,command=lambda:controller.show_frame(dept)).place(x=160,y=320)
                #leave
                lv_btn=Button(self,text='Leave',fg='white',bg='#842bd7',font=('helvetica 14 bold'),width=8,height=3,relief='groove',command=lambda:controller.show_frame(leave)).place(x=160,y=120)
                #expense or reimbursment
                exp_btn=Button(self,text='Expense',fg='white',command=lambda:controller.show_frame(expense),bg='#ffd801',font=('helvetica 14 bold'),width=8,height=3,relief='groove').place(x=40,y=320)
                #your details
                #assigned projects
                ap_btn=Button(self,text='Assigned Projects',command=lambda:controller.show_frame(assigned_or_assign),fg='white',bg='#1338BE',font=('helvetica 14 bold'),width=8,height=3,relief='groove',wraplength=90).place(x=40,y=220)
                #projects submitted
                ps_btn=Button(self,text='Project Submitted',command=lambda:controller.show_frame(submitted_projects),fg='white',bg='black',font=('helvetica 14 bold'),width=8,height=3,relief='groove',wraplength=100).place(x=160,y=220)
                #key qr generate
                qr_btn=Button(self,text='Key QR Generator',command=lambda:controller.show_frame(qr_generator_frame),fg='white',bg='#FF0000',font=('helvetica 14 bold'),width=8,height=3,relief='groove',wraplength=100).place(x=40,y=420)
                #id Generator
                id_btn=Button(self,text='Your Details',command=lambda:controller.show_frame(your_details),fg='white',bg='#bca0dc',font=('helvetica 14 bold'),width=8,height=3,wraplength=100,relief='groove').place(x=160,y=420)
                #Log Out
                #lo_btn=Button(self,text='Log Out',bg='white',fg='black',relief='groove',font=('helvetica 12 bold')).place(x=118,y=520)

                #main screen button

                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=540)

                #logout button

                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=540)




#def uc():
 #       a=messagebox.showerror('Error',"Under Construction")

#XXXXXXXXXXXXXXXXXXXXX DEPARTMENT XXXXXXXXXXXXXXXXXXXX DETAILS XXXXXXXXXXXXXXXXXXXXXX PERFECTLY XXXXXXXXXXXXXXXXXXXXXX WORKING XXXXXXXXXXXXXXXXXXXXXXX

def know_dept(parent):


        info=dept_val.get()

        import mysql.connector as A3
        global listBox

        con3=A3.connect(host='localhost',user='root',password='dayem',database='pycode')

        cur3=con3.cursor()

        query='select uid,name,post from department where department = (%s)'
        val=info,

        cur3.execute(query,val)
        records = cur3.fetchall()
        #print(records)

        for i, (uid,name,post) in enumerate(records, start=1):
                
                listBox.insert("", "end",values=(uid,name,post))
                con3.close()

def get_employee_through_id(parent):

        info_ultra=dept_id.get()

        import mysql.connector as B6

        conb6=B6.connect(host='localhost',user='root',password='dayem',database='pycode')

        curb6=conb6.cursor()

        queryb6='select name,post,department from department where UID = (%s)'
        valb6=info_ultra,

        curb6.execute(queryb6,valb6)
        records = curb6.fetchall()
        #print(records)

        for i, (name,post,department) in enumerate(records, start=1):
                
                listBox.insert("", "end",values=(name,post,department))
                #con3.close()


class dept(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        choose=Label(self,text='Please Choose Department',fg='blue',bg='white').place(x=0,y=20)

        global dept_val
        global listBox
        #global box

        dept_val=StringVar()

        global dept_id

        dept_id=StringVar()

        #box=OptionMenu(self,dept_val,*values).place(x=20,y=60)
        box=ttk.Combobox(self,values=["Finance Department",

                                      "HR Department",

                                      "Head Department",

                                      "Health Department",

                                      "IT & Security Department",

                                      "Project Department",

                                      "Software Department"],textvariable=dept_val).place(x=20,y=60)

        dept_box_label=Button(self,text='ID Search',bg='white',fg='blue',command=lambda:controller.show_frame(get_details)).place(x=0,y=120)
        submit=Button(self,text='Submit',bg='white',fg='red',relief='solid',command=lambda:know_dept(self)).place(x=180,y=60)
        
        cols = ('ID','Name','Post')
        listBox =ttk.Treeview(self, column=cols,show='headings')
        listBox.column('# 1',anchor=CENTER, stretch=NO, width=100)
        listBox.column('# 2',anchor=CENTER, stretch=NO, width=100)
        listBox.column('# 3',anchor=CENTER, stretch=NO, width=100)

        for col in cols:
                listBox.heading(col, text=col)
                listBox.place(x=0,y=180)
        #goback button
        gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

        #main screen button

        ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

        #logout button

        lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

#XXXXXXXXXXXXXXXXXXXXX DEPARTMENT XXXXXXXXXXXXXXXXXXXX DETAILS XXXXXXXXXXXXXXXXXXXXXX PERFECTLY XXXXXXXXXXXXXXXXXXXXXX WORKING XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def get_employee_through_id(parent):

        info_ultra=dept_id.get()

        import mysql.connector as B6

        conb6=B6.connect(host='localhost',user='root',password='dayem',database='pycode')

        curb6=conb6.cursor()

        queryb6='select name,post,department from department where UID = (%s)'
        valb6=info_ultra,

        curb6.execute(queryb6,valb6)
        records = curb6.fetchall()
        #print(records)

        for i, (name,post,department) in enumerate(records, start=1):
                
                listBox_2.insert("", "end",values=(name,post,department))
                #con3.close()


class get_details(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        global listBox_2
        global dept_id

        dept_id=StringVar()

        dept_box_label=Label(self,text='Enter ID to Search :',bg='white',fg='blue').place(x=0,y=20)
        
        dept_box_entry=Entry(self,textvariable=dept_id,relief='solid').place(x=60,y=80)
        
        go_box_button=Button(self,text='→',bg='white',fg='black',width=2,command=lambda:(get_employee_through_id(self))).place(x=210,y=78)
        
        cols = ('Name','Post','Department')
        listBox_2 =ttk.Treeview(self, column=cols,show='headings')
        listBox_2.column('# 1',anchor=CENTER, stretch=NO, width=100)
        listBox_2.column('# 2',anchor=CENTER, stretch=NO, width=100)
        listBox_2.column('# 3',anchor=CENTER, stretch=NO, width=100)

        for col in cols:
                listBox_2.heading(col, text=col)
                listBox_2.place(x=0,y=150)
        #goback button
        gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(dept),width=9).place(x=0,y=480)

        #main screen button

        ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

        #logout button

        lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def other_leaves(parent,controller):

        ultra_name=uid.get()

        import mysql.connector as B2

        conb2=B2.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb2=conb2.cursor()

        queryb2='SELECT POST FROM DEPARTMENT WHERE UID = (%s)'
        valueb2=ultra_name,

        curb2.execute(queryb2,valueb2)
        recordb2=curb2.fetchall()

        for x in recordb2:
                if x[0]=='CEO':

                        other_leave_button=Button(parent,text='Other Leaves',wraplength=100,command=lambda:controller.show_frame(other_leave_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

                elif x[0]=='Manager':

                        other_leave_button=Button(parent,text='Other Leaves',wraplength=100,command=lambda:controller.show_frame(other_leave_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

                elif x[0]=='HR Manager':

                        other_leave_button=Button(parent,text='Other Leaves',wraplength=100,command=lambda:controller.show_frame(other_leave_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

                else:
                        messagebox.showerror('Error','This Feature is Not For Employees')
                        other_leave_button=Button(parent,text='Other Leaves',state='disabled',wraplength=100,command=lambda:controller.show_frame(other_leave_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)
class leave(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                apply_leave=Button(self,command=lambda:controller.show_frame(app_leave),text='Apply Leave',bg='#8cd3ff',fg='white',font=('helvetica 14 bold'),width=8,height=3,wraplength=100).place(x=40,y=120)
                view_leave=Button(self,command=lambda:controller.show_frame(view_leave_frame),text='View Leave',bg='#A4DE02',fg='white',font=('helvetica 14 bold'),width=8,height=3,wraplength=100).place(x=160,y=120)

                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button

                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button

                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def getidnumber(parent):

        namesunderlist=names_under.get()
        
        import mysql.connector as B1
        connection=B1.connect(host='localhost',user='root',password='dayem',database='pycode')
        connectionB1=connection.cursor()

        query123="SELECT UID FROM DEPARTMENT WHERE NAME = (%s)"
        value123=namesunderlist,

        connectionB1.execute(query123,value123)

        resultB1=connectionB1.fetchall()

        for y in resultB1:

                pylabel=Label(parent,text=resultB1,fg='blue',bg='white',font=('helvetica 12')).place(x=160,y=360)

        
def apply_leave_function():

        leaver=uid.get()
        lt=leavetype.get()
        fdt=fromdate.get()
        tdt=tilldate.get()
        orr=offreason.get()
        oe=officer_entry.get()
        nu=names_under.get()

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        stt='Pending'
        
        #pending or approve or rejected
        #Data Control Language

        #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        import mysql.connector as A9
        con9=A9.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur9=con9.cursor()

        query99="INSERT INTO DAYOFF (ID,Leave_Type,From_date,Till_date,ro,Officer_name,reason,status,month) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,MONTHNAME(from_date))"
        value99=(leaver,lt,fdt,tdt,oe,nu,orr,stt)

        # create seperate database view Leave
        #insert apply leave fields in it and make it available fot
        cur9.execute(query99,value99)
        con9.commit() 

        messagebox.showinfo('Leave',('Leave Forwarded To : ',oe+' '+nu))

def go_func(parent):

        getofficerpost=officer_entry.get()

        import mysql.connector as A8
        con8=A8.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur8=con8.cursor()

        query8='SELECT NAME FROM DEPARTMENT WHERE POST=(%s)'
        value8=getofficerpost,

        cur8.execute(query8,value8)

        result=cur8.fetchall()

        name_officer=Label(parent,text='Select Name : ',bg='white',fg='blue',font='helvetica 12').place(x=20,y=320)

        global names_under

        names_under=StringVar()

        for x in result:

                name_officer=Label(parent,text='Select Name : ',bg='white',fg='blue',font='helvetica 12').place(x=20,y=320)

                names_list=ttk.Combobox(parent,values=x,textvariable=names_under,width=15).place(x=160,y=320)
    
class app_leave(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                #leave type

                lv_lbl=Label(self,text='Leave type',bg='white',fg='blue',font=('helvetica 12')).place(x=20,y=20)

                global leavetype

                leavetype=StringVar()

                #leave_typ=OptionMenu(self,leavetype,*values).place(x=120,y=20)
                leave_typ=ttk.Combobox(self,values=[

                        "Casual Leave - CL",
                        "Sick Leave",
                        "Medical Leave",
                        "Child Care Leave",
                        "Marriage Leave",
                        "Earned Leave",
                        "Maternity Leave",
                        "Paternity Leave",
                        "Study Leave",
                        "Bereavement leave",
                        "Sabbatical leave"
                        ],textvariable=leavetype,width=15).place(x=160,y=20)

                #leave date

                dt=Label(self,text='From Date :',font='helvetica 12',bg='white',fg='blue').place(x=20,y=80)
                global fromdate

                fromdate=StringVar()
                
                date_entry=Entry(self,textvariable=fromdate,font=12,width=12,relief='solid').place(x=160,y=80)              
                
                #leave till date

                till_date=Label(self,text='To Date :',font='helvetica 12',bg='white',fg='blue').place(x=20,y=140)
                global tilldate

                tilldate=StringVar()
                
                till_date_entry=Entry(self,textvariable=tilldate,width=12,relief='solid',font=12).place(x=160,y=140)

                #reason

                reason_label=Label(self,text='Short Reason : ',bg='white',fg='blue',font='helvetica 12').place(x=20,y=200)
                
                global offreason
                offreason=StringVar()
                
                reason_entry=Entry(self,textvariable=offreason,width=12,font=12,relief='solid').place(x=160,y=200)

                #officer

                officer_label=Label(self,text='Reporting Officer : ',bg='white',fg='blue',font='helvetica 12').place(x=20,y=260)
                
                global officer_entry

                officer_entry=StringVar()

                #officer_option=OptionMenu(self,officer_entry,*val).place(x=120,y=260)
                
                officer_option=ttk.Combobox(self,values=[
                        "CEO",
                        "Manager",
                        "HR Manager"],textvariable=officer_entry,width=15).place(x=160,y=260)

                go_button=Button(self,text='→',bg='white',fg='black',relief='solid',command=lambda:go_func(self),height=1,width=2).place(x=275,y=257)

                go_button_2=Button(self,text='→',bg='white',fg='black',relief='solid',command=lambda:getidnumber(self),height=1,width=2).place(x=275,y=320)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #Submit Button

                submit_button=Button(self,text='Submit',bg='yellow',fg='black',font='helvetica 12',relief='groove',state='active',command=apply_leave_function).place(x=20,y=380)
                #main screen button

                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button

                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)


def sql_register():

        a=nm.get()
        b=fnm.get()
        c=mnm.get()
        d=dobe.get()
        e=agee.get()
        f=maile.get()
        g=mbe.get()
        h=pwe.get()
        j=ape.get()

        import mysql.connector as A2
        con2=A2.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur2=con2.cursor()

        import random
        epid=random.randint(000000,999999)
        py='PY'
        conv=str(epid)
        comb=py+conv

        query="INSERT INTO DETAILS (uid,name,dept,post,doj,dob,mail,mob,apln,pw) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(comb,a,b,c,e,d,f,g,j,h)

        cur2.execute(query,values)
        con2.commit()
        
        q2="INSERT INTO DEPARTMENT (UID,NAME,POST,department) VALUES (%s,%s,%s,%s)"
        v2=(comb,a,c,b)

        cur2.execute(q2,v2)
        con2.commit()

        q3="INSERT INTO LOGIN (ID,PW,NAME,POST) VALUES (%s,%s,%s,%s)"
        v3=(comb,h,a,c)

        cur2.execute(q3,v3)
        con2.commit()

        messagebox.showinfo('Registered Successfully',('Your Employee ID is :',comb))
        
class register(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                #registration and allotment of employee ID

                #lbl=Label(self,text='Under Construction',bg='red',fg='white',font='helvetica 14 bold').place(x=0,y=500)
                gb=Button(self,text='← Go Back',fg='red',bg='white',relief='groove',borderwidth=2,command=lambda:controller.show_frame(main_screen)).place(x=20,y=460)

                global nm
                global fnm
                global mnm
                global agee
                global dobe
                global maile
                global mbe
                global pwe
                global pw2e
                global ape
                
                nm=StringVar()#name
                fnm=StringVar()#Department
                mnm=StringVar()#Post
                dobe=StringVar()#DOB
                agee=StringVar()#DOJ
                ape=StringVar()#appointment letter no
                maile=StringVar()#email id
                mbe=StringVar()#mobile no
                pwe=StringVar()#password
                pw2e=StringVar()#cnf pw
                
                name=Label(self,text='Name',bg='white',fg='blue').place(x=20,y=20)
                entry_name=Entry(self,textvariable=nm,font=12,width=14,borderwidth=2,relief='groove').place(x=140,y=20)
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                fname=Label(self,text='Department',fg='blue',bg='white').place(x=20,y=60)
                #entry_fname=Entry(self,textvariable=fnm,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=60)

                entry_fname=ttk.Combobox(self,values=["Finance Department",

                                                      "HR Department",

                                                      "Head Department",

                                                      "Health Department",

                                                      "IT & Security Department",

                                                      "Project Department",

                                                      "Software Department"],textvariable=fnm).place(x=140,y=60)
                #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                mname=Label(self,text='Post',fg='blue',bg='white').place(x=20,y=100)
                entry_mname=Entry(self,textvariable=mnm,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=100)

                age=Label(self,text='Date of Joining',fg='blue',bg='white').place(x=20,y=140)
                entry_age=Entry(self,textvariable=agee,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=140)

                dob=Label(self,text='DOB',fg='blue',bg='white').place(x=20,y=180)
                entry_dob=Entry(self,textvariable=dobe,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=180)

                al=Label(self,text='Appt Letter No',fg='blue',bg='white').place(x=20,y=220)
                entry_apl=Entry(self,textvariable=ape,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=220)

                mail=Label(self,text='Email ID',fg='blue',bg='white').place(x=20,y=260)
                entry_mail=Entry(self,textvariable=maile,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=260)

                mb=Label(self,text='Mobile No',fg='blue',bg='white').place(x=20,y=300)
                entry_mob=Entry(self,textvariable=mbe,font=12,width=14,relief='groove',borderwidth=2).place(x=140,y=300)

                pw=Label(self,text='Password',fg='blue',bg='white').place(x=20,y=340)
                entry_pw=Entry(self,textvariable=pwe,font=12,width=14,relief='groove',borderwidth=2,show='•').place(x=140,y=340)

                pw2=Label(self,text='Confirm Password',fg='blue',bg='white').place(x=20,y=380)
                entry_pw2=Entry(self,textvariable=pw2e,font=12,width=14,relief='groove',borderwidth=2,show='•').place(x=140,y=380)

                submit=Button(self,text='Submit',fg='black',bg='yellow',command=sql_register).place(x=20,y=420)

def logouttime():

        import mysql.connector as D2
        cond2=D2.connect(host='localhost',user='root',password='dayem',database='pycode')
        curd2=cond2.cursor()

        logout_id=uid.get()
        print(logout_id)

        queryd2='UPDATE ATTENDANCE SET LOGOUTTIME = (%s) where id = (%s)'

        logoutnow = datetime.now()

        logout_current_time = logoutnow.strftime("%H:%M:%S")
        
        valued2=(logout_current_time,logout_id)

        curd2.execute(queryd2,valued2)
        cond2.commit()

        

class logout(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                lg_lbl=Label(self,text='Successfully Loged Out',bg='white',fg='green',font=12,relief='solid').place(x=20,y=20)

                relogin=Button(self,text='Click Here to Login',bg='white',fg='blue',relief='solid',command=lambda:controller.show_frame(logout)).place(x=20,y=60)

class expense(Frame):
        def __init__(self,parent,controller):

                Frame.__init__(self,parent)

                #Apply for Expense

                apply_expense_label=Button(self,text='Apply Expense',command=lambda:controller.show_frame(apply_expense),wraplength=100,width=8,height=3,font='helvetica 14 bold',bg='#95F985',fg='white',relief='groove').place(x=40,y=120)

                #View Status for Expense

                view_expense_button=Button(self,text='View Expense',command=lambda:controller.show_frame(view_expense_frame),wraplength=100,width=8,height=3,font='helvetica 14 bold',bg='#FF7F7F',fg='white',relief='groove').place(x=160,y=120)

                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button

                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button

                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)
def apply_expense_func():

        getuid=uid.get()
        getdate=date_entry.get()
        gettoe=toe.get()
        getname=name_entry.get()
        getpurpose=purpose_entry.get()
        getamount=amount_entry.get()
        getmethod=payment_entry.get()
        getofficer='Sara Nielsen'
        pend='Pending'

        import mysql.connector as A4
        con4=A4.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur4=con4.cursor()

        query='INSERT into expense (ID,DateExpense,TypeExpense,NameExpense,Purpose,Amount,PaymentMethod,officer,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(getuid,getdate,gettoe,getname,getpurpose,getamount,getmethod,getofficer,pend)

        cur4.execute(query,values)
        con4.commit()

        messagebox.showinfo('Forwarded',('Your Request is Forwarded To ',getofficer))



class apply_expense(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                ae=Label(self,text='Apply Expense or Reimbursement',borderwidth=2,bg='#3895D3',fg='white',relief='groove',font=('helvetica 12 bold')).place(x=20,y=20)
               #Type of Expense

                global date_entry
                global toe
                global name_entry
                global purpose_entry
                global amount_entry
                global payment_entry

                toe=StringVar()
                date_entry=StringVar()
                name_entry=StringVar()
                purpose_entry=StringVar()
                amount_entry=StringVar()
                payment_entry=StringVar()
                

                typeofexpense=Label(self,text='Type of Expense',bg='white',fg='blue',font='helvetica 10').place(x=20,y=80)

                #drop=OptionMenu(self,toe,*values).place(x=150,y=80)
                drop=ttk.Combobox(self,values=[
                        "Travel Expense",
                        "Transport",
                        "Meals",
                        "Office Expense",
                        "Lodging Expense",
                        "Other Expense",
                        "Health Expense"],textvariable=toe).place(x=150,y=80)

                #Date of Expense
                date_label=Label(self,text='Date of Expense : ',bg='white',fg='blue',font='helvetica 10').place(x=20,y=120)
                #global date_entry
                dateentry=Entry(self,textvariable=date_entry,width=12,font=12,relief='solid').place(x=150,y=120)
                #Name of Expense
                name_label=Label(self,text='Name of Expense : ',bg='white',fg='blue',font='helvetica 10').place(x=20,y=160)
                #global name_entry
                nameentry=Entry(self,textvariable=name_entry,width=12,font=12,relief='solid').place(x=150,y=160)
                #purpose of Expense
                purpose_label=Label(self,text='Purpose of Expense : ',bg='white',fg='blue',font='helvetica 10').place(x=20,y=200)
                #global purpose_entry
                purposeentry=Entry(self,width=12,textvariable=purpose_entry,font=12,relief='solid').place(x=150,y=200)
                #amount of Expense
                amount_label=Label(self,text='Amount of Expense : ',bg='white',fg='blue',font='helvetica 10').place(x=20,y=240)
                #global amount_entry
                amountentry=Entry(self,textvariable=amount_entry,width=12,font=12,relief='solid').place(x=150,y=240)
                #payment Method
                payment_label=Label(self,text='Payment Method : ',bg='white',fg='blue',font='helvetica 10').place(x=20,y=280)
               # global payment_entry
                paymententry=Entry(self,textvariable=payment_entry,width=12,font=12,relief='solid').place(x=150,y=280)
                #submit_button
                submit_btn=Button(self,text='Submit',bg='white',fg='red',font='helvetica 12 bold',relief='groove',activebackground='green',command=apply_expense_func).place(x=20,y=340)
                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def view_expense_func(parent):

        import mysql.connector as A6
        con6=A6.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur6=con6.cursor()

        q='SELECT NameExpense,officer,status from expense where id=(%s)'
        newuid=uid.get()
        v=newuid,

        cur6.execute(q,v)
        record54=cur6.fetchall()

        for i, (NameExpense,Officer,Status) in enumerate(record54, start=1):
                view_expense_list.insert("", "end",values=(NameExpense,Officer,Status))

def other_expense_func(parent,controller):

        ultra_pro_name=uid.get()

        import mysql.connector as B8

        conb8=B8.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb8=conb8.cursor()

        queryb8='SELECT POST,Name FROM DEPARTMENT WHERE UID = (%s)'
        valueb8=ultra_pro_name,

        curb8.execute(queryb8,valueb8)
        recordb8=curb8.fetchall()

        for x in recordb8:
                if x[0]=='CEO':

                        other_leave_button=Button(parent,text='Other Expense',wraplength=100,command=lambda:controller.show_frame(other_expense_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

                elif x[1]=='Sara Nielsen':

                        other_leave_button=Button(parent,text='Other Expense',wraplength=100,command=lambda:controller.show_frame(other_expense_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

                else:
                        messagebox.showerror('Error','This Feature is Not For Employees')
                        other_leave_button=Button(parent,text='Other Expense',state='disabled',wraplength=100,command=lambda:controller.show_frame(other_expense_frame),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)

        
def other_expense_ultra_func(parent):

        import mysql.connector as B9
        conb9=B9.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb9=conb9.cursor()

        z9=uid.get()

        name_fetch9='SELECT name,post from department where uid=(%s)'
        value_uid9=z9,

        curb9.execute(name_fetch9,value_uid9)

        resultb9=curb9.fetchall()

        print(resultb9)

        a=resultb9[0]
        name_b3=a[0]#name
        print(name_b3)
        post_b3=a[1]#post
        print('RO : ',post_b3)

        qb3='select id,Nameexpense,purpose,amount,status from expense where officer like (%s) and status=(%s) or status = (%s)'

        vb3=('%'+name_b3+'%','Pending','Forwarded')

        curb9.execute(qb3,vb3)
        record54b9=curb9.fetchall()
        print(record54b9)


        #print(record54b3)

        for i, (id,Nameexpense,purpose,amount,Status) in enumerate(record54b9, start=1):
                other_expense_list.insert("", "end",values=(id,Nameexpense,purpose,amount,Status))

def forward_expense():

        import mysql.connector as B12

        conb12=B12.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb12=conb12.cursor()

        queryb12='UPDATE expense SET STATUS = (%s) , OFFICER = (%s) where id=(%s)'

        getb12id=get5entry.get()

        sttsb12='Forwarded'

        valueb12=(sttsb12,'Dayem Ansari',getb12id)

        curb12.execute(queryb12,valueb12)

        conb12.commit()

        messagebox.showinfo('Approved','Expense Forwarded Successfully')
        

def approve_expense():

        import mysql.connector as B11

        conb11=B11.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb11=conb11.cursor()

        queryb11='UPDATE expense SET STATUS = (%s) where id=(%s)'

        getb11id=get5entry.get()

        sttsb11='Approved'

        valueb11=(sttsb11,getb11id)

        curb11.execute(queryb11,valueb11)

        conb11.commit()

        messagebox.showinfo('Approved','Expense Approved Successfully')

def reject_expense():

        import mysql.connector as B10

        conb10=B10.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb10=conb10.cursor()

        queryb10='UPDATE expense SET STATUS = (%s) where id=(%s)'

        getultraid=get5entry.get()

        sttsb10='Rejected'

        valueb10=(sttsb10,getultraid)

        curb10.execute(queryb10,valueb10)

        conb10.commit()

        messagebox.showinfo('Rejected','Expense Rejected')

class other_expense_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                global other_expense_list

                #view_expense_frame

                other_expense_button=Button(self,text='View Expense',bg='#3895D3',command=lambda:(other_expense_ultra_func(self)),fg='white',relief='groove',font=('helvetica 12 bold')).place(x=100,y=20)

                cols = ('ID','Name','Purpose','Amount','Status')
                
                other_expense_list =ttk.Treeview(self, columns=cols,show='headings')

                other_expense_list.column('# 1',anchor=CENTER, width=75)
                other_expense_list.column('# 2',anchor=CENTER, width=75)
                other_expense_list.column('# 3',anchor=CENTER, width=75)
                other_expense_list.column('# 4',anchor=CENTER, width=75)
                other_expense_list.column('# 5',anchor=CENTER, width=75)

                for col in cols:
                        other_expense_list.heading(col, text=col)
                        other_expense_list.place(x=0,y=120)

                global get5entry

                get5entry=StringVar()

                enter_id=Label(self,text='Enter Employee ID to Approve or Reject or Forward :',bg='white',fg='blue',wraplength=130).place(x=0,y=380)
                enter_id_font=Entry(self,textvariable=get5entry,relief='solid').place(x=135,y=388)

                expense_accept=Button(self,text='Approve',command=approve_expense,bg='#3DED97',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=20,y=440)
                expense_reject=Button(self,text='Reject',command=reject_expense,bg='#FF0000',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=120,y=440)
                expense_forwareded=Button(self,text='Forward',command=forward_expense,bg='#2A9DF4',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=220,y=440)
                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(expense),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)


                

class view_expense_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                your_expense_button=Button(self,text='Your Expense',width=8,height=3,font='helvetica 14 bold',wraplength=100,bg='#3895D3',fg='white',command=lambda:controller.show_frame(view_expense),relief='groove').place(x=40,y=120)
                other_expense_button=Button(self,width=8,height=3,command=lambda:(other_expense_func(self,controller)),text='Other Expense',font='helvetica 14 bold',wraplength=100,bg='#3895D3',fg='white',relief='groove').place(x=160,y=120)

                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(expense),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)
class view_expense(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                global view_expense_list

                #view_expense_frame

                view_expense_button=Button(self,text='View Expense',bg='#3895D3',fg='white',relief='groove',command=lambda:(view_expense_func(self)),font=('helvetica 12 bold')).place(x=100,y=20)

                cols = ('NameExpense','Officer','Status')
                
                view_expense_list =ttk.Treeview(self, columns=cols,show='headings')

                view_expense_list.column('# 1',anchor=CENTER, width=100)
                view_expense_list.column('# 2',anchor=CENTER, width=120)
                view_expense_list.column('# 3',anchor=CENTER, width=80)

                for col in cols:
                        view_expense_list.heading(col, text=col)
                        view_expense_list.place(x=0,y=120)
                #goback button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(view_expense_frame),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def view_leave_func(parent):

        import mysql.connector as B1
        conb1=B1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb1=conb1.cursor()

        q='select leave_type,from_date,till_date,status from dayoff where id=(%s)'
        newuidb1=uid.get()
        v=newuidb1,

        curb1.execute(q,v)
        record54b1=curb1.fetchall()

        print(record54b1)

        for i, (leave_type,from_date,till_date,Status) in enumerate(record54b1, start=1):
                view_leave_list.insert("", "end",values=(leave_type,from_date,till_date,Status))

class view_leave_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                view_leave_label=Label(self,text='View Leave',bg='#3895D3',fg='white',width=22,font='helvetica 12 bold',relief='groove').place(x=40,y=20)
                
                #Your Leave

                your_leave_button=Button(self,text='Your Leaves',command=lambda:controller.show_frame(your_leave_frame),wraplength=100,width=8,height=3,font='helvetica 14 bold',fg='white',bg='orange',relief='groove').place(x=40,y=120)

                #Other Leave
                other_leave_button=Button(self,text='Other Leaves',wraplength=100,command=lambda:(other_leaves(self,controller)),width=8,height=3,font='helvetica 14 bold',fg='white',bg='black',relief='groove').place(x=160,y=120)


                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(leave),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

class your_leave_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                view_leave_label=Button(self,text='Your Leaves',command=lambda:(view_leave_func(self)),bg='#3895D3',fg='white',width=22,font='helvetica 12 bold',relief='groove').place(x=40,y=20)

                global view_leave_list

                cols = ('Leave Type','From','To','Status')
                
                view_leave_list =ttk.Treeview(self, columns=cols,show='headings')

                verscrlbar = ttk.Scrollbar(self,orient ="horizontal",command=view_leave_list.xview)

                verscrlbar.pack(side ='left', fill ='x',expand='yes')

                view_leave_list.configure(xscrollcommand = verscrlbar.set)

                view_leave_list.column('# 1',anchor=CENTER, width=80)
                view_leave_list.column('# 2',anchor=CENTER, width=75)
                view_leave_list.column('# 3',anchor=CENTER, width=75)
                view_leave_list.column('# 4',anchor=CENTER, width=70)

                for col in cols:
                        view_leave_list.heading(col, text=col)
                        view_leave_list.place(x=0,y=120)
                        
                #goback button

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(view_leave_frame),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def other_leave_func(parent):

        import mysql.connector as B3
        conb3=B3.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb3=conb3.cursor()

        z=uid.get()
        
        name_fetch='SELECT name,post from department where uid=(%s)'
        value_uid=z,

        curb3.execute(name_fetch,value_uid)

        resultb3=curb3.fetchall()

        print(resultb3)

        a=resultb3[0]
        name_b3=a[0]#name
        print(name_b3)
        post_b3=a[1]#post
        print('RO : ',post_b3)

        qb3='select id,leave_type,from_date,till_date,Status from dayoff where ro=(%s) and officer_name=(%s) HAVING status=(%s) or status=(%s)'
        
        vb3=(post_b3,name_b3,'Pending','Forwarded')

        curb3.execute(qb3,vb3)
        record54b3=curb3.fetchall()

        print(record54b3)

        for i, (id,leave_type,from_date,till_date,Status) in enumerate(record54b3, start=1):
                pending_leave_list.insert("", "end",values=(id,leave_type,from_date,till_date,Status))

def approve_button():

        import mysql.connector as B4

        conb4=B4.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb4=conb4.cursor()

        queryb4='UPDATE DAYOFF SET STATUS = (%s) where id=(%s)'

        get3id=get2entry.get()

        stts='Approved'

        valueb4=(stts,get3id)

        curb4.execute(queryb4,valueb4)

        conb4.commit()

        messagebox.showinfo('Approved','Leave Approved Successfully')

def reject_button():

        import mysql.connector as B5

        conb5=B5.connect(host='localhost',user='root',password='dayem',database='pycode')
        curb5=conb5.cursor()

        queryb5='UPDATE DAYOFF SET STATUS = (%s) where id=(%s)'

        get3id=get2entry.get()

        stts='Rejected'

        valueb5=(stts,get3id)

        curb5.execute(queryb5,valueb5)

        conb5.commit()

        messagebox.showinfo('Rejected','Leave Rejected')

def forward_button():
        import mysql.connector as C1
        conc1=C1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curc1=conc1.cursor()

        getc1id=get2entry.get()

        queryc1='UPDATE DAYOFF set status=(%s),ro=(%s),officer_name=(%s) where id = (%s)'
        valuec1=('Forwarded','CEO','Dayem Ansari',getc1id)

        curc1.execute(queryc1,valuec1)

        conc1.commit()

        messagebox.showinfo('Forwarded','Leave Forwarded To CEO Dayem Ansari')
    

class other_leave_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                other_leave_button=Button(self,command=lambda:(other_leave_func(self)),text='Other Leaves',bg='#3895D3',fg='white',width=22,font='helvetica 12 bold',relief='groove').place(x=40,y=20)

                global pending_leave_list

                cols = ('ID','Leave Type','From','To','Status')
                
                pending_leave_list =ttk.Treeview(self, columns=cols,show='headings',selectmode='browse')
                
                verscrlbar = ttk.Scrollbar(self,orient ="horizontal",command=pending_leave_list.xview)

                verscrlbar.pack(side ='left', fill ='x',expand='yes')

                pending_leave_list.configure(xscrollcommand = verscrlbar.set)

                pending_leave_list.column('# 1',anchor=CENTER, width=75)
                pending_leave_list.column('# 2',anchor=CENTER, width=75)
                pending_leave_list.column('# 3',anchor=CENTER, width=75)
                pending_leave_list.column('# 4',anchor=CENTER, width=75)
                pending_leave_list.column('#5',anchor=CENTER, width=75)

                global get2entry

                get2entry=StringVar()

                enter_id=Label(self,text='Enter Employee ID to Approve or Reject :',bg='white',fg='blue',wraplength=130).place(x=0,y=380)
                enter_id_font=Entry(self,textvariable=get2entry,relief='solid').place(x=135,y=388)

                accept=Button(self,text='Approve',command=approve_button,bg='#3DED97',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=20,y=440)
                reject=Button(self,text='Reject',command=reject_button,bg='#FF0000',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=120,y=440)
                forward=Button(self,text='Forward',command=forward_button,bg='#2A9DF4',fg='white',font='helvetica 12 bold',relief='groove',width=6).place(x=220,y=440)

                for col in cols:
                        pending_leave_list.heading(col, text=col)
                        pending_leave_list.place(x=0,y=120)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(view_leave_frame),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def attendance_date(parent):

        monthget=monthname.get()

        attendence_uid=uid.get()

        #present

        present_days_box=Label(parent,text='■',bg='white',fg='blue',font=30).place(x=20,y=80)
        present_days=Label(parent,text='Present : ',bg='white',fg='black',font='helvetica 12').place(x=40,y=80)

        import mysql.connector as p1
        conp1=p1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curp1=conp1.cursor()

        queryp1='select Distinct((select count(distinct(logindate)) from attendance)-(select count(distinct(logindate)) from attendance,november_holiday where november_holiday.dates=attendance.logindate)) from attendance,november_holiday where id =(%s)'
        valuep1=attendence_uid,

        curp1.execute(queryp1,valuep1)

        recordp1=curp1.fetchall()

        for w in recordp1:

                present_w=w[0]

                present_ultra_label=Label(parent,text=present_w,bg='white',fg='black',font=12).place(x=130,y=80)
        
        #absent
        
        absent_days_box=Label(parent,text='■',bg='white',fg='yellow',font=30).place(x=20,y=120)
        absent_days=Label(parent,text='Absent : ',bg='white',fg='black',font='helvetica 12').place(x=40,y=120)
        
        #holidays

        holidays_box=Label(parent,text='■',bg='white',fg='green',font=30).place(x=20,y=160)
        holidays_label=Label(parent,text='Holidays : ',bg='white',fg='black',font='helvetica 12').place(x=40,y=160)

        import mysql.connector as h1
        conh1=h1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curh1=conh1.cursor()

        queryh1='SELECT COUNT(*) FROM november_holiday'

        curh1.execute(queryh1)

        resulth1=curh1.fetchall()

        for x in resulth1:

                holiday_x=x[0]

                holiday_no=Label(parent,text=x,bg='white',fg='black',font=12).place(x=130,y=160)
        
        #leaves

        leave_box=Label(parent,text='■',bg='white',fg='red',font=30).place(x=20,y=200)
        leave_label_=Label(parent,text='Leaves : ',bg='white',fg='black',font='helvetica 12').place(x=40,y=200)

        import mysql.connector as l1

        conl1=l1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curl1=conl1.cursor()

        leave_uid=uid.get()
        print(leave_uid)

        queryl1='SELECT COUNT(*) FROM DAYOFF WHERE ID=(%s) and month=(%s)'
        valuel1=(leave_uid,monthget)

        curl1.execute(queryl1,valuel1)

        resultl1=curl1.fetchall()

        for y in resultl1:

                leave_y=y[0]

                leave_number=Label(parent,text=y[0],bg='white',fg='black',font=12).place(x=130,y=200)

                from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
                from matplotlib.figure import Figure
                 
                  
                #canvas1 = Canvas(parent, width = 100, height = 100)
                #canvas1.pack()

                u=0

                new_york = float(present_w) 
                paris = float(u) 
                london = float(holiday_x)
                titan = float(leave_y)

                figure2 = Figure(figsize=(2.8,2)) 
                subplot2 = figure2.add_subplot(111) 
                labels2 = 'Present','Absent','Holidays','Leaves'
                pieSizes = [float(new_york),float(paris),float(london),float(titan)]
                explode2 = (0, 0, 0, 0)
                subplot2.pie(pieSizes,  labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90,textprops={'fontsize': 8}) 
                subplot2.axis('equal')  
                pie2 = FigureCanvasTkAgg(figure2, parent) 
                pie2.get_tk_widget().place(x=20,y=280)

        
class attendance(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                #under_cons=Label(self,text='Under Construction',bg='red',fg='white',font=('helvetica 14 bold'),relief='groove',width=25).place(x=0,y=360)

                count_att=Label(self,text='*Attendance Counted From 01 Of Every Month',bg='white',fg='blue',font=('helvetica 10')).place(x=0,y=0)

                select_month=Label(self,text='Select Month : ',bg='white',fg='blue').place(x=20,y=40)

                global monthname

                monthname=StringVar()
                
                month_list=ttk.Combobox(self,values=[

                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"],textvariable=monthname).place(x=120,y=40)

                month_btn=Button(self,text='→',bg='white',fg='black',relief='solid',height=1,width=2,command=lambda:(attendance_date(self))).place(x=270,y=40)

                
                #year
       
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def project_func(parent):

        import mysql.connector as P1
        
        conp1=P1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curp1=conp1.cursor()

        pro=uid.get()
        
        #queryp1='SELECT Description,LastDate,AssignedBy from projects where id=(%s) and status = (%s)'
        queryp1='select description,lastdate,AssignedBy from projects where id=(%s) and status=(%s) or status=(%s)'
        valuep1=(pro,'Not Submitted','Forwarded')

        curp1.execute(queryp1,valuep1)

        resultp1=curp1.fetchall()

        for i, (Description,LastDate,AssignedBy) in enumerate(resultp1, start=1):
                project_list.insert("", "end",values=(Description,LastDate,AssignedBy))

def submit_project_func():

        import mysql.connector as p2

        conp2=p2.connect(host='localhost',user='root',password='dayem',database='pycode')
        curp2=conp2.cursor()

        pro=uid.get()

        descget=descalpha.get()
        
        queryp2='Update Projects set status = (%s) where id=(%s) and description = (%s)'
        valuep2=('Submitted',pro,descget)

        curp2.execute(queryp2,valuep2)

        conp2.commit()

        messagebox.showinfo('Submitted','Project Submitted Successfully')

def forward_project_to_id():
        import mysql.connector as f2

        conf2=f2.connect(host='localhost',user='root',password='dayem',database='pycode')
        curf2=conf2.cursor()

        pro_id_get=uid.get()

        descget=descalpha.get()

        idtoget=idtoforward.get()

        queryf2='update projects set status=(%s),id=(%s),assigned_id=(%s) where description=(%s)'
        #queryp2='Update Projects set status = (%s) where id=(%s) and description = (%s)'
        #valuep2=('Forwarded',pro,descget)
        #forw
        valuef2=('Forwarded',idtoget,pro_id_get,descget)

        curf2.execute(queryf2,valuef2)

        conf2.commit()

        messagebox.showinfo('Forwarded','Project Forwarded')

        #curp2.execute(queryp2,valuep2)

        #conp2.commit()

        

        
class projects(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                btn_show=Button(self,text='Your Projects',command=lambda:(project_func(self)),bg='#3895D3',fg='white',width=22,font='helvetica 12 bold',relief='groove').place(x=40,y=20)

                global project_list

                cols = ('Project Description','Last Date','Assigned By')
                
                project_list =ttk.Treeview(self, columns=cols,show='headings',selectmode='browse')
                
                verscrlbar = ttk.Scrollbar(self,orient ="horizontal",command=project_list.xview)

                verscrlbar.pack(side ='left', fill ='x',expand='yes')

                project_list.configure(xscrollcommand = verscrlbar.set)

                project_list.column('# 1',anchor=CENTER,width=140)
                project_list.column('# 2',anchor=CENTER, width=75)
                project_list.column('# 3',anchor=CENTER, width=120)

                global descalpha

                global idtoforward

                descalpha=StringVar()

                idtoforward=StringVar()


                for col in cols:
                        project_list.heading(col, text=col)
                        project_list.place(x=0,y=120)

                description_label=Label(self,text='Description to Submit/Forward :',fg='blue',bg='white',wraplength=120).place(x=0,y=360)

                description_entry=Entry(self,textvariable=descalpha,relief='solid').place(x=130,y=360)

                submit_current_project=Button(self,text='Submit Current Project',bg='#3DED97',fg='white',font='helvetica 10 bold',command=submit_project_func).place(x=10,y=440)

                # Forward Project

                idtoforward_label=Label(self,text='ID to Forward :',fg='blue',bg='white').place(x=0,y=400)

                idtoforward_entry=Entry(self,textvariable=idtoforward,relief='solid').place(x=130,y=400)

                forward_project_button=Button(self,text='Forward Project',bg='#77C3EC',fg='white',font='helvetica 10 bold',command=forward_project_to_id).place(x=180,y=440)

                #ID to Forward
                
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(assigned_or_assign),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)


def assign_project_55():

        import mysql.connector as ap2

        conap2=ap2.connect(host='localhost',user='root',password='dayem',database='pycode')
        curap2=conap2.cursor()

        
        queryap2=''
        valueap2=('Submitted',pro)

        curp2.execute(queryp2,valuep2)

        conp2.commit()

        messagebox.showinfo('Submitted','Project Submitted Successfully')

def insertintosql():

        a98=assigned_id.get()
        a99=assigned_description.get()
        a100=last_date_of_projects.get()
        a101='Not Submitted'
        a102=uid.get()


        import mysql.connector as A68

        con68=A68.connect(host='localhost',user='root',password='dayem',database='pycode')
        cur68=con68.cursor()

        query103='SELECT NAME FROM DEPARTMENT WHERE UID=(%s)'
        value103=a102,

        cur68.execute(query103,value103)
        result68=cur68.fetchall()

        for a104 in result68:

                a105=a104[0]

                query68='INSERT INTO PROJECTS VALUES (%s,%s,%s,%s,%s,%s)'
                value68=(a98,a99,a100,a101,a105,a102)

                cur68.execute(query68,value68)

                con68.commit()

                messagebox.showinfo('Assigned','Project Assigned Successfully')
        

class assign_project_frame(Frame):

        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                global assigned_id

                global assigned_description

                global last_date_of_projects

                assigned_id=StringVar()

                assigned_description=StringVar()

                last_date_of_projects=StringVar()

                assign_label=Label(self,text='Enter Employee ID to Assign :',bg='white',fg='blue',font='helvetica').place(x=20,y=40)
                
                assign_entry=Entry(self,textvariable=assigned_id,relief='solid').place(x=100,y=70)
                
                #assign_button=Button(self,text='→',bg='white',fg='black',relief='groove').place(x=150,y=40)

                desc=Label(self,text='Description : ',bg='white',fg='blue',font='helvetica').place(x=20,y=120)
                desc_entry=Entry(self,textvariable=assigned_description,relief='solid').place(x=100,y=150)
                

                ld=Label(self,text='Last Date : ',bg='white',fg='blue',font='helvetica').place(x=20,y=200)
                ld_entry=Entry(self,textvariable=last_date_of_projects,relief='solid').place(x=100,y=230)
                

                assign_button=Button(self,text='Assign',bg='black',fg='white',relief='groove',font='helvetica 12',command=insertintosql).place(x=20,y=300)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(assigned_or_assign),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)


                        

class assigned_or_assign(Frame):
        
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                your_projects_Button=Button(self,command=lambda:controller.show_frame(projects),text='Assigned Projects',bg='#1B1B1B',fg='#A4DE02',font='helvetica 14 bold',wraplength=100,width=8,height=3,relief='groove').place(x=40,y=120)

                other_project_button=Button(self,command=lambda:controller.show_frame(assign_project_frame),text='Assign Project',bg='black',fg='white',font='helvetica 14 bold',wraplength=100,width=8,height=3,relief='groove').place(x=160,y=120)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)


def submitted_project_show(parent):

        import mysql.connector as P7
        
        conp7=P7.connect(host='localhost',user='root',password='dayem',database='pycode')
        curp7=conp7.cursor()

        prop7=uid.get()
        
        queryp7='SELECT Description,LastDate from projects where id=(%s) and status = (%s)'
        valuep7=(prop7,'Submitted')

        curp7.execute(queryp7,valuep7)

        resultp7=curp7.fetchall()

        for i, (Description,LastDate) in enumerate(resultp7, start=1):
                submitted_project_list.insert("", "end",values=(Description,LastDate))
class submitted_projects(Frame):

        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                submitted_btn_show=Button(self,text='Your Projects',command=lambda:(submitted_project_show(self)),bg='#3895D3',fg='white',width=22,font='helvetica 12 bold',relief='groove').place(x=40,y=20)

                global submitted_project_list

                cols = ('Project Description','Last Date')
                
                submitted_project_list =ttk.Treeview(self, columns=cols,show='headings',selectmode='browse')
                
                verscrlbar = ttk.Scrollbar(self,orient ="horizontal",command=submitted_project_list.xview)

                verscrlbar.pack(side ='left', fill ='x',expand='yes')

                submitted_project_list.configure(xscrollcommand = verscrlbar.set)

                submitted_project_list.column('# 1',anchor=CENTER,width=225)
                submitted_project_list.column('# 2',anchor=CENTER, width=75)


                for col in cols:
                        submitted_project_list.heading(col, text=col)
                        submitted_project_list.place(x=0,y=120)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def qr_generator():

        #Employee ID

        b90=employeeidentry.get()

        #Name

        b91=employeenameentry.get()

        #Department

        b92=employeedepartmententry.get()

        #Post

        b93=employeepostentry.get()

        #Organization

        if b90=='':

                messagebox.showerror('Error','Fill the Empty Field')

        else:

                b94='PyCodePro.com'

                data=(b90,b91,b92,b93,b94)

                img=qrcode.make(data)

                try:
                        global qr55

                        qr55=b91+b93+'.jpeg'
                        
                        img.save(qr55)

                        import mysql.connector as qr22

                        conqr22=qr22.connect(host='localhost',user='root',password='dayem',database='pycode')
                        curqr22=conqr22.cursor()

                        queryqr22='INSERT INTO QR VALUES (%s,%s,%s,%s,%s,%s)'
                        valueqr22=(b90,b91,b92,b93,b94,qr55)

                        curqr22.execute(queryqr22,valueqr22)
                        conqr22.commit()

                        messagebox.showinfo('Forwarded','Request Forwarded To CEO')

                except:

                        messagebox.showerror('Error','QR Cannot Be Generated Twice')

                        messagebox.showinfo('Visit','Please Visit View QR')

class request_qr(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                global employeeidentry
                employeeidentry=StringVar()

                global employeenameentry
                employeenameentry=StringVar()

                global employeedepartmententry
                employeedepartmententry=StringVar()

                global employeepostentry
                employeepostentry=StringVar()
                
                employeeid=Label(self,text='Employee ID :',fg='blue',bg='white',font=('helvetica 11')).place(x=0,y=30)
                employeeentry=Entry(self,textvariable=employeeidentry,relief='solid').place(x=140,y=30)

                employeeName=Label(self,text='Employee Name :',fg='blue',bg='white',font=('helvetica 11')).place(x=0,y=70)
                employeeentryname=Entry(self,textvariable=employeenameentry,relief='solid').place(x=140,y=70)

                department_of=Label(self,text='Department :',fg='blue',bg='white',font=('helvetica 11')).place(x=0,y=110)
                employeedepartment=Entry(self,textvariable=employeedepartmententry,relief='solid').place(x=140,y=110)

                post_of_employee=Label(self,text='Post :',fg='blue',bg='white',font=('helvetica 11')).place(x=0,y=150)
                employeepost=Entry(self,textvariable=employeepostentry,relief='solid').place(x=140,y=150)

                submit_qr=Button(self,text='Submit',command=qr_generator,bg='white',fg='blue',relief='groove').place(x=20,y=220)

                

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(qr_generator_frame),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def view_qr_func(parent):

        qridget=uid.get()

        import mysql.connector as r1

        conr1=r1.connect(host='localhost',user='root',password='dayem',database='pycode')
        curr1=conr1.cursor()

        queryr1='select qrlocation,status from qr where id = (%s)'
        valuer1=qridget,

        curr1.execute(queryr1,valuer1)

        recordr1=curr1.fetchall()

        for xr1 in recordr1:

                newimage=xr1[0]

                if xr1[1]=='Approved':

                        global pic
                        global qr_image
                        global img2qr
                        pic = Image.open(newimage)
                        pic = pic.resize((250, 250))
                        qr_image = ImageTk.PhotoImage(pic)
                        img2qr=Label(parent, image=qr_image).place(x=23,y=180)

                else:

                        messagebox.showinfo('Pending','QR Not Approved yet')

class qr_generator_frame(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                

                #view_qr

                view_qr=Button(self,text='View QR Code',command=lambda:(view_qr_func(self)),wraplength=100,fg='white',font='helvetica 14 bold',bg='orange',height=3,width=8,relief='groove').place(x=40,y=80)

                #request_qr

                request_qr_button=Button(self,text='Request QR Code',command=lambda:controller.show_frame(request_qr),wraplength=100,fg='white',font='helvetica 14 bold',bg='#FC4C4E',height=3,width=8,relief='groove').place(x=160,y=80)

                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def yd_func(parent):

        import mysql.connector as yd

        conyd=yd.connect(host='localhost',user='root',password='dayem',database='pycode')

        curyd=conyd.cursor()

        yd_id_get=uid.get()

        queryyd='SELECT UID,NAME,DEPT,POST,DOJ,DOB,MAIL,MOB,APLN from details where uid=(%s)'
        valueyd=yd_id_get,

        curyd.execute(queryyd,valueyd)

        resultyd=curyd.fetchall()

        for xyd in resultyd:

                ayd=xyd[0]
                byd=xyd[1]
                cyd=xyd[2]
                dyd=xyd[3]
                eyd=xyd[4]
                fyd=xyd[5]
                gyd=xyd[6]
                hyd=xyd[7]
                iyd=xyd[8]

        id_show=Label(parent,text=ayd,bg='white',fg='black',font='helvetica 12').place(x=140,y=20)

        #Name

        name_show=Label(parent,text=byd,bg='white',fg='black',font='helvetica 12').place(x=140,y=60)

        #Department

        dept_show=Label(parent,text=cyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=100)

        #Post

        post_show=Label(parent,text=dyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=140)

        #DOJ

        doj_show=Label(parent,text=eyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=180)

        #DOB

        dob_show=Label(parent,text=fyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=220)

        #Mail

        mail_show=Label(parent,text=gyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=260)

        #Mobile

        mobile_show=Label(parent,text=hyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=300)

        #APLN

        apln_show=Label(parent,text=iyd,bg='white',fg='black',font='helvetica 12').place(x=140,y=340)

class your_details(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                id_label_yd=Button(self,text='Employee ID : ',command=lambda:yd_func(self),bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=11).place(x=20,y=20)
                name_label_yd=Label(self,text='Name : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=60)
                dept_label_yd=Label(self,text='Department : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=100)
                post_label_yd=Label(self,text='Post : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=140)
                doj_label_yd=Label(self,text='Date of Joining',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=180)
                dob_label_yd=Label(self,text='Date of Birth',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=220)
                mail_label_yd=Label(self,text='Mail : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=260)
                mobile_label_yd=Label(self,text='Phone : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=300)
                apln_label_yd=Label(self,text='APLN : ',bg='white',fg='black',relief='solid',borderwidth=1,font='helvetica 12',width=12).place(x=20,y=340)
                pw_button_yd=Button(self,text='Change Password',bg='#FFFF33',fg='black',relief='solid',borderwidth=1,font='helvetica',command=lambda:controller.show_frame(change_password)).place(x=20,y=380)

                
                #Go Back Button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)

def change_pw_func():

        pw_id=uid.get()

        getoldpw=oldpw.get()
        getnewpw=newpw.get()
        getcnfpw=cnfnewpw.get()

        import mysql.connector as c22

        conc22=c22.connect(host='localhost',user='root',password='dayem',database='pycode')
        curc22=conc22.cursor()

        if getoldpw==getnewpw:
                messagebox.showinfo('Error','New Password Cannot Be Same As New Password')

        elif getnewpw==getcnfpw:

                queryc22='UPDATE LOGIN SET PW = (%s) where id = (%s)'
                valuec22=(getnewpw,pw_id)

                curc22.execute(queryc22,valuec22)

                conc22.commit()

                queryc33='UPDATE DETAILS SET PW = (%s) where uid = (%s)'
                valuec33=(getnewpw,pw_id)

                curc22.execute(queryc33,valuec33)
                conc22.commit()

                messagebox.showinfo('Changed','Password Changed Successfully')

class change_password(Frame):
        def __init__(self,parent,controller):
                Frame.__init__(self,parent)

                global oldpw
                global newpw
                global cnfnewpw

                oldpw=StringVar()
                newpw=StringVar()
                cnfnewpw=StringVar()

                prev_pw=Label(self,text='Old Password',fg='black',bg='white').place(x=20,y=20)
                entry_pw=Entry(self,textvariable=oldpw,relief='solid',show='•').place(x=130,y=20)
                new_pw=Label(self,text='New Password',fg='black',bg='white').place(x=20,y=60)
                new_pw_entry=Entry(self,textvariable=newpw,relief='solid',show='•').place(x=130,y=60)
                cnf_new=Label(self,text='Confirm Password',fg='black',bg='white').place(x=20,y=100)
                entry_new_cnf=Entry(self,textvariable=cnfnewpw,relief='solid',show='•').place(x=130,y=100)

                sub=Button(self,text='Submit',bg='white',fg='black',relief='groove',command=change_pw_func).place(x=20,y=160)

                

                #Go Back Button
                gb_btn=Button(self,text='⏎',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(your_details),width=9).place(x=0,y=480)

                #main screen button
                ms_btn=Button(self,text='⌘',bg='black',fg='white',font='helvetica 12 bold',command=lambda:controller.show_frame(main_menu),width=9).place(x=100,y=480)

                #logout button
                lg_btn=Button(self,text='⎗',bg='black',fg='white',font='helvetica 12 bold',command=lambda:(logouttime(),controller.show_frame(logout)),width=9).place(x=200,y=480)



                
                

app = tkinterApp()
app.mainloop() 
                
