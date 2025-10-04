import mysql.connector as sq
R=sq.connect(host='localhost',user='root',passwd='Tekina11',charset='utf8')
d=R.cursor()
d.execute('create database if not exists Counselling')
d.execute('use Counselling')
d.execute('create table if not exists student(Name varchar(30),Gender varchar(30),DOB varchar(50),Phone_no varchar(30),Email_ID varchar(30),Password varchar(30),Cut_off varchar(30),Interest varchar(30),Course varchar(30),College varchar(45))')
from tkinter import *
import pickle
def add():
    f=open('new3.dat','ab')
    nl=[]
    nl=[EID,P,m,g,day,pn,cutoff,c,course,college]
    pickle.dump(nl,f)
    f.close()
from tkinter import *
from tkinter import messagebox
from tkinter import *
def display():
    global Found
    H=Tk()
    H.geometry('800x800')
    H.configure(bg='pink')
    H.title('REGISTERED STUDENT"S DETAILS')
    L1=Label(H,text='NAME OF STUDENT=',bg='light blue').grid(row=1,column=170,padx=20,pady=10)
    L2=Label(H,text=m,bg='light blue').grid(row=1,column=175)
    L3=Label(H,text='GENDER=',bg='green',fg='yellow').grid(row=2,column=170,padx=20,pady=20)
    L4=Label(H,text=g,bg='green',fg='yellow').grid(row=2,column=175)
    L5=Label(H,text='DATE OF BIRTH=',bg='blue',fg='white').grid(row=3,column=170,padx=20,pady=20)
    L6=Label(H,text=day,bg='blue',fg='white').grid(row=3,column=175)
    L7=Label(H,text='PHONE NO=',bg='grey',fg='white').grid(row=4,column=170,padx=20,pady=20)
    L8=Label(H,text=str(pn),bg='grey',fg='white').grid(row=4,column=175)
    L9=Label(H,text='MAIL-ID=',bg='orange').grid(row=5,column=170,padx=20,pady=20)
    L10=Label(H,text=EID,bg='orange').grid(row=5,column=175)
    Label(H,text='CUTOFF=',bg='violet').grid(row=6,column=170,padx=20,pady=20)
    Label(H,text=cutoff,bg='violet').grid(row=6,column=175,padx=20,pady=20)
    L11=Label(H,text='INTEREST=',bg='red',fg='white').grid(row=7,column=170,padx=20,pady=20)
    L12=Label(H,text=c,bg='red',fg='white').grid(row=7,column=175)
    L13=Label(H,text='COURSE=',bg='brown',fg='white').grid(row=8,column=170,padx=20,pady=20)
    L14=Label(H,text=course,bg='brown',fg='white').grid(row=8,column=175)
    L15=Label(H,text='COLLEGE=',bg='yellow',fg='red').grid(row=9,column=170,padx=20,pady=20)
    L16=Label(H,text=college,bg='yellow',fg='red').grid(row=9,column=175)
    add()
    def dele():
        H.destroy()
    Button(H,text='EXIT',command=dele).grid(row=10,column=175)
    if Found==True:
        d.execute('update student set Cut_off=%s where Password="%s"'%(cutoff,P))
        d.execute('update student set Interest="%s" where Password="%s"'%(c,P))
        d.execute('update student set Course="%s" where Password="%s"'%(course,P))
        d.execute('update student set College="%s" where Password="%s"'%(college,P))
        R.commit()
    else:
        d.execute('insert into student(Name,Gender,DOB,Phone_no,EMail_ID,Password,Cut_off,Interest,Course,College)Values("{}","{}","{}",{},"{}","{}",{},"{}","{}","{}")'.format(m,g,day,pn,EID,P,cutoff,c,course,college))
        R.commit()
