f.open('c/Users/STATIE-6-C100/Desktop/Caracter.txt','w')
intrare=str(input('Sa se afiseze caracterele'))
f.close()

f=open('c/Users/STATIE-6-C100/Desktop/Caracter.txt','r')
x=f.read()
f.close()
print(x)
vocal