f = open("dateintrare.txt","r")
n = int(f.readline())
graf = [[" "] * n for i in range(n)]
noduri = f.readline().split()
stareinitiala = f.readline()

for i in range(len(noduri)):
    if stareinitiala[0] == noduri[i]:
        pozitie = i
        stare = noduri[i]

starifinale = f.readline().split()
starifinale = [i for i in starifinale]
v = f.readline().split()

while v:
    for z in range(len(noduri)):
        if noduri[z] == v[0]:
            i=z
        if noduri[z] == v[1]:
            j = z
    if graf[i][j] == " ":
        graf[i][j] = v[2]
    else:
        graf[i][j] = list(graf[i][j])
        graf[i][j].append(v[2])
    v = f.readline().split()
f.close()

print(graf)

cuvant = input("cuvant de verificat: ")
ok=0

while cuvant:
    litera = cuvant[0]
    cuvant = cuvant[:0]+cuvant[1:]
    for i in range(n):
        if litera in graf[pozitie][i]:
            stare = noduri[i]
            pozitie = i
            break
    else:
        print("cuvant neacceptat")
        ok=1

if stare in starifinale and ok == 0:
    print("cuvant acceptat")
elif ok==0:
    print("cuvant neacceptat")
