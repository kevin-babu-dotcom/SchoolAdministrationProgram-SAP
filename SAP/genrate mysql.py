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

cu.execute('select id from st')
k=cu.fetchall()
kl=[]
for i in k:
    for j in i:
        kl.append(j)
print(j+1)
i=101
while i in kl:
    i+=1
kl.append(i)
