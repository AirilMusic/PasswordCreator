#### CLUEDO CHEATS UWU ####
## Made by Airil/Ainhoa/Ari (we are the same person, you can use the name that you prefere)
#28-10-2022

### WORK IN PROGRESS ###

import time

# CARDS
allPlaces = []
allWeaphons = []
allSuspicious = []

while True:
    add = input("Add a place (exit if there is no more): ")
    if add.lower() == "exit":
        break
    else:
        allPlaces.append(add.lower())

print("")

while True:
    add = input("Add a weaphon (exit if there is no more): ")
    if add.lower() == "exit":
        break
    else:
        allWeaphons.append(add.lower())

print("")

while True:
    add = input("Add a suspicious (exit if there is no more): ")
    if add.lower() == "exit":
        break
    else:
        allSuspicious.append(add.lower())

# PLAYERS
p = []

for i in range(10):
    class player():
        name = str(i)
        
        place = ""
        weaphon = ""
        suspicious = ""
        
        noCards = [] #cartas que no tiene el jugador
        
        posiblePlaces = []
        posibleWeaphons = []
        posibleSuspicious = []
        
        placesProbabilitys = {}
        weaphonsProbabilitys = {}
        suspiciousProbabilitys = {}
        
        mostProbablePlace = {"" : 0.0}
        mostProbableWeaphon = {"" : 0.0}
        mostProbableSuspicious = {"" : 0.0}
    
    p.append(player)
    
    for a in range (len(allPlaces) - 1):
        p[i].placesProbabilitys.update({allPlaces[a]:0.0})
    for a in range (len(allWeaphons) - 1):
        p[i].weaphonsProbabilitys.update({allWeaphons[a]:0.0})
    for a in range (len(allSuspicious) - 1):
        p[i].suspiciousProbabilitys.update({allSuspicious[a]:0.0})

player1 = p[0]
player2 = p[1]
player3 = p[2]
player4 = p[3]
player5 = p[4]
player6 = p[5]
player7 = p[6]
player8 = p[7]
player9 = p[8]
player10 = p[9]

print("")

while True:
    playersNumT = input("How many players are playing (Max: 10): ")
    if playersNumT.isnumeric():
        if int(playersNumT) < 10 and int(playersNumT) >= 1:
            playersNum = int(playersNumT)
            break
noPlaying = 10-playersNum

names = []
for i in range(playersNum):
    question = "Name of the player" + str(i + 1) + ": "
    names.append(str(input(question)).lower())

for i in range(noPlaying):
    names.append("0")
    
player1.name = names[0]
player2.name = names[1]
player3.name = names[2]
player4.name = names[3]
player5.name = names[4]
player6.name = names[5]
player7.name = names[6]
player8.name = names[7]
player9.name = names[8]
player10.name = names[9]

playerList = (player1, player2, player3, player4, player5, player6, player8, player9, player10)

