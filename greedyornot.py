n= int(input(""))

l = list(map(int, input().split()[:n]))
#l=list(map(int,input("").split(" ")))

p1=0
p2=0


while len(l)!=0:

    if l[0]<l[-1]:

            p1+=l[-1]
            del(l[-1])

    else:
        p1+=l[0]
        del(l[0])

    if len(l)==0:
        if p1>p2:
            print("p1 wins!")
            break
        elif p2>p1:
            print("p2 wins!")
            break
        else:
            print("It's a draw")
            break

    if l[0]<l[-1]:

            p2+=l[-1]
            del(l[-1])

    else:
        p2+=l[0]
        del(l[0])


    if len(l)==0:
        if p1>p2:
            print("p1 wins!")
            break

        elif p2>p1:
            print("p2 wins!")
            break
        else:
            print("Its a draw")