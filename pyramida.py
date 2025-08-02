pocet  = int(input("zadaj cislo:"))
cislo = 1
for riadok in range(1,pocet+1):
    for stlpec in range(1,riadok+1):
        print(cislo,end=" ")
        cislo += 1
    print()