def call():
    g=Tk()                           
    g.configure(bg='pink')
    g.geometry('400x400')
    g.title('COLLEGE ADMISTRATION')
    Label(g,text='WHAT ARE YOUR INTERESTS-',bg='pink',fg='blue').grid(row=0,column=2,padx=20,pady=20)
    def engi():
        g.destroy()
        gg=Tk()
        gg.title('CUT-OFF MARK')
        gg.geometry('350x100')
        gg.configure(bg='pink')
        global c
        c='engineering'
        mark=StringVar(gg)
        Label(gg,text='ENTER YOUR CUTOFF',bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)    #c-intrest,mark,coarse,fac
        cc=Entry(gg,width=10,borderwidth=5,textvariable=mark).grid(row=3,column=1,padx=20,pady=10)
        def new():
            global cutoff
            p=mark.get()
            cutoff=int(p)
            if cutoff>200:
                messagebox.showerror('ERROR','Please enter a valid mark!! Mark greater than 200!!!')
            elif cutoff<170:
                gg.destroy()
                new3=Tk()
                new3.geometry('400x100')
                new3.configure(bg='pink')
                Label(new3,text='THERE ARE NO COLLEGES FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=1,padx=10,pady=10)
                def fi():
                    new3.destroy()
                Button(new3,text='EXIT',command=fi,bg='pink',fg='blue').grid(row=2,column=3,padx=10,pady=10)
            else:
                gg.destroy()
                new=Tk()
                new.title('ENGINEERING')
                new.geometry('500x500')
                new.configure(bg='pink')
                Label(new,text='THE COURSES AVAILABLE FOR ENGINEERING ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=20)
                def aero():
                    new.destroy()
                    global course
                    course='Aerospace'
                    def mit():
                        new1.destroy()
                        global college
                        college='MIT'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def anna():
                        new1.destroy()
                        global college
                        college='Anna University'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  srm():
                        new1.destroy()
                        global college
                        college='SRM Institute of Science and Technology'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  amrita():
                        new1.destroy()
                        global college
                        college='SRM Institute of Science and Technology'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='MIT',command=mit,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='ANNA UNIVERSITY',command=anna,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Amrita School of Engineering',command=amrita,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='Amrita School of Engineering',command=amrita,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Amrita School of Engineering',command=amrita,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                    elif cutoff<170:
                        Label(new1,text='NO COLLEGES AVAILABLE FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        def des():
                            new1.destroy()
                        Button(new1,text='EXIT',command=des).grid(row=6,column=1)
                def mech():
                    new.destroy()
                    global course
                    course='Mechanical Engineering'
                    def mit():
                        new1.destroy()
                        global college
                        college='MIT'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  vit():
                        new1.destroy()
                        global college
                        college='VIT Chennai'
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  ssn():
                        new1.destroy()
                        global college
                        college='SSN College of Engineering'
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 200>=cutoff>195:
                        Button(new1,text='MIT',command=mit,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='VIT Chennai',command=vit,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                        Button(new1,text='SSN College of Engineering',command=ssn,bg='pink',fg='blue').grid(row=5,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='VIT Chennai',command=vit,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 185>cutoff>=175:
                          Button(new1,text='SSN College of Engineering',command=ssn,bg='pink',fg='blue').grid(row=5,column=0,padx=10,pady=10)
                def bio():
                    new.destroy()
                    global course
                    course='Biotechnology'
                    def anna():
                        new1.destroy()
                        global college
                        college='Anna University'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  sat():
                        new1.destroy()
                        global college
                        college='Satyabhama Institute'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  mit():
                        new1.destroy()
                        global college
                        college='MIT'
                        new2=Tk()
                        new2.geometry('400x200')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='MIT',command=mit,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Anna University',command=anna,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                def comp():
                    new.destroy()
                    global course
                    course='Computer Engineering'
                    def anna():
                        new1.destroy()
                        global college
                        college='Anna University'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  vit():
                        new1.destroy()
                        global college
                        college='VIT Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  sat():
                        new1.destroy()
                        global college
                        college='Satyabhama Institute'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('400x400')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=20)
                    if 200>=cutoff>=195:
                        Button(new1,text='VIT',command=vit,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Anna University',command=anna,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='VIT',command=vit,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Satyabhama Institute',command=sat,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                def elec():
                    new.destroy()
                    global course
                    course='Electrical Engineering'
                    def anna():
                        new1.destroy()
                        global college
                        college='Anna University'
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  vit():
                        new1.destroy()
                        global college
                        college='VIT Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  mit():
                        new1.destroy()
                        global college
                        college='MIT'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='MIT',command=mit,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='VIT',command=vit,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Anna University',command=anna,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='VIT',command=vit,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 184>cutoff>=170:
                          Button(new1,text='SRM Institute and Technology',command=srm,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                Button(new,text='Aerospace',command=aero,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                Button(new,text='Mechanical',command=mech,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                Button(new,text='Biotechnology',command=bio,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                Button(new,text='Computer engineering',command=comp,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                Button(new,text='Electrical Engineering',command=elec,bg='pink',fg='blue').grid(row=5,column=0,padx=10,pady=10)
        Button(gg,text='CONFIRM',command=new,bg='pink',fg='blue').grid(row=5,column=1,padx=10,pady=10)
    def com():
        g.destroy()
        gg=Tk()
        gg.geometry('350x100')
        gg.configure(bg='pink')
        global c
        c='Commerce'
        mark=StringVar(gg)
        Label(gg,text='ENTER YOUR BOARD MARK',bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)    #c-intrest,mark,coarse,fac
        cc=Entry(gg,width=10,borderwidth=5,textvariable=mark).grid(row=3,column=1)
        def new():
            global cutoff
            p=mark.get()
            cutoff=int(p)
            if cutoff>500:
                messagebox.showerror('ERROR','Please enter a valid mark!! Mark greater than 500!!!')
            elif cutoff<460:
                gg.destroy()
                new3=Tk()
                new3.geometry('400x100')
                new3.configure(bg='pink')
                Label(new3,text='THERE ARE NO COLLEGES FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=1,padx=10,pady=10)
                def fi():
                    new3.destroy()
                Button(new3,text='EXIT',command=fi,bg='pink',fg='blue').grid(row=2,column=3,padx=10,pady=10)
            else:
                gg.destroy()
                new=Tk()
                new.geometry('400x400')
                new.configure(bg='pink')
                Label(new,text='THE COURSES AVAILABLE FOR COMMERCE ARE-',fg='blue',bg='pink').grid(row=0,column=0,padx=10,pady=10)
                def BCom():
                    new.destroy()
                    global course
                    course='B.Com'
                    def loyal():
                        new1.destroy()
                        global college
                        college='Loyola College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='MCC Chennai' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='Presidency College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='D.G Vaishnav College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='MCC',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Presidency College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='D.G Vaishnav College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='D.G Vaishnav College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                def BAeng():
                    new.destroy()
                    global course
                    course='B.A English'
                    def loyal():
                        new1.destroy()
                        global college
                        college='Loyola College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def psg():
                        new1.destroy()
                        global college
                        college='PSG College of Arts and Science' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='Presidency College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  ram():
                        new1.destroy()
                        global college
                        college='Ramakrishna Mission Vivekananda College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='PSG',command=psg,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Presidency College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                def MCom():
                    new.destroy()
                    global course
                    course='M.Com'
                    def stella():
                        new1.destroy()
                        global college
                        college='Loyola College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def pre():
                        new1.destroy()
                        global college
                        college='Presidency College' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  psg():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  ram():
                        new1.destroy()
                        global college
                        college='Ramakrishna Mission Vivekananda College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=10,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='Stella Maris College',command=stella,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='PSG',command=psg,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Presidency College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Stella Maris College',command=stella,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                def BEco():
                    new.destroy()
                    global course
                    course='B.Economics'
                    def loyal():
                        new1.destroy()
                        global college
                        college='Loyola College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='MCC Chennai' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='Presidency College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='D.G Vaishnav College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',fg='blue',bg='pink').grid(row=0,column=0,padx=10,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='MCC',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Presidency College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='D.G Vaishnav College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='D.G Vaishnav College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 470>cutoff>=460:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                def BAcc():
                    new.destroy()
                    global course
                    course='B Acc & Finance'
                    def loyal():
                        new1.destroy()
                        global college
                        college='Loyola College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='MCC Chennai' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def pre():
                        new1.destroy()
                        global college
                        college='Presidency College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  ram():
                        new1.destroy()
                        global college
                        college='Ramakrishna Mission Vivekananda College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',fg='blue',bg='pink').grid(row=0,column=0)
                    if 500>=cutoff>=485:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='MCC',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='Presidency College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                    elif 485>cutoff>=470:
                        utton(new1,text='Ramakrishna Mission Vivekananda College',command=ram,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                    elif 470>cutoff>=460:
                        Button(new1,text='Loyola College',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                Button(new,text='BCom',command=BCom,bg='pink',fg='blue').grid(row=1,column=0,padx=10,pady=10)
                Button(new,text='BA.English',command=BAeng,bg='pink',fg='blue').grid(row=2,column=0,padx=10,pady=10)
                Button(new,text='M.Com',command=MCom,bg='pink',fg='blue').grid(row=3,column=0,padx=10,pady=10)
                Button(new,text='B Economics',command=BEco,bg='pink',fg='blue').grid(row=4,column=0,padx=10,pady=10)
                Button(new,text='B Acc & Finance',command=BAcc,bg='pink',fg='blue').grid(row=5,column=0,padx=10,pady=10)
        Button(gg,text='CONFIRM',command=new,bg='pink',fg='blue').grid(row=5,column=1,padx=10,pady=10)
    def med():
        g.destroy()
        gg=Tk()
        gg.geometry('350x100')
        gg.configure(bg='pink')
        global c
        c='Medical'
        mark=StringVar(gg)
        Label(gg,text='ENTER YOUR CUTOFF',bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)    #c-intrest,mark,coarse,fac
        cc=Entry(gg,width=10,borderwidth=5,textvariable=mark).grid(row=3,column=1)
        def new():
            global cutoff
            p=mark.get()
            cutoff=int(p)
            if cutoff>200:
                messagebox.showerror('ERROR','Please enter a valid mark!! Mark greater than 200!!!')
            elif cutoff<170:
                gg.destroy()
                new3=Tk()
                new3.geometry('400x100')
                new3.configure(bg='pink')
                Label(new3,text='THERE ARE NO COLLEGES FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=1,padx=10,pady=10)
                def fi():
                    new3.destroy()
                Button(new3,text='EXIT',command=fi,bg='pink',fg='blue').grid(row=2,column=3,padx=10,pady=10)
            else:
                gg.destroy()
                new=Tk()
                new.geometry('400x300')
                new.configure(bg='pink')
                Label(new,text='THE COURSES AVAILABLE FOR MEDICAL ARE-',fg='blue',bg='pink').grid(row=0,column=0,padx=10,pady=10)
                def mbbs():
                    new.destroy()
                    global course
                    course='MBBS'
                    def cmc():
                        new1.destroy()
                        global college
                        college='Christian Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def sav():
                        new1.destroy()
                        global college
                        college='Saveetha Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  srm():
                        new1.destroy()
                        global college
                        college='SRM Institute of Science and Technology'
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    def  mcc():
                        new1.destroy()
                        global college
                        college='Madras Medical College'
                        new2=Tk()
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=10,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=10,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',fg='blue',bg='pink').grid(row=0,column=0,padx=10,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='MMC',command=mcc,fg='blue',bg='pink').grid(row=1,column=0,padx=10,pady=10)
                        Button(new1,text='Christian Medical College',command=cmc,fg='blue',bg='pink').grid(row=2,column=0,padx=10,pady=10)
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,fg='blue',bg='pink').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Saveetha Medical College',command=sav,fg='blue',bg='pink').grid(row=4,column=0,padx=10,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,fg='blue',bg='pink').grid(row=3,column=0,padx=10,pady=10)
                        Button(new1,text='Christian Medical College',command=cmc,fg='blue',bg='pink').grid(row=4,column=0,padx=10,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Christian Medical College',command=cmc,fg='blue',bg='pink').grid(row=4,column=0,padx=10,pady=10)
                def ms():
                    new.destroy()
                    global course
                    course='MS'
                    def cmc():
                        new1.destroy()
                        global college
                        college='Christian Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  smc():
                        new1.destroy()
                        global college
                        college='Saveetha Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  mmc():
                        new1.destroy()
                        global college
                        college='Madras Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',fg='blue',bg='pink').grid(row=0,column=0,padx=20,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='Christian Medical College',command=cmc,fg='blue',bg='pink').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='SRM Institute of Science and Technology',command=srm,fg='blue',bg='pink').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='Saveetha Medical College',command=smc,fg='blue',bg='pink').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Madurai Medical College',command=mmc,fg='blue',bg='pink').grid(row=4,column=0,padx=20,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,fg='blue',bg='pink').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Saveetha Medical College',command=smc,fg='blue',bg='pink').grid(row=4,column=0,padx=20,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Christian Medical College',command=cmc,fg='blue',bg='pink').grid(row=4,column=0,padx=20,pady=10)
                def md():
                    new.destroy()
                    global course
                    course='MD'
                    def cmc():
                        new1.destroy()
                        global college
                        college='Christian Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def srm():
                        new1.destroy()
                        global college
                        college='SRM Institute and Technology' 
                        new2=Tk()
                        new2.configure(bg='pink')
                        new2.geometry('400x300')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  smc():
                        new1.destroy()
                        global college
                        college='Saveetha Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  mmc():
                        new1.destroy()
                        global college
                        college='Madras Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0)
                    if 200>=cutoff>=195:
                        Button(new1,text='Christian Medical College',command=cmc,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='SRM Institute of Science and Technology',command=srm,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='Saveetha Medical College',command=smc,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Madurai Medical College',command=mmc,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 195>cutoff>=195:
                        Button(new1,text='SRM Institute Of Science And Technology',command=srm,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Saveetha Medical College',command=smc,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Christian Medical College',command=cmc,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def bams():
                    new.destroy()
                    global course
                    course='BAMS'
                    def dam():
                        new1.destroy()
                        global college
                        college='Dharma Ayurveda Medical College and Hospital'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def sri():
                        new1.destroy()
                        global college
                        college='Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  sai():
                        new1.destroy()
                        global college
                        college='Sri Sairam Ayurveda Medical College and Research Centre'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  ayu():
                        new1.destroy()
                        global college
                        college='Ayurveda College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 200>=cutoff>=195:
                        Button(new1,text='Dharma Ayurveda Medical College and Hospital',command=dam,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya',command=sri,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='Sri Sairam Ayurveda Medical College and Research Centre',command=sai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Ayurveda College',command=ayu,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 195>cutoff>=185:
                        Button(new1,text='Sri Sairam Ayurveda Medical College and Research Centre',command=sai,bg='pink',fg='blue').grid(row=3,column=0)
                        Button(new1,text='Ayurveda College',command=ayu,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 185>cutoff>=170:
                          Button(new1,text='Sri Sairam Ayurveda Medical College and Research Centre',command=sai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def bhms(): #Vinayaka Missions Homoeopathic Medical College and Hospital\n2.Government Homoeopathic Medical College and Hospital\n3.Sarada Krishna Homoeopathic Medical College\n4.Venkateswara Homoeopathic Medical College and Hospital
                    new.destroy()
                    global course
                    course='BHMS'
                    def vmh():
                        new1.destroy()
                        global college
                        college='Vinayaka Missions Homoeopathic Medical College and Hospital'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def ghm():
                        new1.destroy()
                        global college
                        college='Government Homoeopathic Medical College and Hospital' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  skh():
                        new1.destroy()
                        global college
                        college='Sarada Krishna Homoeopathic Medical College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vhm():
                        new1.destroy()
                        global college
                        college='Venkateswara Homoeopathic Medical College and Hospital'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 200<=cutoff<=190:
                        Button(new1,text='Vinayaka Missions Homoeopathic Medical College and Hospital',command=vmh,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Government Homoeopathic Medical College and Hospital',command=ghm,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='Sarada Krishna Homoeopathic Medical College',command=skh,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='Venkateswara Homoeopathic Medical College and Hospital',command=vhm,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 190>cutoff>=180:
                         Button(new1,text='Sarada Krishna Homoeopathic Medical College',command=skh,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                         Button(new1,text='Venkateswara Homoeopathic Medical College and Hospital',command=vhm,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 180>cutoff>=170:
                          Button(new1,text='Venkateswara Homoeopathic Medical College and Hospital',command=vhm,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                Button(new,text='MBBS',command=mbbs,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                Button(new,text='MS',command=ms,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                Button(new,text='MD',command=md,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                Button(new,text='BAMS',command=bams,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                Button(new,text='BHMS',command=bhms,bg='pink',fg='blue').grid(row=5,column=0,padx=20,pady=10)
        Button(gg,text='CONFIRM',command=new,bg='pink',fg='blue').grid(row=4,column=1,padx=20,pady=10)
    def fas():                              
        g.destroy()
        gg=Tk()
        gg.geometry('350x200')
        gg.configure(bg='pink')
        global c
        c='Fashion Designing'
        mark=StringVar(gg)
        Label(gg,text='ENTER YOUR BOARD MARK',bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)    #c-intrest,mark,coarse,fac
        cc=Entry(gg,width=10,borderwidth=5,textvariable=mark).grid(row=3,column=1)
        def new():
            global cutoff
            p=mark.get()
            cutoff=int(p)
            if cutoff>500:
                messagebox.showerror('ERROR','Please enter a valid mark!! Mark greater than 500!!!')
            elif cutoff<460:
                gg.destroy()
                new3=Tk()
                new3.geometry('400x100')
                new3.configure(bg='pink')
                Label(new3,text='THERE ARE NO COLLEGES FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=1,padx=10,pady=10)
                def fi():
                    new3.destroy()
                Button(new3,text='EXIT',command=fi,bg='pink',fg='blue').grid(row=2,column=3,padx=10,pady=10)
            else:
                gg.destroy()
                new=Tk()
                new.geometry('500x500')
                new.configure(bg='pink')
                Label(new,text='THE COURSES AVAILABLE FOR FASHION DESIGNING ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                def BCom():
                    new.destroy()
                    global course
                    course='B.Des'
                    def loyal():
                        new1.destroy()
                        global college
                        college='National Institute of Fashion Technology(NIFT) Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='Bishop Appaswamy College' 
                        new2=Tk()
                        new2.configure(bg='pink')
                        new2.geometry('400x300')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='N.G.P College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('400x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Bishop Appaswamy College',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='PSG College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def BAeng():
                    new.destroy()
                    global course
                    course='M.Des'
                    def loyal():
                        new1.destroy()
                        global college
                        college='National Institute of Fashion Technology(NIFT) Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='Bishop Appaswamy College' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='N.G.P College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('300x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Bishop Appaswamy College',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='PSG College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def MCom():
                    new.destroy()
                    global course
                    course='B.F Tech'
                    def loyal():
                        new1.destroy()
                        global college
                        college='National Institute of Fashion Technology(NIFT) Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='Bishop Appaswamy College' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='N.G.P College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('400x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Bishop Appaswamy College',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='PSG College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def BEco():
                    new.destroy()
                    global course
                    course='B.S.C Fashion Designing'
                    def loyal():
                        new1.destroy()
                        global college
                        college='National Institute of Fashion Technology(NIFT) Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='Bishop Appaswamy College' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='N.G.P College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.title('COLLEGE')
                    new1.geometry('400x300')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Bishop Appaswamy College',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='PSG College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                def BAcc():
                    new.destroy()
                    global course
                    course='M.S.C Fashion Designing'
                    def loyal():
                        new1.destroy()
                        global college
                        college='National Institute of Fashion Technology(NIFT) Chennai'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def mcc():
                        new1.destroy()
                        global college
                        college='Bishop Appaswamy College' 
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  pre():
                        new1.destroy()
                        global college
                        college='PSG College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    def  vai():
                        new1.destroy()
                        global college
                        college='N.G.P College'
                        new2=Tk()
                        new2.geometry('400x300')
                        new2.configure(bg='pink')
                        Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                        def fac():
                            new2.destroy()
                            display()
                        Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                    new1=Tk()
                    new1.geometry('400x300')
                    new1.title('COLLEGE')
                    new1.configure(bg='pink')
                    Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                    if 500>=cutoff>=485:
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                        Button(new1,text='Bishop Appaswamy College',command=mcc,bg='pink',fg='blue').grid(row=2,column=0,padx=20,pady=10)
                        Button(new1,text='PSG College',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 485>cutoff>=470:
                        Button(new1,text='N.G.P College',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                        Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                    elif 470>cutoff>=460:
                          Button(new1,text='National Institute of Fashion Technology(NIFT) Chennai',command=loyal,bg='pink',fg='blue').grid(row=4,column=0)
                Button(new,text='B.Des',command=BCom,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                Button(new,text='M.Des',command=BAeng,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                Button(new,text='B.F Tech',command=MCom,bg='pink',fg='blue').grid(row=5,column=0,padx=20,pady=10)
                Button(new,text='B.S.C Fashion designing',command=BEco,bg='pink',fg='blue').grid(row=7,column=0,padx=20,pady=10)
                Button(new,text='M.S.C Fashion Designing',command=BAcc,bg='pink',fg='blue').grid(row=9,column=0,padx=20,pady=10)
        Button(gg,text='CONFIRM',command=new,bg='pink',fg='blue').grid(row=5,column=1,padx=20,pady=10)
    def arint():                              
        g.destroy()
        gg=Tk()
        gg.title('MARK')
        gg.geometry('350x100')
        gg.configure(bg='pink')
        global c
        c='Artificial Intelligence'
        mark=StringVar(gg)
        Label(gg,text='ENTER YOUR BOARD MARK',bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)    #c-intrest,mark,coarse,fac
        cc=Entry(gg,width=10,borderwidth=5,textvariable=mark).grid(row=3,column=1)
        global course
        course='AI'
        def new():
            global cutoff
            p=mark.get()
            cutoff=int(p)
            if cutoff>500:
                messagebox.showerror('ERROR','Please enter a valid mark!! Mark greater than 500!!!')
            elif cutoff<460:
                gg.destroy()
                new3=Tk()
                new3.geometry('400x100')
                new3.configure(bg='pink')
                Label(new3,text='THERE ARE NO COLLEGES FOR YOUR MARK',bg='pink',fg='blue').grid(row=1,column=1,padx=10,pady=10)
                def fi():
                    new3.destroy()
                Button(new3,text='EXIT',command=fi,bg='pink',fg='blue').grid(row=2,column=3,padx=10,pady=10)
            else:
                gg.destroy()
                def loyal():
                    new1.destroy()
                    global college
                    college='IIT Delhi'
                    new2=Tk()
                    new2.geometry('400x300')
                    new2.configure(bg='pink')
                    Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                    def fac():
                        new2.destroy()
                        display()
                    Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                def mcc():
                    new1.destroy()
                    global college
                    college='Chennai Indian Institute of Technology' 
                    new2=Tk()
                    new2.geometry('400x300')
                    new2.configure(bg='pink')
                    Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                    def fac():
                        new2.destroy()
                        display()
                    Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                def  pre():
                    new1.destroy()
                    global college
                    college='IIM Calcutta'
                    new2=Tk()
                    new2.geometry('400x300')
                    new2.configure(bg='pink')
                    Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                    def fac():
                        new2.destroy()
                        display()
                    Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                def  vai():
                    new1.destroy()
                    global college
                    college='IISC Bangalore'
                    new2=Tk()
                    new2.geometry('400x300')
                    new2.configure(bg='pink')
                    Label(new2,text='YOU HAVE BEEN SUCCESSFULLY REGISTRED',bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
                    def fac():
                        new2.destroy()
                        display()
                    Button(new2,text='SHOW DETAILS',command=fac,bg='pink',fg='blue').grid(row=5,column=3,padx=20,pady=10)
                new1=Tk()
                new1.geometry('400x300')
                new1.configure(bg='pink')
                new1.title('COLLEGE')
                Label(new1,text='THE AVAILABLE COLLEGES FOR YOUR MARK ARE-',bg='pink',fg='blue').grid(row=0,column=0,padx=20,pady=10)
                if 500>=cutoff>=485:
                    Button(new1,text='IIT Delhi',command=loyal,bg='pink',fg='blue').grid(row=1,column=0,padx=20,pady=10)
                    Button(new1,text='Chennai Indian Institute of Technology',bg='pink',fg='blue',command=mcc).grid(row=2,column=0,padx=20,pady=10)
                    Button(new1,text='IIM Calcutta',command=pre,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                    Button(new1,text='IISC Bangalore',command=vai,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                elif 485>cutoff>=470:
                    Button(new1,text='IISC Bangalore',command=vai,bg='pink',fg='blue').grid(row=3,column=0,padx=20,pady=10)
                    Button(new1,text='IIT Delhi',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
                elif 470>cutoff>=460:
                      Button(new1,text='IIT Delhi',command=loyal,bg='pink',fg='blue').grid(row=4,column=0,padx=20,pady=10)
        Button(gg,text='CONFIRM',command=new,bg='pink',fg='blue').grid(row=5,column=1,padx=20,pady=10)
    Button(g,text='ENGINEERING',command=engi,bg='pink',fg='blue').grid(row=2,column=2,padx=20,pady=10)
    Button(g,text='COMMERCE',bg='pink',fg='blue',command=com).grid(row=4,column=2,padx=20,pady=10)
    Button(g,text='MEDICAL',bg='pink',fg='blue',command=med).grid(row=5,column=2,padx=20,pady=10)
    Button(g,text='FASHION DESIGNING',bg='pink',fg='blue',command=fas).grid(row=6,column=2,padx=20,pady=10)
    Button(g,text='ARTIFICIAL INTELLIGENCE',bg='pink',fg='blue',command=arint).grid(row=7,column=2,padx=20,pady=10)
    g.mainloop()
Found=False
log=Tk()
log.title('LOGIN PAGE')
log.geometry('600x400')
log.configure(bg='pink')
mail=StringVar()
pasw=StringVar()
Label(log,text='LOGIN-',fg='blue',bg='pink').grid(row=1,column=2,padx=10,pady=10)
Label(log,text='MAIL-ID',fg='blue',bg='pink').grid(row=3,column=1,padx=10,pady=10)
Label(log,text='PASSWORD',fg='blue',bg='pink').grid(row=4,column=1,padx=10,pady=10)
k=Entry(log,font=('Calibri',11),textvariable=mail,fg='blue',bg='pink',borderwidth=5).grid(row=3,column=2,padx=10,pady=10)                    
l=Entry(log,font=('Calibri',11),show='*',textvariable=pasw,bg='pink',fg='blue',borderwidth=5).grid(row=4,column=2,padx=10,pady=10)
def con():
    global Found
    a=[];E=0;eE=0
    sw='';wq=''
    sw=mail.get()
    aq=pasw.get()
    import pickle
    f=open('new3.dat','rb')
    try:
        while True:
            As=pickle.load(f)
            a.append(As)
    except EOFError:
        pass
    for i in a:
        global EID
        global P
        global m
        global g
        global day
        global pn
        global cutoff
        global c
        global course
        global college
        EID=i[0];P=i[1];g=i[3];day=i[4];pn=str(i[5]);cutoff=str(i[6]);c=i[7];course=i[8];college=i[9];m=i[2]
        Ec=0;ne=0
        if i[0]==sw:
            E+=1
            if len(aq)>=6:
                if i[0].count('@')==1:
                    if i[1]==aq:
                        try:
                            eE+=1
                            log.destroy()
                            Found=True
                            call()
                        except:
                            break
    if E==0:
        messagebox.showerror('ERROR','INCORRECT MAIL-ID')
    elif eE==0:
        messagebox.showerror('ERROR','INCORRECT PASSWORD')
    elif eE==0 and E==0:
        messagebox.showerror('ERROR','INCORRECT CREDENTIALS')
def regi():
    log.destroy()
    DOB=Tk()
    DOB.geometry('500x200')
    DOB.title('CHECKING ELIGIBILITY')   
    DOB.configure(bg='pink')
    dob=StringVar()
    Label(DOB,text='ENTER YOUR DATE OF BIRTH(DD/MM/YYYY)=',bg='pink',fg='blue').grid(row=3,column=3,padx=20,pady=20)            
    Entry(DOB,font=('Calibri',11),textvariable=dob,bg='pink',fg='blue',borderwidth=5).grid(row=3,column=6,padx=20,pady=20)  
    D=''
    def chk():
        global D
        D=dob.get()
        if D.count('/')==2:
            q=D.split('/')
            if 2000<=int(q[2])<=2006:
                messagebox.showinfo('ELIGIBLE','YOU ARE ELIGIBLE TO REGISTER!')
                DOB.destroy()
                global day
                day=D
                s=Tk()
                s.title('REGISTRATION FORM')
                s.configure(bg='green')
                s.geometry('800x500')
                mm=StringVar()
                gg=StringVar()
                gg.set('SELECT YOUR GENDER')
                pnn=IntVar()
                p=StringVar()
                u=StringVar()
                v=StringVar()
                eE=Label(text='NAME=',bg='pink').grid(row=3,column=25,padx=10,pady=10)
                G=Label(text='GENDER=',bg='red').grid(row=4,column=25,padx=10,pady=10)
                PH=Label(text='PHONE NUMBER=',bg='violet').grid(row=5,column=25,padx=10,pady=10)
                E=Label(text='EMAIL ID=',bg='orange').grid(row=6,column=25,padx=10,pady=10)
                c=Label(text='PASSWORD=',bg='light blue').grid(row=7,column=25,padx=10,pady=10)
                Z=Label(text='CONFIRM PASSWORD=',bg='yellow').grid(row=8,column=25,padx=10,pady=10)
                pl=Label(text='PLEASE FILL IN ALL DETAILS IN THIS FORM!!',bg='black',fg='white').grid(row=9,column=3,padx=10,pady=10)
                ee=Entry(s,font=('Calibri',11),textvariable=mm,bg='pink',borderwidth=3).grid(row=3,column=26)
                drop=OptionMenu(s,gg,'M','F','O').grid(row=4,column=26)
                ph=Entry(s,font=('Calibri',11),textvariable=pnn,bg='violet',borderwidth=3).grid(row=5,column=26)                    
                e=Entry(s,font=('Calibri',11),textvariable=v,bg='orange',borderwidth=3).grid(row=6,column=26)
                i=Entry(s,font=('Calibri',11),textvariable=p,show='*',bg='lightblue',borderwidth=3).grid(row=7,column=26)
                I=Entry(s,font=('Calibri',11),textvariable=u,show='*',bg='yellow',borderwidth=3).grid(row=8,column=26)
                P='';EID='';m='';g='';pn=0
                def comm():
                    global m
                    global g
                    global pn
                    global EID
                    m=mm.get();g=gg.get();pn=pnn.get();EID=v.get()
                    if len(p.get())>=6:
                        if EID.count('@')==1:
                            if len(str(pn))==10:
                                global P
                                P=p.get()
                                W=u.get()
                                if P==W:
                                    s.destroy()
                                else:
                                    messagebox.askretrycancel('ERROR','Passwords don"t match please Retry!!')
                            else:
                                messagebox.showerror('ERROR','Phone number should have 10 digits')
                        else:
                            messagebox.showerror('ERROR','Please enter a valid email-ID')
                    else:
                        messagebox.showwarning('Warning','Password must be atleast 6 characters')
                e=Button(s,text='REGISTER',command=comm,bg='grey').grid(row=10,column=26)
                s.mainloop()
                call()
            else:
                DOB.destroy()
                rrr=Tk()
                rrr.geometry('400x200')
                rrr.configure(bg='pink')
                rrr.title('NOT ELIGIBLE')
                Label(rrr,text='YOU ARE NOT ELIGIBLE TO REGISTER!!',bg='red').grid(row=1,column=2,padx=30,pady=10)
                Label(rrr,text='ONLY STUDENTS AGED BETWEEN 17-22 ARE ELIGIBLE',bg='red').grid(row=2,column=2,padx=30,pady=10)
                def rrR():
                    rrr.destroy()
                Button(rrr,text='EXIT',command=rrR,bg='pink',fg='red').grid(row=4,column=2,padx=30,pady=10)
        else:
            messagebox.showerror('ERROR','INVALID DOB FORMAT')
    Button(DOB,text='CHECK',command=chk,bg='pink',fg='blue').grid(row=4,column=6,padx=20,pady=20)
Button(log,text='CONFIRM',command=con,fg='blue',bg='pink').grid(row=6,column=2,padx=10,pady=10)
Label(log,text='IF YOU HAVE NOT REGISTERED YET, REGISTER BY CLICKING THE "REGISTER" BUTTON',fg='blue',bg='pink').grid(row=7,column=2,padx=10,pady=10)
Button(log,text='REGISTER',command=regi,fg='blue',bg='pink').grid(row=8,column=2,padx=10,pady=10)
log.mainloop()
