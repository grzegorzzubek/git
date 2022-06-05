import turtle
import math

szerokosc_domu=200
wysokosc_domu=100
szerokosc_okna=30
wysokosc_okna=20
szerokosc_drzwi=30
wysokosc_drzwi=30
z=turtle.Turtle()

z.shape("turtle")


def prostokat(a, b):
    z.forward(a)
    z.right(90)
    z.forward(b)
    z.right(90)
    z.forward(a)
    z.right(90)
    z.forward(b)
    z.right(90)

def trojkat(a):
    #c=math.sqrt(pow(a/2,2)+pow(h,2))
    z.forward(a)
    z.left(120)
    z.forward(a)
    z.left(120)
    z.forward(a) 
#sc = turtle.Screen()

def plot(n):
    xpos=szerokosc_domu
    ypos=wysokosc_domu-30
    for i in range(n):
        z.penup()
        z.goto(xpos,-ypos)
        z.pendown()
        prostokat(8, 30)
        xpos=xpos+8*2
    z.penup()    
    z.goto(szerokosc_domu,-wysokosc_domu+6)
    z.setheading(0)
    z.pendown()
    prostokat(n*8*2-8, 4)

    z.penup()    
    z.goto(szerokosc_domu,-wysokosc_domu+30-4)
    z.setheading(0)
    z.pendown()
    prostokat(n*8*2-8, 4)

def promienie_slonca():
    pos=z.position()
    xcenter=pos[0]
    ycenter=pos[1]+20
    z.setheading(-90)
    z.width(2)
    z.pencolor("orange")
    for i in range(12):
        z.penup()
        z.goto(xcenter,ycenter)
        z.right(30)
        z.forward(20)
        z.pendown()
        z.forward(20)


     
 
#quit()
#blok
z.color("black", "red")
z.begin_fill()
prostokat(szerokosc_domu, wysokosc_domu)
z.end_fill()

#dach
z.home()
z.color("black", "yellow")
z.begin_fill()
trojkat(szerokosc_domu)
z.end_fill()
z.color("black", "black")

z.home()

#okno 1
z.penup()
z.goto(20,-20)
z.pendown()
prostokat(szerokosc_okna,wysokosc_okna)

#okno 2
z.penup()
z.goto(szerokosc_domu-szerokosc_okna-20,-20)
z.pendown()
prostokat(szerokosc_okna,wysokosc_okna)

#drzwi
z.penup()
z.goto(szerokosc_domu/2-szerokosc_drzwi/2,-(wysokosc_domu-wysokosc_drzwi))
z.pendown()
prostokat(szerokosc_drzwi,wysokosc_drzwi)

 
#plot
plot(5)


#slonce
z.penup()
z.goto(szerokosc_domu+50,wysokosc_domu-50)
z.pendown()
z.color("orange", "yellow")
z.begin_fill()
z.circle(20)
z.end_fill()

promienie_slonca()
z.hideturtle()

turtle.exitonclick()