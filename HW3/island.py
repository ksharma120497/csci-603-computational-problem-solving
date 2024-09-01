import turtle
import math


def fractal(level: int, side: float):
    """
    This fractal function reads level and runs recursively
    to produce the fractal 1 function

    It uses two recursive calls

    :param level: number of levels
    :param side: number of sides the figure will have
    :return: the perimeter of the figure
    """
    perimeter = 0
    if level == 1:
        turtle.forward(side)
        perimeter+=side
        return perimeter
    else:
        turtle.left(45)
        perimeter+=fractal(level - 1, side/math.sqrt(2))
        turtle.right(90)
        perimeter+=fractal(level - 1, side/math.sqrt(2))
        turtle.left(45)
        return perimeter





def draw_side(level: int, length_of_sides: int):
    """
        This fractal function reads level and runs recursively
        to produce the desired output

        It uses two recursive calls

        :param level: number of levels
        :param side: number of sides the figure will have
        :return: the perimeter of the figure
        """
    perimeter = 0
    if level == 1:
        turtle.forward(length_of_sides)
        perimeter+=length_of_sides
        return perimeter
    else:
        perimeter+= draw_side(level - 1, length_of_sides/3)
        turtle.left(60)
        perimeter+=draw_side(level - 1, length_of_sides/3)
        turtle.right(120)
        perimeter+=draw_side(level - 1, length_of_sides/3)
        turtle.left(60)
        perimeter+=draw_side(level - 1, length_of_sides/3)
        return perimeter


def main():
    turtle.speed(0)
    number_of_sides = input("Number of sides: ")
    while not number_of_sides.isnumeric():
        print("You typed the ",type(number_of_sides)," value")
        number_of_sides = input("Number of sides: ")
    length_of_initial_sides = input("Length of initial side: ")
    while not length_of_initial_sides.isnumeric():
        print("You typed the ", type(length_of_initial_sides), " value")
        length_of_initial_sides = input("Length of initial side: ")
    number_of_levels = input("Number of levels: ")
    while not number_of_levels.isnumeric():
        print("You typed the ", type(number_of_levels), " value")
        number_of_levels = input("Number of levels: ")
    counter=int(number_of_sides)
    acc=0
    while counter > 0:
        acc += draw_side(int(number_of_levels), int(length_of_initial_sides))
        turtle.left(360/int(number_of_sides))
        counter=counter-1
    print("Curve 1 - Island's length is", acc, "units.")
    hit_enter=input("Hit enter to continue...")
    turtle.reset() # Resets the whole turtle screen to start a new drawing
    counter = int(number_of_sides)
    acc = 0
    """
     This while loop will count the perimeter of the fractal curve two
    """
    while counter > 0:
        acc+=fractal(int(number_of_levels), int(length_of_initial_sides))
        turtle.left(360 / int(number_of_sides))
        counter = counter - 1
    print("Curve 2 - Island's length is", acc, "units.")
    print("Bye!")
    turtle.mainloop()


if __name__ == '__main__':
    main()
