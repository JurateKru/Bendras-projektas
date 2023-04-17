import random   ## įkelia "random" biblioteką
import os       ## įkelia "os" biblioteką
os.system('cls')    ## išvalo terminalą


tipai = ['♠️', '♥️', '♦️', '♣️']    ##  sukuriame simbolių sarašą
kortos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']  ## sukuriame skaičių bei raidžių sarašą

kalade = []

for tipas in tipai:     ## priskiriame kortoms simbolius
    for korta1 in kortos:
        if korta1 == 'T ':
            korta1 = korta1 + tipas
        else:
            korta1 = korta1 + ' ' + tipas
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

        nauja_kalade.append(kortos2)    ## prideda ištrauktą kortą į sarašą
        kortu_likutis = len(kalade) ## atspausdinamas likęs kortų sarašas
        os.system('cls')    ## išvalo terminalą
        print('Kortų liko', kortu_likutis)
        print(kortos2)
        if not kalade: ## jeigu baigiasi kortos, ciklas nutrūksta ir atspausdina eilutę su tekstu "baigėsi kortos"
            print('Baigėsi kortos')
            print(nauja_kalade)
            break
    else:   ## atspausdina visas ištrauktas kortas
        print("Nauja ištraukta kaladė", nauja_kalade)
        break



