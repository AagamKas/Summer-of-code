a = list(map(int, input("Enter space-separated integers: ").split(" ")))

def printing(a):
    for i in a:
        for x in range(0,i):
            print("|",end=" ")
        print()


def sum_match(a):
    sum=0
    for x in a:
        sum+=x

    return sum



def playing(a):
    printing(a)
    while(sum_match(a)!=0):
        #p1 play
        print("p1 plays: ")
        b=list(map(int,input("Enter row number and number of matches separated by spaces: ").split(" ")))
        a[b[0]]-=b[1]

        printing(a)

        if sum_match(a)==1:
            print("p1 won")
            break
        
        print("p2 plays: ")
        b=list(map(int,input("Enter row number and number of matches separated by spaces: ").split(" ")))
        a[b[0]]-=b[1]

        printing(a)

        if sum_match(a)==1:
            print("p2 won")
            break

        #printing(a)

playing(a)





        
