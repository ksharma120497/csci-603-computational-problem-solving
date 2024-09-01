import math
import turtle

def calculate_alpha(length):
    return math.sqrt(2*((length/2)**2))

def calculat_beta(length):
    return length/math.sqrt(3)



def draw_square1(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)

def draw_triangle1(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.right(120)

def draw_square2(length):
    draw_square1(length)
    turtle.forward(length/2)
    turtle.left(45)
    alpha_value = calculate_alpha(length)
    draw_square1(alpha_value)

def draw_star1(length):
    draw_square1(length)
    for _ in range(4):
        beta=calculat_beta(length)
        short_distance = (length/2) + (beta/2)
        turtle.forward(short_distance)
        turtle.right(120)
        draw_triangle1(beta)
        turtle.right(240)
        turtle.forward((length/2) - (beta/2))
        turtle.left(90)

def draw_nested_star(length, depth):
    if depth == 0:
        pass
    elif depth == 1:
        return draw_star1(length)
    else:
        draw_star1(length)
        turtle.forward(length/2)
        turtle.left(45)
        alpha = calculate_alpha(length)
        return draw_nested_star(alpha, depth-1)




if __name__ == "__main__":
    turtle.speed(0)
    # draw_square1(100)
    # draw_square2(100)
    # draw_triangle1(100)
    # draw_star1(100)
    draw_nested_star(100,6)
    turtle.update()
    turtle.mainloop()