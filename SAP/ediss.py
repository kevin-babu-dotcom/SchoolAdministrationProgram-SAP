from datetime import date
import pickle
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find2(x,y):
    while x not in y:
        print('Invalid ID')
        x=int(input('Enter your id'))
    return x
def find3(xy):
    x=int(input('Enter your id'))
    x=find2(x,xy)
    wel[0]=x
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    while xy[x]==date(z,w,y):
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
    x=int(input('Enter the class'))
    while x not in nn:
        print('invalid class(1-12)')
        x=int(input('Enter the class'))
    y=input('Enter the division')
    y=y.upper()
    while y not in nn[x]:
        print('Invalid Division. Divisions:',nn[x])
        y=input('Enter the Division')
        y=y.upper()
    return x,y
def find7():
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    return date(z,w,y)
def find8(x,y):
    d['Name']=input("Enter the name")
    d['Name']=d['Name'].title()
    while len(d['Name'])<24:
        d['Name']+=' '*(24-len(d['Name']))
    d['f']=input("Enter father's name").capitalize()
    d['m']=input("Enter mother's name").capitalize()
    d['sex']=find5()
    d['ph1']=int(input('Enter your phone number'))
    d['Address']=input('Enter your current address')
    d['ph2']=int(input('Enter your another phone number'))
    d['Aadhar']=int(input('Enter your aadhar number'))
    d['Date_join']=date.today()
    d['DOB']=find7()
    l=[]
    for i in range(101,150):
        if i in x:
            pass
        else:
            x[i]=d
            y[i]=d['DOB']
            break
def find9(x,y):
    if ch==1:
        y[x]['Name']=input('Enter New name')
        y[x]['Name']=y[x]['Name'].title()
        while len(y[x]['Name'])<24:
            y[x]['Name']+=' '*(24-len(y[x]['Name']))
    elif ch==2:
        y[x]['Address']=input('Enter New Address')
    elif ch==3:
        y[x]['sex']=find5()
    elif ch==4:
        y[x]['Aadhar']=int(input('Enter aadhar number'))
    elif ch==5:
        print('Current phone number :',y[x]['ph1'],'press enter if ok')
        y[x]['ph1']=int(input('Enter New phone number'))
        print('Current phone number :',y[x]['ph2'],'press enter if ok')
        y[x]['ph2']=int(input('Enter New phone number'))
    elif ch==6:
        y[x]['DOB']=find7()
def find10(y):
    x=int(input('Enter  id'))
    x=find2(x,y)
    m=input(upper('Are you sure you need to delete?(y/n)'))
    if m=='y' or m=='Y':
        del y[x]
        print('Deleted Successfully')
    else:
        print('Ok')
def find11():
    x=int(input('Enter class'))
    while x not in nn:
        x=int(input('Enter class'))
    y=input('Enter division')
    y=y.upper()
    while y not in nn[x]:
        print('Invalid division')
        y=input('Enter division')
        y=y.upper()
    for i in stud:
        if stud[i]['class']==x and stud[i]['Div']==y:
            print(i,stud[i],sep=':')
def find12(y):
    x=sum(stud[y]['mark'].values())
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
    print('\t\t\t\tNAME    :',stud[y]['Name'])
    print('\t\t\t\tclass   :',stud[y]['class'])
    print('\t\t\t\tDivision:',stud[y]['Div'])
    print('\t\t\t\tRoll No :',25,'\t'*4,'FATHER        :',stud[y]['f'].capitalize())
    print('\t\t\t\tAdm. NO :',y,'\t'*4,'MOTHER        :',stud[y]['m'].capitalize())
    print('\t\t\t\tDOB     :',stud[y]['DOB'],'\t'*3,'CLASS TEACHER :',find13(y,stud))
    print('\t'*5,'_'*48,)
    print('\t'*5,'|      SUBJECTS','\t|','MAX.','\t','|SCORED   ','|TOP |')
    print('\t'*5,'-'*46,'-|',sep='-')
    for i in stud[y]['mark']:
        print('\t'*5,'|','\t',i,'\t|',50,'\t |',stud[y]['mark'][i],'\t  |',find14(y,i),'  |')
    print('\t'*5,'-'*46,'-|',sep='-')
    #print()
    print('\t'*5,'| TOTAL','\t'*2,'|',250,'\t |',x,' GRADE:',grade,'|')
    print('\t'*5,'-'*46,'-|',sep='-')
    #print('\t'*4,'-'*52)
    from datetime import date
    print('\t'*5,'Place:','Anakkal')
    print('\t'*5,'Date :',date.today())
