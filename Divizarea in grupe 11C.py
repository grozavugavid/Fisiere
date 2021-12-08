with open('C:/Users/Statie-10-C100/Downloads/Lista clasei a 11C.txt','rt') as f:
    linii=list(f)

n=media=0
print('Nume','\tPrenume',sep='\t')
for linie in linii:
    campuri=linie.split()
    nota=int(campuri[2])
    n,media=n+1,media+nota
    print(campuri[0],campuri[1],nota,sep='\t')
print("Media clasei a 11C este",media/float(n))





