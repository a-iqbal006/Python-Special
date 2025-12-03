from random import *
from turtle import *
import random as r


x = []
speed(0)

bgcolor('black')
N=int(input("Enter a Degree : "))
def kolor(R,G,B):
    colormode(255)
    color(R,G,B)

def Limit(k,l,m,n):
    x,y=position()

    if abs(x)>m or abs(y)>n:
        penup()
        goto(k,l)
        pendown()

for i in range(1000):
    o=r.randint(1,20)
    x.append(o*10)

for j in x :
    X = randint(50,255)
    Y = randint(50,255)
    Z = randint(50,255)
    
    kolor(X,Y,Z)

    a=r.randint(0,1)
    if a == 0:
        fd(j)
    elif(1):
        bk(j)

    right(N)
    b=randint(1,499)

    Limit(b,0,600,300)

done()