# UPDATE PROBABILITYS
def updateProbabilitys():
    for i in range(playersNum):
        playerList[i].posiblePlaces = [] #reset
        
        # First we reduce the list of possible cards that each player has
        if playerList[i].place != "":
            playerList[i].posiblePlaces = [playerList[i].place]
        else:
            for a in range(len(allPlaces)):
                if allPlaces[a] in playerList[i].noCards:
                    pass
                else:
                    playerList[i].posiblePlaces.append(allPlaces[a])

        if playerList[i].weaphon != "":
            playerList[i].posibleWeaphons = [playerList[i].place]
        else:
            for a in range(len(allWeaphons)):
                if allWeaphons[a] in playerList[i].noCards:
                    pass
                else:
                    playerList[i].posibleWeaphons.append(allWeaphons[a])
        
        if playerList[i].suspicious != "":
            playerList[i].posibleSuspicious = [playerList[i].suspicious]
        else:
            for a in range(len(allSuspicious)):
                if allSuspicious[a] in playerList[i].noCards:
                    pass
                else:
                    playerList[i].posibleSuspicious.append(allSuspicious[a])
                    
    for i in range(playersNum):
        ## ahora quedaria lo de las probabilidade y eso, pero eso es lo siguiente
        
        # en un principio las probabilidades de que tenga unas posibles cartas son iguales en muchas osea 1/len(posiblesCartas)
        # para solucionarlo tenemos que ver la probabilidad de que salgan esas cartas en todas osea 1/len(posiblesCartas) pero en todos los jugadores
        # para eso tenemos que hacer la suma de todas las probabilidades y la que menor suma tenga es la mas probable que no este en otros jugadores por lo que es mas probable que la tenga este jugador
        # asi que ahora podriamos hacer (sumaMaxima - suma) y ahi tendriamos la probabilidad, luego con una regla de tres ((1 * sumaPcarta) / sumaDeSumasDelJugador)
        
        ##############################################################################################################
        suma1 = 0
        placesProbs = []
        for a in range(len(playerList[i].posiblePlaces)): #calculate probability
            suma = 0.0
            for u in range(playersNum):
                if playerList[i].posiblePlaces[a] in playerList[u].posiblePlaces:
                    suma += (1/len(playerList[u].posiblePlaces))
                    
            suma = 1 - (suma/playersNum)
            probability = 1/len(playerList[i].posiblePlaces)
            
            if len(playerList[i].noCards) > 0:
                if probability > suma:
                    probability -= suma
                if probability < 0:
                   probability = 0.01
            else:
                probability -= suma
            suma1 += probability
            if suma1 == 0:
                suma1 = 1
            
            placesProbs.append(probability)
            
        for a in range(len(playerList[i].posiblePlaces)): #round to 0-1
            cardProbability = placesProbs[a]/suma1
            playerList[i].placesProbabilitys.update({playerList[i].posiblePlaces[a] : cardProbability})
        
        suma2 = 0
        weaphonsProbs = []
        for a in range(len(playerList[i].posibleWeaphons)): #calculate probability
            suma = 0.0
            for u in range(playersNum):
                if playerList[i].posibleWeaphons[a] in playerList[u].posibleWeaphons:
                    suma += (1/len(playerList[u].posibleWeaphons))
                    
            suma = 1 - (suma/playersNum)
            probability = 1/len(playerList[i].posibleWeaphons)
            
            if len(playerList[i].noCards) > 0:
                if probability > suma:
                    probability -= suma
                if probability < 0:
                   probability = 0.01
            else:
                probability -= suma
            suma2 += probability
            if suma2 == 0:
                suma2 = 1
            
            weaphonsProbs.append(probability)
        
        for a in range(len(playerList[i].posibleWeaphons)): #round to 0-1
            cardProbability = weaphonsProbs[a]/suma2
            playerList[i].weaphonsProbabilitys.update({playerList[i].posibleWeaphons[a] : cardProbability})
        
        suma3 = 0
        suspiciousProbs = []
        for a in range(len(playerList[i].posibleSuspicious)): #calculate probability
            suma = 0.0
            for u in range(playersNum):
                if playerList[i].posibleSuspicious[a] in playerList[u].posibleSuspicious:
                    suma += (1/len(playerList[u].posibleSuspicious))
                    
            suma = 1 - (suma/playersNum)
            probability = 1/len(playerList[i].posibleSuspicious)
            
            if len(playerList[i].noCards) > 0:
                if probability > suma:
                    probability -= suma
                if probability < 0:
                   probability = 0.01
            else:
                probability -= suma
            suma3 += probability
            if suma3 == 0:
                suma3 = 1
            
            suspiciousProbs.append(probability)
        
        for a in range(len(playerList[i].posibleSuspicious)): #round to 0-1
            cardProbability = suspiciousProbs[a]/suma3
            playerList[i].suspiciousProbabilitys.update({playerList[i].posibleSuspicious[a] : cardProbability})
            
        # SET MOST PROBABLE CARDS
        placeKey = max(playerList[i].placesProbabilitys)
        placeValue = playerList[i].placesProbabilitys[placeKey]
        
        weaphonKey = max(playerList[i].weaphonsProbabilitys)
        weaphonValue = playerList[i].weaphonsProbabilitys[weaphonKey]
        
        suspiciousKey = max(playerList[i].suspiciousProbabilitys)
        suspiciousValue = playerList[i].suspiciousProbabilitys[suspiciousKey]
        
        playerList[i].mostProbablePlace = {placeKey:placeValue}
        playerList[i].mostProbableWeaphon = {weaphonKey:weaphonValue}
        playerList[i].mostProbableSuspicious = {suspiciousKey:suspiciousValue}

updateProbabilitys() # this is for set all stadistics to 0 or initial probabilitys...

print("")

# OTHER STADISTICS
class suspicious():
    name = ""
    nameProbability = 0.0
    weaphon = ""
    weaphonProbability = 0.0
    place = ""
    placeProbability = 0.0
    
class askAbout():
    name = ""
    nameProbability = 0.0
    weaphon = ""
    weaphonProbability = 0.0
    place = ""
    placeProbability = 0.0

