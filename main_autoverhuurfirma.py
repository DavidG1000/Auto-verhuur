"""Schrijf een programma voor een autoverhuur firma.
Data wordt bijgehouden in een dictionary{id:id_auto,merk:auto_merk,brandstof: brandstof_auto, verhuurd: verhuurd_ja/nee}
Functies
1.toonwagens(toont alle wagen)
2.toon_beschikbare_wagens(toont wagens waar verhuurd nee is)
3.Toon_verhuurde_wagens(toont de wagen waar verhuurd ja is)
4.Verhuur_wagen(wagen id) enkel wagen die beschikbaar zijn,
  indien niet beschikbaar melding, deze wagen is reeds verhuurd, zorg er ook voor dat de wagen hierna niet meer verhuurd kan worden.
5.Wagen_terug_beschikbaar(wagen id) de verhuurde wagen wordt terug beschikbaar gezet, melding indien wagen reeds beschikbaar is
6.Voeg wagen toe(id,merk,model,brandstof,verhuurd=“nee”)
7.Verwijder wagen(id) melding indien id niet bestaat.
8.Logboek(IO) Schrijf telkens naar een bestand welke acties er uitgevoerd zijn.
"""

import module_autoverhuurfirma
import sys
from tabulate import tabulate



# Hoofd deel 1 : kies de lijst
def keuze_lijst():
    print("1. Lijst auto's")
    print("2. Lijst bestelwagens")


# Hoofd. deel 2 druk het keuze menu af
def keuze_menu():
    print("1.Tonen alle wagens")
    print("2.Tonen beschikbare wagens")
    print("3.Tonen verhuurde wagens")
    print("4.Verhuur wagen")
    print("5.Wagen terug beschikbaar stellen")
    print("6.Wagen toevoegen")
    print("7.Wagen verwijderen")

# 4:{"Merk":"Renault","Brandstof":"Diesel","Verhuurd":"ja"}}

# 1.Druk items af
def tonen(dictio):
    for wagen_id, wagen_info in dictio.items():
        print("\nWagen nr.:", wagen_id)
        for key in wagen_info:
            print(key + ":", wagen_info[key])
    main()
#1.a Tonen uitgebreid
def uitgebr_tonen(dictio):
    headers = ["Nummer", "Merk", "Brandstof", "Verhuurd"]
    dictio = [[name, *inner.values()] for name, inner in dictio.items()]
    print("")
    print(tabulate(dictio, headers=headers, tablefmt="grid"))
    print("")
    main()
# 2.Toon beschikbare wagens
def beschikb_wagens(dictio):
    teller = 0
    for wagen_id, wagen_info in dictio.items():
        if dictio[wagen_id]["Verhuurd"] == "nee":
            teller = 1
            print("\nWagen nr.:", wagen_id)
            for key in wagen_info:
                print(key + ":", wagen_info[key])
    if teller == 0: print("Geen enkele wagen is beschikbaar")
    main()

# 3.Toon verhuurde wagens
def verhuurde_wagens(dictio):
    teller = 0
    for wagen_id, wagen_info in dictio.items():
        if dictio[wagen_id]["Verhuurd"] == "ja":
            teller = teller + 1
            print("\nWagen nr.:", wagen_id)
            for key in wagen_info:
                print(key + ":", wagen_info[key])
    if teller == 0: print("Geen enkele wagen is verhuurd")
    main()

# 4.Verhuur wagen
def verhuur_wagen(dictio):
    for wagen_id in dictio.items():
        print(wagen_id)
    keuze = ""
    while not keuze == 0:
        keuze = int(input("Geef het wagennr. van de wagen die u wil verhuren of '0' om te stoppen ? "))
        if not keuze == 0:
            if dictio[keuze]["Verhuurd"] == "ja":
                print("Deze wagen is al verhuurd.")
            else:
                dictio[keuze]["Verhuurd"] = "ja"
                print("\nWagen nr.:", keuze, " is nu verhuurd.")
    main()

# 5.Beschikbaar stellen wagen
def beschikb_stellen_wagen(dictio):
    for wagen_id in dictio.items():
        print(wagen_id)
    keuze = ""
    while not keuze == 0:
        keuze = int(input("Geef het wagennr. van de wagen die u wil beschikbaar stellen of '0' om te stoppen ? "))
        if not keuze == 0:
            if dictio[keuze]["Verhuurd"] == "nee":
                print("Deze wagen is al beschikbaar.")
            else:
                dictio[keuze]["Verhuurd"] = "nee"
                print("\nWagen nr.:", keuze, " is nu terug beschikbaar.")

    main()

# 6.Voeg nieuwe wagen toe
def toevoegen(dictio):
    wagen_id = max(list(dictio.keys())) + 1  #hier gaan we de hoogste wagennr zoeken en 1 bijtellen
    merk = input("Geef het merk van nieuwe wagen nr " + str(wagen_id) + " in: ")
    brandstof = input("Geef de brandstof in: ")
    dictio[wagen_id] = {"Merk": merk, "Brandstof": brandstof, "Verhuurd": "nee"}
    for wagens in dictio.items():
        print(wagens)
    print("Wagen nr. " + str(wagen_id) + " is toegevoegd.")
    main()

# 4:{"Merk":"Renault","Brandstof":"Diesel","Verhuurd":"ja"}}


# 7.verwijderd een item uit de lijst
def verwijder(dictio):
    for wagens in dictio.items():
        print(wagens)
    wagen_id = int(input("Geef de wagen nr. die je wenst te verwijderen: "))
    if wagen_id in dictio.keys():
        bevestiging = input("Bent u zeker dat u wagen "+ str(wagen_id) + " wil verwijderen j/n ?")
        if bevestiging == "j":
            dictio.pop(wagen_id)
            print("Wagen nr. " + str(wagen_id) + " is weg uit de lijst")
    else:
        print("Wagennr. " + str(wagen_id) + " is niet in de lijst")

    main()
# Key en waarde aanpassen / word voorlopig niet gebruikt in dit programma
def aanpassen(dictio):
    tonen(dictio)
    aan_te_passen_key = input("Welke key wil u aanpassen: ")
    if aan_te_passen_key in dictio:
        nieuwe_key = input("Geef de nieuwe key in: ")
        dictio[aan_te_passen_key] = nieuwe_key
        aan_te_passen_value = input("Geef de nieuwe waarde in: ")
        dictio[nieuwe_key] = aan_te_passen_value
        tonen(dictio)
    else:
        print("Key staat niet in de lijst")



# hoofdprogramma
def main():
    keuze_lijst()
    lijst_kiezen = input("Maak een keuze welke lijst of 'stop' om te stoppen (1-2) : ")

    if lijst_kiezen == "1":
        dictio = module_autoverhuurfirma.autos_verhuur
    elif lijst_kiezen == "2":
        dictio = module_autoverhuurfirma.bestelwagens_verhuur
    elif lijst_kiezen == "stop": sys.exit()

    keuze_menu()
    keuze = input("Maak een keuze 1-7 : ")
    if (keuze == "1"):
        uitgebr_tonen(dictio)
    elif (keuze == "2"):
        beschikb_wagens(dictio)
    elif (keuze == "3"):
        verhuurde_wagens(dictio)
    elif (keuze == "4"):
        verhuur_wagen(dictio)
    elif (keuze == "5"):
        beschikb_stellen_wagen(dictio)
    elif (keuze == "6"):
        toevoegen(dictio)
    elif (keuze == "7"):
        verwijder(dictio)
    #elif (keuze == ""): word niet gebruikt
        #dictio = aanpassen(dictio): idem

main()
