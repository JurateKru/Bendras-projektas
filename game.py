import random   ## įkelia "random" biblioteką
import os       ## įkelia "os" biblioteką
os.system('cls')    ## išvalo terminalą


tipai = ['♠️', '♥️', '♦️', '♣️']    ##  sukuriame simbolių sarašą
kortos = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}  ## sukuriame skaičių bei raidžių sarašą



kalade = []

for tipas in tipai:     ## priskiriame kortoms simbolius
    for korta1 in kortos:
        korta1 = korta1 + tipas
        kalade.append(korta1)

maisyti = input('Ar norite išmaišyti kaladę?: ')
maisyti = maisyti.lower()   ## atsakymą padarome mažosiomis raidėmis, kad sutaptų su turimais pasirinkimais

if maisyti == "taip":
    os.system('cls')    ## išvalo terminalą
    random.shuffle(kalade)  ## išmaišo kortų kaladę
    print(kalade)
elif maisyti == "ne":
    print(kalade)
else:
    print('Įvedėte netinkamą atsakymą')

nauja_kalade = [] ## Ištrauktos kortos

while True: ## kol sąlyga tenkina, traukiama korta
    response = input("Ar norite traukti kortą: ")
    response = response.lower()

    if response == "taip":
        kortos2 = kalade.pop()
        kortos3 = kalade.pop()

        nauja_kalade.append(kortos2)    ## prideda ištrauktą kortą į sarašą
        kortu_likutis = len(kalade) ## atspausdinamas likęs kortų sarašas
        os.system('cls')    ## išvalo terminalą
        print('Kortų liko', kortu_likutis)
        print(f"Mūsų ištraukta korta: {kortos2}")
        print(f"Kompiuterio ištraukta korta: {kortos3}")

        if kortos2[0] == kortos3[0]:
            print('Lygiosios')
        elif kortos2[0] < kortos3[0]:
            print('Jūs pralaimėjote')
        elif kortos2[0] > kortos3[0]:
            print('Jūs laimėjote')

        if not kalade: ## jeigu baigiasi kortos, ciklas nutrūksta ir atspausdina eilutę su tekstu "baigėsi kortos"
            print('Baigėsi kortos')
            print(nauja_kalade)
            break
    else:   ## atspausdina visas ištrauktas kortas
        print("Nauja ištraukta kaladė", nauja_kalade)
        break



