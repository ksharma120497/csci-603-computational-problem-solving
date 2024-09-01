import math
import turtle

'''
Author Kapil Sharma ks4643
Quilt Design Pattern HW1
'''

# Initialing Turtle class to use all its methods
t = turtle.Turtle()


# Main function containing three functions for three patterns
def main():
    patternone()
    patterntwo()
    patternthree()
    t.screen.mainloop()


'''
This function is used for finding 
the center point in the box
'''


def findcenter():
    t.back(100)
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()

'''
Quilt Pattern One

The Design is making a pattern that looks like Deadpool

'''
def patternthree():
    t.color('black')
    createborders()
    findcenter()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.color('#eb3b3b')
    t.begin_fill()
    t.circle(60)
    t.left(90)
    t.forward(20)
    t.end_fill()

    # eyes
    t.color('white')
    t.penup()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.forward(40)  # draw base
    t.left(120)
    t.forward(40)
    t.left(120)
    t.forward(40)
    t.penup()
    t.right(150)
    t.forward(80)
    #
    # second triangle for star
    t.pendown()
    t.right(90)
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.end_fill()


'''
Quilt Pattern Two
'''
def patterntwo():
    t.color('black')
    createborders()

    # Taking the pen to the center for the box
    t.penup()
    t.backward(100)
    t.left(90)
    t.forward(85)
    t.pendown()

    # This function creates the Star of red color fill
    t.color('red')
    t.begin_fill()
    t.right(90)
    t.forward(30)
    t.left(135)
    t.forward(math.sqrt(900 / 2)) # Applying pythagoras theorem for 30 as side length

    t.right(90)
    t.forward(math.sqrt(900 / 2))
    t.left(135)
    t.forward(30)

    t.right(90)
    t.forward(30)
    t.left(135)
    t.forward(math.sqrt(900 / 2))

    t.right(90)
    t.forward(math.sqrt(900 / 2))
    t.left(135)
    t.forward(30)

    t.right(90)
    t.forward(30)
    t.left(135)
    t.forward(math.sqrt(900 / 2))

    t.right(90)
    t.forward(math.sqrt(900 / 2))
    t.left(135)
    t.forward(30)

    t.right(90)
    t.forward(30)
    t.left(135)
    t.forward(math.sqrt(900 / 2))

    t.right(90)
    t.forward(math.sqrt(900 / 2))
    t.left(135)
    t.forward(30)

    t.right(90)
    t.forward(30)
    t.left(135)
    t.forward(math.sqrt(900 / 2))
    t.end_fill()

    # Sky-blue square
    t.color('#70d7e0')
    t.begin_fill()
    t.forward(math.sqrt(900 / 2) * 2)
    t.left(90)
    t.forward(math.sqrt(900 / 2))
    t.forward(math.sqrt(900 / 2))
    t.left(90)
    t.forward(math.sqrt(900 / 2))
    t.forward(math.sqrt(900 / 2))
    t.left(90)
    t.forward(math.sqrt(900 / 2))
    t.forward(math.sqrt(900 / 2))
    t.end_fill()

    # Dark blue square
    t.backward(math.sqrt(900 / 2))
    t.left(45)
    t.left(90)
    t.forward(15)
    t.right(90)

    t.color('#324ca8')
    t.begin_fill()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.end_fill()

    # This is to go to new space for the next diagram
    t.penup()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(180)
    t.pendown()


'''
Quilt Pattern One 
'''


def patternone():
    createborders()
    findcenter()
    # Step 1: Making the inner square
    innersquare()

    # Step 2: Making the outer triangles
    drawtriangles()
    t.right(180)
    drawtriangles()
    t.left(90)
    drawtriangles()
    t.right(180)
    drawtriangles()

    # This is to go to new space for the next diagram
    t.penup()
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(130)
    t.pendown()


'''
This function makes a square that forms as the base for 
the first pattern
'''


def innersquare():
    t.color('#4a9ae0')
    t.begin_fill()
    t.backward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.end_fill()
    t.right(90)
    t.forward(20)


'''
This function draws four 45-45-90 isoceles triangles
This function makes use of Pythagoras theorem to find 
the hypotenuse
'''


def drawtriangles():
    t.color('#2721db')
    t.begin_fill()  # start filling the shape with #2721db color
    t.left(45)
    t.forward(math.sqrt(800))  # Since the length is 20 the hypotenuse will be SQRT(400+400)
    t.right(90)
    t.forward(math.sqrt(800))
    t.right(135)
    t.forward(40)
    t.left(180)
    t.end_fill()  # end of color fill


'''
This function is used for creating the larger borders
that are outside 
'''


def outerborder():
    for _ in range(0,3):
        t.forward(200)
        t.left(90)
    t.forward(200)
    t.back(10)
    t.left(90)
    t.forward(200)


'''
This function is specifically used for 
creating the smaller 
borders that are inside
'''


def innerborder():
    for _ in range(0,3):
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(200)


'''
This function creates borders making use of another two functions
'''


def createborders():
    outerborder()
    innerborder()


if __name__ == "__main__":
    main()
