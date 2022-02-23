from io import open

#lo han calculado matematicamente hasta 5.764.000.000.000.000.000
#en teoria ya se ha calculado hasta este numero 295.147.905.179.352.825.856 con computacion, asi que tengo que empezar a partir de ahi
#he analizado hasta: 295147905179570000000

while True:
    num=int(input("Write a number please: "))
    tryingNum=num
    stopNum=int(input("Write a number to stop in that: "))

    listNums=[]
    archivo_texto=open("lista_numeros.txt", "w")

    bucle=True

    print("PROCESING...")

    while bucle==True:
        #Try a single number
        '''num=int(input("write a number please: "))
        tryingNum=num
        counter=0
        buscando=True
        listNums=[]

        while buscando==True:
            if tryingNum%2==0:
                tryingNum=tryingNum/2
            else:
                tryingNum=(tryingNum*3)+1

            if tryingNum==1:
                print("Este numero no es :(")
                buscando=False

            if counter==10000:
                listNums.append(num)
                buscando=False
                print("¡Posible numero encontrado! (necesita probarse en profundidad)")
                print(num)
            
            counter=counter+1'''

        counter=0
        buscando=True

        #print(tryingNum)

        if tryingNum==stopNum:
            buscando=False
            print("¡Finished!")
            bucle=False

        while buscando==True:
            if tryingNum%2==0:
                tryingNum=tryingNum/2
            else:
                tryingNum=(tryingNum*3)+1

            if tryingNum==1:
                #print("Este numero no es :(")
                buscando=False

            if counter==10000:
                listNums.append(tryingNum)
                buscando=False
                archivo_texto.write(tryingNum)
                print("¡Posible numero encontrado! (necesita probarse en profundidad)")
                print(tryingNum)

            counter=counter+1

        num=num+1
        tryingNum=num

