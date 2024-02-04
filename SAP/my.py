import mysql.connector as ms
from datetime import date
def find1(x,y,z):
    while x<y or x>z:
        print('Invalid choice (',y,'-',z,')')
        x=int(input('Enter your choice'))
    return x
def find7():
    y=int(input('Enter date of birth'))
    y=find1(y,1,31)
    w=int(input('Enter month number of birth'))
    w=find1(w,1,12)
    z=int(input('Enter your year of birth'))
    while len(str(z))!=4:
        z=int(input('Enter your year of birth'))
    return date(z,w,y)
con=ms.connect(host='localhost',user='root',passwd='rohan')
if con.is_connected():
    print('Successfully connected')
    cu=con.cursor()
    cu.execute('Create database if not exists sch')
    con.commit()
    cu.execute('use sch')
    con.commit()
    #cu.execute('Drop table ad')
    #con.commit()
    cu.execute("create table if not exists ad (ID int(3) primary key,NAME varchar(20),CLASS int(2),DIVI char(2),DOB date,PASS varchar(10))")
    
    con.commit()
    '''i=int(input('enter id'))
    n=input("Enter the name").title()
    c=int(input('Enter the class'))
    c=find1(c,1,12)
    d=input('Enter the division')
    d=d.upper()
    dob=find7()
    pas=input('Enter passsword')
    s="insert into ad values(%s,'%s',%s,'%s','%s','%s')"%(i,n,c,d,dob,pas)
    cu.execute(s)
    con.commit()'''
    k=int(input('Enter id'))
    kl=input('Enter password')
    cu.execute('select * from ad')

    f=cu.fetchall()
    for i in f:
        if i[0]==k and i[-1]==kl:
            print(i)
        
    con.close()
else:
    print("connection failed")
