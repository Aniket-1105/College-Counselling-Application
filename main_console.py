row=10
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ",end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print('*','COUNSELLING APP','*')
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
Q=input('Press Enter to Start')
print('\nRegister if you don"t have a user ID')

'''from tkinter import *
from tkinter import messagebox

win=Tk()
win.title('HOME PAGE')
win.geometry('500x400')'''

#sql database
import mysql.connector as sq
R=sq.connect(host='localhost',user='root',passwd='Tekina11',charset='utf8')
d=R.cursor()
d.execute('create database if not exists Counselling')
d.execute('use Counselling')
d.execute('create table if not exists students(ID integer,Name char(20),Gender char(10),DOB varchar(20),Phoneno numeric(10),MailID varchar(50),Passwd varchar(40),Interest char(35),Course char(35),College char(65),Faculty char(25),Feesperyear integer)')

from tkinter import *
from tkinter import messagebox


from datetime import date,datetime
today = date.today()

#adding students
D=input('\nEnter your Date of Birth(DD/MM/YYYY)=')
k=input('Have you already registered?(y/n)')
q=D.split('/')
d.execute('select * from students')
Id=d.fetchall()
if Id==[]:
    n=1
else:
    n=Id[-1][0]+1
while k.lower()=='n' and int(q[2])<=2005:
    m=input('Enter name=')
    g=input('Enter your Gender(M/F/O)=')
    pn=int(input('Enter phoneno='))
    if len(str(pn))==10:
        M=input('Enter E-mail ID=')
        A=M.count('@')
        if A==1:
            s=Tk()
            s.title('PASSWORD')
            s.configure(bg='green')
            s.geometry('400x400')
            p=StringVar()
            u=StringVar()
            c=Label(text='PASSWORD=',bg='light blue').grid(row=3,column=3,padx=10,pady=10)
            Z=Label(text='CONFIRM PASSWORD=',bg='yellow').grid(row=4,column=3,padx=10,pady=10)
            i=Entry(s,font=('Calibri',11),textvariable=p,show='*',bg='lightblue').grid(row=3,column=6)
            I=Entry(s,font=('Calibri',11),textvariable=u,show='*',bg='yellow').grid(row=4,column=6)
            P=''
            def comm():
               if len(p.get())>=6:
                   global P
                   P=p.get()
                   W=u.get()
                   if P==W:
                      s.destroy()
                   else:
                      messagebox.askretrycancel('ERROR','Passwords don"t match please Retry!!')
               else:
                   messagebox.showwarning('Warning','Password must be atleast 6 characters')
            e=Button(s,text='REGISTER',command=comm,bg='grey').grid(row=5,column=6)
            s.mainloop()
            print('\n','~'*80,'NEW USER ID CREATED','~'*83)
            I=input('What is your Interest?("Engineering","Arts and Science","Commerce","Fashion designing","Medical","Sociology")')               #interest and college selection
            print('\nNOTE:\nYOU CAN CHANGE YOUR INTEREST AFTER LOGGING IN WITH YOUR E-MAIL ID AND PASSWORD')
            if I.lower()=='engineering':
                print('\nMain Courses offered for Engineering:\na)Aerospace Engineering\nb)Mechanical engineering\nc)Biotechnology\nd)Chemical Engineering\ne)Civil Engineering\nf)Computer Science Engineering\ng)Electrical Engineering')
                c1=input('\nEnter your choice for course selection=')                                                    #Picking courses
                if c1.lower()=='a':
                    a='Aerospace Engineering'
                    print('\nTOP Colleges in Chennai are:\n1.Indian Institute of Technology(IIT) Madras\n2.Anna University\n3.SRM Institute of Science and Technology\n4.Amrita School of Engineering')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            #Picking colleges and faculty
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Luoyi Tao\n2.Dr.M.Ramakrishna\n3.Dr.Nandan K.Sinha\n4.Dr.Bharath M.Govindarajan\n5.Dr.Rajesh G')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Luoyi Tao'
                            f=100000
                            print('Fees is Rs 1,00,000/year with Dr.Luoyi Tao')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                #Registration last process
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M.Ramakrishna'
                            f=89000
                            print('Fees is Rs 89,000/year with Dr.M.Ramakrishna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Nandan K Sinha'
                            f=125000
                            print('Fees is Rs 1,25,000/year with Dr.Nandan K Sinha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Bharath M Govindarajan'
                            f=97000
                            print('Fees is Rs 97,000/year with Dr.Bharath M Govindarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.Rajesh G'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.Rajesh G')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='Anna University'
                        print('Main Faculties:\n1.Dr.B.T.N.Sridhar\n2.Dr.K M Paramasivam\n3.Dr.C.Senthil Kumar\n4.Dr.V Arumugam\n5.Dr.V Suresh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.B.T.N Sridhar'
                            f=145000
                            print('Fees is Rs 1,45,000/year with Dr.B.T.N Sridhar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K.M Paramasivam'
                            f=132000
                            print('Fees is Rs 1,32,000/year with Dr.K.M.Paramasivam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.C Senthil Kumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.C Senthil Kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Arumugam'
                            f=107000
                            print('Fees is Rs 1,07,000/year with Dr.V Arumugam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.V Suresh'
                            f=100000
                            print('Fees is Rs 1,00,000/year with Dr.V Suresh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='SRM Institute'
                        print('\nMain Faculties:\n1.Dr.R Vasudevan\n2.Dr L.R.Ganapathy Subramanian\n3.Dr.S Sivakumar\n4.Dr.T Selvakumaran\n5.Dr.S Gurusideswar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Vasudevan'
                            f=115000
                            print('Fees is Rs 1,15,000/year with Dr.R Vasudevan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.L.R Ganapathy Subramanian'
                            f=92000
                            print('Fees is Rs 92,000/year with Dr.L.R Ganapathy Subramanian')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Sivakumar'
                            f=140000
                            print('Fees is Rs 1,40,000/year with Dr.S Sivakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.T Selvakumaran'
                            f=137000
                            print('Fees is Rs 1,37,000/year with Dr.T Selvakumaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Gurusideshwar'
                            f=110000
                            print('Fees is Rs 1,10,000/year with Dr.S Gurusideshwar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Amrita School of Engineering'
                        print('\nMain Faculty:\n1.Dr Srikrishnan A R\n2.Dr.V Sivadas\n3.Dr.Shantanu Bhowmik\n4.Dr.V Sivakumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Srikrishnan A'
                            f=97000
                            print('Fees is Rs 97,000/year with Dr.Srikrishnan A')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.V Sivadas'
                            f=121000
                            print('Fees is Rs 1,21,000/year with Dr.V Sivadas')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Shantanu Bhowmik'
                            f=131000
                            print('Fees is Rs 1,31,000/year with Dr.Shantanu Bhowmik')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Sivakumar'
                            f=157000
                            print('Fees is Rs 1,57,000/year with Dr.V Sivakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='b':
                    a='Mechanical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.SSN College of Engineering\n5.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            #Picking colleges and faculty
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Seshadri Sekar A\n2.Dr.Abhijit Sarkar\n3.Dr.Anand Krishnasamy\n4.Dr.Amitava Ghosh\n5.Arunachalam D')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Seshadri Sekar'
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.Seshadri Sekar')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                #Registration last process
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Abhijith Sarkar'
                            f=189000
                            print('Fees is Rs 1,89,000/year with Dr.Abhijith Sarkar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Anand Krishnasamy'
                            f=195000
                            print('Fees is Rs 1,95,000/year with Dr.Anand Krishnasamy')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Amitava Ghosh'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.Amitava Ghosh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.D Arunachalam'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.D Arunachalam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.T V Gopal\n2.Dr.S Prabhu\n3.Dr.T Rajasekaran\n4.Dr.K Duraivelu\n5.Dr.V Suresh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.T V Gopal'
                            f=205000
                            print('Fees is Rs 2,05,000/year with Dr.T V Gopal')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.S Prabhu'
                            f=232000
                            print('Fees is Rs 2,32,000/year with Dr.S Prabhu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Rajasekaran'
                            f=190000
                            print('Fees is Rs 1,90,000/year with Dr.T Rajasekaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Duraivelu'
                            f=207000
                            print('Fees is Rs 2,07,000/year with Dr.K Duraivelu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.P Nandakumar'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.P Nandakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.K Annamalai\n2.Dr Bhaskara Rao\n3.Dr.R Deivanathan\n4.Dr.Padmanabhan\n5.Dr.G Sakthivel')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Annamalai'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.K Annamalai')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Bhaskara Rao'
                            f=162000
                            print('Fees is Rs 1,62,000/year with Dr.Bhaskara Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Deivanathan'
                            f=165000
                            print('Fees is Rs 1,65,000/year with Dr.R Deivanathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Padmanabhan'
                            f=177000
                            print('Fees is Rs 1,77,000/year with Dr.Padmanabhan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.G Sakthivel'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.G Sakthivel')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='SSN College of Engineering'
                        print('\nMain Faculty:\n1.Dr.S Vijayan\n2.Dr.Vijaysekar K\n3.Dr.A Jayasekar\n4.Dr.V Rajkumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Vijayan'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.S Vijayan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vijaysekar K'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.Vijaysekar K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.A Jayasekar'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.A Jayasekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Rajkumar'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.V Rajkumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr.S Vijayan\n2.Dr.Vijaysekar K\n3.Dr.A Jayasekar\n4.Dr.V Rajkumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Vijayan'
                            f=1,97000
                            print('Fees is Rs 1,97,000/year with Dr.S Vijayan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vijaysekar K'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.Vijaysekar K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.A Jayasekar'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.A Jayasekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Rajkumar'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.V Rajkumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='c':
                    a='Biotechnology'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.Anna University\n3.SRM Institute\n4.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Gopalakrishnan\n2.Dr.Arumugam Rajavelu\n3.Dr.Chandraraj\n4.Dr.N Manoj\n5.Dr.N Michael')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gopalakrishnan'
                            f=170000
                            print('Fees is Rs 1,70,000/year with Dr.Gopalakrishnan')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Arumugam Rajavelu'
                            f=189000
                            print('Fees is Rs 1,89,000/year with Dr.Arumugam Rajavelu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Chandraraj'
                            f=125000
                            print('Fees is Rs 1,80,000/year with Dr.Chandraraj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.N Manoj'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.N Manoj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Michael'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.N Michael')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='Anna University'
                        print('Main Faculties:\n1.Dr.B.S Lakshmi\n2.Dr.M Sukumar\n3.Dr.C.D Anuradha\n4.Dr.S Ramalingam\n5.Dr.S Ranganathan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.B.S Lakshmi'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.B.S Lakshmi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Sukumar'
                            f=212000
                            print('Fees is Rs 2,12,000/year with Dr.M Sukumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.C.D Anuradha'
                            f=190000
                            print('Fees is Rs 1,90,000/year with Dr.C.D Anuradha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Ramalingam'
                            f=187000
                            print('Fees is Rs 1,87,000/year with Dr.S Ramalingam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Ranganathan'
                            f=200000
                            print('Fees is Rs 2,00,000/year with Dr.S Ranganathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                                          
                        C='SRM Institute'
                        print('\nMain Faculties:\n1.Dr.R A Nazeer\n2.Dr M Ramya\n3.Dr.N Selvamurugan\n4.Dr.K Ramani\n5.Dr.S Barathi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R A Nazeer'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.R A Nazeer')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Ramya'
                            f=192000
                            print('Fees is Rs 1,92,000/year with Dr.M Ramya')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.N Selvamurugan'
                            f=180000
                            print('Fees is Rs 1,80,000/year with Dr.N Selvamurugan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Ramani'
                            f=187000
                            print('Fees is Rs 1,87,000/year with Dr.K Ramani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Barathi'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.S Barathi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr K Rahman\n2.Dr.R Hari\n3.Dr.T Prashaant\n4.Dr.G Sekar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Rahman'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.K Rahman')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.R Hari'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.R Hari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Prashaant'
                            f=174000
                            print('Fees is Rs 1,74,000/year with Dr.T Prashaant')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G Sekar'
                            f=188000
                            print('Fees is Rs 1,88,000/year with Dr.G Sekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='d':
                    a='Chemical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.HITS Chennai\n4.Rajalakshmi Engineering College')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Arun K\n2.Dr.Aravind kumar\n3.Dr.Abhijith P\n4.Dr.A Kannan\n5.R Nagarajan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Arun K'
                            f=220000
                            print('Fees is Rs 2,20,000/year with Dr.Arun K')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Aravind kumar'
                            f=239000
                            print('Fees is Rs 2,39,000/year with Dr.Aravind kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Abhijith P'
                            f=198000
                            print('Fees is Rs 1,98,000/year with Dr.Abhijith P')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.A Kannan'
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.A Kannan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Nagarajan'
                            f=234000
                            print('Fees is Rs 2,34,000/year with Dr.R Nagarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.M P Rajesh\n2.Dr.Ashish K\n3.Dr.S Vishal\n4.Dr.K Suresh\n5.Dr.K Selvam')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M P Rajesh'
                            f=225000
                            print('Fees is Rs 2,25,000/year with Dr.M P Rajesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Ashish K'
                            f=242000
                            print('Fees is Rs 2,42,000/year with Dr.Ashish K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Vishal'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.S Vishal')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Suresh'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.K K Suresh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Selvam'
                            f=250500
                            print('Fees is Rs 2,50,500/year with Dr.K Selvam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                          
                        C='HITS Chennai'
                        print('\nMain Faculties:\n1.Dr.Anitha A\n2.Dr.B Vivek\n3.Dr.R Keerthana\n4.Dr.Siva prakash\n5.Dr.J Malathy')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Anitha A'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.Anitha A')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.B Vivek'
                            f=162000
                            print('Fees is Rs 2,32,600/year with Dr.B Vivek')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Keerthana'                            
                            f=243890
                            print('Fees is Rs 2,43,890/year with Dr.R Keerthana')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':                                                  
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Siva prakash'
                            f=244400
                            print('Fees is Rs 2,44,400/year with Dr.Siva prakash')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.G Saravanan'
                            f=246000
                            print('Fees is Rs 2,46,000/year with Dr.G Saravanan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Rajalakshmi College of Engineering'
                        print('\nMain Faculty:\n1.Dr.K Nagarajan\n2.Dr.Vincent J\n3.Dr.S Sivamani\n4.Dr.K Sriram\n5.N Kalaiarasi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Nagarajan'
                            f=197560
                            print('Fees is Rs 1,97,560/year with Dr.K Nagarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vincent J'
                            f=261800
                            print('Fees is Rs 2,61,800/year with Dr.Vincent J')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Sivamani'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.S Sivamani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Sriram'
                            f=187650
                            print('Fees is Rs 1,87,650/year with Dr.K Sriram')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Kalaiarasi'
                            f=237600
                            print('Fees is Rs 2,37,600/year with Dr.N Kalaiarasi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='e':
                    a='Civil Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.HITS Chennai\n4.VIT Chennai')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.P Alagappan\n2.Dr.Amlan kumar\n3.Dr.G Appa Rao\n4.Dr.Ashwin M\n5.R Benny')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.P Alagappan'
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.P Alagappan')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Amlan kumar'
                            f=232550
                            print('Fees is Rs 2,32,550/year with Dr.Amlan kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G Appa Rao'
                            f=228800
                            print('Fees is Rs 2,28,800/year with Dr.G Appa Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Ashwin M'
                            f=247750
                            print('Fees is Rs 2,47,750/year with Dr.Ashwin M')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Benny'
                            f=234000
                            print('Fees is Rs 2,34,000/year with Dr.R Benny')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.M Annadurai\n2.Dr.Senthil Selvan\n3.Dr.R Ravi\n4.Dr.S Aparna\n5.Dr.K Sunny')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M Annadurai'
                            f=245000
                            print('Fees is Rs 2,45,000/year with Dr.M Annadurai')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Senthil Selvan'
                            f=222000
                            print('Fees is Rs 2,22,000/year with Dr.Senthil selvan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Ravi'
                            f=221600
                            print('Fees is Rs 2,21,600/year with Dr.R Ravi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Aparna'
                            f=237580
                            print('Fees is Rs 2,37,580/year with Dr.S Aparna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Sunny'
                            f=250570
                            print('Fees is Rs 2,50,570/year with Dr.K Sunny')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                          
                        C='HITS Chennai'
                        print('\nMain Faculties:\n1.Dr.V Subbiah\n2.Dr.V Paramasivam\n3.Dr.J Samuel\n4.Dr.S Vijayan\n5.Dr.G Saravanan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.V Subbiah'
                            f=243000
                            print('Fees is Rs 2,43,000/year with Dr.V Subbiah')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.V Paramasivam'
                            f=252730
                            print('Fees is Rs 2,52,730/year with Dr.V Paramasivam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.J Samuel'                            
                            f=199000
                            print('Fees is Rs 1,99,000/year with Dr.J Samuel')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':                                                  
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Prabhu'                            #continue from here
                            f=243000
                            print('Fees is Rs 2,43,000/year with Dr.V Prabhu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.J Malathy'
                            f=226000
                            print('Fees is Rs 2,26,000/year with Dr.J Malathy')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='VIT Chennai'
                        print('\nMain Faculty:\n1.Dr.Mohan Ganesh\n2.Dr.Sekar SK\n3.Dr.T Meena\n4.Dr.S.S Ajeesh\n5.N Rama Rao')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Mohan Ganesh'
                            f=241560
                            print('Fees is Rs 2,41,560/year with Dr.Mohan Ganesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Sekar SK'
                            f=263820
                            print('Fees is Rs 2,63,820/year with Dr.Sekar SK')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Meena'
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.T Meena')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.S Ajeesh'
                            f=251650
                            print('Fees is Rs 2,51,650/year with Dr.S.S Ajeesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Rama Rao'
                            f=233400
                            print('Fees is Rs 2,33,400/year with Dr.N Rama Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                                                  
                                pass
                elif c1.lower()=='f':
                    a='Computer Engineering'
                    print('\nBest colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.SSN College of Engineering\n5.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.John A\n2.Dr.C Sarath\n3.Dr.Deepak K\n4.Dr.M Sreenivasan\n5.Dr.M Nitesh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.John A'
                            f=223000
                            print('Fees is Rs 2,23,000/year with Dr.John A')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.C Sarath'
                            f=219000
                            print('Fees is Rs 2,19,000/year with Dr.C Sarath')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Deepak K'
                            f=198890
                            print('Fees is Rs 1,98,890/year with Dr.Deepak K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.M Sreenivasan'
                            f=211000
                            print('Fees is Rs 2,11,000/year with Dr.M Sreenivasan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.M Nitesh'
                            f=195000
                            print('Fees is Rs 1,95,000/year with Dr.M Nitesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.S Krishna\n2.Dr.C Vasudevan\n3.Dr.B Amudha\n4.Dr.S.S Sridhar\n5.Dr.R Revathi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Krishna'
                            f=225000
                            print('Fees is Rs 2,25,000/year with Dr.S Krishna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.C Vasudevan'
                            f=221570
                            print('Fees is Rs 2,21,570/year with Dr.C Vasudevan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.B Amudha'                            
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.B Amudha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.S Sridhar'
                            f=237000
                            print('Fees is Rs 2,37,000/year with Dr.S.S Sridhar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Revathi'
                            f=233000
                            print('Fees is Rs 2,33,000/year with Dr.R Revathi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.R Ganesan\n2.Dr.S Geeta\n3.Dr.K.R Jagadish\n4.Dr.L Jagannathan\n5.Dr.N Maheshwari')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Ganesan'
                            f=245660
                            print('Fees is Rs 2,45,660/year with Dr.R Ganesan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.S Geeta'
                            f=226000
                            print('Fees is Rs 2,26,000/year with Dr.S Geeta')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K.R Jagadish'
                            f=236890
                            print('Fees is Rs 2,36,890/year with Dr.K.R Jagadish')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.L Jagannathan'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.L Jagannathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Maheshwari'                  
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.N Maheshwari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='SSN College of Engineering'
                        print('\nMain Faculty:\n1.Dr.R.S Milton\n2.Dr.Chitra Babu\n3.Dr.G Raghu\n4.Dr.S Bhuvana')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R.S Milton'
                            f=235000
                            print('Fees is Rs 2,35,000/year with Dr.R.S Milton')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Chitra Babu'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.Chitra Babu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G Raghu'
                            f=221000
                            print('Fees is Rs 2,21,000/year with Dr.G Raghu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Bhuvana'
                            f=237000
                            print('Fees is Rs 2,37,000/year with Dr.S Bhuvana')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr.T Sasikala\n2.Dr.K Verma\n3.Dr.S Vedhika\n4.Dr.H Siddharth')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.T Sasikala'
                            f=246000
                            print('Fees is Rs 2,46,000/year with Dr.T Sasikala')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K Verma'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.K Verma')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Vedhika'
                            f=232500
                            print('Fees is Rs 2,32,500/year with Dr.S Vedhika')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.H Siddharth'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.H Siddharth')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='g':
                    a='Electrical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.MIT Chennai\n5.HITS Chennai')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.R Venkatesh\n2.Dr.K.S Pradeep\n3.Dr.D Soumya\n4.Dr.A Sankaran\n5.Dr.M Anbarasu')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Venkatesh'
                            f=233000
                            print('Fees is Rs 2,33,000/year with Dr.R Venkatesh')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K.S Pradeep'
                            f=219780
                            print('Fees is Rs 2,19,780/year with Dr.K.S Pradeep')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.D Soumya'
                            f=234890
                            print('Fees is Rs 2,34,890/year with Dr.D Soumya')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.A Sankaran'
                            f=222000
                            print('Fees is Rs 2,22,000/year with Dr.A Sankaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.M Anbarasu'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.M Anbarasu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.A Ratnam\n2.Dr.K Vijaykumar\n3.Dr.K Saravanan\n4.Dr.S Padmini\n5.Dr.K Mohanraj')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.A Ratnam'
                            f=229950
                            print('Fees is Rs 2,29,950/year with Dr.A Ratnam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K Vijaykumar'
                            f=231870
                            print('Fees is Rs 2,31,870/year with Dr.K Vijaykumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K Saravanan'                            
                            f=237500
                            print('Fees is Rs 2,37,500/year with Dr.K Saravanan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Padmini'
                            f=247440
                            print('Fees is Rs 2,47,440/year with Dr.S Padmini')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Mohanraj'
                            f=234100
                            print('Fees is Rs 2,34,100/year with Dr.K Mohanraj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.R Jacob\n2.Dr.B.J Edward\n3.Dr.M Janaki\n4.Dr.C Rani\n5.Dr.N Srihari')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Jacob'
                            f=235690
                            print('Fees is Rs 2,35,690/year with Dr.R Jacob')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.B.J Edward'
                            f=223430
                            print('Fees is Rs 2,23,430/year with Dr.B.J Edward')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.M Janaki'
                            f=232700
                            print('Fees is Rs 2,32,700/year with Dr.M Janaki')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.C Rani'
                            f=267000
                            print('Fees is Rs 2,67,000/year with Dr.C Rani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Srihari'                  
                            f=243660
                            print('Fees is Rs 2,43,660/year with Dr.N Srihari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='MIT Chennai'
                        print('\nMain Faculty:\n1.Dr.Mala John\n2.Dr.M Kannan\n3.Dr.P Prakash\n4.Dr.G Kavitha')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Mala John'
                            f=225670
                            print('Fees is Rs 2,25,670/year with Dr.Mala John')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Kannan'
                            f=247800
                            print('Fees is Rs 2,47,800/year with Dr.M Kannan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P Prakash'
                            f=251000
                            print('Fees is Rs 2,51,000/year with Dr.P Prakash')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G Kavitha'
                            f=225990
                            print('Fees is Rs 2,25,990/year with Dr.G Kavitha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='HITS Chennai'
                        print('\nMain Faculty:\n1.Dr.M Manikandan\n2.Dr.J Alex\n3.Dr.V Preethi\n4.Dr.J Sudhakar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M Manikandan'
                            f=247200
                            print('Fees is Rs 2,47,200/year with Dr.M Manikandan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.J Alex'
                            f=245900
                            print('Fees is Rs 2,45,900/year with Dr.J Alex')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.V Preethi'
                            f=240560
                            print('Fees is Rs 2,40,560/year with Dr.V Preethi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.J Sudhakar'
                            f=237810
                            print('Fees is Rs 2,37,810/year with Dr.J Sudhakar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
                R.commit()
                '''else:
                    print('\nInvalid choice')'''
            elif I.lower()=='arts and science':
                print('\nBest courses offered for Arts and science are:\n1.B.Arts\n2.B.A English\n3.B.B.A(Bachelor of Business Administration)\n4')
                c1=int(input('which course would you like?'))
                if c1==1:
                    a='B.Arts'
                    print('\nBest Colleges for BA Economics in Tamil Nadu are:\n1.Loyola College\n2.PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Loyola College'
                        print('\nMain Faculty:\n1.Dr.R.Leema Rose\n2.Ms.F.Reena\n3.Dr.D.Jerusha Chitra\n4.Ms.J Minothi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.R.Leema Rose'
                            f=98000
                            print('Fees is Rs 98,000/year with Dr.R.Leema Rose')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.F.Reena'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.F.Reena')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='D.Jerusha Chitra'
                            f=90000
                            print('Fees is Rs 90,000/year with D.Jerusha Chitra')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.J Minothi'
                            f=91000
                            f=90000
                            print('Fees is Rs 91,000/year with Ms.J Minothi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='PSG College of Arts and Science'    
                        print('\nMain Faculty:\n1.Shiv Nadar\n2.K. Annamalai\n3.C Vijayakumar\n4.Madhu Bhaskaran')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Shiv Nadar'
                            f=98000
                            print('Fees is Rs 98,000/year with Shiv Nadar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='K.Annamalai'
                            f=90000
                            print('Fees is Rs 90,000/year with K.Annamalai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='C.Vijayakumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Vijayakumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Madhu Baskaran'
                            f=91000
                            print('Fees is Rs 91,000/year with Madhu Baskaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==3:
                        C='Presidency College'     #Dr. K. ATHINARAYANAN ,Dr.B.THAMARAIKKANNAN M.A., Dr.G.SHAIKMEERAN, Dr.G.SEKAR
                        print('\nMain Faculty:\n1.Dr.K.Athinarayanan\n2.Dr.B.Thamaraikkanna\n3.Dr.G.Shaikeeran\n4.Dr.G.Sekar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.K.Athinarayanan'
                            f=98000
                            print('Fees is Rs 98,000/year with Dr.K.Athinarayanan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.B.Thamaraikkanna'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.B.Thamaraikkanna')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G.Shaikeeran'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.G.Shaikeeran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G.Sekar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.G.Sekar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==4:
                        C='Government Arts College'     #Mrs.T.Abirami,Dr.N.Lalitha,Dr.J.Udhaya kumar,Dr.S.Sagayadoss
                        print('\nMain Faculty:\n1.Mrs.T.Abirami\n2.Dr.N.Lalitha\n3.Dr.J.Udhaya kumar\n4.Dr.S.Sagayadoss')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.T.Abirami'
                            f=98000
                            print('Fees is Rs 98,000/year with Mrs.T.Abirami' )
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.N.Lalitha'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.N.Lalitha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.J.Udhaya kumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.J.Udhaya kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.Sagayadoss'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.S.Sagayadoss')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Ramakrishna Mission Vivekananda College'
                        print('\nMain Faculty:\n1.Dr. P. Pattinathar\n2.Dr. A. Satheesh Babu\n3.Dr. M. Arulmaran\n4.Mr. N. Dhinakaran\n5.Dr. G. Ashok Kumar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. P. Pattinathar'
                            f=1,00,000
                            print('Fees is Rs 1,00,000/year with Dr. P. Pattinathar' )
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr. A. Satheesh Babu'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr. A. Satheesh Babu')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F=' Dr.M.Arulmaran' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.M.Arulmaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Mr.N.Dhinakaran'
                            f=91000
                            print('Fees is Rs 91,000/year with Mr.N.Dhinakaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Dr. G. Ashok Kumar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr. G. Ashok Kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==2:
                    a='B.A English'
                    print('The Best Colleges for B.A English are:\n1.Loyala College\n2.PSG College of Arts and Science\n3.Rajeswari Vedachalam Government Arts College\n4.Government Arts College')
                    c3=int(input('enter the choice of college-'))
                    if c3==1:
                        C='Loyala College' #Dr. K.S. Antonysamy, Dr. V. David Jayabalan  Mr. X. Manoharan Dr. P. Mary Vidya Porselvi Ms. D. Christina Sagayamary 
                        print('\nMain Faculty:\n1Dr. K.S. Antonysamy\n2.Dr. V. David Jayabalan\n3.Mr. X. Manoharan\n4.Dr. P. Mary Vidya Porselvi\n5.Ms. D. Christina Sagayamary')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. K.S. Antonysamy'
                            f=1,00,000
                            print('Fees is Rs 1,00,000/year with Dr. K.S. Antonysamy')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr. V. David Jayabalan'
                            f=95000
                            print('Fees is Rs 95,000/year with Dr.V.David Jayabalan ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Mr. X. Manoharan' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=93000
                            print('Fees is Rs 93,000/year with Mr. X. Manoharan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr. P. Mary Vidya Porselvi'
                            f=91500
                            print('Fees is Rs 91,500/year with Dr. P. Mary Vidya Porselvi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Ms. D. Christina Sagayamary'
                            f=94000
                            print('Fees is Rs 94,000/year with Dr. G. Ms. D. Christina Sagayamary')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='PSG College of Arts and Science'
                        print('\nMain Faculty:\n1.Dr. Priya M\n2.Dr.Kausalya D\n3.Dr.Brinda P\n4.Dr.John Suganya M\n5.Dr.Nancy Thambi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. Priya M'
                            f=1,10,000
                            print('Fees is Rs 1,10,000/year with Dr. Priya M ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Kausalya D'
                            f=96000
                            print('Fees is Rs 96,000/year with Dr.Kausalya D')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Brinda P' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=93500
                            print('Fees is Rs 93,500/year with Dr.Brinda P ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.John Suganya M'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.John Suganya M')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Dr.Nancy Thambi'
                            f=94500
                            print('Fees is Rs 94,500/year with Dr.Nancy Thambi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          
                                pass
                d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
                R.commit()
            elif I.lower()=='commerce':
                print('\nBest colleges of Commerce in Chennai:\n1.Loyola College\n2.MCC Chennai\n3.Stella Maris College Chennai\n4.D.G Vaishnav College Chennai\n5.Presidency college chennai')
                c=int(input('\nEnter your choice of college='))
                if c==1:
                    C='Loyola College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.S Moshin\n2.Dr.G Allen\n3.Dr.R Simon\n4.Dr.K Akshay\n5.Dr.R Sushanth')                   
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.S Moshin'
                        f=105800
                        print('Fees is Rs 1,05,800/year with Dr.S Moshin')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.G Allen'
                        f=96550
                        print('Fees is Rs 96,550/year with Dr.G Allen')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.R Simon'
                        f=102000
                        print('Fees is Rs 1,02,000/year with Dr.R Simon')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.K Akshay'
                        f=94500
                        print('Fees is Rs 94,500/year with Dr.K Akshay')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.R Sushanth'                  
                        f=97430
                        print('Fees is Rs 97,430/year with Dr.R Sushanth')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==2:
                    C='MCC Chennai'                                                                                                         
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.A Denson\n2.Dr.R Kurian\n3.Dr.Jayasurya\n4.Dr.S Nandhini\n5.Dr.R Khaleel')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.A Denson'
                        f=104100
                        print('Fees is Rs 1,04,100/year with Dr.A Denson')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')                                                  #continue from here
                            pass
                    elif c2==2:
                        F='Dr.R Kurian'
                        f=203100
                        print('Fees is Rs 2,03,100/year with Dr.R Kurian')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.Jayasurya'
                        f=97430
                        print('Fees is Rs 97,430/year with Dr.Jayasurya')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.S Nandhini'
                        f=97000
                        print('Fees is Rs 97,000/year with Dr.S Nandhini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.A Khaleel'                  
                        f=103620
                        print('Fees is Rs 1,03,620/year with Dr.A Khaleel')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==3:
                    C='Stella Maris College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Amivarsha\n2.Dr.Sarath lal\n3.Dr.G Robert\n4.Dr.K Neerav\n5.Dr.E Sujith')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Amivarsha'
                        f=105800
                        print('Fees is Rs 1,05,800/year with Dr.Amivarsha')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.Sarath Lal'
                        f=100240
                        print('Fees is Rs 1,00,240/year with Dr.Sarath Lal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.G Robert'
                        f=101920
                        print('Fees is Rs 1,01,920/year with Dr.G Robert')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.K Neerav'
                        f=95000
                        print('Fees is Rs 95,000/year with Dr.K Neerav')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.E Sujith'                  
                        f=105160
                        print('Fees is Rs 1,05,160/year with Dr.E Sujith')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==4:
                    C='D.G Vaishnav College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.G Sivan\n2.Dr.P Ramlal\n3.Dr.N Bindhu\n4.Dr.P Dinesh\n5.Dr.T Natarajan')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.G Sivan'
                        f=98900
                        print('Fees is Rs 98,900/year with Dr.G Sivan')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.P Ramlal'
                        f=109000
                        print('Fees is Rs 1,09,000/year with Dr.P Ramlal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.N Bindhu'
                        f=102640
                        print('Fees is Rs 1,02,640/year with Dr.D Nalini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.P Dinesh'
                        f=107220
                        print('Fees is Rs 1,07,220/year with Dr.P Dinesh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Natarajan'                  
                        f=103300
                        print('Fees is Rs 1,03,300/year with Dr.T Natarajan')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==5:
                    C='Presidency College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.N Varsha\n2.Dr.K Sampath\n3.Dr.R Shankar\n4.Dr.N.K Sheetal\n5.Dr.J Rose')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.N Varsha'
                        f=107670
                        print('Fees is Rs 1,07,670/year with Dr.N Varsha')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.K Sampath'                                           #continue
                        f=97320
                        print('Fees is Rs 97,320/year with Dr.K Sampath')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.R Shankar'
                        f=101920
                        print('Fees is Rs 1,01,920/year with Dr.R Shankar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.N.K Sheetal'
                        f=99800
                        print('Fees is Rs 99,800/year with Dr.N.K Sheetal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.J Rose'                  
                        f=96250
                        print('Fees is Rs 96,250/year with Dr.J Rose')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
                R.commit()
                '''else:
                    print('Invalid choice')'''
            elif I.lower()=='fashion designing':
                print('\nBest colleges for Fashion Designing:\n1.National Institute of Fashion Technology(NIFT) Chennai\n2.Bishop Appasamy College of Arts and Science\n3.PSG College of Arts and Science\n4.Dr. N.G.P. Arts & Science College')
                c=int(input('\nEnter your choice of college='))
                if c==1:
                    C='NIFT Chennai'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Narendran M\n2.Dr.A Shreyas\n3.Dr.G Rohit\n4.Dr.R Ajmal\n5.Dr.T Suhail')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.M Narendran'
                        f=215800
                        print('Fees is Rs 2,15,800/year with Dr.M Narendran')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.A Shreyas'
                        f=213250
                        print('Fees is Rs 2,13,250/year with Dr.A Shreyas')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.G Rohit'
                        f=226000
                        print('Fees is Rs 2,26,000/year with Dr.G Rohit')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.R Ajmal'
                        f=220000
                        print('Fees is Rs 2,20,000/year with Dr.R Ajmal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Suhail'                  
                        f=228600
                        print('Fees is Rs 2,28,600/year with Dr.T Suhail')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==2:
                    C='Bishop Appaswamy College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Anil Kumar\n2.Dr.S Sunil\n3.Dr.J Venkat\n4.Dr.N Gayathri\n5.Dr.W Sundar')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.Anil Kumar'
                        f=185800
                        print('Fees is Rs 1,85,800/year with Dr.Anil Kumar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.S Sunil'
                        f=203100
                        print('Fees is Rs 2,03,100/year with Dr.S Sunil')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.J Venkat'
                        f=191000
                        print('Fees is Rs 1,91,000/year with Dr.J Venkat')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.N Gayathri'
                        f=187000
                        print('Fees is Rs 1,87,000/year with Dr.N Gayathri')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.W Sundar'                  
                        f=206620
                        print('Fees is Rs 2,06,620/year with Dr.W Sundar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==3:
                    C='PSG College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.C.V Raman\n2.Dr.P Aryabhatta\n3.Dr.K Abhinav\n4.Dr.S Adharsh\n5.Dr.C Deepak')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.C.V Raman'
                        f=195800
                        print('Fees is Rs 1,95,800/year with Dr.C.V Raman')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.P Aryabhatta'
                        f=204440
                        print('Fees is Rs 2,04,440/year with Dr.P Aryabhatta')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.K Abhinav'
                        f=201000
                        print('Fees is Rs 2,01,000/year with Dr.K Abhinav')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.S Adharsh'
                        f=197000
                        print('Fees is Rs 1,97,000/year with Dr.S Adharsh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.C Deepak'                  
                        f=209120
                        print('Fees is Rs 2,09,120/year with Dr.C Deepak')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==4:
                    C='N.G.P College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.S Anirudh\n2.Dr.H Aadithyaa\n3.Dr.D Nalini\n4.Dr.A Sharon\n5.Dr.T Murali')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.S Anirudh'
                        f=205900
                        print('Fees is Rs 2,05,900/year with Dr.S Anirudh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.H Aadithyaa'
                        f=210000
                        print('Fees is Rs 2,10,000/year with Dr.H Aadithyaa')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.D Nalini'
                        f=206650
                        print('Fees is Rs 2,06,650/year with Dr.D Nalini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.A Sharon'
                        f=207110
                        print('Fees is Rs 2,07,110/year with Dr.A Sharon')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Murali'                  
                        f=207260
                        print('Fees is Rs 2,07,260/year with Dr.T Murali')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
                R.commit()
                '''else:
                    print('\nInvalid Choice')'''
            elif I.lower()=='medical':
                print('\nBest courses offered for Medical:\n1.MBBS\n2.MS\n3.MD\n4.BAMS\n5.BHMS')
                c1=int(input('which course would you like?'))
                if c1==1:
                    a='MBBS'
                    print('\nBest Colleges for MBBS in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Sajan Phiip George\n2.Raj S\n3.Ekta Rai\n4.Tony Thomson Chandy')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Sajan Phiip George'
                            f=98500
                            print('Fees is Rs 98,500/year with Sajan Phiip George')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Raj S'
                            f=90000
                            print('Fees is Rs 90,000/year with Raj S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ekta Rai'
                            f=90000
                            print('Fees is Rs 90,000/year with Ekta Rai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Tony Thomson Chandy'
                            f=91000
                            print('Fees is Rs 91,000/year with Tony Thomson Chandy')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Dr.Nelsonmandela S\n2.Ms.Krishnaveni S\n3.Ms.Sathya B\n4.Mr.Vignesh N')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Nelsonmandela S'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Nelsonmandela S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.Krishnaveni S'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Krishnaveni S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sathya B'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sathya B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Mr.Vignesh N'
                            f=91000
                            print('Fees is Rs 91,000/year with Mr.Vignesh N')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr. Dinesh Kumar G\n2.Dr.Kalal Subhashchandra\n3.Dr.Charumathi B\n4.Dr.Timsi Jain')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. Dinesh Kumar G'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. Dinesh Kumar G')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Kalal Subhashchandra'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Kalal Subhashchandra')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Charumathi B'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Charumathi B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Timsi Jain'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Timsi Jain')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr. B. Chezhian\n2.Dr.V.Rajapriya\n3.Dr.P.Kanagavalli\n4.Dr. Elamathi Boss')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. B. Chezhian'               # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. B. Chezhian ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.V.Rajapriya'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.V.Rajapriya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Kanagavalli'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Kanagavalli')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr. Elamathi Boss'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr. Elamathi Boss')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Nagaraj.P\n2.Dr.Vignesh\n3.Dr.P.Ashok\n4.Dr.Sasheem Haris')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Nagaraj.P'              # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Nagaraj.P')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Vignesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vignesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Ashok'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Ashok')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Sasheem Haris'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Sasheem Haris')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==2:           # Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='MS'
                    print('\nBest Colleges for MS in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Sri Ramachandra Medical College and Research Institute\n4.Madras Medical College\n5.PSG Institute of Medical Sciences and Research')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Vernon Lee\n2.Ms.Ramamani M\n3.Ms.Bina Isaac\n4.Ms.Molly Jacob')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Vernon Lee'
                            f=98500
                            print('Fees is Rs 98,500/year with Vernon Lee')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.Ramamani M'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Ramamani M')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Bina Isaac'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Bina Isaac')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.Molly Jacob'
                            f=91000
                            print('Fees is Rs 91,000/year with Ms.Molly Jacob')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Mrs.J.Vasavi\n2.Mr.U.M.Prakash\n3.Ms.Sathya B\n4.Ahalya.S.P')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.J.Vasavi'
                            f=98500
                            print('Fees is Rs 98,500/year with Mrs.J.Vasavi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.U.M.Prakash'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.U.M.Prakash')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sathya B'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sathya B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ahalya.S.P'
                            f=91000
                            print('Fees is Rs 91,000/year with Ahalya.S.P')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr.Gunapriya Raghunath\n2.Dr.Vijayalakshmi\n3.Dr.Vijayakumar\n4.Dr.Archana')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gunapriya Raghunath'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Gunapriya Raghunath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Vijayalakshmi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vijayalakshmi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Vijayakumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vijayakumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Archana'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Archana')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr.P.Murugesan\n2.Dr.B.Sathyalakshmi\n3.Dr.M.Vijayalakshi\n4.Dr V.Loganayaki')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.P.Murugesan'             # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. B. Chezhian ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.B.Sathyalakshmi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.B.Sathyalakshmi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.M.Vijayalakshi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.M.Vijayalakshi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr V.Loganayaki'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr V.Loganayaki')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Raj\n2.Dr.E.Durai\n3.Dr.P.Anand\n4.Dr.S.Suresh')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Raj'              # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Raj')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.E.Durai'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.E.Durai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Anand'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Anand')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.Suresh'
                            f=9100
                            print('Fees is Rs 91,000/year with Dr.S.Suresh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==3:# MD\n4.BAMS\n5.BHMS')  Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='MD'
                    print('\nBest Colleges for MD in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Joshua Uzagare\n2.Keval Pandya\n3.Saurav Rath\n4.Arnav Pandey')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Joshua Uzagare'
                            f=98500
                            print('Fees is Rs 98,500/year with Joshua Uzagare')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Keval Pandya'
                            f=90000
                            print('Fees is Rs 90,000/year with Keval Pandya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Saurav Rath'
                            f=90000
                            print('Fees is Rs 90,000/year with Saurav Rath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Arnav Pandey'
                            f=91000
                            print('Fees is Rs 91,000/year with Arnav Pandey')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Ms.K.Vani\n2.Mr.R.Umesh\n3.Ms.S.Shanti\n4.Ms.A.Akshaya')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Ms.K.Vani'
                            f=98500
                            print('Fees is Rs 98,500/year with Ms.K.Vani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.R.Umesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.R.Umesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.Shanti'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.Shanti')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.A.Akshaya'
                            f=91000
                            print('Fees is Rs 91,000/year with Ms.A.Akshaya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr.Prathibha\n2.Dr.Premkumar\n3.Dr.Rengaramani\n4.Dr.Ananthi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Prathibha'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Prathibha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Premkumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Premkumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Rengaramani'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Rengaramani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Ananthi'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Ananthi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr.C.Gomathi\n2.Dr.J.V.S.Prakash\n3.Dr.P.Karkuzhali\n4.Dr.Geetha Devadas')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.C.Gomathi'          # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.C.Gomathi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.J.V.S.Prakash'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.J.V.S.Prakash')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Karkuzhali'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Karkuzhali')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Geetha Devadas'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Geetha Devadas')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Harish\n2.Elango.T\n3.A.G.Sangeetha\n4.Dr.P.Jaganath')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Harish'            # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Harish')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Elango.T'
                            f=90000
                            print('Fees is Rs 90,000/year with Elango.T')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='A.G.Sangeetha'
                            f=90000
                            print('Fees is Rs 90,000/year with A.G.Sangeetha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.P.Jaganath'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.P.Jaganath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==4:
                    a='BAMS'
                    print('\nBest Colleges for BAMS in Tamil Nadu are:\n1Dharma Ayurveda Medical College and Hospital\n2.Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya\n3.Sri Sairam Ayurveda Medical College and Research Centre\n4.Ayurveda College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Dharma Ayurveda Medical College and Hospital'    #Dr. N. HARVIN GEORGE,Dr. DANDEY MALLIKA,Dr. T. UDHAYA SHANKAR,Dr. VEENA. P. REGHUNATHAN
                        print('\nMain Faculty:\n1.Dr.N.Harvin George\n2.Dr.Dandey Mallika\n3.Dr.T.Udhaya Shankar\n4.Dr.Veena.P.Reghunathan')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.N.Harvin George'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.N.Harvin George')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Dandey Mallika'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Dandey Mallika')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T.Udhaya Shankar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.T.Udhaya Shankar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Veena.P.Reghunathan'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Veena.P.Reghunathan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya'
                        print('\nMain Faculty:\n1.Dr.Goruganthu\n2.Dr.Mulaka Shiva\n3.Dr.Praveen Kumar\n4.Dr.Prem Kumar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Goruganthu'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Goruganthu')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Mulaka Shiva'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Mulaka Shiva')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.Shanti'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.Shanti')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Prem Kumar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Prem Kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Sri Sairam Ayurveda Medical College and Research Centre'
                        print('\nMain Faculty:\n1.Dr.K.K.Balendar\n2.Dr.P.C.Penchalaiah\n3.Ms.S.M.Subhani\n4.Dr.Velmurugan')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.K.K.Balendar'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.K.K.Balendar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='P.C.Penchalaiah'
                            f=90000
                            print('Fees is Rs 90,000/year with P.C.Penchalaiah')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.M.Subhani'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.M.Subhani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Velmurugan'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Velmurugan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Ayurveda College'
                        print('\nMain Faculty:\n1.Dr.T.John\n2.Mr.Mahesh\n2.Dr.Premanand\n4.Dr.Pradeep')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.T.John'          # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year withDr.T.John ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.Mahesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.Mahesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Premanand'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Premanand')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Pradeep'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Pradeep')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==5:# MD\n4.BAMS\n5.BHMS')  Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='BHMS'
                    print('\nBest Colleges for BHMS in Tamil Nadu are:\n1.Vinayaka Missions Homoeopathic Medical College and Hospital\n2.Government Homoeopathic Medical College and Hospital\n3.Sarada Krishna Homoeopathic Medical College\n4.Venkateswara Homoeopathic Medical College and Hospital')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Vinayaka Missions Homoeopathic Medical College and Hospital'    #Dr. N. HARVIN GEORGE,Dr. DANDEY MALLIKA,Dr. T. UDHAYA SHANKAR,Dr. VEENA. P. REGHUNATHAN
                        print('\nMain Faculty:\n1.Dr.E.Rathnasabapathi Chairperson\n2.Prof.Dr.R.S.Shanmugasundaram\n3.M.Sree Abinav\n4.T.Amsavali')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.E.Rathnasabapathi Chairperson'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.E.Rathnasabapathi Chairperson')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Prof.Dr.R.S.Shanmugasundaram'
                            f=90000
                            print('Fees is Rs 90,000/year with Prof.Dr.R.S.Shanmugasundaram')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='M.Sree Abinav'
                            f=90000
                            print('Fees is Rs 90,000/year with M.Sree Abinav')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='T.Amsavali'
                            f=91000
                            print('Fees is Rs 91,000/year with T.Amsavali')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='Government Homoeopathic Medical College and Hospital'
                        print('\nMain Faculty:\n1.Dr.Gurunathan\n2.Dr.Shukla\n3.Mrs.K.Priya\n4.Dr.Selvam')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gurunathan'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Gurunathan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Shukla'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Shukla')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Mrs.K.Priya'
                            f=90000
                            print('Fees is Rs 90,000/year with Mrs.K.Priya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Selvam'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Selvam')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Sarada Krishna Homoeopathic Medical College'
                        print('\nMain Faculty:\n1.Mrs.V.Maya\n2.Dr.D.Lokesh\n3.Ms.Sulaka\n4.Dr.Vetri')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.V.Maya'
                            f=98500
                            print('Fees is Rs 98,500/year with Mrs.V.Maya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.D.Lokesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.D.Lokesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sulaka'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sulaka')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Vetri'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Vetri')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Ayurveda College'
                        print('\nMain Faculty:\n1.Dr.E.Senthil\n2.Mr.Nagaraj\n2.Dr.K.Radha\n4.G.Kavitha')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.E.Senthil'        # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.E.Senthil')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.Nagaraj'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.Nagaraj')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K.Radha'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.K.Radha') 
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='G.Kavitha'
                            f=91000
                            print('Fees is Rs 91,000/year with G.Kavitha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
                R.commit()
            elif I.lower()=='sociology':
                print('\nBest Colleges for AI:\n1.NIT Trichy\n2.Presidency College\n3.Loyola College\n4.PSG College of Arts and Science\n5.University of Madras')
                c=int(input('\nEnter your choice of college='))
            else:
                print('\nPlease Choose any interest from this set:\n1.Engineering\n2.Arts and Science\n3.Commerce\n4.Fashion designing\n5.Medical\n6.Sociology')
                print('\nPlease try again')
            '''d.execute('insert into students values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(n,m,g,D,pn,M,P,I,a,C,F,f))
            R.commit()'''
            '''print('RECORDS ENTERED SO FAR:\n')
            d.execute('select * from students')
            z=d.fetchall()
            for i in z:
                print(i)'''
            d2 = today.strftime("%B %d, %Y")
            print("\nDATE OF REGISTRATION=", d2)
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            print("TIME OF REGISTRATION", dt_string)
            H=Tk()
            H.geometry('800x800')
            H.configure(bg='pink')
            H.title('REGISTERED STUDENT"S DETAILS')
            L1=Label(text='NAME OF STUDENT=',bg='light blue').grid(row=1,column=170,padx=20,pady=10)
            L2=Label(text=m,bg='light blue').grid(row=1,column=175)
            L3=Label(text='GENDER=',bg='green',fg='yellow').grid(row=2,column=170,padx=20,pady=20)
            L4=Label(text=g,bg='green',fg='yellow').grid(row=2,column=175)
            L5=Label(text='DATE OF BIRTH=',bg='blue',fg='white').grid(row=3,column=170,padx=20,pady=20)
            L6=Label(text=D,bg='blue',fg='white').grid(row=3,column=175)
            L7=Label(text='PHONE NO=',bg='grey',fg='white').grid(row=4,column=170,padx=20,pady=20)
            L8=Label(text=str(pn),bg='grey',fg='white').grid(row=4,column=175)
            L9=Label(text='MAIL-ID=',bg='orange').grid(row=5,column=170,padx=20,pady=20)
            L10=Label(text=M,bg='orange').grid(row=5,column=175)
            L11=Label(text='INTEREST=',bg='red',fg='white').grid(row=6,column=170,padx=20,pady=20)
            L12=Label(text=I,bg='red',fg='white').grid(row=6,column=175)
            L13=Label(text='COURSE=',bg='brown',fg='white').grid(row=7,column=170,padx=20,pady=20)
            L14=Label(text=a,bg='brown',fg='white').grid(row=7,column=175)
            L15=Label(text='COLLEGE=',bg='yellow',fg='red').grid(row=8,column=170,padx=20,pady=20)
            L16=Label(text=C,bg='yellow',fg='red').grid(row=8,column=175)
            L17=Label(text='FACULTY=',bg='black',fg='white').grid(row=9,column=170,padx=20,pady=20)
            L18=Label(text=F,bg='black',fg='white').grid(row=9,column=175)
            L19=Label(text='FEES/YEAR=',bg='magenta',fg='blue').grid(row=10,column=170,padx=20,pady=20)
            L20=Label(text=str(f),bg='magenta',fg='blue').grid(row=10,column=175)
            L21=Label(text='YOUR SEAT IS ALLOCATED!!',fg='black').grid(row=11,column=50,padx=20,pady=20)
            def close():
                H.destroy()
            e=Button(H,text='OK',command=close).grid(row=11,column=173)
            H.mainloop()
            K=input('Do you want to add students(y/n)?')
            if K.lower()=='y':
                k=input('Have you registered?')
                if k.lower()=='n':
                    D=input('Enter Date of Birth(DD/MM/YYYY)=')
                    q=D.split('/')
                    n+=1
            else:
                print('\nExitting app')
                break
        else:
            print('\nInvalid E-mail ID')
            print('\nPlease try again\n')
    else:
        print('\nPhone number should contain 10 digits\n\nPlease Retry!')
else:
    if int(q[2])>2005:
        print('\nYou are not eligible for registering in this app\n\nOnly people aged 17 or above can register\n\nPlease Try Again')
    else:
        w=Tk()
        w.configure(bg='orange')
        w.title('LOGIN PAGE')
        w.geometry('400x300')
        q=StringVar()
        p=StringVar()
        a=Label(text='EMAIL-ID=',bg='red').grid(row=1,column=3,padx=10,pady=10)
        b=Entry(w,font=('Calibri',11),textvariable=q).grid(row=1,column=6)
        c=Label(text='PASSWORD=',bg='blue').grid(row=3,column=3,padx=10,pady=10)
        s=Entry(w,font=('Calibri',11),textvariable=p,show='*').grid(row=3,column=6)
        d.execute('select * from students')
        W=d.fetchall()
        P=''
        def comm():
            v=0
            global P
            P=p.get()
            for i in W:
                if q.get() in i and p.get() in i:
                    v+=1
                    messagebox.showinfo('Info','SUCCESSFULLY LOGGED IN')
                    w.destroy()
            if v==0:
                messagebox.showerror('Error','Incorrect credentials')
        rep=''
        def fg():
            w.destroy()
            WE=Tk()
            WE.title('RESET PASSWORD')
            WE.geometry('600x600')
            WE.configure(bg='violet')
            aA=Label(text='EMAIL-ID=',bg='orange').grid(row=1,column=3,padx=10,pady=10)
            Q=StringVar()
            pP=StringVar()
            wW=StringVar()
            b=Entry(WE,font=('Calibri',11),textvariable=Q).grid(row=1,column=6)
            cC=Label(text='ENTER NEW PASSWORD=',bg='red').grid(row=3,column=3,padx=10,pady=10)
            sS=Entry(WE,font=('Calibri',11),textvariable=pP,show='*').grid(row=3,column=6)
            zZ=Label(text='CONFIRM NEW PASSWORD=',bg='blue').grid(row=5,column=3,padx=10,pady=10)
            oO=Entry(WE,font=('Calibri',11),textvariable=wW,show='*').grid(row=5,column=6)
            global rep
            def re():
                global rep
                E=Q.get()
                rep=pP.get()
                crep=wW.get()
                if len(rep)>=6:
                    if rep==crep:
                        d.execute('update students set passwd="%s" where MailID="%s"'%(rep,E))
                        R.commit()
                        messagebox.showinfo('RESET SUCCESSFUL','PASSWORD CHANGED')
                        WE.destroy()
                    else:
                        messagebox.showerror('ERROR','Passwords don"t match')
                else:
                    messagebox.showwarning('WARNING','Password should be atleast 6 chracters')
            fF=Button(WE,text='RESET',command=re).grid(row=7,column=7)
            WE.mainloop()
        e=Button(w,text='LOGIN',command=comm).grid(row=5,column=6)
        f=Button(w,text='FORGOT PASSWORD...',command=fg).grid(row=5,column=10)
        w.mainloop()
        d2 = today.strftime("%B %d, %Y")
        print("\nDATE OF LOGIN=", d2)
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        print("TIME OF LOGIN", dt_string)
        print('\n1.PERSONAL DETAILS\n2.INTEREST')
        up=int(input('\nSELECT WHAT TO UPDATE:'))
        if up==1:
            print('\nUPDATE:\n1.NAME\n2.GENDER\n3.DATE OF BIRTH\n4.PHONE NUMBER\n5.MAIL-ID')
            d.execute('select * from students')
            W=d.fetchall()
            UP=int(input('\nEnter your choice='))
            if UP==1:
                nn=input('Enter already existing name=')
                NN=input('Enter new name to be updated=')
                d.execute('update students set name="%s" where passwd="%s"'%(NN,P))
                d.execute('update students set name="%s" where passwd="%s"'%(NN,rep))
                R.commit()
                print('\nName updated successfully')
            elif UP==2:
                gg=input('New Gender=')
                d.execute('update students set gender="%s" where passwd="%s"'%(gg,P))
                d.execute('update students set gender="%s" where passwd="%s"'%(gg,rep))
                R.commit()
                print('\nGender updated successfully')
            elif UP==3:
                dob=input('Enter new DOB=')
                d.execute('update students set DOB="%s" where passwd="%s"'%(dob,P))
                d.execute('update students set DOB="%s" where passwd="%s"'%(dob,rep))
                R.commit()
                print('\nDOB updated successfully')
            elif UP==4:
                pp=int(input('Enter old phone number='))
                v=0
                for i in W:
                    if pp==i[4]:
                        v+=1
                        PP=int(input('Enter new phone number='))
                        d.execute('update students set Phoneno="%s" where passwd="%s"'%(PP,P))
                        d.execute('update students set Phoneno="%s" where passwd="%s"'%(PP,rep))
                        R.commit()
                        print('\nPhone number updated successfully')
                if v==0:
                    print('\nTry Again')
            elif UP==5:
                mm=input('Enter old Mail-ID=')
                v=0
                for i in W:
                    if mm==i[5]:
                        v+=1
                        MM=input('Enter new Mail-ID=')
                        d.execute('update students set MailId="%s" where passwd="%s"'%(MM,P))
                        d.execute('update students set MailID="%s" where passwd="%s"'%(MM,rep))
                        R.commit()
                        print('\nMail-Id updated successfully')
                if v==0:
                    print('\nTry Again')
        elif up==2:
            I=input('\nWhat is your new Interest?("Engineering","Arts and Science","Commerce","Fashion designing","Medical","Sociology")')               #interest and college selection
            if I.lower()=='engineering':
                print('\nMain Courses offered for Engineering:\na)Aerospace Engineering\nb)Mechanical engineering\nc)Biotechnology\nd)Chemical Engineering\ne)Civil Engineering\nf)Computer Science Engineering\ng)Electrical Engineering')
                c1=input('\nEnter your choice for course selection=')                                                    #Picking courses
                if c1.lower()=='a':
                    a='Aerospace Engineering'
                    print('\nTOP Colleges in Chennai are:\n1.Indian Institute of Technology(IIT) Madras\n2.Anna University\n3.SRM Institute of Science and Technology\n4.Amrita School of Engineering')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            #Picking colleges and faculty
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Luoyi Tao\n2.Dr.M.Ramakrishna\n3.Dr.Nandan K.Sinha\n4.Dr.Bharath M.Govindarajan\n5.Dr.Rajesh G')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Luoyi Tao'
                            f=100000
                            print('Fees is Rs 1,00,000/year with Dr.Luoyi Tao')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                #Registration last process
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M.Ramakrishna'
                            f=89000
                            print('Fees is Rs 89,000/year with Dr.M.Ramakrishna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Nandan K Sinha'
                            f=125000
                            print('Fees is Rs 1,25,000/year with Dr.Nandan K Sinha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Bharath M Govindarajan'
                            f=97000
                            print('Fees is Rs 97,000/year with Dr.Bharath M Govindarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.Rajesh G'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.Rajesh G')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='Anna University'
                        print('Main Faculties:\n1.Dr.B.T.N.Sridhar\n2.Dr.K M Paramasivam\n3.Dr.C.Senthil Kumar\n4.Dr.V Arumugam\n5.Dr.V Suresh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.B.T.N Sridhar'
                            f=145000
                            print('Fees is Rs 1,45,000/year with Dr.B.T.N Sridhar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K.M Paramasivam'
                            f=132000
                            print('Fees is Rs 1,32,000/year with Dr.K.M.Paramasivam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.C Senthil Kumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.C Senthil Kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Arumugam'
                            f=107000
                            print('Fees is Rs 1,07,000/year with Dr.V Arumugam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.V Suresh'
                            f=100000
                            print('Fees is Rs 1,00,000/year with Dr.V Suresh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='SRM Institute'
                        print('\nMain Faculties:\n1.Dr.R Vasudevan\n2.Dr L.R.Ganapathy Subramanian\n3.Dr.S Sivakumar\n4.Dr.T Selvakumaran\n5.Dr.S Gurusideswar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Vasudevan'
                            f=115000
                            print('Fees is Rs 1,15,000/year with Dr.R Vasudevan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.L.R Ganapathy Subramanian'
                            f=92000
                            print('Fees is Rs 92,000/year with Dr.L.R Ganapathy Subramanian')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Sivakumar'
                            f=140000
                            print('Fees is Rs 1,40,000/year with Dr.S Sivakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.T Selvakumaran'
                            f=137000
                            print('Fees is Rs 1,37,000/year with Dr.T Selvakumaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Gurusideshwar'
                            f=110000
                            print('Fees is Rs 1,10,000/year with Dr.S Gurusideshwar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Amrita School of Engineering'
                        print('\nMain Faculty:\n1.Dr Srikrishnan A R\n2.Dr.V Sivadas\n3.Dr.Shantanu Bhowmik\n4.Dr.V Sivakumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Srikrishnan A'
                            f=97000
                            print('Fees is Rs 97,000/year with Dr.Srikrishnan A')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.V Sivadas'
                            f=121000
                            print('Fees is Rs 1,21,000/year with Dr.V Sivadas')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Shantanu Bhowmik'
                            f=131000
                            print('Fees is Rs 1,31,000/year with Dr.Shantanu Bhowmik')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Sivakumar'
                            f=157000
                            print('Fees is Rs 1,57,000/year with Dr.V Sivakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='b':
                    a='Mechanical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.SSN College of Engineering\n5.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            #Picking colleges and faculty
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Seshadri Sekar A\n2.Dr.Abhijit Sarkar\n3.Dr.Anand Krishnasamy\n4.Dr.Amitava Ghosh\n5.Arunachalam D')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Seshadri Sekar'
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.Seshadri Sekar')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                #Registration last process
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Abhijith Sarkar'
                            f=189000
                            print('Fees is Rs 1,89,000/year with Dr.Abhijith Sarkar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Anand Krishnasamy'
                            f=195000
                            print('Fees is Rs 1,95,000/year with Dr.Anand Krishnasamy')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Amitava Ghosh'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.Amitava Ghosh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.D Arunachalam'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.D Arunachalam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.T V Gopal\n2.Dr.S Prabhu\n3.Dr.T Rajasekaran\n4.Dr.K Duraivelu\n5.Dr.V Suresh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.T V Gopal'
                            f=205000
                            print('Fees is Rs 2,05,000/year with Dr.T V Gopal')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.S Prabhu'
                            f=232000
                            print('Fees is Rs 2,32,000/year with Dr.S Prabhu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Rajasekaran'
                            f=190000
                            print('Fees is Rs 1,90,000/year with Dr.T Rajasekaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Duraivelu'
                            f=207000
                            print('Fees is Rs 2,07,000/year with Dr.K Duraivelu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.P Nandakumar'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.P Nandakumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.K Annamalai\n2.Dr Bhaskara Rao\n3.Dr.R Deivanathan\n4.Dr.Padmanabhan\n5.Dr.G Sakthivel')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Annamalai'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.K Annamalai')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Bhaskara Rao'
                            f=162000
                            print('Fees is Rs 1,62,000/year with Dr.Bhaskara Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Deivanathan'
                            f=165000
                            print('Fees is Rs 1,65,000/year with Dr.R Deivanathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Padmanabhan'
                            f=177000
                            print('Fees is Rs 1,77,000/year with Dr.Padmanabhan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.G Sakthivel'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.G Sakthivel')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='SSN College of Engineering'
                        print('\nMain Faculty:\n1.Dr.S Vijayan\n2.Dr.Vijaysekar K\n3.Dr.A Jayasekar\n4.Dr.V Rajkumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Vijayan'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.S Vijayan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vijaysekar K'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.Vijaysekar K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.A Jayasekar'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.A Jayasekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Rajkumar'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.V Rajkumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr.S Vijayan\n2.Dr.Vijaysekar K\n3.Dr.A Jayasekar\n4.Dr.V Rajkumar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Vijayan'
                            f=1,97000
                            print('Fees is Rs 1,97,000/year with Dr.S Vijayan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vijaysekar K'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.Vijaysekar K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.A Jayasekar'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.A Jayasekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Rajkumar'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.V Rajkumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='c':
                    a='Biotechnology'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.Anna University\n3.SRM Institute\n4.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Gopalakrishnan\n2.Dr.Arumugam Rajavelu\n3.Dr.Chandraraj\n4.Dr.N Manoj\n5.Dr.N Michael')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gopalakrishnan'
                            f=170000
                            print('Fees is Rs 1,70,000/year with Dr.Gopalakrishnan')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Arumugam Rajavelu'
                            f=189000
                            print('Fees is Rs 1,89,000/year with Dr.Arumugam Rajavelu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Chandraraj'
                            f=125000
                            print('Fees is Rs 1,80,000/year with Dr.Chandraraj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.N Manoj'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.N Manoj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Michael'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.N Michael')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='Anna University'
                        print('Main Faculties:\n1.Dr.B.S Lakshmi\n2.Dr.M Sukumar\n3.Dr.C.D Anuradha\n4.Dr.S Ramalingam\n5.Dr.S Ranganathan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.B.S Lakshmi'
                            f=175000
                            print('Fees is Rs 1,75,000/year with Dr.B.S Lakshmi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Sukumar'
                            f=212000
                            print('Fees is Rs 2,12,000/year with Dr.M Sukumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.C.D Anuradha'
                            f=190000
                            print('Fees is Rs 1,90,000/year with Dr.C.D Anuradha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Ramalingam'
                            f=187000
                            print('Fees is Rs 1,87,000/year with Dr.S Ramalingam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Ranganathan'
                            f=200000
                            print('Fees is Rs 2,00,000/year with Dr.S Ranganathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                                          
                        C='SRM Institute'
                        print('\nMain Faculties:\n1.Dr.R A Nazeer\n2.Dr M Ramya\n3.Dr.N Selvamurugan\n4.Dr.K Ramani\n5.Dr.S Barathi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R A Nazeer'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.R A Nazeer')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Ramya'
                            f=192000
                            print('Fees is Rs 1,92,000/year with Dr.M Ramya')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.N Selvamurugan'
                            f=180000
                            print('Fees is Rs 1,80,000/year with Dr.N Selvamurugan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Ramani'
                            f=187000
                            print('Fees is Rs 1,87,000/year with Dr.K Ramani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.S Barathi'
                            f=210000
                            print('Fees is Rs 2,10,000/year with Dr.S Barathi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr K Rahman\n2.Dr.R Hari\n3.Dr.T Prashaant\n4.Dr.G Sekar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Rahman'
                            f=197000
                            print('Fees is Rs 1,97,000/year with Dr.K Rahman')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.R Hari'
                            f=181000
                            print('Fees is Rs 1,81,000/year with Dr.R Hari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Prashaant'
                            f=174000
                            print('Fees is Rs 1,74,000/year with Dr.T Prashaant')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G Sekar'
                            f=188000
                            print('Fees is Rs 1,88,000/year with Dr.G Sekar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='d':
                    a='Chemical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.HITS Chennai\n4.Rajalakshmi Engineering College')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.Arun K\n2.Dr.Aravind kumar\n3.Dr.Abhijith P\n4.Dr.A Kannan\n5.R Nagarajan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Arun K'
                            f=220000
                            print('Fees is Rs 2,20,000/year with Dr.Arun K')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Aravind kumar'
                            f=239000
                            print('Fees is Rs 2,39,000/year with Dr.Aravind kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Abhijith P'
                            f=198000
                            print('Fees is Rs 1,98,000/year with Dr.Abhijith P')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.A Kannan'
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.A Kannan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Nagarajan'
                            f=234000
                            print('Fees is Rs 2,34,000/year with Dr.R Nagarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.M P Rajesh\n2.Dr.Ashish K\n3.Dr.S Vishal\n4.Dr.K Suresh\n5.Dr.K Selvam')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M P Rajesh'
                            f=225000
                            print('Fees is Rs 2,25,000/year with Dr.M P Rajesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Ashish K'
                            f=242000
                            print('Fees is Rs 2,42,000/year with Dr.Ashish K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Vishal'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.S Vishal')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Suresh'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.K K Suresh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Selvam'
                            f=250500
                            print('Fees is Rs 2,50,500/year with Dr.K Selvam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                          
                        C='HITS Chennai'
                        print('\nMain Faculties:\n1.Dr.Anitha A\n2.Dr.B Vivek\n3.Dr.R Keerthana\n4.Dr.Siva prakash\n5.Dr.J Malathy')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Anitha A'
                            f=215000
                            print('Fees is Rs 2,15,000/year with Dr.Anitha A')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.B Vivek'
                            f=162000
                            print('Fees is Rs 2,32,600/year with Dr.B Vivek')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Keerthana'                            
                            f=243890
                            print('Fees is Rs 2,43,890/year with Dr.R Keerthana')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':                                                  
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Siva prakash'
                            f=244400
                            print('Fees is Rs 2,44,400/year with Dr.Siva prakash')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.G Saravanan'
                            f=246000
                            print('Fees is Rs 2,46,000/year with Dr.G Saravanan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='Rajalakshmi College of Engineering'
                        print('\nMain Faculty:\n1.Dr.K Nagarajan\n2.Dr.Vincent J\n3.Dr.S Sivamani\n4.Dr.K Sriram\n5.N Kalaiarasi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.K Nagarajan'
                            f=197560
                            print('Fees is Rs 1,97,560/year with Dr.K Nagarajan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Vincent J'
                            f=261800
                            print('Fees is Rs 2,61,800/year with Dr.Vincent J')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Sivamani'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.S Sivamani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.K Sriram'
                            f=187650
                            print('Fees is Rs 1,87,650/year with Dr.K Sriram')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Kalaiarasi'
                            f=237600
                            print('Fees is Rs 2,37,600/year with Dr.N Kalaiarasi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='e':
                    a='Civil Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.HITS Chennai\n4.VIT Chennai')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.P Alagappan\n2.Dr.Amlan kumar\n3.Dr.G Appa Rao\n4.Dr.Ashwin M\n5.R Benny')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.P Alagappan'
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.P Alagappan')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Amlan kumar'
                            f=232550
                            print('Fees is Rs 2,32,550/year with Dr.Amlan kumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G Appa Rao'
                            f=228800
                            print('Fees is Rs 2,28,800/year with Dr.G Appa Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Ashwin M'
                            f=247750
                            print('Fees is Rs 2,47,750/year with Dr.Ashwin M')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Benny'
                            f=234000
                            print('Fees is Rs 2,34,000/year with Dr.R Benny')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.M Annadurai\n2.Dr.Senthil Selvan\n3.Dr.R Ravi\n4.Dr.S Aparna\n5.Dr.K Sunny')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M Annadurai'
                            f=245000
                            print('Fees is Rs 2,45,000/year with Dr.M Annadurai')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Senthil Selvan'
                            f=222000
                            print('Fees is Rs 2,22,000/year with Dr.Senthil selvan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.R Ravi'
                            f=221600
                            print('Fees is Rs 2,21,600/year with Dr.R Ravi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Aparna'
                            f=237580
                            print('Fees is Rs 2,37,580/year with Dr.S Aparna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Sunny'
                            f=250570
                            print('Fees is Rs 2,50,570/year with Dr.K Sunny')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:                                                          
                        C='HITS Chennai'
                        print('\nMain Faculties:\n1.Dr.V Subbiah\n2.Dr.V Paramasivam\n3.Dr.J Samuel\n4.Dr.S Vijayan\n5.Dr.G Saravanan')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.V Subbiah'
                            f=243000
                            print('Fees is Rs 2,43,000/year with Dr.V Subbiah')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.V Paramasivam'
                            f=252730
                            print('Fees is Rs 2,52,730/year with Dr.V Paramasivam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.J Samuel'                            
                            f=199000
                            print('Fees is Rs 1,99,000/year with Dr.J Samuel')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':                                                  
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.V Prabhu'                            #continue from here
                            f=243000
                            print('Fees is Rs 2,43,000/year with Dr.V Prabhu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.J Malathy'
                            f=226000
                            print('Fees is Rs 2,26,000/year with Dr.J Malathy')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='VIT Chennai'
                        print('\nMain Faculty:\n1.Dr.Mohan Ganesh\n2.Dr.Sekar SK\n3.Dr.T Meena\n4.Dr.S.S Ajeesh\n5.N Rama Rao')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Mohan Ganesh'
                            f=241560
                            print('Fees is Rs 2,41,560/year with Dr.Mohan Ganesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Sekar SK'
                            f=263820
                            print('Fees is Rs 2,63,820/year with Dr.Sekar SK')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T Meena'
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.T Meena')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.S Ajeesh'
                            f=251650
                            print('Fees is Rs 2,51,650/year with Dr.S.S Ajeesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Rama Rao'
                            f=233400
                            print('Fees is Rs 2,33,400/year with Dr.N Rama Rao')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                                                  
                                pass
                elif c1.lower()=='f':
                    a='Computer Engineering'
                    print('\nBest colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.SSN College of Engineering\n5.Satyabhama Institute')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.John A\n2.Dr.C Sarath\n3.Dr.Deepak K\n4.Dr.M Sreenivasan\n5.Dr.M Nitesh')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.John A'
                            f=223000
                            print('Fees is Rs 2,23,000/year with Dr.John A')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.C Sarath'
                            f=219000
                            print('Fees is Rs 2,19,000/year with Dr.C Sarath')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Deepak K'
                            f=198890
                            print('Fees is Rs 1,98,890/year with Dr.Deepak K')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.M Sreenivasan'
                            f=211000
                            print('Fees is Rs 2,11,000/year with Dr.M Sreenivasan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.M Nitesh'
                            f=195000
                            print('Fees is Rs 1,95,000/year with Dr.M Nitesh')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.S Krishna\n2.Dr.C Vasudevan\n3.Dr.B Amudha\n4.Dr.S.S Sridhar\n5.Dr.R Revathi')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.S Krishna'
                            f=225000
                            print('Fees is Rs 2,25,000/year with Dr.S Krishna')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.C Vasudevan'
                            f=221570
                            print('Fees is Rs 2,21,570/year with Dr.C Vasudevan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.B Amudha'                            
                            f=247000
                            print('Fees is Rs 2,47,000/year with Dr.B Amudha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.S Sridhar'
                            f=237000
                            print('Fees is Rs 2,37,000/year with Dr.S.S Sridhar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.R Revathi'
                            f=233000
                            print('Fees is Rs 2,33,000/year with Dr.R Revathi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.R Ganesan\n2.Dr.S Geeta\n3.Dr.K.R Jagadish\n4.Dr.L Jagannathan\n5.Dr.N Maheshwari')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Ganesan'
                            f=245660
                            print('Fees is Rs 2,45,660/year with Dr.R Ganesan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.S Geeta'
                            f=226000
                            print('Fees is Rs 2,26,000/year with Dr.S Geeta')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K.R Jagadish'
                            f=236890
                            print('Fees is Rs 2,36,890/year with Dr.K.R Jagadish')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.L Jagannathan'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.L Jagannathan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Maheshwari'                  
                            f=240000
                            print('Fees is Rs 2,40,000/year with Dr.N Maheshwari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='SSN College of Engineering'
                        print('\nMain Faculty:\n1.Dr.R.S Milton\n2.Dr.Chitra Babu\n3.Dr.G Raghu\n4.Dr.S Bhuvana')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R.S Milton'
                            f=235000
                            print('Fees is Rs 2,35,000/year with Dr.R.S Milton')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.Chitra Babu'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.Chitra Babu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G Raghu'
                            f=221000
                            print('Fees is Rs 2,21,000/year with Dr.G Raghu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Bhuvana'
                            f=237000
                            print('Fees is Rs 2,37,000/year with Dr.S Bhuvana')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='Satyabhama Institute'
                        print('\nMain Faculty:\n1.Dr.T Sasikala\n2.Dr.K Verma\n3.Dr.S Vedhika\n4.Dr.H Siddharth')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.T Sasikala'
                            f=246000
                            print('Fees is Rs 2,46,000/year with Dr.T Sasikala')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K Verma'
                            f=241000
                            print('Fees is Rs 2,41,000/year with Dr.K Verma')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.S Vedhika'
                            f=232500
                            print('Fees is Rs 2,32,500/year with Dr.S Vedhika')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.H Siddharth'
                            f=227000
                            print('Fees is Rs 2,27,000/year with Dr.H Siddharth')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                elif c1.lower()=='g':
                    a='Electrical Engineering'
                    print('\nBest Colleges in Chennai:\n1.IIT Madras\n2.SRM Institute\n3.VIT Chennai\n4.MIT Chennai\n5.HITS Chennai')
                    c=int(input('\nEnter your choice of college='))
                    if c==1:                                                                                            
                        C='IIT Madras'
                        print('\Main Faculties:\n1.Dr.R Venkatesh\n2.Dr.K.S Pradeep\n3.Dr.D Soumya\n4.Dr.A Sankaran\n5.Dr.M Anbarasu')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Venkatesh'
                            f=233000
                            print('Fees is Rs 2,33,000/year with Dr.R Venkatesh')
                            r=input('\nAre you sure you want to continue(y/n)?')                                                
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K.S Pradeep'
                            f=219780
                            print('Fees is Rs 2,19,780/year with Dr.K.S Pradeep')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.D Soumya'
                            f=234890
                            print('Fees is Rs 2,34,890/year with Dr.D Soumya')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.A Sankaran'
                            f=222000
                            print('Fees is Rs 2,22,000/year with Dr.A Sankaran')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.M Anbarasu'
                            f=231000
                            print('Fees is Rs 2,31,000/year with Dr.M Anbarasu')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==2:
                        C='SRM Institute'                                                                               
                        print('Main Faculties:\n1.Dr.A Ratnam\n2.Dr.K Vijaykumar\n3.Dr.K Saravanan\n4.Dr.S Padmini\n5.Dr.K Mohanraj')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.A Ratnam'
                            f=229950
                            print('Fees is Rs 2,29,950/year with Dr.A Ratnam')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.K Vijaykumar'
                            f=231870
                            print('Fees is Rs 2,31,870/year with Dr.K Vijaykumar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K Saravanan'                            
                            f=237500
                            print('Fees is Rs 2,37,500/year with Dr.K Saravanan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S Padmini'
                            f=247440
                            print('Fees is Rs 2,47,440/year with Dr.S Padmini')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.K Mohanraj'
                            f=234100
                            print('Fees is Rs 2,34,100/year with Dr.K Mohanraj')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==3:
                        C='VIT Chennai'
                        print('\nMain Faculties:\n1.Dr.R Jacob\n2.Dr.B.J Edward\n3.Dr.M Janaki\n4.Dr.C Rani\n5.Dr.N Srihari')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.R Jacob'
                            f=235690
                            print('Fees is Rs 2,35,690/year with Dr.R Jacob')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.B.J Edward'
                            f=223430
                            print('Fees is Rs 2,23,430/year with Dr.B.J Edward')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.M Janaki'
                            f=232700
                            print('Fees is Rs 2,32,700/year with Dr.M Janaki')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.C Rani'
                            f=267000
                            print('Fees is Rs 2,67,000/year with Dr.C Rani')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==5:
                            F='Dr.N Srihari'                  
                            f=243660
                            print('Fees is Rs 2,43,660/year with Dr.N Srihari')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==4:
                        C='MIT Chennai'
                        print('\nMain Faculty:\n1.Dr.Mala John\n2.Dr.M Kannan\n3.Dr.P Prakash\n4.Dr.G Kavitha')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.Mala John'
                            f=225670
                            print('Fees is Rs 2,25,670/year with Dr.Mala John')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.M Kannan'
                            f=247800
                            print('Fees is Rs 2,47,800/year with Dr.M Kannan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P Prakash'
                            f=251000
                            print('Fees is Rs 2,51,000/year with Dr.P Prakash')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G Kavitha'
                            f=225990
                            print('Fees is Rs 2,25,990/year with Dr.G Kavitha')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                    elif c==5:
                        C='HITS Chennai'
                        print('\nMain Faculty:\n1.Dr.M Manikandan\n2.Dr.J Alex\n3.Dr.V Preethi\n4.Dr.J Sudhakar')
                        c2=int(input('\nEnter your choice of faculty:'))
                        if c2==1:
                            F='Dr.M Manikandan'
                            f=247200
                            print('Fees is Rs 2,47,200/year with Dr.M Manikandan')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==2:
                            F='Dr.J Alex'
                            f=245900
                            print('Fees is Rs 2,45,900/year with Dr.J Alex')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.V Preethi'
                            f=240560
                            print('Fees is Rs 2,40,560/year with Dr.V Preethi')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.J Sudhakar'
                            f=237810
                            print('Fees is Rs 2,37,810/year with Dr.J Sudhakar')
                            r=input('\nAre you sure you want to continue(y/n)?')
                            if r.lower()=='y':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,P))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,P))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,P))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,P))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,P))
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,rep))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,rep))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,rep))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,rep))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,rep))
                R.commit()
                '''else:
                    print('\nInvalid choice')'''
            elif I.lower()=='arts and science':
                print('\nBest courses offered for Arts and science are:\n1.B.Arts\n2.B.A English\n3.B.B.A(Bachelor of Business Administration)\n4')
                c1=int(input('which course would you like?'))
                if c1==1:
                    a='B.Arts'
                    print('\nBest Colleges for BA Economics in Tamil Nadu are:\n1.Loyola College\n2.PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Loyola College'
                        print('\nMain Faculty:\n1.Dr.R.Leema Rose\n2.Ms.F.Reena\n3.Dr.D.Jerusha Chitra\n4.Ms.J Minothi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.R.Leema Rose'
                            f=98000
                            print('Fees is Rs 98,000/year with Dr.R.Leema Rose')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.F.Reena'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.F.Reena')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='D.Jerusha Chitra'
                            f=90000
                            print('Fees is Rs 90,000/year with D.Jerusha Chitra')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.J Minothi'
                            f=91000
                            f=90000
                            print('Fees is Rs 91,000/year with Ms.J Minothi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='PSG College of Arts and Science'    
                        print('\nMain Faculty:\n1.Shiv Nadar\n2.K. Annamalai\n3.C Vijayakumar\n4.Madhu Bhaskaran')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Shiv Nadar'
                            f=98000
                            print('Fees is Rs 98,000/year with Shiv Nadar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='K.Annamalai'
                            f=90000
                            print('Fees is Rs 90,000/year with K.Annamalai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='C.Vijayakumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Vijayakumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Madhu Baskaran'
                            f=91000
                            print('Fees is Rs 91,000/year with Madhu Baskaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==3:
                        C='Presidency College'     #Dr. K. ATHINARAYANAN ,Dr.B.THAMARAIKKANNAN M.A., Dr.G.SHAIKMEERAN, Dr.G.SEKAR
                        print('\nMain Faculty:\n1.Dr.K.Athinarayanan\n2.Dr.B.Thamaraikkanna\n3.Dr.G.Shaikeeran\n4.Dr.G.Sekar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.K.Athinarayanan'
                            f=98000
                            print('Fees is Rs 98,000/year with Dr.K.Athinarayanan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.B.Thamaraikkanna'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.B.Thamaraikkanna')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.G.Shaikeeran'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.G.Shaikeeran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.G.Sekar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.G.Sekar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==4:
                        C='Government Arts College'     #Mrs.T.Abirami,Dr.N.Lalitha,Dr.J.Udhaya kumar,Dr.S.Sagayadoss
                        print('\nMain Faculty:\n1.Mrs.T.Abirami\n2.Dr.N.Lalitha\n3.Dr.J.Udhaya kumar\n4.Dr.S.Sagayadoss')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.T.Abirami'
                            f=98000
                            print('Fees is Rs 98,000/year with Mrs.T.Abirami' )
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.N.Lalitha'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.N.Lalitha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.J.Udhaya kumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.J.Udhaya kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.Sagayadoss'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.S.Sagayadoss')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Ramakrishna Mission Vivekananda College'
                        print('\nMain Faculty:\n1.Dr. P. Pattinathar\n2.Dr. A. Satheesh Babu\n3.Dr. M. Arulmaran\n4.Mr. N. Dhinakaran\n5.Dr. G. Ashok Kumar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. P. Pattinathar'
                            f=1,00,000
                            print('Fees is Rs 1,00,000/year with Dr. P. Pattinathar' )
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr. A. Satheesh Babu'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr. A. Satheesh Babu')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F=' Dr.M.Arulmaran' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.M.Arulmaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Mr.N.Dhinakaran'
                            f=91000
                            print('Fees is Rs 91,000/year with Mr.N.Dhinakaran')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Dr. G. Ashok Kumar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr. G. Ashok Kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==2:
                    a='B.A English'
                    print('The Best Colleges for B.A English are:\n1.Loyala College\n2.PSG College of Arts and Science\n3.Rajeswari Vedachalam Government Arts College\n4.Government Arts College')
                    c3=int(input('enter the choice of college-'))
                    if c3==1:
                        C='Loyala College' #Dr. K.S. Antonysamy, Dr. V. David Jayabalan  Mr. X. Manoharan Dr. P. Mary Vidya Porselvi Ms. D. Christina Sagayamary 
                        print('\nMain Faculty:\n1Dr. K.S. Antonysamy\n2.Dr. V. David Jayabalan\n3.Mr. X. Manoharan\n4.Dr. P. Mary Vidya Porselvi\n5.Ms. D. Christina Sagayamary')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. K.S. Antonysamy'
                            f=1,00,000
                            print('Fees is Rs 1,00,000/year with Dr. K.S. Antonysamy')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr. V. David Jayabalan'
                            f=95000
                            print('Fees is Rs 95,000/year with Dr.V.David Jayabalan ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Mr. X. Manoharan' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=93000
                            print('Fees is Rs 93,000/year with Mr. X. Manoharan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr. P. Mary Vidya Porselvi'
                            f=91500
                            print('Fees is Rs 91,500/year with Dr. P. Mary Vidya Porselvi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Ms. D. Christina Sagayamary'
                            f=94000
                            print('Fees is Rs 94,000/year with Dr. G. Ms. D. Christina Sagayamary')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='PSG College of Arts and Science'
                        print('\nMain Faculty:\n1.Dr. Priya M\n2.Dr.Kausalya D\n3.Dr.Brinda P\n4.Dr.John Suganya M\n5.Dr.Nancy Thambi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. Priya M'
                            f=1,10,000
                            print('Fees is Rs 1,10,000/year with Dr. Priya M ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Kausalya D'
                            f=96000
                            print('Fees is Rs 96,000/year with Dr.Kausalya D')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Brinda P' #Mr.N.Dhinakaran,.Dr. G. Ashok Kumar
                            f=93500
                            print('Fees is Rs 93,500/year with Dr.Brinda P ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.John Suganya M'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.John Suganya M')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                        elif c2==5:
                            F='Dr.Nancy Thambi'
                            f=94500
                            print('Fees is Rs 94,500/year with Dr.Nancy Thambi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                            else:
                                print('\nRecord Deleted')                          
                                pass
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,P))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,P))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,P))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,P))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,P))
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,rep))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,rep))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,rep))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,rep))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,rep))
                R.commit()
            elif I.lower()=='commerce':
                print('\nBest colleges of Commerce in Chennai:\n1.Loyola College\n2.MCC Chennai\n3.Stella Maris College Chennai\n4.D.G Vaishnav College Chennai\n5.Presidency college chennai')
                c=int(input('\nEnter your choice of college='))
                if c==1:
                    C='Loyola College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.S Moshin\n2.Dr.G Allen\n3.Dr.R Simon\n4.Dr.K Akshay\n5.Dr.R Sushanth')                   
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.S Moshin'
                        f=105800
                        print('Fees is Rs 1,05,800/year with Dr.S Moshin')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.G Allen'
                        f=96550
                        print('Fees is Rs 96,550/year with Dr.G Allen')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.R Simon'
                        f=102000
                        print('Fees is Rs 1,02,000/year with Dr.R Simon')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.K Akshay'
                        f=94500
                        print('Fees is Rs 94,500/year with Dr.K Akshay')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.R Sushanth'                  
                        f=97430
                        print('Fees is Rs 97,430/year with Dr.R Sushanth')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==2:
                    C='MCC Chennai'                                                                                                         
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.A Denson\n2.Dr.R Kurian\n3.Dr.Jayasurya\n4.Dr.S Nandhini\n5.Dr.R Khaleel')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.A Denson'
                        f=104100
                        print('Fees is Rs 1,04,100/year with Dr.A Denson')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')                                                  #continue from here
                            pass
                    elif c2==2:
                        F='Dr.R Kurian'
                        f=203100
                        print('Fees is Rs 2,03,100/year with Dr.R Kurian')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.Jayasurya'
                        f=97430
                        print('Fees is Rs 97,430/year with Dr.Jayasurya')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.S Nandhini'
                        f=97000
                        print('Fees is Rs 97,000/year with Dr.S Nandhini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.A Khaleel'                  
                        f=103620
                        print('Fees is Rs 1,03,620/year with Dr.A Khaleel')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==3:
                    C='Stella Maris College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Amivarsha\n2.Dr.Sarath lal\n3.Dr.G Robert\n4.Dr.K Neerav\n5.Dr.E Sujith')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Amivarsha'
                        f=105800
                        print('Fees is Rs 1,05,800/year with Dr.Amivarsha')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.Sarath Lal'
                        f=100240
                        print('Fees is Rs 1,00,240/year with Dr.Sarath Lal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.G Robert'
                        f=101920
                        print('Fees is Rs 1,01,920/year with Dr.G Robert')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.K Neerav'
                        f=95000
                        print('Fees is Rs 95,000/year with Dr.K Neerav')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.E Sujith'                  
                        f=105160
                        print('Fees is Rs 1,05,160/year with Dr.E Sujith')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==4:
                    C='D.G Vaishnav College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.G Sivan\n2.Dr.P Ramlal\n3.Dr.N Bindhu\n4.Dr.P Dinesh\n5.Dr.T Natarajan')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.G Sivan'
                        f=98900
                        print('Fees is Rs 98,900/year with Dr.G Sivan')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.P Ramlal'
                        f=109000
                        print('Fees is Rs 1,09,000/year with Dr.P Ramlal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.N Bindhu'
                        f=102640
                        print('Fees is Rs 1,02,640/year with Dr.D Nalini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.P Dinesh'
                        f=107220
                        print('Fees is Rs 1,07,220/year with Dr.P Dinesh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Natarajan'                  
                        f=103300
                        print('Fees is Rs 1,03,300/year with Dr.T Natarajan')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==5:
                    C='Presidency College'
                    print('\nMain degrees are:\n1.B Com\n2.M Com\n3.B Economics\n4.B Acc & Finance\n5.B Marketing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Com'
                    elif t==2:
                        a='M Com'
                    elif t==3:
                        a='B Economics'
                    elif t==4:
                        a='B Acc & Finance'
                    elif t==5:
                        a='B Marketing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.N Varsha\n2.Dr.K Sampath\n3.Dr.R Shankar\n4.Dr.N.K Sheetal\n5.Dr.J Rose')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.N Varsha'
                        f=107670
                        print('Fees is Rs 1,07,670/year with Dr.N Varsha')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.K Sampath'                                           #continue
                        f=97320
                        print('Fees is Rs 97,320/year with Dr.K Sampath')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.R Shankar'
                        f=101920
                        print('Fees is Rs 1,01,920/year with Dr.R Shankar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.N.K Sheetal'
                        f=99800
                        print('Fees is Rs 99,800/year with Dr.N.K Sheetal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.J Rose'                  
                        f=96250
                        print('Fees is Rs 96,250/year with Dr.J Rose')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,P))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,P))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,P))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,P))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,P))
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,rep))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,rep))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,rep))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,rep))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,rep))
                R.commit()
                '''else:
                    print('Invalid choice')'''
            elif I.lower()=='fashion designing':
                print('\nBest colleges for Fashion Designing:\n1.National Institute of Fashion Technology(NIFT) Chennai\n2.Bishop Appasamy College of Arts and Science\n3.PSG College of Arts and Science\n4.Dr. N.G.P. Arts & Science College')
                c=int(input('\nEnter your choice of college='))
                if c==1:
                    C='NIFT Chennai'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Narendran M\n2.Dr.A Shreyas\n3.Dr.G Rohit\n4.Dr.R Ajmal\n5.Dr.T Suhail')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.M Narendran'
                        f=215800
                        print('Fees is Rs 2,15,800/year with Dr.M Narendran')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.A Shreyas'
                        f=213250
                        print('Fees is Rs 2,13,250/year with Dr.A Shreyas')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.G Rohit'
                        f=226000
                        print('Fees is Rs 2,26,000/year with Dr.G Rohit')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.R Ajmal'
                        f=220000
                        print('Fees is Rs 2,20,000/year with Dr.R Ajmal')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Suhail'                  
                        f=228600
                        print('Fees is Rs 2,28,600/year with Dr.T Suhail')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==2:
                    C='Bishop Appaswamy College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.Anil Kumar\n2.Dr.S Sunil\n3.Dr.J Venkat\n4.Dr.N Gayathri\n5.Dr.W Sundar')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.Anil Kumar'
                        f=185800
                        print('Fees is Rs 1,85,800/year with Dr.Anil Kumar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.S Sunil'
                        f=203100
                        print('Fees is Rs 2,03,100/year with Dr.S Sunil')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.J Venkat'
                        f=191000
                        print('Fees is Rs 1,91,000/year with Dr.J Venkat')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.N Gayathri'
                        f=187000
                        print('Fees is Rs 1,87,000/year with Dr.N Gayathri')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.W Sundar'                  
                        f=206620
                        print('Fees is Rs 2,06,620/year with Dr.W Sundar')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==3:
                    C='PSG College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.C.V Raman\n2.Dr.P Aryabhatta\n3.Dr.K Abhinav\n4.Dr.S Adharsh\n5.Dr.C Deepak')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.C.V Raman'
                        f=195800
                        print('Fees is Rs 1,95,800/year with Dr.C.V Raman')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.P Aryabhatta'
                        f=204440
                        print('Fees is Rs 2,04,440/year with Dr.P Aryabhatta')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.K Abhinav'
                        f=201000
                        print('Fees is Rs 2,01,000/year with Dr.K Abhinav')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.S Adharsh'
                        f=197000
                        print('Fees is Rs 1,97,000/year with Dr.S Adharsh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.C Deepak'                  
                        f=209120
                        print('Fees is Rs 2,09,120/year with Dr.C Deepak')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                elif c==4:
                    C='N.G.P College'
                    print('\nMain degrees are:\n1.B Des\n2.M Des\n3.B.F Tech\n4.B.S.c Fashion Designing\n5.M.S.c Fashion Designing')
                    t=int(input('Enter choice of degree='))
                    if t==1:
                        a='B Des'
                    elif t==2:
                        a='M Des'
                    elif t==3:
                        a='B.F Tech'
                    elif t==4:
                        a='B.S.c Fashion Designing'
                    elif t==5:
                        a='M.S.c Fashion Designing'
                    else:
                        print('Invalid choice')
                        pass
                    print('\nBest Faculty:\n1.Dr.S Anirudh\n2.Dr.H Aadithyaa\n3.Dr.D Nalini\n4.Dr.A Sharon\n5.Dr.T Murali')
                    c2=int(input('Enter choice of faculty='))
                    if c2==1:
                        F='Dr.S Anirudh'
                        f=205900
                        print('Fees is Rs 2,05,900/year with Dr.S Anirudh')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==2:
                        F='Dr.H Aadithyaa'
                        f=210000
                        print('Fees is Rs 2,10,000/year with Dr.H Aadithyaa')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==3:
                        F='Dr.D Nalini'
                        f=206650
                        print('Fees is Rs 2,06,650/year with Dr.D Nalini')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==4:
                        F='Dr.A Sharon'
                        f=207110
                        print('Fees is Rs 2,07,110/year with Dr.A Sharon')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    elif c2==5:
                        F='Dr.T Murali'                  
                        f=207260
                        print('Fees is Rs 2,07,260/year with Dr.T Murali')
                        r=input('\nAre you sure you want to continue(y/n)?')
                        if r.lower()=='y':
                            print('\n','*'*83,'SEAT ASSIGNED SUCCESSFULLY','*'*83)
                        else:
                            print('\nRecord Deleted')
                            pass
                    d.execute('update students set Interest="%s" where Passwd="%s"'%(I,P))
                    d.execute('update students set Course="%s" where Passwd="%s"'%(a,P))
                    d.execute('update students set College="%s" where Passwd="%s"'%(C,P))
                    d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,P))
                    d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,P))
                    d.execute('update students set Interest="%s" where Passwd="%s"'%(I,rep))
                    d.execute('update students set Course="%s" where Passwd="%s"'%(a,rep))
                    d.execute('update students set College="%s" where Passwd="%s"'%(C,rep))
                    d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,rep))
                    d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,rep))
                    R.commit()
                '''else:
                    print('\nInvalid Choice')'''            
            elif I.lower()=='medical':
                print('\nBest courses offered for Medical:\n1.MBBS\n2.MS\n3.MD\n4.BAMS\n5.BHMS')
                c1=int(input('which course would you like?'))
                if c1==1:
                    a='MBBS'
                    print('\nBest Colleges for MBBS in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Sajan Phiip George\n2.Raj S\n3.Ekta Rai\n4.Tony Thomson Chandy')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Sajan Phiip George'
                            f=98500
                            print('Fees is Rs 98,500/year with Sajan Phiip George')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Raj S'
                            f=90000
                            print('Fees is Rs 90,000/year with Raj S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ekta Rai'
                            f=90000
                            print('Fees is Rs 90,000/year with Ekta Rai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Tony Thomson Chandy'
                            f=91000
                            print('Fees is Rs 91,000/year with Tony Thomson Chandy')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Dr.Nelsonmandela S\n2.Ms.Krishnaveni S\n3.Ms.Sathya B\n4.Mr.Vignesh N')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Nelsonmandela S'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Nelsonmandela S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.Krishnaveni S'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Krishnaveni S')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sathya B'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sathya B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Mr.Vignesh N'
                            f=91000
                            print('Fees is Rs 91,000/year with Mr.Vignesh N')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr. Dinesh Kumar G\n2.Dr.Kalal Subhashchandra\n3.Dr.Charumathi B\n4.Dr.Timsi Jain')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. Dinesh Kumar G'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. Dinesh Kumar G')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Kalal Subhashchandra'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Kalal Subhashchandra')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Charumathi B'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Charumathi B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Timsi Jain'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Timsi Jain')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr. B. Chezhian\n2.Dr.V.Rajapriya\n3.Dr.P.Kanagavalli\n4.Dr. Elamathi Boss')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr. B. Chezhian'               # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. B. Chezhian ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.V.Rajapriya'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.V.Rajapriya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Kanagavalli'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Kanagavalli')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr. Elamathi Boss'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr. Elamathi Boss')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Nagaraj.P\n2.Dr.Vignesh\n3.Dr.P.Ashok\n4.Dr.Sasheem Haris')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Nagaraj.P'              # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Nagaraj.P')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Vignesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vignesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Ashok'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Ashok')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Sasheem Haris'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Sasheem Haris')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==2:           # Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='MS'
                    print('\nBest Colleges for MS in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Sri Ramachandra Medical College and Research Institute\n4.Madras Medical College\n5.PSG Institute of Medical Sciences and Research')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Vernon Lee\n2.Ms.Ramamani M\n3.Ms.Bina Isaac\n4.Ms.Molly Jacob')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Vernon Lee'
                            f=98500
                            print('Fees is Rs 98,500/year with Vernon Lee')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Ms.Ramamani M'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Ramamani M')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Bina Isaac'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Bina Isaac')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.Molly Jacob'
                            f=91000
                            print('Fees is Rs 91,000/year with Ms.Molly Jacob')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Mrs.J.Vasavi\n2.Mr.U.M.Prakash\n3.Ms.Sathya B\n4.Ahalya.S.P')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.J.Vasavi'
                            f=98500
                            print('Fees is Rs 98,500/year with Mrs.J.Vasavi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.U.M.Prakash'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.U.M.Prakash')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sathya B'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sathya B')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ahalya.S.P'
                            f=91000
                            print('Fees is Rs 91,000/year with Ahalya.S.P')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr.Gunapriya Raghunath\n2.Dr.Vijayalakshmi\n3.Dr.Vijayakumar\n4.Dr.Archana')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gunapriya Raghunath'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Gunapriya Raghunath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Vijayalakshmi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vijayalakshmi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Vijayakumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Vijayakumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Archana'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Archana')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr.P.Murugesan\n2.Dr.B.Sathyalakshmi\n3.Dr.M.Vijayalakshi\n4.Dr V.Loganayaki')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.P.Murugesan'             # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr. B. Chezhian ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.B.Sathyalakshmi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.B.Sathyalakshmi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.M.Vijayalakshi'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.M.Vijayalakshi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr V.Loganayaki'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr V.Loganayaki')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Raj\n2.Dr.E.Durai\n3.Dr.P.Anand\n4.Dr.S.Suresh')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Raj'              # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Raj')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.E.Durai'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.E.Durai')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Anand'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Anand')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.S.Suresh'
                            f=9100
                            print('Fees is Rs 91,000/year with Dr.S.Suresh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==3:# MD\n4.BAMS\n5.BHMS')  Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='MD'
                    print('\nBest Colleges for MD in Tamil Nadu are:\n1.Christian Medical College\n2.SRM Institute of Science and Technology\n3.Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Christian Medical College'
                        print('\nMain Faculty:\n1.Joshua Uzagare\n2.Keval Pandya\n3.Saurav Rath\n4.Arnav Pandey')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Joshua Uzagare'
                            f=98500
                            print('Fees is Rs 98,500/year with Joshua Uzagare')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Keval Pandya'
                            f=90000
                            print('Fees is Rs 90,000/year with Keval Pandya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Saurav Rath'
                            f=90000
                            print('Fees is Rs 90,000/year with Saurav Rath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Arnav Pandey'
                            f=91000
                            print('Fees is Rs 91,000/year with Arnav Pandey')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='SRM Institute of Science and Technology'
                        print('\nMain Faculty:\n1.Ms.K.Vani\n2.Mr.R.Umesh\n3.Ms.S.Shanti\n4.Ms.A.Akshaya')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Ms.K.Vani'
                            f=98500
                            print('Fees is Rs 98,500/year with Ms.K.Vani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.R.Umesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.R.Umesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.Shanti'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.Shanti')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Ms.A.Akshaya'
                            f=91000
                            print('Fees is Rs 91,000/year with Ms.A.Akshaya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Saveetha Medical College'
                        print('\nMain Faculty:\n1.Dr.Prathibha\n2.Dr.Premkumar\n3.Dr.Rengaramani\n4.Dr.Ananthi')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Prathibha'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Prathibha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Premkumar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Premkumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Rengaramani'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Rengaramani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Ananthi'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Ananthi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Madras Medical College'
                        print('\nMain Faculty:\n1.Dr.C.Gomathi\n2.Dr.J.V.S.Prakash\n3.Dr.P.Karkuzhali\n4.Dr.Geetha Devadas')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.C.Gomathi'          # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.C.Gomathi')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.J.V.S.Prakash'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.J.V.S.Prakash')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.P.Karkuzhali'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.P.Karkuzhali')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Geetha Devadas'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Geetha Devadas')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==5:
                        C='Madurai Medical College'
                        print('\nMain Faculty:\n1.Dr.Harish\n2.Elango.T\n3.A.G.Sangeetha\n4.Dr.P.Jaganath')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Harish'            # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Harish')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Elango.T'
                            f=90000
                            print('Fees is Rs 90,000/year with Elango.T')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='A.G.Sangeetha'
                            f=90000
                            print('Fees is Rs 90,000/year with A.G.Sangeetha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.P.Jaganath'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.P.Jaganath')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==4:
                    a='BAMS'
                    print('\nBest Colleges for BAMS in Tamil Nadu are:\n1Dharma Ayurveda Medical College and Hospital\n2.Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya\n3.Sri Sairam Ayurveda Medical College and Research Centre\n4.Ayurveda College')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Dharma Ayurveda Medical College and Hospital'    #Dr. N. HARVIN GEORGE,Dr. DANDEY MALLIKA,Dr. T. UDHAYA SHANKAR,Dr. VEENA. P. REGHUNATHAN
                        print('\nMain Faculty:\n1.Dr.N.Harvin George\n2.Dr.Dandey Mallika\n3.Dr.T.Udhaya Shankar\n4.Dr.Veena.P.Reghunathan')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.N.Harvin George'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.N.Harvin George')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Dandey Mallika'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Dandey Mallika')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.T.Udhaya Shankar'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.T.Udhaya Shankar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Veena.P.Reghunathan'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Veena.P.Reghunathan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya'
                        print('\nMain Faculty:\n1.Dr.Goruganthu\n2.Dr.Mulaka Shiva\n3.Dr.Praveen Kumar\n4.Dr.Prem Kumar')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Goruganthu'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Goruganthu')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Mulaka Shiva'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Mulaka Shiva')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.Shanti'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.Shanti')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Prem Kumar'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Prem Kumar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Sri Sairam Ayurveda Medical College and Research Centre'
                        print('\nMain Faculty:\n1.Dr.K.K.Balendar\n2.Dr.P.C.Penchalaiah\n3.Ms.S.M.Subhani\n4.Dr.Velmurugan')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.K.K.Balendar'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.K.K.Balendar')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='P.C.Penchalaiah'
                            f=90000
                            print('Fees is Rs 90,000/year with P.C.Penchalaiah')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.S.M.Subhani'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.S.M.Subhani')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Velmurugan'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Velmurugan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Ayurveda College'
                        print('\nMain Faculty:\n1.Dr.T.John\n2.Mr.Mahesh\n2.Dr.Premanand\n4.Dr.Pradeep')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.T.John'          # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year withDr.T.John ')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.Mahesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.Mahesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.Premanand'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Premanand')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Pradeep'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Pradeep')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                elif c1==5:# MD\n4.BAMS\n5.BHMS')  Christian Medical College. . Madras Medical College. SRM Medical College Hospital and Research Centre,. Sri Ramachandra Medical College and Research Institute. PSG Institute of Medical Sciences and Research
                    a='BHMS'
                    print('\nBest Colleges for BHMS in Tamil Nadu are:\n1.Vinayaka Missions Homoeopathic Medical College and Hospital\n2.Government Homoeopathic Medical College and Hospital\n3.Sarada Krishna Homoeopathic Medical College\n4.Venkateswara Homoeopathic Medical College and Hospital')
                    c3=int(input('\nEnter your choice of college='))
                    if c3==1:
                        C='Vinayaka Missions Homoeopathic Medical College and Hospital'    #Dr. N. HARVIN GEORGE,Dr. DANDEY MALLIKA,Dr. T. UDHAYA SHANKAR,Dr. VEENA. P. REGHUNATHAN
                        print('\nMain Faculty:\n1.Dr.E.Rathnasabapathi Chairperson\n2.Prof.Dr.R.S.Shanmugasundaram\n3.M.Sree Abinav\n4.T.Amsavali')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.E.Rathnasabapathi Chairperson'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.E.Rathnasabapathi Chairperson')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Prof.Dr.R.S.Shanmugasundaram'
                            f=90000
                            print('Fees is Rs 90,000/year with Prof.Dr.R.S.Shanmugasundaram')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='M.Sree Abinav'
                            f=90000
                            print('Fees is Rs 90,000/year with M.Sree Abinav')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='T.Amsavali'
                            f=91000
                            print('Fees is Rs 91,000/year with T.Amsavali')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                    elif c3==2:
                        C='Government Homoeopathic Medical College and Hospital'
                        print('\nMain Faculty:\n1.Dr.Gurunathan\n2.Dr.Shukla\n3.Mrs.K.Priya\n4.Dr.Selvam')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.Gurunathan'
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.Gurunathan')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.Shukla'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.Shukla')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Mrs.K.Priya'
                            f=90000
                            print('Fees is Rs 90,000/year with Mrs.K.Priya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Selvam'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Selvam')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                                pass
                    elif c3==3:
                        C='Sarada Krishna Homoeopathic Medical College'
                        print('\nMain Faculty:\n1.Mrs.V.Maya\n2.Dr.D.Lokesh\n3.Ms.Sulaka\n4.Dr.Vetri')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Mrs.V.Maya'
                            f=98500
                            print('Fees is Rs 98,500/year with Mrs.V.Maya')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Dr.D.Lokesh'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.D.Lokesh')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Ms.Sulaka'
                            f=90000
                            print('Fees is Rs 90,000/year with Ms.Sulaka')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='Dr.Vetri'
                            f=91000
                            print('Fees is Rs 91,000/year with Dr.Vetri')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                    elif c3==4:
                        C='Ayurveda College'
                        print('\nMain Faculty:\n1.Dr.E.Senthil\n2.Mr.Nagaraj\n2.Dr.K.Radha\n4.G.Kavitha')
                        c2=int(input('\nEnter  your choice of faculty:'))
                        if c2==1:
                            F='Dr.E.Senthil'        # #Saveetha Medical College\n4.Madras Medical College\n5.Madurai Medical College
                            f=98500
                            print('Fees is Rs 98,500/year with Dr.E.Senthil')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass 
                        elif c2==2:
                            F='Mr.Nagaraj'
                            f=90000
                            print('Fees is Rs 90,000/year with Mr.Nagaraj')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==3:
                            F='Dr.K.Radha'
                            f=90000
                            print('Fees is Rs 90,000/year with Dr.K.Radha') 
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')
                                pass
                        elif c2==4:
                            F='G.Kavitha'
                            f=91000
                            print('Fees is Rs 91,000/year with G.Kavitha')
                            r=input('\nAre you sure you want to register(yes/no)?')
                            if r.lower()=='yes':
                                 print('\n','*'*83,'SUCCESSFULLY REGISTERED','*'*83)
                            else:
                                print('\nRecord Deleted')                          #PSG College of Arts and Science\n3.Presidency College Chennai\n4.Government Arts College\n5.Ramakrishna Mission Vivekananda College')
                                pass
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,P))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,P))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,P))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,P))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,P))
                d.execute('update students set Interest="%s" where Passwd="%s"'%(I,rep))
                d.execute('update students set Course="%s" where Passwd="%s"'%(a,rep))
                d.execute('update students set College="%s" where Passwd="%s"'%(C,rep))
                d.execute('update students set Faculty="%s" where Passwd="%s"'%(F,rep))
                d.execute('update students set Feesperyear="%s" where Passwd="%s"'%(f,rep))
                R.commit()
            elif I.lower()=='sociology':
                print('\nBest Colleges for Sociology:\n1.NIT Trichy\n2.Presidency College\n3.Loyola College\n4.PSG College of Arts and Science\n5.University of Madras')
                c=int(input('\nEnter your choice of college='))
            else:
                print('\nPlease Choose any interest from this set:\n1.Engineering\n2.Arts and Science\n3.Commerce\n4.Fashion designing\n5.Medical\n6.Artificial Intelligence')
                print('\nPlease try again')
def remrec():
    print('\nRemove by:\n1.ID\n2.Name')
    r=int(input('Enter choice='))
    if r==1:
        j=int(input('Enter ID to remove='))
        d.execute('select * from students')
        w=d.fetchall()
        k=0
        for i in w:
            if j==i[0]:
                w.remove(i)
                d.execute('delete from students where ID="%s"'%j)
                R.commit()
                print('\nStudent removed Successfully')
                k+=1
        if k==0:
            print('\nNo student with that ID')
    elif r==2:
        b=input('Enter Name to remove=')
        d.execute('select * from students')
        w=d.fetchall()
        k=0
        for i in w:
            if b.lower()==i[1].lower():
                w.remove(i)
                d.execute('delete from students where Name="%s"'%b)
                R.commit()
                print('\nStudent removed Successfully')
                k+=1
        if k==0:
            print('\nNo student with that name')
    else:
        print('\nInvalid choice')

E=input('Do you want to remove record(y/n)?')
while E.lower()=='y':
    remrec()
    E=input('Remove another?')

    
    

