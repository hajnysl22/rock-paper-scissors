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