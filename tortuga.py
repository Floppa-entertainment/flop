import turtle

t=turtle.Turtle()
t.speed(0)
t.shape("turtle")        
def cuadrado(tortuga,lado):
    for i in range(0,4):
        tortuga.fd(lado)
        tortuga.left(90)


def triangulo(tortuga,lado):
    for i in range(0,3):
        tortuga.left(120)
        tortuga.fd(lado)

def poli(tortuga,n,lado):
    for i in range(0,n):
        tortuga.left(360/n)
        tortuga.fd(lado)
