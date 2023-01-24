from tabulate import tabulate

tablePakar = [['Kode Gejala', 'Gejala', 'CFpakar'],
         ['G01', 'Demam', 0.6],
         ['G02', 'Menggigil', 0.5],
         ['G03', 'Letih atau lesu', 0.6],
         ['G04', 'Sakit kepala', 0.6],
         ['G05', 'Nyeri otot', 0.7],
         ['G06', 'Pembengkakan kelenjar getah benih', 0.8]]

pa = tablePakar[1][2]
pb = tablePakar[2][2]
pc = tablePakar[3][2]
pd = tablePakar[4][2]
pe = tablePakar[5][2]
pf = tablePakar[6][2]

def OpsiUser():
    print("Input gejala yang dirasakan berdasarkan keyakinan")
    print("(Ketik 1/Tidak, 2/Tidak tahu, 3/Sedikit yakin, 4/Cukup Yakin, 5/Yakin, 6/Sangat Yakin)")
    global a,b,c,d,e,f
    a = int(input("Apakah kamu merasa Demam? "))
    b = int(input("Apakah tubuhmu terasa menggigil? "))
    c = int(input("Apakah kamu merasa letih atau lesu? "))
    d = int(input("Apakah kepalamu terasa sakit? "))
    e = int(input("Apakah terdapat rasa nyeri di otot? "))
    f = int(input("Apakah ada pembengkakkan kelenjar getah benih? "))

    if a == 1:
        a = 0
    elif a == 2:
        a = 0.2
    elif a == 3:
        a = 0.4
    elif a == 4:
        a = 0.6
    elif a == 5:
        a = 0.8
    elif a == 6:
        a = 1

    if b == 1:
        b = 0
    elif b == 2:
        b = 0.2
    elif b == 3:
        b = 0.4
    elif b == 4:
        b = 0.6
    elif b == 5:
        b = 0.8
    elif b == 6:
        b = 1

    if c == 1:
        c = 0
    elif c == 2:
        c = 0.2
    elif c == 3:
        c = 0.4
    elif c == 4:
        c = 0.6
    elif c == 5:
        c = 0.8
    elif c == 6:
        c = 1

    if d == 1:
        d = 0
    elif d == 2:
        d = 0.2
    elif d == 3:
        d = 0.4
    elif d == 4:
        d = 0.6
    elif d == 5:
        d = 0.8
    elif d == 6:
        d = 1

    if e == 1:
        e = 0
    elif e == 2:
        e = 0.2
    elif e == 3:
        e = 0.4
    elif e == 4:
        e = 0.6
    elif e == 5:
        e = 0.8
    elif e == 6:
        e = 1

    if f == 1:
        f = 0
    elif f == 2:
        f = 0.2
    elif f == 3:
        f = 0.4
    elif f == 4:
        f = 0.6
    elif f == 5:
        f = 0.8
    elif f == 6:
        f = 1


tableEvidence = [['Kode Gejala', 'Gejala', 'Evidence'],
          ['G01', 'Demam'],
          ['G02', 'Menggigil'],
          ['G03', 'Letih atau lesu'],
          ['G04', 'Sakit kepala'],
          ['G05', 'Nyeri otot'],
          ['G06', 'Pembengkakan kelenjar getah benih']]

OpsiUser()

tableEvidence[1].append(a)
tableEvidence[2].append(b)
tableEvidence[3].append(c)
tableEvidence[4].append(d)
tableEvidence[5].append(e)
tableEvidence[6].append(f)


cf1 = pa * a
cf2 = pb * b
cf3 = pc * c
cf4 = pd * d
cf5 = pe * e
cf6 = pf * f

ccf12 = cf1 + cf2 * (1 - cf1)
ccfo13 = ccf12 + cf3 * (1 - ccf12)
ccfo24 = ccfo13 + cf4 * (1 - ccfo13)
ccfo35 = ccfo24 + cf5 * (1 - ccfo24)
ccfo46 = ccfo35 + cf6 * (1 - ccfo35)

diag = ccfo46 * 100


print("\nTabel Nilai Pakar")
print(tabulate(tablePakar, headers='firstrow', tablefmt='fancy_grid'))
print("\nTabel Nilai Evidence")
print(tabulate(tableEvidence, headers='firstrow', tablefmt='fancy_grid'))
print("")
print("Tingkat presetanse penyakit monkey pox menggunakan metoda certainty factor (CF) sebesar ",round(diag),"%.",sep="")
