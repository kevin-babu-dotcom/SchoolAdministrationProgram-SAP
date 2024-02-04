from datetime import date
import mysql.connector as ms,pickle,os,sys
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find2(x):
    cu.execute('select id from %s'%(x,))
    k=cu.fetchall()
    kl=[]
    j=101
    for i in k:
        for j in i:
            kl.append(j)
    i=101
    while i in kl:
        i+=1
    kl.append(i)
    return i

def find7():
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    return date(z,w,y)
def find3(x):
    k=int(input('Enter id'))
    kl=input('Enter password')
    cu.execute('select * from %s'%(x,))
    f=cu.fetchall()
    for i in f:
        print(i)
        if i[0]==k and i[-1]==kl:
            return 0
    return 1
def find44(x):
    an=1
    while an==1:
        cu.execute('select id from st')
        f=cu.fetchall()
        for i in f:
            if x in i:
                return x
        print('invalid ID')
        x=int(input('Enter ID'))
    
dept1={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTERSC'}
dept={1: 'ENG', 2: 'CHEM', 3: 'PHY', 4: 'MATH', 5: 'CS'}
def find4():
    print('1.English\n2.Chemistry\n3.Physics\n4.Mathematics\n5.Computer Science')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return dept1[ch] 
def find5():
    gen={1:'Male',2:'Girl'}
    print('1.Male\n2.Female')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return gen[ch]
dept1={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTERSC'}

def find12(k):
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
    cu.execute('select * from st where id=%s'%(k,))
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
dept={1: 'ENG', 2: 'CHEM', 3: 'PHY', 4: 'MATH', 5: 'CS'}
con=ms.connect(host='localhost',user='root',passwd='')
if con.is_connected():
    print('Successfully connected')
    cu=con.cursor()
    cu.execute('Create database if not exists sch')
    con.commit()
    cu.execute('use sch')
    con.commit()
    #cu.execute('Drop table st')
    #con.commit()
    cu.execute("create table if not exists ad (ID int(3) primary key,NAME varchar(20),DOB date,PASS varchar(10))")
    con.commit()
    cu.execute("create table if not exists pr (ID int(3) primary key,NAME varchar(20),DOB date,PASS varchar(10))")
    con.commit()
    cu.execute("create table if not exists st (ID int(3) primary key,NAME varchar(20),CLASS int(2),DIVI char(1),DOB date,PASS varchar(10),ENG int(2),CHEM int(2),PHY int(2),MATH int(2),CS int(2))")
    con.commit()
    cu.execute("create table if not exists te (ID int(3) primary key,NAME varchar(20),DEPT varchar(15),DOB date,PASS varchar(10))")
    con.commit()
def find6():
    con=1
    while con==1:
        x=int(input('Enter the class'))
        x=find1(x,1,12)
        y=input('Enter the division').upper()
        cu.execute('select class from cd')
        f=cu.fetchall()
        for i in f:
            if str(x)+y in i:
                return x,y
        print('INVALID Class or Division')
        

    
ans='y'
wel={}
while ans=='y' or ans=='Y':
    print('\t\t\t\t\tLOGIN INTERFACE\n1.Principal\n2.Teacher\n3.Student\n4.Admin')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,4)
    if ch==1:
        print('\t\t\t\tPRINCIPAL LOGIN')
        '''m=find3(pr)
        while m==1:
            m=find3(pr)'''
        m=0
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
                    if ch==1:
                        pass
            elif ch==2:
                ms=0
                while ms==0:
                    print('1.View Division\n2.View Class\n3.View Student\n4.View Students\n5.Back\n6.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,6)
                    if ch==1:
                        k=int(input('Enter class'))
                        k=find1(k,1,12)
                        k1=input('Enter division')
                        k1=k1.upper()
                        cu.execute('select * from st where class=%s and divi="%s"'%(k,k1))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==2:
                        k=int(input('Enter class'))
                        k=find1(k,1,12)
                        cu.execute('select * from st where class=%s'%(k,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==3:
                        n=int(input('Enter id'))
                        n=find44(n)
                        cu.execute('select * from st where id="%s"'%(n,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==4:
                        cu.execute('select * from st')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==5:
                        ms=1
                    else:
                        ms=1
                        m=1
                        
            elif ch==3:
                ms=0
                while ms==0:
                    print('1.add teacher\n2.remove teacher\n3.change teacher\n4.change class teacher\n5.remove class teacher')
                    print('6.add class teacher\n7.Remove a class\n8.Add a Class \n9.Back\n10.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,10)
                    if ch in [1,2,3,4,5,6,7,8]:
                        x,y=find6() 
                    if ch==1:
                        k=int(input('Enter teacher id'))
                        cu.execute('')
            else:
                m=1
    elif ch==2:
        print('\t\t\t\tTEACHER LOGIN')
        wel={}
        m=find3('te')
        while m==1:
            m=find3('te')
        while m==0:
            print('1.View My Class\n2.View Classes\n3.Edit Marks\n4.Edit marks of a full division\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            
    else:
        print('\t\t\t\tADMIN LOGIN')
        '''m=find3('ad')
        while m==1:
            m=find3('ad')'''
        m=0
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
                        i=find2('te')
                        n=input("Enter the name").title()
                        dept=find4() 
                        dob=find7()
                        pas=input('Enter password')
                        s="insert into te values(%s,'%s','%s','%s','%s')"%(i,n,dept,dob,pas)
                        cu.execute(s)
                        con.commit()
                    elif ch==2:
                        i=find2('st')
                        n=input("Enter the name").title()
                        c=int(input('Enter the class'))
                        c=find1(c,1,12)
                        d=input('Enter the division')
                        d=d.upper()
                        dob=find7()
                        pas=input('Enter password')
                        s="insert into st values(%s,'%s',%s,'%s','%s','%s',%s,%s,%s,%s,%s)"%(i,n,c,d,dob,pas,0,0,0,0,0)
                        cu.execute(s)
                        con.commit()
                    elif ch==3:
                        i=find2('pr')
                        n=input("Enter the name").title()
                        dob=find7()
                        pas=input('Enter password')
                        s="insert into pr values(%s,'%s','%s','%s',)"%(i,n,dob,pas)
                        cu.execute(s)
                        con.commit()
                    elif ch==4:
                        ms=1
                        m=0
                    else:
                        ms=1
                        m=1
            elif ch==2:
                ms=0
                while ms==0:
                    print('1.Edit Student\n2.Edit Teacher\n3.Edit Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        nj=0
                        while nj==0:
                            print('1.Edit Name\n2.Date of birth')
                            print('3.Edit Class\n4.Edit Division\n5.Edit Mark\n6.Edit password\n7.Back\n8.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,8)
                            if ch in [1,2,3,4,5,6]:
                                x=int(input('Enter your id'))
 
                            if ch==1:
                                n=input('Enter new name')
                                cu.execute("update st set name='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==2:
                                n=find7()
                                cu.execute("update st set dob='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==3:
                                n=int(input('Enter new class'))
                                n=find1(n,1,12)
                                cu.execute("update st set class='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==4:
                                n=input('Enter new division')
                                cu.execute("update st set divi='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==5:
                                for i in dept:
                                    print('Enter',dept[i],'mark')
                                    n=int(input('enter new mark'))
                                    cu.execute("update st set %s='%s' where id=%s"%(dept[i],n,x))
                                    con.commit()
                                print('Edited Successfully')
                            elif ch==6:
                                n=input('Enter new password')
                                cu.execute("update st set pass='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==7:
                                nj=1
                                ms=0
                            else:
                                nj=1
                                ms=1
                                m=1
                    elif ch==2:
                        nj=0
                        while nj==0:
                            print('1.Edit Name\n2.Date of birth')
                            print('3.Edit Department\n4.Edit password\n5.Back\n6.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,6)
                            if ch in [1,2,3,4]:
                                x=int(input('Enter your id'))
                            if ch==1:
                                n=input('Enter new name')
                                cu.execute("update te set name='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==2:
                                n=find7()
                                cu.execute("update te set dob='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==3:
                                n=find4()
                                cu.execute("update te set dept='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==4:
                                n=input('Enter new password')
                                cu.execute("update te set pass='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==5:
                                nj=1
                                ms=0
                            else:
                                nj=1
                                ms=1
                                m=1
                    elif ch==3:
                        nj=0
                        while nj==0:
                            print('1.Edit Name\n2.Date of birth')
                            print('3.Edit password\n4.Back\n5.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,5)
                            if ch in [1,2,3]:
                                x=int(input('Enter your id'))
                            if ch==1:
                                n=input('Enter new name')
                                cu.execute("update pr set name='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==2:
                                n=find7()
                                cu.execute("update pr set dob='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==3:
                                n=input('Enter new password')
                                cu.execute("update pr set pass='%s' where id=%s"%(n,x))
                                con.commit()
                                print('Edited Successfully')
                            elif ch==5:
                                nj=1
                                ms=0
                            else:
                                nj=1
                                ms=1
                                m=1
                    elif ch==4:
                        ms=1
                    else:
                        ms=1
                        m=1
            elif ch==3:
                ms=0
                while ms==0:
                    print('1.Display all teachers\n2.Display all students\n3.Display Principal\n4.Display students of a class')
                    print('5.Display students of a division\n6.Display teachers of a department\n7.Display Students having birthday on a date')
                    print('8.View a Student\n9.Print Report Card\n10.Back\n11.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,11)
                    if ch==1:
                        cu.execute('select * from te')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==2:
                        cu.execute('select * from st')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==3:
                        cu.execute('select * from pr')
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==4:
                        k=int(input('Enter class'))
                        k=find1(k,1,12)
                        cu.execute('select * from st where class=%s'%(k,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==5:
                        k=int(input('Enter class'))
                        k=find1(k,1,12)
                        k1=input('Enter division')
                        k1=k1.upper()
                        cu.execute('select * from st where class=%s and divi="%s"'%(k,k1))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==6:
                        n=find4()
                        cu.execute('select * from te where dept="%s"'%(n,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==7:
                        n=find7()
                        cu.execute('select * from st where dob="%s"'%(n,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==8:
                        n=int(input('Enter id'))
                        n=find44(n)
                        cu.execute('select * from st where id="%s"'%(n,))
                        f=cu.fetchall()
                        for i in f:
                            print(i)
                    elif ch==9:
                        ans1 ='y'
                        while ans1=='y' or ans1=='Y':
                            print('1.Generate report card for 1\n2.Generate for whole class')
                            ch1=int(input('Enter your ch1oice'))
                            ch1=find1(ch1,1,2)
                            if ch1==1:
                                n=int(input('Enter id'))
                                cu.execute('select * from st where id="%s"'%(n,))
                                f=cu.fetchall()
                                for i in f:
                                    find12(i[0])
                            else:
                                cu.execute('select * from st')
                                f=cu.fetchall()
                                for i in f:
                                    find12(i[0])
                            ans1=input('Do You need to continue with report card')
                    elif ch==10:
                        ms=1
                    else:
                        ms=1
                        m=1
            elif ch==4:
                ms=0
                while ms==0:
                    print('1.Delete Student\n2.Delete Teacher\n3.Delete Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    k=int(input('enter id'))
                    if ch==1:
                        y='Delete from st where id=%s'%(k,)
                    elif ch==2:
                        y='Delete from te where id=%s'%(k,)
                    elif ch==3:
                        y='Delete from pr where id=%s'%(k,)
                    elif ch==4:
                        ms=1
                        
                    else:
                        ms=1
                        m=1
                    cu.execute(y)
                    con.commit()
                    print('Deleted Successfully')
            else:
                m=1
                
                        
