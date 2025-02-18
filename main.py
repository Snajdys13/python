#proměnná
text = "ahoj"
cislo = 1
desetinne = 1.5

#načítání od uživatele
nacteniTextu = input("Zadejte: ")
nacteniCisla = int(input("Zadejte: "))

#vypsání do konzole
print("text")
print(cislo)
print("text", cislo)

#podminky
if (cislo==10):
    print("číslo je 10")
elif(cislo==15):
    print("číslo je 15")
elif(cislo>==10):
    print("číslo je větší nebo 10")
else:
    print("číslo je nějaké divné")

#cykly
for i in range (2,10,2):
    print(i)
    