while True:
    num = int(input("Write the first number to analize: "))
    if num == 0 or num == 1:
        num = 1
    tryingNum = num
    stopNum = int(input("Write a number to stop in that: "))

    #GENERA LOS PRIMOS
    listPrimos = []

    for numero in range(num, stopNum): #Agradecimientos a EDDxample por ayudarme con esta parte
        flag = True

        for divisor in range (2, numero):
            if numero % divisor == 0:
                flag = False
                break
        if flag:
            listPrimos.append(numero)
    #print(listPrimos)

    #ANALIZA LOS PRIMOS Y SOLO DEJA LOS GEMELOS
    tryingNum = num

    if (int(listPrimos[1])-int(listPrimos[0])) == 2:
        print(listPrimos[observer2], listPrimos[observer3])
    else:
        listPrimos.pop(0)

    observer1 = 0
    observer2 = 1
    observer3 = 3

    while True:
        if int(listPrimos[observer2]) - int(listPrimos[observer1]) == 2:
            print(listPrimos[observer1], listPrimos[observer2]) 
        elif int(listPrimos[observer3]) - int(listPrimos[observer2]) == 2:
            print(listPrimos[observer2], listPrimos[observer3])
        else:
            listPrimos.pop(observer1)

        if observer3 == len(listPrimos):
            break

        observer1 += 1
        observer2 += 1
        observer3 += 1
    
    #print(listPrimos)
    print("\n¡Finished!", "\n")