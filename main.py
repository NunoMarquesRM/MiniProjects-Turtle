import turtle as t
import random
import colorgram

# Options - Mini Projects
def menu():
    print("------Multiple Mini Projects with Turtle Library------")
    print("  1 - Draw a Square")
    print("  2 - Draw a Dashed Line")
    print("  3 - Draw various shapes")
    print("  4 - Random Walk")
    print("  5 - Spirograph")
    print("  6 - Draw Dots painting")
    print("  0 - Exit")
    print("------------------------------------------------------")

# Random RBG Color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

# Square
def opt1_square(tim1):
    for _ in range(4):
        tim1.forward(100)
        tim1.left(90)

# Dashed Line
def opt2_dashed(tim2):
    for _ in range(10):
        tim2.forward(10)
        tim2.penup()
        tim2.forward(10)
        tim2.pendown()

# Draw Various Shapes
def opt3_shapes(tim3):
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    def draw_shape(num_sides):
        angle = 360 / num_sides
        for _ in range(num_sides):
            tim3.forward(100)
            tim3.right(angle)

    for shape_side_n in range(3,11):
        tim3.color(random.choice(colours))
        draw_shape(shape_side_n)

# Random Walk
def opt4_walk(tim4):
    t.colormode(255)
    tim4.pensize(15)
    tim4.speed("fastest")
    directions = [0, 90, 180, 270]

    for _ in range(200):
        tim4.color(random_color())
        tim4.forward(30)
        tim4.setheading(random.choice(directions))

# Spirograph
def opt5_spirograph(tim5):
    tim5.speed("fastest")
    t.colormode(255)

    def draw_spirograph(size_of_gap):
        for _ in range(int(360 / size_of_gap)):
            tim5.color(random_color())
            tim5.circle(100)
            tim5.setheading(tim5.heading() + size_of_gap)

    draw_spirograph(5)

# Draw Dots painting
def opt6_dots(tim6):
    # Extract colors from image
    """
    colors = colorgram.extract('image.jpg', 30)
    rbg_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rbg_colors.append(new_color)
    print(rbg_colors)
    """
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

    t.colormode(255)
    tim6.speed("fastest")
    tim6.penup()
    tim6.hideturtle()

    tim6.setheading(225)
    tim6.forward(300)
    tim6.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        tim6.dot(20, random.choice(color_list))
        tim6.forward(50)

        if dot_count % 10 == 0:
            tim6.setheading(90)
            tim6.forward(50)
            tim6.setheading(180)
            tim6.forward(500)
            tim6.setheading(0)

def main():
    game_is_running = True

    while game_is_running:
        menu()
        choice = int(input("What project do you want to run? "))

        if choice == 0:
            game_is_running = False
        elif 0 < choice < 7:
            tim = t.Turtle()
            tim.shape("turtle")

            if choice == 1:
                opt1_square(tim)
            elif choice == 2:
                opt2_dashed(tim)
            elif choice == 3:
                opt3_shapes(tim)
            elif choice == 4:
                opt4_walk(tim)
            elif choice == 5:
                opt5_spirograph(tim)
            elif choice == 6:
                opt6_dots(tim)

            screen = t.Screen()
            screen.exitonclick()
            game_is_running = False
        else:
            print("\n")
            print("That number isn't in the options menu!!")
            print("Please input a correct number.")
            print("\n\n")

main()