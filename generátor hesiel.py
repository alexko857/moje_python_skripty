import random
tvoje_heslo = ""
dlzka = int(input("zadaj dlzku hesla:"))
moznosti = "abcdefghijklmnopqrstvABCDEFGHIJKLMNOPQRSTVW&:?ô!%=!@><_"
    
for pismeno in range(dlzka):
          alex = random.choice(moznosti)
          tvoje_heslo += alex
    
print("tvoje heslo je:{} ".format(tvoje_heslo))
