herhalen = "y"
TotaalBakjes = 0
totaalHoorntjes = 0
TotaleBolletjes = 0
Besteldesmakenlijst = []
BestaandeSmaken = ["aardbei", "a", "chocolade", "c", "munt", "m", "vanille", "v"]
prijsPerBakje = 0.75
prijsPerHoorntje = 1.25
prijsPerBolletje = 1.10

print("Welkom bij Papi Gelato.")

def smaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C), Munt(M) of Vanille(V)")
    returnsInLoop = 1
    while returnsInLoop != aantal + 1:
        smaak = input("Welke smaak wilt U hebben voor uw "+ str(returnsInLoop) + "e bolletje?").lower()
        if smaak in BestaandeSmaken:
            returnsInLoop += 1
            Besteldesmakenlijst.append(smaak)
        else:
            print("Sorry, maar dat begrijp ik niet, probeer het opnieuw.")


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
        print("Fill in a number above zero.")
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
    print("Hier is uw", bakjeOfHoorntje, "met", aantal, "bolletje(s)")
    overnieuw = input("Wilt u nog wat bestellen?(Y/N): ").lower()
    return overnieuw


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
            print("An Error occurred, please try again")
    else:

        print("")

print('---------["Papi Gelato"]---------')
print("")
if TotaleBolletjes >= 1:
    print("Bolletje(s)    "+ str(TotaleBolletjes)+ " X " + "€" + str(round(float(TotaleBolletjes) * prijsPerBolletje,2)))

if totaalHoorntjes >= 1:
    print("Hoorntje(s)    "+ str(totaalHoorntjes)+ " X " + "€" + str(round(float(totaalHoorntjes) * prijsPerHoorntje,2)))

if TotaalBakjes >= 1:
    print("Bakje(s)       "+ str(TotaalBakjes)+ " X " + "€" + str(round(float(TotaalBakjes) * prijsPerBakje,2)))