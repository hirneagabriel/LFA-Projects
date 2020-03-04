f=open("dateintrare.txt","r")
n=int(f.readline())
graf = [["0"] * n for i in range(n)]
stareinitiala=int(f.readline())
starifinale=f.readline().split()
starifinale=[int(i) for i in starifinale]
v=f.readline().split()
while v:
    i=int(v[0])
    j=int(v[1])
    if graf[i][j]=="0":
        graf[i][j]=v[2]
    else:
        graf[i][j]=list(graf[i][j])
        graf[i][j].append(v[2])
    v = f.readline().split()
f.close()
cuvant=input("cuvant de verificat: ")
ok=0
while cuvant:
    litera=cuvant[0]
    cuvant=cuvant[:0]+cuvant[1:]
    for i in range(n):
        if litera in graf[stareinitiala][i]:
            stareinitiala=i
            break
    else:
        print("cuvant neacceptat")
        ok=1
if stareinitiala in starifinale:
    print("cuvant acceptat")
elif ok==0:
    print("cuvant neacceptat")
