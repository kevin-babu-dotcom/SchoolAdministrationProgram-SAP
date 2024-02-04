import pickle,os,sys,csv
from datetime import date
ans=1
def find(x,y,z):
    while x<=y or x>=z:
        print('invalid choice')
        x=int(input("Enter your choice"))
    return x

def dob():
    y=int(input("Enter Date of Birth"))
    y=find(y,1,131)
    w=int(input("Enter month no"))
    w=find(w,1,12)
    z=int(input("Enter birth year:"))
    while len(str(z))!=4:
        z=int(input("Enter birth year:"))
    return date(z,w,y)

def addtc():
    fh=open('teacher.dat','ab')
    st={}
    st['name']=input("Enter name:")
    st['dept']=input("enter subject:")
    st['dob']=dob()
    st['address']=input("Enter address:")
    st['dateofjoin']=date.today()
    st['adno']=int(input("Enter identification no:"))
    st['pass']=eval(input("Set new password:"))
    print("1)ENGLISH\n2)HINDI\n3)SPORTS\n4)PHYSICS\n5)CHEMISTRY\n6)MATHEMATICS\n7)SOCIAL SCIENCE8\n9COMPUTER SCIENCE\n9)BIOLOGY")
    subch=int(input("Enter your choice:"))
    find(1,subch,9)
    st['subject']=subch
    pickle.dump(st,fh)
    fh.close()

def marks():
    marks=[]
    for i in range(5):
        print("Enter mark",i+1)
        marks[i]=int(input('>>>'))
    return marks
    
def addst():
    fh=open('students.dat','ab')
    st={}
    st['adno']=int(input("Enter admission no:"))
    st['pass']=eval(input("Enter password:"))
    st['name']=input("Enter name:")
    st['class']=input("enter class:")
    st['div']=input("enter division:")
    st['dob']=dob()
    st['address']=input("Enter address:")
    st['marks']= marks()
    st['dateofjoin']=date.today()
    
    pickle.dump(st,fh)
    fh.close()

def addprp():
    fh=open('principal.csv','a',newline='')
    wo=csv.writer(fh)
    p1=print("is this the first principal?if yes type 1 else 0")
    if p1==1:
        st=[]
        st=['name','date of joining','login_id','password']
        wo.writerow(st)
    date=date.today()
    st=[]
    st[0]=input("Enter name:")
    st[1]=date.today
    st[2]=eval(input("Enter login-id:"))
    st[3]=eval(input("Enter password:"))
    wo.writerow(st)
    fh.close()

def Etc():
    fh=open('teacher.dat','rb')
    fh1=open('teachertemp.dat','ab+')
    print('1)Name\n2)Department\n3)Date of birth\n4)Address\n5)password')
    ch=print('Enter your choice:')
    find(1,ch,6)
    fh.seek(0)
    fh1.seek(0)
    if ch==1:
        x='name'
        y=input("Enter name:")
    elif x=='dept':
        
        y=input("enter subject:")
    elif x=='dob':
        
        y=dob()
    elif x=='address':
       
        y=input("Enter address:")
    elif x=='pass':
        
        y=eval(input("Set new password"))
    id=int(input("Enter your identification no:"))
    found='false'
    try:
        while True:
            st=pickle.load(fh)
            if st['id']!=id:
                pickle.dump(st,fh1)
            else:
                st['x']=y
                found='true'
                pickle.dump(st,fh1)
    except EOFError:
        if found=='false':
            print("Sorry,no such record found'")
        fh.close()
    fh1.close()
    os.remove('teacher.dat')
    os.rename('teachertemp.dat','teacher.dat')

def Est():
    fh=open('student.dat','rb')
    fh1=open('studenttemp.dat','ab+')
    print('1)Name\n2)class\n3)Date of birth\n4)Address\n5)password\n6)division\n7)marks')
    ch=print('Enter your choice:')
    find(1,ch,7)
    fh.seek(0)
    fh1.seek(0)
    if ch==1:
        x='name'
        y=input("Enter name:")
    elif x=='dept':
        
        y=input("enter class:")
    elif x=='dob':
        
        y=dob()
    elif x=='address':
        
        y=input("Enter address:")
    elif x=='pass':
        
        y=eval(input("Set new password"))
    elif x=='division':
        
        y=input("Enter division:")
    elif x=='marks':
        
        y=marks()

        
    id=int(input("Enter your identification no:"))
    found='false'


    try:
        if x=='marks':
            print()
        while True:

                st=pickle.load(fh)
                if st['id']!=id:
                    pickle.dump(st,fh1)
                else:
                    st['x']=y
                    found='true'
                    pickle.dump(st,fh1)
    except EOFError:
            if found=='false':
                print("Sorry,no such record found'")
            fh.close()
    fh1.close()


    os.remove('student.dat')
    os.rename('studenttemp.dat','student.dat')

def Dsalltc():
    fh=open('teachers.dat','rb')
    try:
        while True:
            st=pickle.load(fh)
            print(st)
    except EOFError:
        fh.close()

def Dsprp():
    fh=open('principal','r',newline='')
    ro=csv.reader(fh)
    print(ro)
    fh.close()

def Eprp():
    fh=open('principal.csv','r',newline='')
    id=int(input("Enter the identification no:"))
    print("ENTER WHAT YOU WANT TO EDIT\n1)NAME\n2)PASSWORD")
    ep=int(input())
    if ep==1:
        x=0
        n=input("ENTER NEW NAME:")
    else:
        n=input("ENTER NEW PASSWORD")
        x=3
    temp=[]
    st=csv.reader(fh)
    for i in st:
        if i[2]!=id:
            temp.append(i)
        else:
            i[x]=n
            temp.append(i)
    fh.close()
    fh=open('principal.csv','w',newline='')
    wo=csv.writer(fh)
    wo.writerows(temp)
    fh.close()

