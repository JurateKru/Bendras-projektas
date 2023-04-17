import random
import os
os.system('cls')


tipai = ['♠️', '♥️', '♦️', '♣️']
kortos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

kalade = []

for tipas in tipai:
    for korta1 in kortos:
        if korta1 == 'T ':
            korta1 = korta1 + tipas
        else:
            korta1 = korta1 + ' ' + tipas
        kalade.append(korta1)

maisyti = input('Ar norite išmaišyti kaladę?: ')
maisyti = maisyti.lower()

if maisyti == "taip":
    os.system('cls')
    random.shuffle(kalade)
    print(kalade)
elif maisyti == "ne":
    print(kalade)
else:
    print('Įvedėte netinkamą atsakymą')

nauja_kalade = []

while True:
    response = input("Ar norite traukti kortą: ")
    response = response.lower()

    if response == "taip":
        kortos2 = kalade.pop()

        nauja_kalade.append(kortos2)
        kortu_likutis = len(kalade)
        os.system('cls')
        print('Kortų liko', kortu_likutis)
        print(kortos2)
        if not kalade: 
            print('Baigėsi kortos')
            print(nauja_kalade)
            break
    else:
        print("Nauja ištraukta kaladė", nauja_kalade)
        break



