import random


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

if maisyti == "taip":
    random.shuffle(kalade)
    print(kalade)
elif maisyti == "ne":
    print(kalade)
else:
    print('Įvedėte netinkamą atsakymą')

while True:
    response = input("Ar norite traukti kortą: ")

    if response == "taip":
        kortos2 = kalade.pop()
        print(kortos2)
        if not kalade: 
            print('Baigėsi kortos')
            break
    else:
        break