def DstcDP():
    fh=open('teachers.dat','rb')
    dep=input("ENTER DEPARTMENT:")
    found='false'
    try:
        while True:
            st=pickle.load(fh)
            if st['dept']==dep:
             found='true'
             print(st)
            else:
                continue
    except EOFError:
        if found=='false':
            print("NO TEACHERS IN THE DEPARTMENT")
        fh.close()

def Dltc():
    fh=open('teacher.dat','rb')
    fh1=open('teachertemp.dat','ab+')
    fh.seek(0)
    fh1.seek(0)
    id=int(input("Enter the identification no:"))
    found='false'
    try:
        while True:
            st=pickle.load(fh)
            if st['id']!=id:
                pickle.dump(st,fh1)
            else:
                continue
    except EOFError:
        if found=='false':
            print("Sorry,no such record found'")
        fh.close()
    fh1.close()
    os.remove('teacher.dat')
    os.rename('teachertemp.dat','teacher.dat')

def Dlprp():
    fh=open('principal.csv','r',newline='')
    id=int(input("Enter the identification no:"))
    temp=[]
    st=csv.reader(fh)
    for i in st:
        if i[2]!=id:
            temp.append(i)
    fh.close()
    fh=open('principal.csv','w',newline='')
    wo=csv.writer(fh)
    wo.writerows(temp)
    fh.close()


while ans==1:
    print('LOGIN INTERFACE')
    print('Who wants to Login?')
    print('1)PRINCIPAL\n2)TEACHER\n3)STUDENT\n4)ADMIN\n5)EXIT')
    ch=int(input())
    find(ch,1,4)
    if ch==1:
        pass

    elif ch==4:
        print('1)ADD\n2)EDIT\n3)DISPLAY\n4)DELETE\n5)BACK\n6)LOGOUT')
        ch1=int(input())
        find(ch1,1,6)
        if ch1==1:
            print('1)NEW TEACHER\n2)NEW STUDENT\n3)NEW PRINCIPAL\n4)BACK\n5)LOGOUT')
            ch11=int(input())
            if ch11==1:
                addtc()
            elif ch11==2:
                pass
            elif ch11==3:
                addprp()
            elif ch11==4:
                print('1)ADD\n2)EDIT\n3)DISPLAY\n4)DELETE\n5)BACK\n6)LOGOUT')
                ch1=int(input())
                break
            elif ch11==5:
                print('1)PRINCIPAL\n2)TEACHER\n3)STUDENT\n4)ADMIN\n5)EXIT')
                ch=int(input())
                break
        elif ch1==2:
            print('1)EDIT TEACHER\n2)EDIT STUDENT\n3)EDIT PRINCIPAL\n4)BACK\n5)LOGOUT')
            ch12=int(input())
            find(ch12,1,5)
            if ch12==1:
                Etc()
            elif ch12==2:
                pass
            elif ch12==3:
                Eprp()
            elif ch12==4:
                print('1)ADD\n2)EDIT\n3)DISPLAY\n4)DELETE\n5)BACK\n6)LOGOUT')
                ch1=int(input())
                break
            elif ch12==5:
                print('1)PRINCIPAL\n2)TEACHER\n3)STUDENT\n4)ADMIN\n5)EXIT')
                ch=int(input())
                break
        elif ch1==3:
            print('1)DISPLAY ALL TEACHER\n2)DISPLAY ALL STUDENT\n3)DISPLAY PRINCIPAL\n4)STUDENTS OF A CLASS\n5)STUDENTS OF A DIVISON\n6)TEACHERS OF A DEPARTMENT\n7)STUDENT WITH A BIRTHDAY\n8 DISPLAY A STUDENT\n9)DISPLAY REPORT CARD\n10)BACK\n11)LOGOUT')
            ch13=int(input())
            find(ch13,1,11)
            if ch13==1:
                Dsalltc()
            elif ch13==2:
                pass
            elif ch13==3:
                Dsprp()
            elif ch13==4:
                pass
            elif ch13==5:
                pass
            elif ch13==6:
                DstcDP()
            elif ch13==7:
                pass
            elif ch13==8:
                pass
            elif ch13==9:
                pass
            elif ch13==10:
                print('1)ADD\n2)EDIT\n3)DISPLAY\n4)DELETE\n5)BACK\n6)LOGOUT')
                ch1=int(input())
                break
            elif ch13==11:
                print('1)PRINCIPAL\n2)TEACHER\n3)STUDENT\n4)ADMIN\n5)EXIT')
                ch=int(input())
                break
        elif ch1==4:
            print('1)DELETE STUDENT\n2)DELETE TEACHER\n3)DELETE PRINCIPAL\n4)BACK\n5)LOGOUT')
            ch14=int(input())
            find(ch14,1,5)
            if ch14==1:
                pass
            elif ch14==2:
                Dltc()
            elif ch14==3:
                Dlprp()
            elif ch14==4:
                print('1)ADD\n2)EDIT\n3)DISPLAY\n4)DELETE\n5)BACK\n6)LOGOUT')
                ch1=int(input())
                break
            elif ch14==5:
                print('1)PRINCIPAL\n2)TEACHER\n3)STUDENT\n4)ADMIN\n5)EXIT')
                ch=int(input())
                break
    
            







        









    
