from datetime import date
import mysql.connector as ms,pickle,os,sys
con=ms.connect(host='localhost',user='root',passwd='')
print('Successfully connected')
cu=con.cursor()
cu.execute('Create database if not exists sch')
con.commit()
cu.execute('use sch')
con.commit()
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find4():
    dept={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTER SC'}
    print('1.English\n2.Chemistry\n3.Physics\n4.Mathematics\n5.Computer Science')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return dept[ch] 
def dob():
    y=int(input("Enter Date of Birth"))
    y=find(y,1,131)
    w=int(input("Enter month no"))
    w=find(w,1,12)
    z=int(input("Enter birth year:"))
    while len(str(z))!=4:
        z=int(input("Enter birth year:"))
    return date(z,w,y)
def find3(x):
    k=int(input('Enter id'))
    kl=input('Enter password')
    cu.execute('select * from st where id=%s'%(k,))
    global i
    i=cu.fetchone()
    if i[0]==k and i[-6]==kl:
        return 0
    return 1
dept1={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTERSC'}
dept={1: 'ENG', 2: 'CHEM', 3: 'PHY', 4: 'MATH', 5: 'CS'}
def find12(km):
    def find13():
        m1=str(i[2])+i[3]
        cu.execute('select * from cd where class="%s"'%(m1,))
        f=cu.fetchall()
        for j in f:
            pass
            #print(j)
            
        f1=open('te.dat','ab+')
        f1.seek(0)
        try:
            while True:
                jk=pickle.load(f1)
                if jk['id']==j[1]:
                    return jk['Name']
        except EOFError:
            f1.close()        
    def find14(z):
        mz=0
        cu.execute('select max(%s) from st where class=%s and divi="%s"'%(z,i[2],i[3]))
        f=cu.fetchone()
        return f[0]
    cu.execute('select * from st where id=%s'%(km,))
    f=cu.fetchall()
    for i in f:
        pass
    x=sum((i[-1],i[-2]+i[-3]+i[-4]+i[-5]))
    if x>200:
        grade='A1'
    elif x>175:
        grade='A2'
    elif x>150:
        grade='B1'
    elif x>125:
        grade='B2'
    else:
        grade='c '
    print(' '*48,"St.Antony's Public School")
    print(' '*48,"  Anakkal , Kanjirapally")
    print(' '*48,"CBSE AFFLICATION NO:930037")
    print("\n",' '*55,"REPORT CARD")
    print(' '*57,'2022-2023')
    print('\t\t\t\tNAME    :',i[1])
    print('\t\t\t\tclass   :',i[2])
    print('\t\t\t\tDivision:',i[3])
    print('\t\t\t\tRoll No :',25,'\t'*4,'FATHER        :',i[1].title())
    print('\t\t\t\tAdm. NO :',i[0],'\t'*4,'MOTHER        :',i[1].title())
    print('\t\t\t\tDOB     :',i[4],'\t'*3,'CLASS TEACHER :',find13())
    print('\t'*5,'_'*48,)
    print('\t'*5,'| SUBJECTS',' |','MAX.','\t','|SCORED  | TOP  |')
    print('\t'*5,'-'*46,'-|',sep='-')
    for j in dept1:
        print('\t'*5,'|',dept1[j],'\t|',50,'\t |',i[-6+j],'\t  |',find14(dept[j]),'  |')  
    print('\t'*5,'-'*46,'-|',sep='-')
    print('\t'*5,'| TOTAL','\t'*2,'|',250,'\t |',x,' GRADE:',grade,'|')
    print('\t'*5,'-'*46,'-|',sep='-')
    from datetime import date
    print('\t'*5,'Place:','Anakkal')
    print('\t'*5,'Date :',date.today())

ans='y'
wel={}
while ans=='y' or ans=='Y':
    print('\t\t\t\t\tLOGIN INTERFACE\n1.Principal\n2.Teacher\n3.Student\n4.Admin')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,4)
    if ch==1:
        print('\t\t\t\tPRINCIPAL LOGIN')
        m=0
        while m==1:
            m=find3('pr.dat')
        while m==0:
            print('1.View teacher\n2.View student\n3.Data control\n4.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,4)
            if ch==1:
                ms=0
                while ms==0:
                    print('1.View Teacher\n2.View Department\n3.View teachers\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    f1=open('teachers.dat','rb')
                    f1.seek(0)
                    n=1
                    nn=0
                    try:
                        while True:
                            l=pickle.load(f1)
                            if ch==1:
                                x=int(input('Enter Teachers ID'))
                                x=find2(x,'teachers.dat')
                                print(l)
                                nn=1
                                break
                            elif ch==2:
                                if n==1:
                                    x=find4()
                                    n=0
                                if l['Dept']==x:
                                    print(l)
                                    nn=1
                            elif ch==3:
                                print(l)
                                nn=1
                            elif ch==4:
                                nn=1
                                ms=1
                            elif ch==5:
                                nn=1
                                ms=1
                                m=1
                            else:
                                pass
                    except EOFError:
                        if nn==0:
                            print('NO Teacher Found')
                        f1.close()
            elif ch==2:
                ms=0
                while ms==0:
                    print('1.View Division\n2.View Class\n3.View Student\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
            elif ch==3:
                ms=0
                while ms==0:
                    print('1.add teacher\n2.remove teacher\n3.change teacher\n4.change class teacher\n5.remove class teacher')
                    print('6.add class teacher\n7.Remove a class\n8.Add a Class \n9.Back\n10.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,10)
                    if ch in [1,2,3,4,5,6]:
                        k=int(input('Enter teacher id'))
            else:
                m=1
    elif ch==2:
        
        print('\t\t\t\tTEACHER LOGIN')
        wel={}
        m=0
        while m==1:
            m=find3('te.dat')
        while m==0:
            print('1.View My Class\n2.View Classes\n3.Edit Marks\n4.Edit marks of a full division\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            if ch==1:
                jj=0
                while jj==0:
                    print('1.View a student\n2.View Marks\n3.Print report card\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        pass
                    if ch==2:
                        pass
                    if ch==3:
                        ans='y'
                        while ans=='y' or ans=='Y':
                            print('1.Generate report card for one student\n2.Generate for the whole class')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,2)
    
    elif ch==3:
        print('\t\t\t\tSTUDENT LOGIN')
        m=find3('st')
        while m==1:
            m=find3('st')
        while m==0:
            print('1.View my Class and Div\n2.View Report Card\n3.View my Details\n4.View fee details')
            print('5.View class teacher\n6.View Other teachers\n7.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,7)
            if ch==1:
                print('Class',i[2])
                print('Division',i[3])
            elif ch==2:
                find12(i[0])
            elif ch==3:
                print(i)
            elif ch==4:
                print('paid')
            elif ch==5:
                k=(str(i[2])+i[3])
                cu.execute('select * from cd where class="%s"'%(k,))
                k=cu.fetchone()
                fh=open('teachers.dat','rb')
                    try:
                        while True:
                            st=pickle.load(fh)
                            if st['id']==k[1]:
                                print(st['id'],st['Name'])
                    except EOFError:
                        fh.close()
            elif ch==6:
                k=(str(i[2])+i[3])
                cu.execute('select * from cd where class="%s"'%(k,))
                k=cu.fetchone()
                fh=open('teachers.dat','rb')
                for jk in k:
                    try:
                        while True:
                            st=pickle.load(fh)
                            if st['id']==k[jk]:
                                print(st['id'],st['Name'])
                    except EOFError:
                        fh.close()
            else:
                m=1
            
    '''else:
        print('\t\t\t\tADMIN LOGIN')
        m=0
        while m==1:
            m=find3('ad.dat')
        while m==0:
            print('1.Add\n2.Edit\n3.Display\n4.Delete\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            if ch==1:
                ms=0
                while ms==0:
                    print('1.Add New Teacher\n2.Add New Student\n3.Add New Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                    elif ch==2:
                    elif ch==3:
                    elif ch==4:
                    else:
            elif ch==2:
                nj=0
                while nj==0:
                    print('1.Edit Name\n2.Edit Address\n3.Edit gender\n4.Edit Aadhar\n5.edit phone number\n6.Date of birth')
                    print('7.Edit class and div\n8.Edit Mark\n9.Back\n10.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,10)
                    if ch==1:
                    elif ch==2:
                    elif ch==3:
                    elif ch==4:
                    else:
            elif ch==3:
                mn=1
                while mn==1:
                    print('1.Display all teachers\n2.Display all students\n3.Display Principal\n4.Display students of a class')
                    print('5.Display students of a division\n6.Display teachers of a department\n7.Display Students having birthday on a date')
                    print('8.View a Student\n9.Print Report Card\n10.Back\n11.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,11)
                    if ch==1:
                    elif ch==2:
                    elif ch==3:
                    elif ch==4:
                    else:
            elif ch==4:
                kl=0
                while kl==0:
                    print('1.Delete Student\n2.Delete Teacher\n3.Delete Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                    elif ch==2:
                    elif ch==3:
                    elif ch==4:
                    else:
            else:
                m=1'''
