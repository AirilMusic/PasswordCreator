#Made by Airil
while True:
    periLeght=int(input("Please, put the length of the perimeter: "))
    parcblock=0

    for i in range(periLeght-5):
        parcblock=parcblock+1
        
        if periLeght%parcblock == 0:
            print(int(periLeght/parcblock), " plots of ", parcblock, " blocks")
    print("\n")