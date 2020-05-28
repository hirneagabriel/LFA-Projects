def terminalaCuvant(x):
    for j in x:
        if j in neterminale:
            return 1
    return 0


def dezvoltareProductii(x):
    for i in x:
        if terminalaCuvant(i) == 1:
            for j in i:
                if j in neterminale:
                    for k in productii.get(j):
                        y = i
                        if k == "~":
                            k=""
                        y=y.replace(j,k)
                        if len(y) <= 2*n:
                            x.append(y)
        elif terminalaCuvant(i) != 1 and len(i)<=n and i not in rezultat:
            if i=="":
                rezultat.append("~")
                x.remove(i)
            else:
                rezultat.append(i)
    for c in x:
        if terminalaCuvant(c) != 1 and len(c)<=n and c not in rezultat:
            if c == "":
                rezultat.append("~")
                x.remove(c)
            else:
                rezultat.append(c)
                x.remove(c)


f = open("input.txt", "r")

n = int(f.readline())

neterminale = [x.strip() for x in f.readline().split()]
terminale = [x.strip() for x in f.readline().split()]

S = f.readline().strip()

p =[x.strip().split('->') for x in f.readlines()]

productii = {}

for i in range(len(p)):
    productii[p[i][0]]=p[i][1].split(' | ')

x = []
rezultat = []

for i in productii[S]:
    x.append(i)

if n!=0:
    dezvoltareProductii(x)
    if rezultat:
        print(rezultat)
    else:
        print("Nu sunt cuvinte")
