import turtle

szerokosc_domu=200
wysokosc_domu=150
szerokosc_okna=30
wysokosc_okna=30
szerokosc_drzwi=30
wysokosc_drzwi=40
wysokosc_plotu=50
szerokosc_deski=8

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
    z.forward(a)
    z.left(120)
    z.forward(a)
    z.left(120)
    z.forward(a) 

def plot(n):
    xpos=szerokosc_domu
    ypos=wysokosc_domu-wysokosc_plotu
    z.color("black", "green")
    #pionowe deski
    
    for i in range(n):
        z.penup()
        z.goto(xpos,-ypos)
        z.pendown()
        z.begin_fill()
        prostokat(szerokosc_deski, wysokosc_plotu)
        z.end_fill()
        xpos=xpos+szerokosc_deski*2
    
    #poziome deski
    z.color("black", "black")
    z.penup()    
    z.goto(szerokosc_domu,-wysokosc_domu+6)
    z.setheading(0)
    z.pendown()
    z.begin_fill()
    prostokat(n*szerokosc_deski*2-szerokosc_deski, 4)
    z.end_fill()
   
    z.penup()    
    z.goto(szerokosc_domu,-wysokosc_domu+wysokosc_plotu-4)
    z.setheading(0)
    z.pendown()
    z.begin_fill()
    prostokat(n*szerokosc_deski*2-szerokosc_deski, 4)
    z.end_fill()

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


#okno 1
z.home()
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