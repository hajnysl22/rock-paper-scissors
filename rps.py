#KAMENNUZKYPAPIR
print("Kámen, nůžky a papír")
import random
first = str(input("Zadejte Kámen, Nůžky nebo Papír: "))
second = random.randint(1,3)

#CISLA
if second == 1:
    second = "Kámen"
elif second == 2:
    second = "Nůžky"
elif second == 3:
    second = "Papír"

#UKAŽVSTUPY
print("Zahrál jste:", first)
print("Soupeř zahrál:", second)

#REMIZA
#1-KAMEN
if first == "Kámen" and second == "Kámen":
    print("Remíza.")
#2-NUZKY
elif first == "Nůžky" and second == "Nůžky":
    print("Remíza.")
#3-PAPIR
elif first == "Papír" and second == "Papír":
    print("Remíza.")