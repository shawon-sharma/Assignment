import turtle  # Allows us to use turtles
import time

turtle.setup(1600, 800)  # Determine the window size
wn = turtle.Screen()  # Creates a playground for turtles
wn.title('traffic light using different turtles')  # Set the window title
wn.bgcolor('black')  # Set the window background color
tess = turtle.Turtle()  # Create a turtle, assign to tess
an_tess = turtle.Turtle()  # Create a turtle, assign to tess
road = turtle.Turtle()  # create a turtle, assign to road
pm_road = turtle.Turtle()  # create a turtle, assign to primary road

henry = turtle.Turtle()  # Create henry
pmcar1 = turtle.Turtle()  # create car
an_tess_red=turtle.Turtle()

#making car for the secondary road through turtle module
pmcar2 = turtle.Turtle()  # create car
pmcar2.hideturtle()


pmcar3 = turtle.Turtle()
pmcar3.hideturtle()


pmcar4 = turtle.Turtle()


pmcar5 = turtle.Turtle()
pmcar5.hideturtle()


# creating car for primary road
car1= turtle.Turtle()#create car for primary road
car2=turtle.Turtle()#creeate 2nd car for primary road
car2.hideturtle()


screen = turtle.Screen()
turtle.tracer(0, 0)

#draw time changes
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.setx(170)
pen.sety(-160)


#draw timer
box = turtle.Turtle()
box.hideturtle()
box.color("white")
box.pensize(5)
box.penup()
box.setx(150)
box.sety(-200)
box.pendown()
box.forward(250)
box.left(90)
box.forward(150)
box.left(90)
box.forward(300)
box.left(90)
box.forward(150)
box.left(90)
box.forward(150)



#setting up initial time
num =30 #considering it as second
minute = 0
hours = 0
stop = False

pen.write(str(hours)+":"+str(minute)+":"+str(num), font=("Arial", 50))

def countDownTimer():
    global num;
    while True:
        num -= 1;
        time.sleep(1)
        pen.clear()
        if num >= 0:
            pen.write(str(hours) + ":" + str(minute) + ":" + str(num), font=("Arial", 50))
        else:
            break



# road for primary road with blue color
def draw_primaryroad():
    """ Draw a nice housing to hold the traffic lights"""
    pm_road.pensize(3)  # Change tess' pen width
    pm_road.color('black', 'white')  # Set tess' color
    pm_road.begin_fill()  # Tell tess to start filling the color
    pm_road.forward(500)  # Tell tess to move forward by 80 units
    pm_road.left(90)  # Tell tess to turn left by 90 degrees
    pm_road.forward(300)
    pm_road.left(90)
    # tess.circle(20, 180)  # Tell tess to draw a semi-circle
    pm_road.forward(1200)
    pm_road.left(-90)
    pm_road.forward(-300)
    pm_road.right(90)
    pm_road.forward(400)
    pm_road.end_fill()  # Tell tess to stop filling the color


draw_primaryroad()


def another_draw_housing():
    """ Draw a nice housing to hold the traffic lights"""

    an_tess.penup()
    an_tess.goto(0, 300)
    an_tess.pendown()
    an_tess.pensize(3)  # Change tess' pen width
    an_tess.color('green', 'white')  # Set tess' color
    an_tess.begin_fill()  # Tell tess to start filling the color

    an_tess.forward(40)  # Tell tess to move forward by 80 units
    an_tess.left(90)  # Tell tess to turn left by 90 degrees
    an_tess.forward(50)
    an_tess.circle(20, 180)  # Tell tess to draw a semi-circle
    an_tess.forward(50)
    an_tess.left(90)
    an_tess.end_fill()  # Tell tess to stop filling the color



another_draw_housing()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)  # Change tess' pen width
    tess.color('red', 'white')  # Set tess' color
    tess.begin_fill()  # Tell tess to start filling the color
    tess.forward(40)  # Tell tess to move forward by 80 units
    tess.left(90)  # Tell tess to turn left by 90 degrees
    tess.forward(60)
    tess.circle(20, 180)  # Tell tess to draw a semi-circle
    tess.forward(60)
    tess.left(90)
    tess.end_fill()  # Tell tess to stop filling the color


draw_housing()

#drawing raffic light cirlce
def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()  # This allows us to move a turtle without drawing a line
    t.forward(20)
    t.left(90)
    t.forward(ht)
    t.shape('circle')  # Set tutle's shape to circle
    t.shapesize(1)  # Set size of circle
    t.fillcolor(colr)  # Fill color in circle


circle(tess, 20, 'gray')
circle(henry, 60, 'gray')
circle(an_tess,20,'gray')
circle(an_tess_red,350,'gray')


