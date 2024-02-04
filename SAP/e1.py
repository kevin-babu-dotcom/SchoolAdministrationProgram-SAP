from datetime import date
import pickle,os
f1=open('te.dat','rb')
try:
    while True:
        l=pickle.load(f1)
        print(l)
except EOFError:
    f1.close()
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find2(x,y):
    a=1
    while a==1:
        f1=open(y,'rb')
        
        found=False
        try:
            while True:
                global l
                l=pickle.load(f1)
                if l['id']==x:
                    found=True
                    f1.close()
                    return x
        except EOFError:
            if found==False:
                print('INVALID id')
                x=int(input('Enter Your id'))
                a=1
        f1.close()
wel={}
def find3(xy):
    x=int(input('Enter your id'))
    x=find2(x,xy)
    wel[0]=x
    wel['Name']=l['Name']
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    while l['id']==x and l['DOB']==date(z,w,y):
        print('Login Successsful')
        return 0
    print('Invalid Credentials')
    return 1
def find4():
    dept={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTER SC'}
    print('1.English\n2.Chemistry\n3.Physics\n4.Mathematics\n5.Computer Science')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return dept[ch] 
def find5():
    gen={1:'Male',2:'Girl'}
    print('1.Male\n2.Female')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,5)
    return gen[ch]
def find6():
    con=1
    while con==1:
        x=int(input('Enter the class'))
        x=find1(x,1,12)
        y=input('Enter the division')
        y=y.upper()
        f=open('cd.dat','rb')
        j=str(x)+y
        try:
            while True:
                l=pickle.load(f)
                if j in l:
                    f.close()
                    return x,y
        except EOFError:
            f.close()
            print('INVALID Division')
            y=input('Enter the Division')
            y=y.upper()
            con=1
def find7():
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    return date(z,w,y)
kl=[]
def find8(x):
    f1=open(x,'ab+')
    f1.seek(0)
    
    try:
        while True:
            l=pickle.load(f1)
            
            kl.append(l['id'])
    except EOFError:
        f1.close()
    i=101
    while i in kl:
        i+=1
    kl.append(i)
    
    d['id']=i
    d['Name']=input("Enter the name").title()
    while len(d['Name'])<24:
        d['Name']+=' '*(24-len(d['Name']))
    d['f']=input("Enter father's name").title()
    d['m']=input("Enter mother's name").title()
    d['sex']=find5()
    d['ph1']=int(input('Enter your phone number'))
    d['Address']=input('Enter your current address')
    d['ph2']=int(input('Enter your another phone number'))
    d['Aadhar']=int(input('Enter your aadhar number'))
    d['Date_join']=date.today()
    d['DOB']=find7()
    f1=open(x,'ab')
    pickle.dump(d,f1)
    f1.close()
    kl.clear()
    print('Your id is ',i)
def find9(x,y):
    f1=open('temp.dat','ab')
    f=open(y,'rb+')
    try:
        while True:
            pos=f.tell()
            l=pickle.load(f)
            if l['id']==x and ch==1:
                l['Name']=input('Enter new name')
                l['Name']=l['Name'].title()
                while len(l['Name'])<24:
                    l['Name']+=' '*(24-len(l['Name']))
                
            elif l['id']==x and ch==2:
                l['Address']=input('Enter new address')
                
            elif l['id']==x and ch==3:
                l['sex']=find5()
              
            elif l['id']==x and ch==4:
                l['Aadhar']=int(input('Enter aadhar number'))
                
            elif l['id']==x and ch==5:
                
                print('Current phone number :',l['ph1'],'Press enter if ok')
                l['ph1']=int(input('Enter New phone number'))
                print('Current phone number :',l['ph2'],'Press enter if ok')
                l['ph2']=int(input('Enter New phone number'))
                
            elif l['id']==x and ch==6:
                l['DOB']=find7()
                
            else:
                pass
            pickle.dump(l,f1)
    except EOFError:
        f.close()
    f1.close()
    os.remove('st.dat')
    os.rename('temp.dat','st.dat')

