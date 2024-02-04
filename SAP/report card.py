'''n='ROHAN SONY'
c=12
d='E'
r=25
a='j10921'
do='03-01-2005'
ct='SAJAN SEBASTION'
f='SONY P JOHN'
m='MINI SONY'
ma={'CHEMISTRY       ':45,
    'PHYSICS         ':44,
    'COMPUTER SCIENCE':42,
    'MATHEMATICS     ':40,
    'ENGLISH         ':50}
x=sum(ma.values())
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
print('\t\t\t\tNAME    :',n)
print('\t\t\t\tclass   :',c)
print('\t\t\t\tDivision:',d)
print('\t\t\t\tRoll No :',r,'\t'*4,'FATHER        :',f)
print('\t\t\t\tAdm. NO :',a,'\t'*3,'MOTHER        :',m)
print('\t\t\t\tDOB     :',do,'\t'*3,'CLASS TEACHER :',ct)
print('\t'*5,'_'*48,)
print('\t'*5,'|      SUBJECTS','\t|','MAX.','\t','|SCORED   ','|TOP |')
print('\t'*5,'-'*46,'-|-')
for i in ma:
    print('\t'*5,'|',i,'\t|',50,'\t |',ma[i],'\t','   |TOP |')
print('\t'*5,'-'*46,'-|-')
#print()
print('\t'*5,'| TOTAL','\t'*2,'|',250,'\t |',sum(ma.values()),' GRADE:',grade,'|')
print('\t'*5,'-'*46,'-|-')
#print('\t'*4,'-'*52)
from datetime import date
print('\t'*5,'Place:','Anakkal')
print('\t'*5,'Date :',date.today())'''
mn={1:['A','B','C','D','E','F'],}
X=2
while X not in mn:
    X=int(input('Enter the'))
