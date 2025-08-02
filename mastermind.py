spravne = 0
nespravne = 0

from random import randint
myslene_cislo = randint(1,10)
meno = input("ako sa volas:")
print("vitaj",meno)
print("pravidla su jednoduche staci hadat cislo")
print("ked budes chcet skoncit napis koniec")
while True:
    typ = input("hadaj cislo:").lower()
    if typ =="koniec":
        break
    if typ.isdecimal():
        typ = int(typ)
    if typ ==myslene_cislo:
        print("spravne")
        spravne +=1
        myslene_cislo = randint(1,10)
    else:
        print("zle")
        nespravne +=1

        
print("--------tvoje skore---------")
print(f"spravne:{spravne}")
print(f"nespravne:{nespravne}")
print(f"spolu:{spravne+nespravne}")

