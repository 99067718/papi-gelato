herhalen = "y"
TotaalBakjes = 0
totaalHoorntjes = 0
TotaleBolletjes = 0

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

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
    print("Hier is uw", bakjeOfHoorntje, "met", aantal, "bolletje(s)")
    overnieuw = input("Wilt u nog wat bestellen?(Y/N): ").lower()
    return overnieuw


while herhalen == "y":
    aantal = aantalbolletjes()

    bakjeOfHoorntje = WatVoorVerpakking()
    if bakjeOfHoorntje != "ERROR":
        herhalen = nogEenKeer()
    else:
        TotaleBolletjes += aantal
        if bakjeOfHoorntje == "bakje":
            TotaalBakjes += 1
        elif bakjeOfHoorntje == "hoorntje":
            totaalHoorntjes += 1
        else:
            print("An Error occurred, please try again")

        print("")