def find12():
    def find13():
        m1=str(l['class'])+l['Div']
        f1=open('cd.dat','ab+')
        f1.seek(0)
        try:
            while True:
                j=pickle.load(f1)
                for i in j:
                    if i==m1:
                        g=j[i][0]
                        break
        except EOFError:
            f1.close()
        f1=open('te.dat','ab+')
        f1.seek(0)
        try:
            while True:
                jk=pickle.load(f1)
                if jk['id']==g:
                    return jk['Name']
        except EOFError:
            f1.close()        
    def find14(z):
        f=open('st.dat','rb')
        mz=l['mark'][z]
        
        try:
            while True:
                j=pickle.load(f)
                
                if str(l['class'])+l['Div']==str(j['class'])+j['Div'] and j['mark'][z]>mz:
                    mz=j['mark'][z]
        except EOFError:
            f.close()
            if len(str(mz))==1:
                return '0'+str(mz)
            else:
                return mz
    if None in l['mark'].values():
        print('Marks are NOT Entered Right Now')
        return
    x=sum(l['mark'].values())
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
    print('\t\t\t\tNAME    :',l['Name'])
    print('\t\t\t\tclass   :',l['class'])
    print('\t\t\t\tDivision:',l['Div'])
    print('\t\t\t\tRoll No :',25,'\t'*4,'FATHER        :',l['f'].title())
    print('\t\t\t\tAdm. NO :',l['id'],'\t'*4,'MOTHER        :',l['m'].title())
    print('\t\t\t\tDOB     :',l['DOB'],'\t'*3,'CLASS TEACHER :',find13())
    print('\t'*5,'_'*48,)
    print('\t'*5,'|      SUBJECTS','\t|','MAX.','\t','|SCORED  | TOP  |')
    print('\t'*5,'-'*46,'-|',sep='-')
    for i in l['mark']:
        print('\t'*5,'|','\t',i,'\t|',50,'\t |',l['mark'][i],'\t  |',find14(i),'  |')
    print('\t'*5,'-'*46,'-|',sep='-')
    
    print('\t'*5,'| TOTAL','\t'*2,'|',250,'\t |',x,' GRADE:',grade,'|')
    print('\t'*5,'-'*46,'-|',sep='-')
    from datetime import date
    print('\t'*5,'Place:','Anakkal')
    print('\t'*5,'Date :',date.today())
def find15():
    for i in l['mark']:
        print('  ',l['mark'][i],end='\t'*2)
