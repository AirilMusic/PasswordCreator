#### CLUEDO CHEATS UWU ####
## Made by Airil/Ainhoa/Ari (we are the same person)
#28-10-2022

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

while True:
    add = input("Add a weaphon (exit if there is no more): ")
    if add.lower() == "exit":
        break
    else:
        allWeaphons.append(add.lower())
        
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
        
        cards = []
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
    
    for a in range (len(allPlaces)):
        p[i].placesProbabilitys.update({allPlaces[a]:0.0})
    for a in range (len(allPlaces)):
        p[i].weaphonsProbabilitys.update({allWeaphons[a]:0.0})
    for a in range (len(allWeaphons)):
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
    option = input("What do you want to do? (show/add/ask/question)")
    
    if option.lower() == "help":
        print(
            "\nHELP:"
            "'show' to see the probabilitys of a player",
            "\n'add' to add a information of a player",
            "\n'question' best question about suspicious, weaphon and place"
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

            if isName == True or isNum == True:
                print("\nPROBABILITY:")
                if selectPlayer.isnumeric():
                    if int(selectPlayer) == 1:
                        print("Most probable place: ", player1.mostProbablePlace, "\nMost probable weaphon: ", player1.mostProbableWeaphon, "\nMost probable suspicious: ", player1.mostProbableSuspicious)
                    elif int(selectPlayer) == 2 and playersNum < 1:
                        print("Most probable place: ", player2.mostProbablePlace, "\nMost probable weaphon: ", player2.mostProbableWeaphon, "\nMost probable suspicious: ", player2.mostProbableSuspicious)
                    elif int(selectPlayer) == 3 and playersNum < 2:
                        print("Most probable place: ", player3.mostProbablePlace, "\nMost probable weaphon: ", player3.mostProbableWeaphon, "\nMost probable suspicious: ", player3.mostProbableSuspicious)
                    elif int(selectPlayer) == 4 and playersNum < 3:
                        print("Most probable place: ", player4.mostProbablePlace, "\nMost probable weaphon: ", player4.mostProbableWeaphon, "\nMost probable suspicious: ", player4.mostProbableSuspicious)
                    elif int(selectPlayer) == 5 and playersNum < 4:
                        print("Most probable place: ", player5.mostProbablePlace, "\nMost probable weaphon: ", player5.mostProbableWeaphon, "\nMost probable suspicious: ", player5.mostProbableSuspicious)
                    elif int(selectPlayer) == 6 and playersNum < 5:
                        print("Most probable place: ", player6.mostProbablePlace, "\nMost probable weaphon: ", player6.mostProbableWeaphon, "\nMost probable suspicious: ", player6.mostProbableSuspicious)
                    elif int(selectPlayer) == 7 and playersNum < 6:
                        print("Most probable place: ", player7.mostProbablePlace, "\nMost probable weaphon: ", player7.mostProbableWeaphon, "\nMost probable suspicious: ", player7.mostProbableSuspicious)
                    elif int(selectPlayer) == 8 and playersNum < 7:
                        print("Most probable place: ", player8.mostProbablePlace, "\nMost probable weaphon: ", player8.mostProbableWeaphon, "\nMost probable suspicious: ", player8.mostProbableSuspicious)
                    elif int(selectPlayer) == 9 and playersNum < 8:
                        print("Most probable place: ", player9.mostProbablePlace, "\nMost probable weaphon: ", player9.mostProbableWeaphon, "\nMost probable suspicious: ", player9.mostProbableSuspicious)
                    elif int(selectPlayer) == 10 and playersNum < 9:
                        print("Most probable place: ", player10.mostProbablePlace, "\nMost probable weaphon: ", player10.mostProbableWeaphon, "\nMost probable suspicious: ", player10.mostProbableSuspicious)
                    if selectPlayer == playersNum + 1:
                        pass
                    ####################################### falta el sospechoso
                        
                else:
                    if selectPlayer.lower() == player1.name:
                        print(player1.probabilitys)
                    elif selectPlayer.lower() == player2.name:
                        print(player2.probabilitys)
                    elif selectPlayer.lower() == player3.name:
                        print(player3.probabilitys)
                    elif selectPlayer.lower() == player4.name:
                        print(player4.probabilitys)
                    elif selectPlayer.lower() == player5.name:
                        print(player5.probabilitys)
                    elif selectPlayer.lower() == player6:
                        print(player6.probabilitys)
                    elif selectPlayer.lower() == player7:
                        print(player7.probabilitys)
                    elif selectPlayer.lower() == player8:
                        print(player8.probabilitys)
                    elif selectPlayer.lower() == player9:
                        print(player9.probabilitys)
                    elif selectPlayer.lower() == player10:
                        print(player10.probabilitys)
                    if selectPlayer.lower() == "suspicious":
                        pass
                        ####################################### falta el sospechoso
                
                break
            
            else:
                print("Shomething is WRONG!\nTry Again\n")
            
        
    
    elif option.lower() == "add":
        pass
    
    else:
        print("Shomething is WRONG!\nTry Again")
        
    print("\n\n\n\n\n")
