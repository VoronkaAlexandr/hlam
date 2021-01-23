n, m = input().split()
table_raz = input().split()
table_razmer = []
for i in table_raz:
    table_razmer.append(int(i))
puti = {}
for i in range(len(table_razmer)):
    puti[i+1] = [table_razmer[i],i+1]

def poisk_ssilki(i):
    if puti[i][0] == 0:
        print('не выход',i)
        poisk_ssilki(puti[i][1])
    else:
        print('выход',i)
        return i

for i in range(int(m)):
    dest, source = input().split()
    dest = int(dest)
    source = int(source)
    if dest == source:
        print(puti[dest][0])
    elif puti[dest][0] != 0 and puti[source][0] != 0:
        puti[dest][0]+=puti[source][0]
        puti[source][0] = 0
        puti[source][1] = dest
        print(puti[dest][0])
    elif puti[source][0] == 0 and puti[dest][0] != 0:
        table = poisk_ssilki(puti[source][1])
        puti[dest][0] += puti[table][0]
        puti[table][0] = 0
        puti[table][1] = dest
        print(puti[dest][0])
    elif puti[dest][0] == 0:
        if puti[source][0] != 0:
            hoziain = poisk_ssilki(puti[dest][1])
            puti[hoziain][0] += puti[source][0]
            puti[source][0] = 0
            puti[source][1] = hoziain
            print(puti[hoziain][0])
        else:
            print(puti)
            hoziain_a = poisk_ssilki(puti[dest][1])
            print('хозяин',hoziain_a)
            tablica = poisk_ssilki(puti[source][1])
            print('табле',tablica)
            puti[hoziain_a][0] += puti[tablica][0]
            puti[tablica][0] = 0
            puti[tablica][1] = hoziain_a
            print(puti[hoziain_a][0])
            print(puti)