ans='y'
wel={}
while ans=='y' or ans=='Y':
    print('\t\t\t\t\tLOGIN INTERFACE\n1.Principal\n2.Teacher\n3.Student\n4.Admin')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,4)
    if ch==1:
        print('\t\t\t\tPRINCIPAL LOGIN')
        m=find3('pr.dat')
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
                    f1=open('te.dat','rb')
                    f1.seek(0)
                    n=1
                    nn=0
                    try:
                        while True:
                            l=pickle.load(f1)
                            if ch==1:
                                x=int(input('Enter Teachers ID'))
                                x=find2(x,'te.dat')
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
                    f1=open('st.dat','rb')
                    f1.seek(0)
                    n=0
                    nn=0
                    try:
                        while True:
                            l=pickle.load(f1)
                            if ch==1:
                                if nn==0:
                                    x,y=find6()
                                    nn=1
                                if str(x)+y==str(l['class'])+l['Div']:
                                    print(l)
                                    n=1
                                
                            elif ch==2:
                                if nn==0:
                                    x=int(input('Enter class'))
                                    nn=1
                                if l['class']==x:
                                    print(l)
                                    n=1
                            elif ch==3:
                                if n==0:
                                    x=int(input('Enter Id'))
                                    x=find2(x,'st.dat')
                                    print(l)
                                    break
                            elif ch==4:
                                ms=1
                                n=1
                            elif ch==5:
                                n=1
                                ms=1
                                m=1
                                
                            else:
                                pass
                    except EOFError:
                        if n==0:
                            print('No Student FOUND')
                        f1.close()
            elif ch==3:
                ms=0
                while ms==0:
                    print('1.add teacher\n2.remove teacher\n3.change teacher\n4.change class teacher\n5.remove class teacher')
                    print('6.add class teacher\n7.Remove a class\n8.Add a Class \n9.Back\n10.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,10)
                    if ch in [1,2,3,4,5,6]:
                        k=int(input('Enter teacher id'))
                        k=find2(k,'te.dat')
                        print(l)
                        x,y=find6()
                        f=open('cd.dat','rb+')
                        f1=open('temp.dat','ab+')
                        n=1
                        try:
                            while True:
                                l=v=pickle.load(f)
                                for i in l:
                                    if ch==1:
                                        if i==str(x)+y:
                                            l[str(x)+y].append(k) #add teacher
                                            print('Added Successfully')
                                    elif ch==2:
                                        if i==(str(x)+y):
                                            if k in l[str(x)+y] and l[str(x)+y].index(k)==0:
                                                print('Unable to remove at the moment')
                                            elif k in l[str(x)+y] and l[str(x)+y].index(k)!=0:
                                                l[(str(x)+y)].remove(k)  #remove teacher
                                                print('Removed Successfully')
                                            else:
                                                print(k,'NOT In',(str(x)+y))
                                    elif ch==3:
                                        if i==str(x)+y:
                                            if k in l[str(x)+y] and l[str(x)+y].index(k)==0:
                                                print('Unable to remove at the moment')
                                            elif k in l[str(x)+y] and l[str(x)+y].index(k)!=0:
                                                mk=int(input('Enter the teacher you need to add'))
                                                mk=find2(mk,'te.dat')
                                                l=v
                                                l[(str(x)+y)].remove(k)
                                                l[str(x)+y].append(mk)
                                                print('Changed Successully')
                                            else:
                                                print(k,'NOT In',(str(x)+y)) #change teacher
                                    elif ch==4:
                                        if i==str(x)+y:
                                            if k in l[str(x)+y] and l[str(x)+y].index(k)!=0:
                                                print('Unable to remove at the moment')
                                            elif k in l[str(x)+y] and l[str(x)+y].index(k)==0:
                                                mk=int(input('Enter the teacher you need to add'))
                                                mk=find2(mk,'te.dat')
                                                l=v
                                                l[str(x)+y].remove(k) #change class teacher
                                                l[str(x)+y].insert(0,mk)
                                                print('Changed Successully')
                                            else:
                                                print(k,'NOT In',(str(x)+y))
                                    elif ch==5:
                                        if i==str(x)+y:
                                            if k in l[str(x)+y] and l[str(x)+y].index(k)!=0:
                                                print('Unable to remove at the moment')
                                            elif k in l[str(x)+y] and l[str(x)+y].index(k)==0:
                                                l[str(x)+y].remove(k) #remove class teacher
                                                print('Removed Successfully')
                                            else:
                                                print(k,'Not in',str(x)+y)
                                    elif ch==6:
                                        if i==str(x)+y: #add class teacher
                                            l[str(x)+y].insert(0,k)
                                            print('Added Successfully')
                                    else:
                                        pass
                                    pickle.dump(l,f1)
                                    
                        except EOFError:
                            pass
                        f.close()
                        f1.close()
                        os.remove('cd.dat')
                        os.rename('temp.dat','cd.dat')
                    elif ch in [7,8]:
                        j='cd.dat'
                        fh=open(j,'ab+')
                        pos=fh.tell()
                        f1=open('tem.dat','ab+')
                        fh.seek(0)
                        kk=0
                        m2=1
                        found=True
                        try:
                            while True:
                                l=pickle.load(fh)
                                for i in l:
                                    if ch==7:
                                        if m2==1:
                                            x,y=find6()
                                            m2=0
                                        if i==str(x)+y:
                                            found=False
                                            print('DELETED Successfully')
                                            continue
                                        else:
                                            pickle.dump(l,f1)
                                    if ch==8:
                                        if m2==1:
                                            x=int(input('Enter the class'))
                                            x=find1(x,1,12)
                                            y=input('Enter the division')
                                            y=y.upper()
                                            m2=0
                                            found=False
                                        pickle.dump(l,f1)
                                        if str(x)+y in l:
                                            kk=1
                                            print(str(x)+y,'Already Exist')
                        except EOFError:
                            if ch==8 and kk==0:
                                d={}
                                d[str(x)+y]=[]
                                print('ADDED Successfully')
                                pickle.dump(d,f1)
                            if found==True:
                                print('Account NOT Found')
                            fh.close()
                        f1.close()
                        os.remove(j)
                        os.rename('tem.dat',j)
                    elif ch==9:
                        ms=1
                    else:
                        ms=1
                        m=1
            else:
                m=1
    elif ch==2:
        print('\t\t\t\tTEACHER LOGIN')
        wel={}
        m=find3('te.dat')
        while m==1:
            m=find3('te.dat')
        while m==0:
            print('1.View My Class\n2.View Classes\n3.Edit Marks\n4.Edit marks of a full division\n5.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,5)
            f=open('te.dat','rb')
            try:
                while True:
                    l=pickle.load(f)
                    if wel[0]==l['id']:
                        wel['Name']=l['Name']
                        wel['Dept']=l['Dept']
                        print('Welcome',l['Name'])
                        break
            except EOFError:
                f.close()
            if ch==1:
                jj=0
                while jj==0:
                    print('1.View a student\n2.View Marks\n3.Print report card\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    f=open('cd.dat','rb')
                    try:
                        n=1
                        while True and n==1:
                            l=pickle.load(f)
                            for i in l:
                                if len(l[i])!=0 and wel[0]==l[i][0]:
                                    x=i
                                    n=2
                    except EOFError:
                        f.close()
                    if ch==1:
                        n=1
                        k=int(input('Enter id'))
                        k=find2(k,'st.dat')
                        if str(l['class'])+l['Div']==x:
                            for i in l:
                                print(i,l[i],sep=':')
                                n+=1
                            if n>2:
                                jj=0
                            else:
                                f1=open('te.dat','ab+')
                                f1.seek(0)
                                try:
                                    while True:
                                        l=pickle.load(f1)
                                        if l['id']==wel[0]:
                                            print('Sorry Mr.',l['Name'].rstrip(),'you Have NO ACCESS to data')
                                            break
                                except EOFError:
                                    f1.close()
                    elif ch==2:
                        print('admno\tName\t\tChemistry\tPhysics\t\tComputer Sci\tMathematcs\tEnglish')
                        f=open('st.dat','rb')
                        n=1
                        try:
                            while True:
                                l=pickle.load(f)
                                if str(l['class'])+l['Div']==x:
                                    if n==1:
                                        print('admno\tName\t\tChemistry\tPhysics\t\tComputer Sci\tMathematcs\tEnglish')
                                        n+=1
                                    print(l['id'],l['Name'].rstrip(),sep='\t',end='\t')
                                    find15()
                                    print()
                        except EOFError:
                            if n==1:
                                print('No Student in this class')
                            f.close()
                    elif ch==3:
                        ans='y'
                        while ans=='y' or ans=='Y':
                            print('1.Generate report card for 1\n2.Generate for whole class')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,2)
                            if ch==1:
                                k=int(input('Enter id'))
                                k=find2(k,'st.dat')
                                f=open('st.dat','rb')
                                try:
                                    while True:
                                        l=pickle.load(f)
                                        if l['id']==k and str(l['class'])+l['Div']==x:
                                           find12()
                                           break
                                except EOFError:
                                    print('Sorry you have no access')
                                    f.close()
                            else:
                                f=open('st.dat','rb')
                                try:
                                    while True:
                                        l=pickle.load(f)
                                        if str(l['class'])+l['Div']==x:
                                            find12()
                                except EOFError:
                                    f.close()
                            ans1=input('Do you need to continue with report card(y/n)')
                    elif ch==4:
                        jj=1
                    else:   
                      m=1
            elif ch==2:
                n=1
                lo={}
                f=open('cd.dat','rb')
                try:
                    while True:
                        l=pickle.load(f)
                        for i in l:
                            if len(l[i])!=0 and wel[0] in l[i]:
                                x=i
                                print(n,i,sep='.')
                                lo[n]=i
                                n+=1
                except EOFError:
                    f.close()

                k=int(input('Enter choice'))
                while k not in lo:
                    print('INVALID Choice')
                    k=int(input('Enter choice'))
                n=1 
                f=open('st.dat','rb')
                try:
                    while True:
                        l=pickle.load(f)
                        if (str(l['class'])+l['Div'])==lo[k]:
                            if n==1:
                                print('Adm.n\t    Name\t\t',wel['Dept'],'Mark')
                                n+=1
                            print(l['id'],l['Name'].strip(),'\t  ',l['mark'][wel['Dept']],sep='\t')
                except EOFError:
                    if n==1:
                        print('NO student in Class')
                    f.close()
            elif ch==3:
                an='y'
                while an=='y' or an=='Y':
                    km='y'
                    while km=='y' or km=='y':
                        n=1
                        lo={}
                        f=open('cd.dat','rb')
                        try:
                            while True:
                                l=pickle.load(f)
                                for i in l:
                                    if len(l[i])!=0 and wel[0] in l[i]:
                                        x=i
                                        print(n,i,sep='.')
                                        lo[n]=i
                                        n+=1
                        except EOFError:
                            f.close()
                        k=int(input('Enter choice'))
                        while k not in lo:
                            print('INVALID Choice')
                            k=int(input('Enter choice'))
                        mh='y'
                        while mh=='Y' or mh=='y':
                            print('ok')
                            n=1
                            lm={}
                            f=open('st.dat','rb')
                            try:
                                while True:
                                    l=pickle.load(f)
                                    if (str(l['class'])+l['Div'])==lo[k]:
                                        print(n,l['Name'],sep='.')
                                        lm[n]=l
                                        n+=1
                            except EOFError:
                                f.close()
                            if len(lm)==0:
                                print('No student in class')
                            else:
                                kk=int(input('Enter choice'))
                                while kk not in lm:
                                    print('INVALID Choice')
                                    kk=int(input('Enter choice'))
                                f=open('st.dat','rb+')
                                try:
                                    while True:
                                        pos=f.tell()
                                        l=pickle.load(f)
                                        if l['id']==lm[kk]['id']:
                                            l['mark'][wel['Dept']]=int(input('Enter Mark'))
                                            f.seek(pos)
                                            pickle.dump(l,f)
                                            f.seek(pos)
                                            print(l)
                                            break
                                except EOFError:
                                    f.close()
                            mh=input('Do you want to continue with same class(y/n)')
                        km=input('Do you want to change class(y/n)')
                    an=input('Do you want to go BACK(y/n)')
            elif ch==4:
                ans1='y'
                while ans1=='y' or ans1=='Y':
                    km='y'
                    while km=='y' or km=='y':
                        n=1
                        lo={}
                        f=open('cd.dat','rb')
                        try:
                            while True:
                                l=pickle.load(f)
                                for i in l:
                                    if len(l[i])!=0 and wel[0] in l[i]:
                                        x=i
                                        print(n,i,sep='.')
                                        lo[n]=i
                                        n+=1
                        except EOFError:
                            f.close()
                        k=int(input('Enter choice'))
                        while k not in lo:
                            print('INVALID Choice')
                            k=int(input('Enter choice'))
                        mh='y'
                        while mh=='Y' or mh=='y':
                            
                            n=1
                            lm={}
                            f=open('st.dat','rb')
                            try:
                                while True:
                                    l=pickle.load(f)
                                    if (str(l['class'])+l['Div'])==lo[k]:
                                        print(n,l['Name'],sep='.')
                                        lm[n]=l
                                        n+=1
                            except EOFError:
                                f.close()
                            if len(lm)==1:
                                print('No student in class')
                            else:
                                f=open('st.dat','rb+')
                                n=1
                                try:
                                    while True and n==1:
                                        pos=f.tell()
                                        l=pickle.load(f)
                                        for i in lm:
                                            print(lm[i]['id'],l['id'])
                                            if lm[i]['id']==l['id']:
                                                print(i,lm[i]['Name'],sep='.')
                                                print('Press 0 to Stop')
                                                kg=int(input('Enter Mark'))
                                                if kg==0:
                                                    n=0
                                                else:
                                                    l['mark'][wel['Dept']]=kg
                                                    f.seek(pos)
                                                    pickle.dump(l,f)
                                                    break
                                except EOFError:
                                    f.close()
                            mh=input('Do you want to continue with same class(y/n)')
                        km=input('Do you want to change class(y/n)')
                    ans1=input('Do you want to go BACK(y/n)')
            else:
                m=1
    elif ch==3:
        print('\t\t\t\tSTUDENT LOGIN')
        m=find3('st.dat')
        while m==1:
            m=find3('st.dat')
        while m==0:
            print('1.View my Class and Div\n2.View Report Card\n3.View my Details\n4.View fee details')
            print('5.View class teacher\n6.View Other teachers\n7.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,7)
            f1=open('st.dat','ab+')
            f1.seek(0)
            try:
                while True:
                    l=pickle.load(f1)
                    if l['id']==wel[0]:
                        break
            except EOFError:
                f1.close()
            if ch==1:
                print('Class :',l['class'])
                print('Division :',l['Div'])
            elif ch==2:
                find12()
            elif ch==3:
                for i in l:
                    print(i,l[i],sep=':')
            elif ch==4:
                print('paid')
            elif ch==5 or ch==6:
                f1=open('cd.dat','ab+')
                f1.seek(0)
                try:
                    while True:
                        j=pickle.load(f1)
                        for i in j:
                            if i==str(l['class'])+l['Div']:
                                f2=open('te.dat','ab+')
                                f2.seek(0)
                                try:
                                    while True:
                                        jj=pickle.load(f2)
                                        if ch==5:
                                            if len(j[i])!=0 and j[i][0]==jj['id']:
                                                print('Class Teacher:',jj['Name'].strip(),'    Phone number',jj['ph1'])
                                                f2.close()
                                                break
                                        if ch==6:
                                            if len(j[i])!=0 and jj['id'] in j[i]:
                                                print('Teacher:',jj['Name'].strip(),'    Phone number',jj['ph1'])
                                except EOFError:
                                    f2.close()
                except EOFError:
                    f1.close()
            else:
                m=1
    else:
        print('\t\t\t\tADMIN LOGIN')
        m=find3('ad.dat')
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
                        d={}
                        d['Dept']=find4()   
                        find8('te.dat')
                        f2=open('te.dat','rb')
                        try:
                            while True:
                                l=pickle.load(f2)
                                print(l)
                        except EOFError:
                            f2.close()
                    elif ch==2:
                        d={}
                        d['class'],d['Div']=find6()
                        if d['class']<10:
                            d['class']='0'+str(d['class'])
                            d['class']=int(d['class'])
                        d['mark']={'CHEMISTRY':None ,
                                   'PHYSICS':None,
                                   'COMPUTER SC':None,
                                   'MATHEMATICS':None,
                                   'ENGLISH':None}
                        find8('st.dat')
                        f2=open('st.dat','rb')
                        try:
                            while True:
                                l=pickle.load(f2)
                                print(l)
                        except EOFError:
                            f2.close()
                    elif ch==3:
                        d={}
                        find8('pr.dat')
                        f2=open('pr.dat','rb')
                        try:
                            while True:
                                l=pickle.load(f2)
                                print(l)
                        except EOFError:
                            f2.close()
                    elif ch==4:
                        ms=1
                        m=0
                    else:
                        ms=1
                        m=1
            elif ch==2:
                x=int(input('Enter your id'))
                x=find2(x,'st.dat')
                nj=0
                while nj==0:
                    print('1.Edit Name\n2.Edit Address\n3.Edit gender\n4.Edit Aadhar\n5.edit phone number\n6.Date of birth')
                    print('7.Edit class and div\n8.Edit Mark\n9.Back\n10.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,10)
                    while ch in [1,2,3,4,5,6]:
                        find9(x,'st.dat')
                        break
                    f=open('st.dat','rb')
                    f1=open('temp.dat','ab')
                    try:
                        while True:
                            
                            l=pickle.load(f)
                            if l['id']==x and ch==7:
                                l['class'],l['Div']=find6()
                            elif  l['id']==x and ch==8:
                                l['mark']={'CHEMISTRY':int(input('Enter CHEMISTRY Mark')),
                                           'PHYSICS':int(input('Enter PHYSICS Mark')),
                                           'COMPUTER SC':int(input('Enter COMPUTER SCIENCE Mark')),
                                           'MATHEMATICS':int(input('Enter MATHEMATICS Mark')),
                                           'ENGLISH':int(input('Enter ENGLISH Mark'))}
                                
                            elif ch==9 and l['id']==x:
                                nj=1
                            elif ch==10 and l['id']==x:
                                nj=1 
                                m=1
                                break
                            else:
                                pass
                            pickle.dump(l,f1)
                    except EOFError:
                        pass
                    f.close()
                    f1.close()
                    os.remove('st.dat')
                    os.rename('temp.dat','st.dat')
            elif ch==3:
                mn=1
                while mn==1:
                    print('1.Display all teachers\n2.Display all students\n3.Display Principal\n4.Display students of a class')
                    print('5.Display students of a division\n6.Display teachers of a department\n7.Display Students having birthday on a date')
                    print('8.View a Student\n9.Print Report Card\n10.Back\n11.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,11)
                    if ch in [1,6]:
                        f=open('te.dat','rb')
                        f.seek(0)
                        n=1
                        try:
                            while True:
                                l=pickle.load(f)
                                if ch==1:
                                    print(l)
                                elif ch==6:
                                    if n==1:
                                        x=find4()
                                        n=0
                                    if l['Dept']==x:
                                        print(l)
                                else:
                                    pass
                        except EOFError:
                            f.close()
                    elif ch in [2,4,5,7,8,9]:
                        f=open('st.dat','rb+')
                        f.seek(0)
                        n=1
                        try:
                            while True:
                                l=pickle.load(f)
                                if ch==2:
                                    print(l)
                                elif ch==4:
                                    if n==1:
                                        x=int(input('Enter class'))
                                        x=find1(x,1,12)
                                        n=0
                                    if l['class']==x:
                                        print(l)
                                elif ch==5:
                                    if n==1:
                                        x,y=find6()
                                        j=str(x)+y
                                        n=0
                                    if str(l['class'])+l['Div']==j:
                                        print(l)
                                elif ch==7:
                                    if n==1:
                                        x=find7()
                                        n=0
                                    if l['DOB']==x:
                                        print(l)
                                elif ch==8:
                                    if n==1:
                                        x=int(input('Enter the student id'))
                                        n=0
                                    if l['id']==x:
                                        print(l)
                                elif ch==9:
                                    ans1 ='y'
                                    while ans1=='y' or ans1=='Y':
                                        print('1.Generate report card for 1\n2.Generate for whole class')
                                        ch1=int(input('Enter your ch1oice'))
                                        ch1=find1(ch1,1,2)
                                        if ch1==1:
                                            k=int(input('Enter id'))
                                            k=find2(k,'st.dat')
                                            f2=open('st.dat','rb')
                                            try:
                                                while True:
                                                    l=pickle.load(f2)
                                                    if l['id']==k:
                                                       find12()
                                                       break
                                            except EOFError:
                                                f2.close()
                                        else:
                                            f1=open('st.dat','rb')
                                            try:
                                                while True:
                                                    l=pickle.load(f1)
                                                    find12()
                                            except EOFError:
                                                f1.close()
                                        ans1=input('Do you need to continue with report card(y/n)')
                                    n=0
                                else:
                                    pass
                        except EOFError:
                            if n==1:
                                print('Account not Found')
                            f.close()
                    elif ch==3:
                        f=open('pr.dat','rb')
                        f.seek(0)
                        n=1
                        try:
                            while True:
                                if ch==3:
                                    l=pickle.load(f)
                                    print(l)
                        except EOFError:
                            f.close()
                    elif ch==10:
                        mn=0
                        break
                    else:
                        n=0
                        mn=0
                        m=1
            elif ch==4:
                kl=0
                while kl==0:
                    print('1.Delete Student\n2.Delete Teacher\n3.Delete Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        y='st.dat'
                    elif ch==2:
                        y='te.dat'
                    elif ch==3:
                        y='pr.dat'
                    elif ch==4:
                        m=0
                        kl=1
                    else:
                        kl=1
                    if ch in [1,2,3]:
                        fh=open(y,'ab+')
                        f1=open('tem.dat','ab+')
                        fh.seek(0)
                        n=int(input('Enter id'))
                        found=True
                        try:
                            while True:
                                l=pickle.load(fh)
                                if l['id']==n:
                                    found=False
                                    print('DELETED Successfully')
                                    continue
                                else:
                                    pickle.dump(l,f1)
                        except EOFError:
                            if found==True:
                                print('Account NOT Found')
                            fh.close()
                        f1.close()
                        os.remove(y)
                        os.rename('tem.dat',y)
            else:
                m=1
