from graphviz import Digraph

def inchidere(i,line):
    line.append(noduri[i])
    for w in range(n):
        if '~' in graf[i][w]:
            if noduri[w] in line:
                break
            else:
                inchidere(w,line)

    line.sort()
    return tuple(line)


def tabel(indiceNod,indiceAlfabet):
    lin = []
    for w in range(n):
        if alfabet[indiceAlfabet] in graf[indiceNod][w]:
            lin.append(noduri[w])
    return lin


f = open("dateintrare.txt","r")

n = int(f.readline())

graf = [[" "] * n for i in range(n)]

noduri = f.readline().split()

stareinitiala = f.readline().split()

starifinale = f.readline().split()

starifinale = [i for i in starifinale]

alfabet=f.readline().split()

v = f.readline().split()

while v:
    for z in range(len(noduri)):
        if noduri[z] == v[0]:
            i = z
        if noduri[z] == v[1]:
            j = z

    if graf[i][j] == " ":
        graf[i][j] = v[2]
    else:
        graf[i][j] = list(graf[i][j])
        graf[i][j].append(v[2])
    v = f.readline().split()

f.close()


inchideri=[]
for i in range(n):
    line = []
    inchideri.append(inchidere(i,line))

alfabetrelatii = []
for i in range(len(alfabet)):
    lista2 = []
    for j in range(n):
        lista1 = []
        for k in inchideri[j]:
            for l in range(n):
                if k == noduri[l]:
                    lista = tabel(l,i)
                    lista1.extend(lista)
                    lista = []
        lista1 = list(dict.fromkeys(lista1))
        lista3 = []

        for q in lista1:
            for m in range(n):
                if q == noduri[m]:
                    lista3.extend(inchideri[m])

        lista3.sort()
        lista3 = tuple(dict.fromkeys(lista3))
        lista2.append(lista3)

    alfabetrelatii.append(lista2)

nodurifinale = []
for i in range(n):
    if stareinitiala[0] == noduri[i]:
        nodurifinale.append(inchideri[i])

relatiifinale = []
ok = 1
j = 0
while ok != 0:
    ok -= 1
    lista2 = []
    for i in range(len(alfabet)):
        lista = []
        for k in nodurifinale[j]:
            for l in range(len(noduri)):
                if k in noduri[l]:
                    lista.extend(alfabetrelatii[i][l])
        lista.sort()
        lista = tuple(dict.fromkeys(lista))
        lista2.append(lista)

    relatiifinale.append(lista2)
    for q in range(len(alfabet)):
        if lista2[q] not in nodurifinale and lista2[q] != ():
            nodurifinale.append(lista2[q])
            ok += 1

    j += 1

stariFinale = []
for stare in starifinale:
    for i in range(len(nodurifinale)):
        if stare in nodurifinale[i]:
            stariFinale.append(nodurifinale[i])

stariFinale = list(dict.fromkeys(stariFinale))


f = open("rezultat.txt","w")

f.write("AFD pentru ~AFD-lambda este:\n")
f.write("stareinitiala: " + str(nodurifinale[0]) + "\n")
f.write("starifinale: "+ str(stariFinale)+ "\n")

for i in range(len(nodurifinale)):
    for j in range(len(relatiifinale[i])):
        if relatiifinale[i][j] != ():
            f.write(str(nodurifinale[i])+" ---> " + str(relatiifinale[i][j])+" cu " + str(alfabet[j])+ "\n")
f.close()

f = Digraph('fnd', filename='fsm.gv')
f.attr(rankdir='LR', size='4')

if nodurifinale[0] in stariFinale:
    f.attr('node', shape='doublecircle', fillcolor="green", style="filled")
    f.node(str(nodurifinale[0]))
else:
    f.attr('node', shape='circle', fillcolor="green", style="filled")
    f.node(str(nodurifinale[0]))

f.attr('node', shape='doublecircle', fillcolor="white", style="filled")

for i in range(len(stariFinale)):
    f.node(str(stariFinale[i]))


f.attr('node', shape='circle', fillcolor="white", style="filled")
for i in range(len(nodurifinale)):
    for j in range(len(relatiifinale[i])):
        if relatiifinale[i][j] != ():
            f.edge(str(nodurifinale[i]),str(relatiifinale[i][j]),str(alfabet[j]))
f.view()