sus = suspicious()
ask = askAbout()

# OPTIONS
while True:
    option = input("What do you want to do? (show/add/help)")
    
    if option.lower() == "help":
        print(
            "\nHELP:"
            "'show' to see the probabilitys of a player",
            "\n'add' to add a information of a player",
        )
    
    elif option.lower() == "show":
        print("\nPLAYERS:")
        for i in range(playersNum):
            print(str(i + 1), "-", str(playerList[i].name))
        print(str(playersNum + 1), "-Suspicious")
        
        while True:
            selectPlayer = input("Player: ")
            
            isName = False
            isNum = False
            
            for i in range(playersNum):
                if selectPlayer == playerList[i].name:
                    isName = True
            if selectPlayer.isnumeric():
                if int(selectPlayer) >= 1 and int(selectPlayer) <= (playersNum + 1):
                    isNum = True
                    
            if (isName == True) or (isNum == True):
                print("\nPROBABILITY:")
                
                if isNum == True:
                    if int(selectPlayer) == 1:
                        print("Most probable place: ", player1.mostProbablePlace, "\nMost probable weaphon: ", player1.mostProbableWeaphon, "\nMost probable suspicious: ", player1.mostProbableSuspicious)
                    elif int(selectPlayer) == 2 and (playersNum + 1) > 2:
                        print("Most probable place: ", player2.mostProbablePlace, "\nMost probable weaphon: ", player2.mostProbableWeaphon, "\nMost probable suspicious: ", player2.mostProbableSuspicious)
                    elif int(selectPlayer) == 3 and (playersNum + 1) > 3:
                        print("Most probable place: ", player3.mostProbablePlace, "\nMost probable weaphon: ", player3.mostProbableWeaphon, "\nMost probable suspicious: ", player3.mostProbableSuspicious)
                    elif int(selectPlayer) == 4 and (playersNum + 1) > 4:
                        print("Most probable place: ", player4.mostProbablePlace, "\nMost probable weaphon: ", player4.mostProbableWeaphon, "\nMost probable suspicious: ", player4.mostProbableSuspicious)
                    elif int(selectPlayer) == 5 and (playersNum + 1) > 5:
                        print("Most probable place: ", player5.mostProbablePlace, "\nMost probable weaphon: ", player5.mostProbableWeaphon, "\nMost probable suspicious: ", player5.mostProbableSuspicious)
                    elif int(selectPlayer) == 6 and (playersNum + 1) > 6:
                        print("Most probable place: ", player6.mostProbablePlace, "\nMost probable weaphon: ", player6.mostProbableWeaphon, "\nMost probable suspicious: ", player6.mostProbableSuspicious)
                    elif int(selectPlayer) == 7 and (playersNum + 1) > 7:
                        print("Most probable place: ", player7.mostProbablePlace, "\nMost probable weaphon: ", player7.mostProbableWeaphon, "\nMost probable suspicious: ", player7.mostProbableSuspicious)
                    elif int(selectPlayer) == 8 and (playersNum + 1) > 8:
                        print("Most probable place: ", player8.mostProbablePlace, "\nMost probable weaphon: ", player8.mostProbableWeaphon, "\nMost probable suspicious: ", player8.mostProbableSuspicious)
                    elif int(selectPlayer) == 9 and (playersNum + 1) > 9:
                        print("Most probable place: ", player9.mostProbablePlace, "\nMost probable weaphon: ", player9.mostProbableWeaphon, "\nMost probable suspicious: ", player9.mostProbableSuspicious)
                    elif int(selectPlayer) == 10 and (playersNum + 1) > 10:
                        print("Most probable place: ", player10.mostProbablePlace, "\nMost probable weaphon: ", player10.mostProbableWeaphon, "\nMost probable suspicious: ", player10.mostProbableSuspicious)
                    if int(selectPlayer) == playersNum + 1: ### SUSPICIOUS: CRIME SCENE, MURDER WEAPHON, MURDERER
                        placeKey = ""
                        placeValue = 1
                        for a in range(len(allPlaces)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].placesProbabilitys[allPlaces[a]]
                                except:
                                    pass
                                
                            if suma < placeValue:
                                placeValue = suma
                                placeKey = allPlaces[a]
                            suma = suma/playersNum
                        placeValue = 1 - placeValue      
                        
                        weaphonKey = ""
                        weaphonValue = 1
                        for a in range(len(allWeaphons)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].weaphonsProbabilitys[allWeaphons[a]]
                                except:
                                    pass
                                
                            if suma < weaphonValue:
                                weaphonValue = suma
                                weaphonKey = allWeaphons[a]
                            suma = suma/playersNum
                        weaphonValue = 1 - weaphonValue  
                            
                        suspiciousKey = ""
                        suspiciousValue = 1
                        for a in range(len(allSuspicious)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].suspiciousProbabilitys[allSuspicious[a]]
                                except:
                                    pass
                                
                            if suma < suspiciousValue:
                                suspiciousValue = suma
                                suspiciousKey = allSuspicious[a]
                            suma = suma/playersNum
                        suspiciousValue = 1 - suspiciousValue  
                        
                        print("SUSPICIOUS:", "\n    ·Crime Scene: ", placeKey, " : ", placeValue, "\n    ·Murder Weapon: ", weaphonKey, " : ", weaphonValue, "\n    ·Murderer: ", suspiciousKey, " : ", suspiciousValue)
                        
                else:
                    if selectPlayer.lower() == player1.name:
                        print("Most probable place: ", player1.mostProbablePlace, "\nMost probable weaphon: ", player1.mostProbableWeaphon, "\nMost probable suspicious: ", player1.mostProbableSuspicious)
                    elif selectPlayer.lower() == player2.name:
                        print("Most probable place: ", player2.mostProbablePlace, "\nMost probable weaphon: ", player2.mostProbableWeaphon, "\nMost probable suspicious: ", player2.mostProbableSuspicious)
                    elif selectPlayer.lower() == player3.name:
                        print("Most probable place: ", player3.mostProbablePlace, "\nMost probable weaphon: ", player3.mostProbableWeaphon, "\nMost probable suspicious: ", player3.mostProbableSuspicious)
                    elif selectPlayer.lower() == player4.name:
                        print("Most probable place: ", player4.mostProbablePlace, "\nMost probable weaphon: ", player4.mostProbableWeaphon, "\nMost probable suspicious: ", player4.mostProbableSuspicious)
                    elif selectPlayer.lower() == player5.name:
                        print("Most probable place: ", player5.mostProbablePlace, "\nMost probable weaphon: ", player5.mostProbableWeaphon, "\nMost probable suspicious: ", player5.mostProbableSuspicious)
                    elif selectPlayer.lower() == player6:
                        print("Most probable place: ", player6.mostProbablePlace, "\nMost probable weaphon: ", player6.mostProbableWeaphon, "\nMost probable suspicious: ", player6.mostProbableSuspicious)
                    elif selectPlayer.lower() == player7:
                        print("Most probable place: ", player7.mostProbablePlace, "\nMost probable weaphon: ", player7.mostProbableWeaphon, "\nMost probable suspicious: ", player7.mostProbableSuspicious)
                    elif selectPlayer.lower() == player8:
                        print("Most probable place: ", player8.mostProbablePlace, "\nMost probable weaphon: ", player8.mostProbableWeaphon, "\nMost probable suspicious: ", player8.mostProbableSuspicious)
                    elif selectPlayer.lower() == player9:
                        print("Most probable place: ", player9.mostProbablePlace, "\nMost probable weaphon: ", player9.mostProbableWeaphon, "\nMost probable suspicious: ", player9.mostProbableSuspicious)
                    elif selectPlayer.lower() == player10:
                        print("Most probable place: ", player10.mostProbablePlace, "\nMost probable weaphon: ", player10.mostProbableWeaphon, "\nMost probable suspicious: ", player10.mostProbableSuspicious)
                    if selectPlayer.lower() == "suspicious": ### SUSPICIOUS: CRIME SCENE, MURDER WEAPHON, MURDERER
                        placeKey = ""
                        placeValue = 1
                        for a in range(len(allPlaces)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].placesProbabilitys[allPlaces[a]]
                                except:
                                    pass
                                
                            if suma < placeValue:
                                placeValue = suma
                                placeKey = allPlaces[a]
                            suma = suma/playersNum
                        placeValue = 1 - placeValue      
                        
                        weaphonKey = ""
                        weaphonValue = 1
                        for a in range(len(allWeaphons)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].weaphonsProbabilitys[allWeaphons[a]]
                                except:
                                    pass
                                
                            if suma < weaphonValue:
                                weaphonValue = suma
                                weaphonKey = allWeaphons[a]
                            suma = suma/playersNum
                        weaphonValue = 1 - weaphonValue  
                            
                        suspiciousKey = ""
                        suspiciousValue = 1
                        for a in range(len(allSuspicious)):
                            suma = 0
                            for u in range(playersNum):
                                try:
                                    suma += playerList[u].suspiciousProbabilitys[allSuspicious[a]]
                                except:
                                    pass
                                
                            if suma < suspiciousValue:
                                suspiciousValue = suma
                                suspiciousKey = allSuspicious[a]
                            suma = suma/playersNum
                        suspiciousValue = 1 - suspiciousValue  
                        
                        print("SUSPICIOUS:", "\n    ·Crime Scene: ", placeKey, " : ", placeValue, "\n    ·Murder Weapon: ", weaphonKey, " : ", weaphonValue, "\n    ·Murderer: ", suspiciousKey, " : ", suspiciousValue)
                break
            else:
                print("Shomething is WRONG!\nTry Again\n")
    
    elif option.lower() == "add":
        while True:
            print("\nOPTIONS:", "\n    1-card that a player has", "\n    2-card that a player doesn't have")
            option = input("Option: ")
            
            if option.lower() == "card that a player has" or option == "1":
                print("Select Player:")
                for i in range(playersNum):
                    print(str(i + 1), "-", str(playerList[i].name))
                
                playeradd = input("Player: ")
                
                playNum = 1
                
                if playeradd.lower() == player1.name.lower() or playeradd == "1":
                    playNum = 1
                if playeradd.lower() == player2.name.lower() or playeradd == "2":
                    playNum = 2
                if playeradd.lower() == player3.name.lower() or playeradd == "3":
                    playNum = 3
                if playeradd.lower() == player4.name.lower() or playeradd == "4":
                    playNum = 4
                if playeradd.lower() == player5.name.lower() or playeradd == "5":
                    playNum = 5
                if playeradd.lower() == player6.name.lower() or playeradd == "6":
                    playNum = 6
                if playeradd.lower() == player7.name.lower() or playeradd == "7":
                    playNum = 7
                if playeradd.lower() == player8.name.lower() or playeradd == "8":
                    playNum = 8
                if playeradd.lower() == player9.name.lower() or playeradd == "9":
                    playNum = 9
                if playeradd.lower() == player10.name.lower() or playeradd == "10":
                    playNum = 10
                
                card = input("\nCard: ")
                category = input("Category of the card (place/weaphon/suspicious): \n")
                
                if category.lower() == "place":
                    playerList[playNum - 1].place = card
                elif category.lower() == "weaphon":
                    playerList[playNum - 1].weaphon = card
                elif category.lower() == "suspicious":
                    playerList[playNum - 1].suspicious = card
                else:
                    print("Something is WRONG!\n Try again")
                print("Card ", card , " has been added to player ", playerList[playNum -1].name)
                updateProbabilitys()
                break
            
            elif option.lower() == "card that a player doesn't have" or option == "2":
                print("Select Player:")
                for i in range(playersNum):
                    print(str(i + 1), "-", str(playerList[i].name))
                
                playeradd = input("Player: ")
                
                playNum = 1
                
                if playeradd.lower() == player1.name.lower() or playeradd == "1":
                    playNum = 1
                if playeradd.lower() == player2.name.lower() or playeradd == "2":
                    playNum = 2
                if playeradd.lower() == player3.name.lower() or playeradd == "3":
                    playNum = 3
                if playeradd.lower() == player4.name.lower() or playeradd == "4":
                    playNum = 4
                if playeradd.lower() == player5.name.lower() or playeradd == "5":
                    playNum = 5
                if playeradd.lower() == player6.name.lower() or playeradd == "6":
                    playNum = 6
                if playeradd.lower() == player7.name.lower() or playeradd == "7":
                    playNum = 7
                if playeradd.lower() == player8.name.lower() or playeradd == "8":
                    playNum = 8
                if playeradd.lower() == player9.name.lower() or playeradd == "9":
                    playNum = 9
                if playeradd.lower() == player10.name.lower() or playeradd == "10":
                    playNum = 10
                
                card = input("\nCard: ")
                
                playerList[playNum - 1].noCards.append(card)

                print("Card ", card , " has been added to player ", playerList[playNum -1].name)
                updateProbabilitys()
                break
            
            else:
                print("Something is WRONG!\nTry Again\n")
    
    else:
        print("Something is WRONG!\nTry Again")
    
    time.sleep(3)
    print("")
    time.sleep(0.05)
    print("")
    time.sleep(0.025)
    print("")
    time.sleep(0.01)
    print("")
    time.sleep(0.005)
    print("")
