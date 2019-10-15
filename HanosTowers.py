def menu(option):
    if str.upper(option) == "A":
        disks = 4
        castle = fillTowers(disks)      
        print(castle)
        hano(castle, disks)
    else:
        disks = int(input("Enter the number of disks: "))
        castle = fillTowers(disks)      
        print(castle)
        hano(castle, disks)    
        

def fillTowers(disks):
    castle =  {'t1':[],'t2':[],'t3':[]}
    aux = 0
    for x in castle.values():
        for y in range(disks):
            if aux!=disks:
                x.append(str(aux))
                aux= aux+1
            else:
                x.append(" ")
    return castle

def hano(place, n, inicial='t1', temporal='t2', final='t3'):
    if n>0:
        hano(place, n-1, inicial, final, temporal)
        print("\nIt moves from ", inicial, " to ",final)
        grafhano(place, inicial, final)    
        hano(place, n-1, temporal, inicial, final)
    
def grafhano(place, inicial, final):
    x = place[inicial]
    y = place[final]
    aux = len(y)-1
    for i in x:
        if i != " ":
            for j in reversed(y):
                if j == " ":
                    y[aux] = x[x.index(i)]
                    x[x.index(i)] = " "
                    print(place)
                    break
                aux-=1
            break

print("Wolcome to hano's game")
menu(input("Push A for 4 disks\nor push B for n disks\n"))