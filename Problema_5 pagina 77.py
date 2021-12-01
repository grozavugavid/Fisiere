f.open('c/Users/STATIE-6-C100/Desktop/Caracter.txt','w')
intrare=str(input('Sa se afiseze caracterele'))
f.close()

f=open('c/Users/STATIE-6-C100/Desktop/Caracter.txt','r')
x=f.read()
f.close()
print(x)
vocal=[]
for i in range(0,len(x)):
  if x[i]=='o' or 'a' or 'u' or 'e' or 'i':
    vocal[i]!=x[i]
f=open('c/Users/STATIE-6-C100/Desktop/Caracter.txt','w')
f.write(vocal)
f.close()
