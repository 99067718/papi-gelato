from os import truncate


herhalen = "y"
repeat = True
TotaalBakjes = 0
totaalHoorntjes = 0
TotaleBolletjes = 0
particulier = "...."

#------Zakelijk------#
Liters_ijs = 0
Btw = 6
prijsPerLiter = 9.80
#-----------------------#

Besteldesmakenlijst = []
BestaandeSmaken = ["aardbei", "a", "chocolade", "c", "vanille", "v"]

toppings = []
aantalToppings = 0
bestaandeToppings = ["sl", "slagroom", "sp", "sprinkels", "c", "caramel"]
toppingKosten = 0.00

prijsPerBakje = 0.75
prijsPerHoorntje = 1.25
prijsPerBolletje = 0.95

print("Welkom bij Papi Gelato.")

def WrongAnswer():
    print("Sorry dat is geen optie die we aanbieden...")

def AantalLiter():
    global Liters_ijs
    Liters_ijs = int(input("Hoeveel liter ijs wilt U bestellen?: "))

def topping():
    
    
        toppingKeuze = input("Wat voor topping wilt u: (G) Geen, (Sl) Slagroom, (Sp) Sprinkels of (C) Caramel Saus?: ").lower()
        if toppingKeuze == "g":
            print("")
            
        elif toppingKeuze in bestaandeToppings:
            
            toppings.append(toppingKeuze)
            global aantalToppings
            global toppingKosten
            aantalToppings += 1

            if toppingKeuze == "sl" or "slagroom":
                
                toppingKosten += 0.50
            elif toppingKeuze == "sp" or "sprinkels":
                
                toppingKosten += 0.30
            elif toppingKeuze == "c" or "caramel":
                if bakjeOfHoorntje == "bakje":
                    
                    toppingKosten += 0.90
                elif bakjeOfHoorntje == "hoorntje":
            
                    toppingKosten += 0.60

        else:
            WrongAnswer()

def ParticulierSmaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    smaak = input("Welke smaak ijs wilt U?")


def smaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    returnsInLoop = 1
    while returnsInLoop != aantal + 1:
        smaak = input("Welke smaak wilt U hebben voor uw "+ str(returnsInLoop) + "e bolletje?").lower()
        if smaak in BestaandeSmaken:
            returnsInLoop += 1
            Besteldesmakenlijst.append(smaak)
            
        else:
            WrongAnswer()


def aantalbolletjes():
    aantalBolletjesijs = int(input("Hoe veel bolletjes ijs wil je?: "))
    return aantalBolletjesijs

def WatVoorVerpakking():
    if aantal <= 3:
        waarin = keuzeBakjeOfHoorntje()

    elif aantal > 3 and aantal < 8:
        print("Dan krijgt u van mij een bakje met", aantal, "bolletjes.")
        waarin = "bakje"
    
    elif aantal > 8:
        print("Sorry, maar zulke grote bakjes hebben wij niet.")
        waarin = "ERROR"
      
    else:
        WrongAnswer()
        waarin = "ERROR"
       
    return waarin

def keuzeBakjeOfHoorntje():
    soort = input("Wilt U een hoorntje of een bakje?(H of B): ").lower()
    if soort == "b":
        soort = "bakje"
    elif soort == "h":
        soort = "hoorntje"
    return soort

def nogEenKeer():
    smaak()
    topping()
    print("Hier is uw", bakjeOfHoorntje, "met", aantal, "bolletje(s)")
    overnieuw = input("Wilt u nog wat bestellen?(Y/N): ").lower()
    return overnieuw

while repeat == True:
    Soort = input("Bent u Particulier (P) of zakelijk (Z)?: ").lower()
    if Soort == "p" or Soort == "particulier":
        herhalen = "y"
        particulier = "ja"
        repeat = False
    elif Soort == "z" or Soort =="zakelijk":
        particulier = "nee"
        herhalen = "n"
        repeat = False
    else:
        WrongAnswer()
        repeat = True


while herhalen == "y":
    
    aantal = aantalbolletjes()

    bakjeOfHoorntje = WatVoorVerpakking()
    if bakjeOfHoorntje != "ERROR":
        herhalen = nogEenKeer()
        TotaleBolletjes += aantal
        if bakjeOfHoorntje == "bakje":
            
            TotaalBakjes = TotaalBakjes + 1
        elif bakjeOfHoorntje == "hoorntje":
            totaalHoorntjes = totaalHoorntjes + 1
        else:
            WrongAnswer()
    else:

        print("")

if particulier == "nee":
    Litersijs = AantalLiter()
    ParticulierSmaak()

if particulier == "ja":
    print('---------["Papi Gelato"]---------')
    print("")
    if TotaleBolletjes >= 1:
        print("Bolletje(s)    "+ str(TotaleBolletjes)+ " X " + "€" + str(round(float(TotaleBolletjes) * prijsPerBolletje,2)))

    if totaalHoorntjes >= 1:
        print("Hoorntje(s)    "+ str(totaalHoorntjes)+ " X " + "€" + str(round(float(totaalHoorntjes) * prijsPerHoorntje,2)))

    if TotaalBakjes >= 1:
        print("Bakje(s)       "+ str(TotaalBakjes)+ " X " + "€" + str(round(float(TotaalBakjes) * prijsPerBakje,2)))

    if aantalToppings >= 1:
        print("topping(s)     "+ str(aantalToppings)+ " X " + "€" + str(round(toppingKosten,2)))

    print("                   ----- +")
    totaalprijs = float(totaalHoorntjes) * prijsPerHoorntje + float(TotaalBakjes) * prijsPerBakje + TotaleBolletjes * prijsPerBolletje
    totaal2 = round(float(totaalprijs),2)

    print("Totaal"+ "              "+ "€" + str(totaal2))
else:
    print('---------["Papi Gelato"]---------')
    print("")
    totaalprijs = float(Liters_ijs) * float(prijsPerLiter)
    totaalprijs2 = round(float(totaalprijs),2)
    print("Liter   "+ str(Liters_ijs), " X "+ str(prijsPerLiter)+ " = "+"€"+ str(totaalprijs2))
    print("                -------- +")
    print("Totaal           = €"+ str(totaalprijs2))
    btwprijs = round(float(totaalprijs/100 * Btw),2)
    print("BTW  ("+ str(Btw) + "%)        = €"+ str(btwprijs))


