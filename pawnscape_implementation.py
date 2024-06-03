
n=int(input("Enter a number :"))
a=[]
for i in range(0,n):
    b=[]
    for j in range(0,n):
        b.append("-")
    a.append(b)

for i in range(0,n):
    a[0][i]='B'

for i in range(0,n):
    a[n-1][i]='W'

def printing():
    print(" ",end=" ")
    for k in range(0,n):
        print(k,end=" ")

    print()

    for i in range(0,n):
        print(i,end=" ")
        for j in range(0,n):
            print(a[i][j],end=' ')
        print()

def updation(a,move,c):
    cur,fin=move/100,move%100
    curx=cur/10
    cury=cur%10
    finx=fin/10
    finy=fin%10
    a[int(finx)][int(finy)]=c
    a[int(curx)][int(cury)]='-'


def play():
    while True:
        printing()
        move=int(input(("Enter white move: ")))
        updation(a,move,'W')
        printing()


        move=int(input(("Enter black move: ")))
        updation(a,move,'B')


play()
  