state_num = 0;

#maintaining traffic light from here
def advance_state_machine():
    """A state machine for traffic light"""
    global state_num  # Tells Python not to create a new local variable for state_num

    if state_num == 0:
        henry.color('darkgray')
        tess.color('red')
        an_tess.color("green")
        an_tess_red.color("gray")

    else:
        henry.color('green')
        tess.color("darkgray")
        an_tess_red.color("red")
        an_tess.color("gray")

# drawing road for secondary road
def draw_road():
    """ Draw a nice housing to hold the traffic lights"""
    road.pensize(3)  # Change tess' pen width
    road.color('black', 'gray')  # Set tess' color
    road.begin_fill()  # Tell tess to start filling the color
    road.forward(-300)  # Tell tess to move forward by 80 units
    road.left(-90)  # Tell tess to turn left by 90 degrees
    road.forward(400)
    road.left(-90)
    # tess.circle(20, 180)  # Tell tess to draw a semi-circle
    road.forward(-300)
    road.left(-90)
    road.end_fill()  # Tell tess to stop filling the color


draw_road()


car1.color('purple')
car1.shape('turtle')
car1.penup()
car1.goto(-600, 100)
car1.showturtle()

car2.color('purple')
car2.shape('turtle')
car2.penup()
car2.goto(-600, 100)






# car for secondary road
pmcar1.color('purple')
pmcar1.shape('turtle')
pmcar1.penup()
pmcar1.left(90)
pmcar1.goto(-200, -400)


pmcar2.color('green')
pmcar2.shape('turtle')
pmcar2.penup()
pmcar2.left(90)
pmcar2.goto(-150, -400)

pmcar3.color('black')
pmcar3.shape('turtle')
pmcar3.penup()
pmcar3.left(90)
pmcar3.goto(-150, -400)

pmcar4.color('green')
pmcar4.shape('turtle')
pmcar4.penup()
pmcar4.left(90)
pmcar4.goto(-150, -400)

pmcar5.color('purple')
pmcar5.shape('turtle')
pmcar5.penup()
pmcar5.left(90)
pmcar5.goto(-150, -400)

def trafficLight():
    henry.color('darkgray')
    tess.color('red')
    an_tess.color("green")
    an_tess_red.color("gray")
    for i in range(9):
        car2.forward(100)


def collision():
    global state_num
    if pmcar1.ycor()>0 and pmcar2.ycor()>0 and pmcar3.ycor()>0 and pmcar4.ycor()>0 and pmcar5.ycor()>0:
        print("there is no car in the street")
        print("for car1 : " + str(pmcar1.ycor()))
        print("for car2 : " + str(pmcar2.ycor()))
        print("for car3 : " + str(pmcar3.ycor()))
        print("for car4 : " + str(pmcar4.ycor()))
        print("for car5 : " + str(pmcar5.ycor()))
        state_num=0
        advance_state_machine()
    else:
        print("still the car needs to pass the street")
        state_num=1
        advance_state_machine()

turtle.update()
turtle.tracer(1,50)

def movement():
    global state_num
    global num

    for movement in range(250):

        if pmcar1.ycor() <= 1:
            pmcar1.forward(42.5)

        if movement > 4.5:
            pmcar2.showturtle()
            if pmcar2.ycor() <= 1:
                pmcar2.forward(42.5)

        if movement > 9:
            pmcar3.showturtle()
            if pmcar3.ycor() <= 1:
                pmcar3.forward(42.5)

        if movement > 14:
            pmcar4.showturtle()
            if pmcar4.ycor() <= 1:
                pmcar4.forward(42.5)

        if movement > 24:
            pmcar5.showturtle()
            if pmcar5.ycor() <= 1:
                pmcar5.forward(42.5)

        if num > 0:

            if pmcar1.ycor() > 0 and pmcar2.ycor() > 0 and pmcar3.ycor() > 0 and pmcar4.ycor() > 0 and pmcar5.ycor() > 0:
                trafficLight()
                break

            num -= 1
            if num == 0:
                num += 30

            time.sleep(1)
            pen.clear()
            pen.write(str(hours) + ":" + str(minute) + ":" + str(num), font=("Arial", 50))

for i in range(250):
    state_num=0
    advance_state_machine()
    if car1.xcor()<510:
        car1.forward(100)
    else:
        car2.showturtle()
        if car2.xcor() < -300:
            car2.forward(10)
        if car2.xcor() >= -300:
            state_num = 1
            advance_state_machine()
            movement()
            break

wn.mainloop()  # Wait for user to close window
