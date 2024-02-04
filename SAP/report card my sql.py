import mysql.connector as ms
import pickle
con=ms.connect(host='localhost',user='root',passwd='rohan')
if con.is_connected():
    print('Successfully connected')
    cu=con.cursor()
    cu.execute('Create database if not exists sch')
    con.commit()
    cu.execute('use sch')
    con.commit()
dept1={1: 'ENGLISH', 2: 'CHEMISTRY', 3: 'PHYSICS', 4: 'MATHEMATICS', 5: 'COMPUTERSC'}

def find12():
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
    k=int(input('Enter id'))
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
find12()