def find13(x,y):
    m=str(y[x]['class'])+y[x]['Div']
    for i in ct:
        if i==m:
            return teach[ct[i]]['Name']
def find14(y,z):
    mz=stud[y]['mark'][z]
    for i in stud:
        for j in stud:
            if stud[i]['mark'][z]>stud[j]['mark'][z]:
                mz=stud[i]['mark'][z]
    return mz
    def find15():
        for i in stud[j]['mark']:
            print('  ',stud[j]['mark'][i],end='\t'*2)
wel={}
teach={101: {'Dept': 'MATHEMATICS', 'Name': 'Sajan Sebastion         ', 'f': 'Sebastion', 'm': 'Parvathy', 'sex': 'Male', 'ph1': 999, 'Address': '999', 'ph2': 999, 'Aadhar': 999, 'Date_join': date(2022, 10, 12), 'DOB': date(1990, 10, 11)},
       102: {'Dept': 'COMPUTER SCIENCE', 'Name': 'Justine Cyriac          ', 'f': 'Cyriac', 'm': 'Maria', 'sex': 'Male', 'ph1': 999, 'Address': '999', 'ph2': 999, 'Aadhar': 999, 'Date_join': date(2022, 10, 12), 'DOB': date(1989, 10, 12)},
       103: {'Dept': 'CHEMISTRY', 'Name': 'Annie Luke              ', 'f': 'Luka', 'm': 'Annamma', 'sex': 'Girl', 'ph1': 999, 'Address': '999', 'ph2': 999, 'Aadhar': 999, 'Date_join': date(2022, 10, 12), 'DOB': date(1999, 5, 23)},
       }

stud={101:{'class': 1, 'Div': 'A', 'mark': {'CHEMISTRY': 42, 'PHYSICS': 37, 'COMPUTER SC': 32, 'MATHEMATICS': 40, 'ENGLISH': 45}, 'Name': 'Rohitha Sony            ', 'f':'Sony P john', 'm': 'Mini Sony', 'sex': 'Girl', 'ph1': 9847189897, 'Address': 'PARAKULANGARA', 'ph2': 9656003055, 'Aadhar': 123123123123, 'Date_join': date(2022, 10, 9), 'DOB': date(2010, 7, 23)},
      103:{'class': 12, 'Div': 'E', 'mark': {'CHEMISTRY': 40, 'PHYSICS': 42, 'COMPUTER SC': 40, 'MATHEMATICS': 45, 'ENGLISH': 37}, 'Name': 'Rohan Sony              ', 'f': 'Sony p john', 'm': 'Mini sony', 'sex': 'Male', 'ph1': 99, 'Address': '00', 'ph2': 0, 'Aadhar': 88, 'Date_join': date(2022, 10, 12), 'DOB': date(2005, 1, 3)},
      }


prin={}
ll={'1A': [102,103], '1B': [], '1C': [], '1D': [], '1E': [], '1F': [],
        '2A': [], '2B': [], '2C': [], '2D': [], '2E': [], '2F': [],
        '3A': [], '3B': [], '3C': [], '3D': [], '3E': [], '3F': [],
        '4A': [], '4B': [], '4C': [], '4D': [], '4E': [], '4F': [],
        '5A': [], '5B': [], '5C': [], '5D': [], '5E': [], '5F': [],
        '6A': [], '6B': [], '6C': [], '6D': [], '6E': [], '6F': [],
        '7A': [], '7B': [], '7C': [], '7D': [], '7E': [], '7F': [],
        '8A': [], '8B': [], '8C': [], '8D': [], '8E': [], '8F': [],
        '9A': [], '9B': [], '9C': [], '9D': [], '9E': [], '9F': [],
        '10A': [], '10B': [], '10C': [], '10D': [], '10E': [], '10F': [],
        '11A': [], '11B': [], '11C': [], '11D': [], '11E': [], '11F': [],
        '12A': [101,102,103], '12B': [101,102,103], '12C': [], '12D': [], '12E': [101,102,103], '12F': [101,102,103]}

fee={1:{1:1000,2:1500,3:1000},2:{1:1000,2:1500,3:2000}}    
nn={1:['A','B','C','D','E','F'],
    2:['A','B','C','D','E','F'],
    3:['A','B','C','D','E','F'],
    4:['A','B','C','D','E','F'],
    5:['A','B','C','D','E','F'],
    6:['A','B','C','D','E','F'],
    7:['A','B','C','D','E','F'],
    8:['A','B','C','D','E','F'],
    9:['A','B','C','D','E','F'],
    10:['A','B','C','D','E','F'],
    11:['A','B','C','D','E','F'],
    12:['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R']}
