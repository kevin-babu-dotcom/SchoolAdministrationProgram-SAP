import mysql.connector as ms
import pickle,os
#os.remove('cd.dat')
f=open('cd.dat','ab+')
mm={'1A': [], '1B': [], '1C': [], '1D': [], '1E': [], '1F': [],
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
    '12A': [], '12B': [], '12C': [], '12D': [], '12E': [], '12F': []}
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
    cu.execute("create table if not exists cd (CLASS varchar(3) primary key,CLSTHR int(3),CHEM int(3),ENG int(3),PHY int(3),MATH int(3),CS int(3))")
    con.commit()

for i in mm:
    s="insert into cd values('%s',%s,%s,%s,%s,%s,%s)"%(i,'null','null','null','null','null','null')
    cu.execute(s)
    con.commit()
    m={i:mm[i]}
    pickle.dump(m,f)
f.seek(0)
try:
    while True:
        l=pickle.load(f)
        print(l)
except EOFError:
    print('Closind...')
    f.close()
#os.remove('cd.dat')
