a = {1: "one", 2: "two"}
b = {2: "dva", 3: "three"}

spojeny = a.copy()  # potrebné volať copy() s () - inak to nie je slovník

for k, v in b.items():
    if k in spojeny:
        spojeny[k] = [spojeny[k], v]  # pridá oba prekladané významy do zoznamu
    else:
        spojeny[k] = v  # oprava: bolo tam "kluc" namiesto "k"

print(spojeny)