ct={'1A':102,'12A':102,'12B': None,'12E':101,'12L':103}
p={101: date(2005, 1, 3), 102: date(2005,2,7),}
t={101: date(2005, 1, 3), 102: date(2005,2,7),}
s={101: date(2005, 1, 3), 102: date(2005,2,7),}
a={101: date(2005, 1, 3), 102: date(2005,2,7),}
ans='y'
while ans=='y' or ans=='Y':
    
    print('\t\t\t\t\tLOGIN INTERFACE\n1.Principal\n2.Teacher\n3.Student\n4.Admin')
    ch=int(input('Enter your choice'))
    ch=find1(ch,1,4)
    if ch==1:
        print('\t\t\t\tPRINCIPAL LOGIN')
        #m=find3(p)
        #while m==1:
            #m=find3(p)
        #while m==0:
        m=1
        while m:
            print('1.View teacher\n2.View student\n3.Logout\n4.Data control')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,4)
            if ch==4:
                print('Assign class')
                k=int(input('Enter teacher id'))
                k=find2(k,teach)
                print('ok')
                x,y=find6()
                print('ok')
                ll[str(x)+y].append(k)
                print(ll)
            if ch==1:
                print('1.View Teacher\n2.View Department\n3.View teachers\n4.Back\n5.Logout')
                ch=int(input('Enter your choice'))
                ch=find1(ch,1,5)
                if ch==1:
                    x=int(input('Enter Teachers ID'))
                    x=find2(x,teach)
                    print(x,teach[x],sep=':')
                elif ch==2:
                    x=find4()
                    for i in teach:
                        if teach[i]['Dept']==x:
                            print(i,teach[x],sep=':')
                elif ch==3:
                    for i in teach:
                        print(i,teach[i],sep=':')
                elif ch==4:
                    m=0
                else:
                    m=1
            elif ch==2:
                print('1.View Division\n2.View Class\n3.View Student\n4.Back\n5.Logout')
                ch=int(input('Enter your choice'))
                ch=find1(ch,1,5)
                if ch==1:
                    find11()
                elif ch==2:
                    x=int(input('Enter class'))
                    while x not in nn:
                        x=int(input('Enter class'))
                    for i in stud:
                        if stud[i]['class']==x:
                            print(i,stud[i],sep=':')
                elif ch==3:
                    x=int(input('Enter Id'))
                    x=find2(x,stud)
                    print(x,stud[x],sep=':')
                elif ch==4:
                    m=0
                else:
                    m=1
            else:
                m=1
                    

    elif ch==2:
        print('\t\t\t\tTEACHER LOGIN')
        wel={}
        m=find3(t)
        for i in ct:
            if ct[i]==wel[0]:
                x=i
        while m==1:
            m=find3(t)
        m=0
        #wel[0]=find2(int(input('Enter id')),teach)
        while m==0:
            print('1.View My Class\n2.View Classes\n3.Edit Marks\n4.Logout')
            ch=int(input('Enter your choice'))
            ch=find1(ch,1,4)
            if ch==1:
                print('Welcome',teach[wel[0]]['Name'])
                jj=0
                while jj==0:
                    print('1.View a student\n2.View Marks\n3.Print report card\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        for i in ct:
                            if ct[i]==wel[0]:
                                x=i
                                k=int(input('Enter id'))
                                k=find2(k,stud)
                                if str(stud[k]['class'])+stud[k]['Div']==x:
                                    for i in stud[k]:
                                        print(i,stud[k][i],sep=':')
                                    break
                        else:
                            print('Sorry Mr.',teach[wel[0]]['Name'].rstrip(),'you Have NO ACCESS to data')
                    elif ch==2:
                        print('admno\tName\t\tChemistry\tPhysics\t\tComputer Sci\tMathematcs\tEnglish')
                        for i in ct:
                            if ct[i]==wel[0]:
                                x=i
                                for j in stud:
                                    if str(stud[j]['class'])+stud[j]['Div']==x:
                                        print(j,stud[j]['Name'].rstrip(),sep='\t',end='\t')
                                        find15()
                                        print()
                    elif ch==3:
                        ans='y'
                        while ans=='y' or ans=='Y':
                            print('1.Generate report card for 1\n2.Generate for whole class')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,2)
                            if ch==1:
                                k=int(input('Enter id'))
                                k=find2(k,stud)
                                if str(stud[k]['class'])+stud[k]['Div']==x:
                                   find12(k)
                                else:
                                    print('Sorry you have no access')
                            else:
                                for i in stud:
                                    if str(stud[i]['class'])+stud[i]['Div']==x:
                                        find12(i)
                            ans=input('Do you neeed to continue with report card(y/n)')
                        
                    elif ch==4:
                        jj=1
                        m=0
                    else:
                        m=1
                        break
            elif ch==2:
                n=1
                lo={}
                for i in ll:
                    if wel[0] in ll[i]:
                        print(n,i,sep='.')
                        lo[n]=i
                        n+=1
                k=int(input('Enter choice'))
                k=find2(k,lo)
                print('Adm.n\t    Name\t\t',teach[wel[0]]['Dept'],'Mark')
                for j in stud:
                    if (str(stud[j]['class'])+stud[j]['Div'])==lo[k]:
                        print(j,stud[j]['Name'].strip(),'\t  ',stud[j]['mark'][teach[wel[0]]['Dept']],sep='\t')
            elif ch==3:
                ans='y'
                while ans=='y' or ans=='Y':
                    km='y'
                    while km=='y' or km=='y':
                        n=1
                        lo={}
                        for i in ll:
                            if wel[0] in ll[i]:
                                print(n,i,sep='.')
                                lo[n]=i
                                n+=1
                        k=int(input('Enter choice'))
                        k=find2(k,lo)
                        mh='y'
                        while mh=='Y' or mh=='y':
                            print('ok')
                            n=1
                            lm={}
                            for i in stud:
                                if (str(stud[i]['class'])+stud[i]['Div'])==lo[k]:
                                    print(n,stud[i]['Name'],sep='.')
                                    lm[n]=i
                                    n+=1
                            if len(lm)==0:
                                print('No student in class')
                            else:
                                kk=int(input('Enter choice'))
                                kk=find2(kk,lm)
                                stud[lm[kk]]['mark'][teach[wel[0]]['Dept']]=int(input('Enter Mark'))
                            mh=input('Do you want to continue with same class(y/n)')
                        km=input('Do you want to change class(y/n)')
                    ans=input('Do you want to go BACK(y/n)')
                
            elif ch==4:
                m=0
                break
                
            else:
                m=1
                print('ok_')
                
                    
    else:
        print('\t\t\t\tADMIN LOGIN')
        m=find3(a)
        while m==1:
            m=find3(a)
        while m==0:
                print('1.Add\n2.Edit\n3.Display\n4.Delete')
                ch=int(input('Enter your choice'))
                ch=find1(ch,1,4)
                if ch==1:
                    print('1.Add New Teacher\n2.Add New Student\n3.Add New Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,5)
                    if ch==1:
                        d={}
                        d['Dept']=find4()   
                        find8(teach,t)
                    elif ch==2:
                        d={}
                        #int(input('Enter CHEMISTRY Mark'))
                        #int(input('Enter PHYSICS Mark'))
                        #int(input('Enter COMPUTER SCIENCE Mark'))
                        #int(input('Enter MATHEMATICS Mark'))
                        #int(input('Enter ENGLISH Mark'))
                        d['class'],d['Div']=find6()
                        if d['class']<10:
                            d['class']='0'+str(d['class'])
                            d['class']=int(d['class'])
                        d['mark']={'CHEMISTRY':None ,
                                   'PHYSICS':None,
                                   'COMPUTER SC':None,
                                   'MATHEMATICS':None,
                                   'ENGLISH':None}
                        find8(stud,s)
                    elif ch==3:
                        d={}
                        find8(prin,p)
                    elif ch==4:
                        nm=1
                        
                    else:
                        m=1
                        break
                elif ch==2:
                    mn=1
                    while mn==1:
                        print('1.Edit Teacher\n2.Edit Student\n3.Edit Principal\n4.Back\n5.Logout')
                        ch=int(input('Enter your choice'))
                        ch=find1(ch,1,5)
                        
                        if ch==1:
                            x=int(input('Enter you id'))
                            x=find2(x,teach)
                            print('1.Edit Name\n2.Edit Address\n3.Edit gender\n4.Edit Aadhar\n5.edit phone number\n6.Date of birth\n7.Edit Deaprtment\n8.Back\n9.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,9)
                            while ch in [1,2,3,4,5,6]:
                                find9(x,teach)
                            if ch==7:
                                teach[x]['Dept']=find4()
                            elif ch==8:
                                nm=1
                            else:
                                m=1
                                nm=0
                                break
                        elif ch==2:
                            x=int(input('Enter you id'))
                            x=find2(x,stud)
                            print('1.Edit Name\n2.Edit Address\n3.Edit gender\n4.Edit Aadhar\n5.edit phone number\n6.Date of birth')
                            print('7.Edit class and div\n8.Edit Mark\n9.Back\n10.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,10)
                            while ch in [1,2,3,4,5,6]:
                                find9(x,stud)
                            if ch==7:
                                stud[x]['class'],stud[x]['Div']=find6()
                            elif ch==8:
                                stud[x]['mark']={  'CHEMISTRY':int(input('Enter CHEMISTRY Mark')),
                                                   'PHYSICS':int(input('Enter PHYSICS Mark')),
                                                   'COMPUTER SC':int(input('Enter COMPUTER SCIENCE Mark')),
                                                   'MATHEMATICS':int(input('Enter MATHEMATICS Mark')),
                                                   'ENGLISH':int(input('Enter ENGLISH Mark'))}
                            elif ch==9:
                                nm=1
                            else:
                                m=1
                                nm=0
                                break
                        elif ch==3:
                            x=int(input('Enter you id'))
                            x=find2(x,stud)
                            print('1.Edit Name\n2.Edit Address\n3.Edit gender\n4.Edit Aadhar\n5.edit phone number\n6.Date of birth\n7.Back\n8.Logout')
                            ch=int(input('Enter your choice'))
                            ch=find1(ch,1,8)
                            while ch in [1,2,3,4,5,6]:
                                find9(x,prin)
                            if ch==7:
                                nm=1
                            else:
                                m=1
                                nm=0
                                break
                        elif ch==4:
                            m=1
                            break
                        else :
                            m=1
                            nm=0
                            break
                elif ch==3:
                    mn=1
                    while mn==1:
                        print('1.Display all teachers\n2.Display all students\n3.Display Principal\n4.Display students of a class')
                        print('5.Display students of a division\n6.Display teachers of a department\n7.Display Students having birthday on a date')
                        print('8.View a Student\n9.Print Report Card\n10.Back\n11.Logout')
                        ch=int(input('Enter your choice'))
                        ch=find1(ch,1,11)
                        if ch==1:
                            
                            for i in teach:
                                print(i,teach[i],sep=':')
                        elif ch==2:
                            for i in stud:
                                print(i,stud[i],sep=':')
                        elif ch==3:
                            for i in prin:
                                print(i,prin[i],sep=':')
                        elif ch==4:
                            x=int(input('Enter class'))
                            while x not in nn:
                                x=int(input('Enter class'))
                            for i in stud:
                                if stud[i]['class']==x:
                                    print(i,stud[i],sep=':')
                        elif ch==5:
                            x=int(input('Enter class'))
                            while x not in nn:
                                x=int(input('Enter class'))
                            y=input('Enter division')
                            y=y.upper()
                            while y not in nn[x]:
                                print('Invalid division')
                                y=input('Enter division')
                                y=y.upper()
                            for i in stud:
                                if stud[i]['class']==x and stud[i]['Div']==y:
                                    print(i,stud[i],sep=':')
                        elif ch==6:
                            x=find4()
                            for i in teach:
                                if teach[i]['Dept']==x:
                                    print(i,teach[i],sep=':')
                        elif ch==7:
                            x=find7()
                            for i in stud:
                                if stud[i]['DOB']==x:
                                    print(i,stud[i],sep=':')
                        elif ch==8:
                            x=int(input('Enter the student id'))
                            x=find2(x,stud)
                            print(x,stud[x],sep=':')
                        elif ch==9:
                            '''x=int(input('Enter the student id'))
                            x=find2(x,stud)
                            find12(x)'''
                            for i in stud:
                                x=find2(i,stud)
                                find12(x)
                        elif ch==10:
                            mn=0
                            break
                        else:
                            m=1
                            nm=0
                            break
                else:
                    print('1.delete Student\n2.Delete Teacher\n3.Delete Principal\n4.Back\n5.Logout')
                    ch=int(input('Enter your choice'))
                    ch=find1(ch,1,9)
                    if ch==1:
                        find10(stud)
                    elif ch==2:
                        find10(teach)
                    elif ch==3:
                        find10(prin)
                    elif ch==4:
                        mn=0
                        break
                    else:
                        m=1
                        nm=0
                        break
        

    
