"""
Turtle Graphics Drawing Application

This module provides a collection of drawing projects using Python's Turtle graphics library.
It offers various drawing options including basic shapes, patterns, and artistic designs.
Users can select different drawing options through a menu-driven interface.

Dependencies:
    - turtle: Python's built-in graphics library
    - random: For generating random values
    - colorgram: For color extraction from images (optional)
"""

import turtle as t
import random
import colorgram

def menu():
    """
    Display the main menu of available drawing options.
    
    Prints a formatted menu with numbered options for different drawing projects
    and an exit option.
    """
    print("------Multiple Mini Projects with Turtle Library------")
    print("  1 - Draw a Square")
    print("  2 - Draw a Dashed Line")
    print("  3 - Draw various shapes")
    print("  4 - Random Walk")
    print("  5 - Spirograph")
    print("  6 - Draw Dots painting")
    print("  0 - Exit")
    print("------------------------------------------------------")

def random_color():
    """
    Generate a random RGB color.
    
    Returns:
        tuple: A tuple of three integers representing RGB values (0-255)
    """
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

def opt1_square(tim1):
    """
    Draw a square using the turtle object.
    
    Args:
        tim1 (turtle.Turtle): Turtle object to draw with
    """
    for _ in range(4):
        tim1.forward(100)  # Draw a line 100 units long
        tim1.left(90)      # Turn 90 degrees left

def opt2_dashed(tim2):
    """
    Draw a dashed line using the turtle object.
    
    Args:
        tim2 (turtle.Turtle): Turtle object to draw with
    """
    for _ in range(10):
        tim2.forward(10)   # Draw a line segment
        tim2.penup()       # Lift the pen
        tim2.forward(10)   # Move without drawing
        tim2.pendown()     # Put the pen down

def opt3_shapes(tim3):
    """
    Draw various shapes from triangle to decagon with different colors.
    
    Args:
        tim3 (turtle.Turtle): Turtle object to draw with
    """
    # Predefined list of colors for the shapes
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
              "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    
    def draw_shape(num_sides):
        """
        Draw a regular polygon with specified number of sides.
        
        Args:
            num_sides (int): Number of sides in the polygon
        """
        angle = 360 / num_sides  # Calculate the angle for each turn
        for _ in range(num_sides):
            tim3.forward(100)
            tim3.right(angle)

    # Draw shapes from triangle (3 sides) to decagon (10 sides)
    for shape_side_n in range(3,11):
        tim3.color(random.choice(colours))
        draw_shape(shape_side_n)

def opt4_walk(tim4):
    """
    Create a random walk pattern with changing colors.
    
    Args:
        tim4 (turtle.Turtle): Turtle object to draw with
    """
    t.colormode(255)  # Set color mode to RGB
    tim4.pensize(15)  # Set pen thickness
    tim4.speed("fastest")  # Set drawing speed
    directions = [0, 90, 180, 270]  # Possible directions: right, up, left, down

    for _ in range(200):
        tim4.color(random_color())
        tim4.forward(30)
        tim4.setheading(random.choice(directions))

def opt5_spirograph(tim5):
    """
    Create a spirograph pattern with changing colors.
    
    Args:
        tim5 (turtle.Turtle): Turtle object to draw with
    """
    tim5.speed("fastest")
    t.colormode(255)

    def draw_spirograph(size_of_gap):
        """
        Draw a complete spirograph pattern.
        
        Args:
            size_of_gap (int): Angle between each circle
        """
        for _ in range(int(360 / size_of_gap)):
            tim5.color(random_color())
            tim5.circle(100)
            tim5.setheading(tim5.heading() + size_of_gap)

    draw_spirograph(5)

def opt6_dots(tim6):
    """
    Create a dot painting using predefined colors.
    
    Args:
        tim6 (turtle.Turtle): Turtle object to draw with
    """
    # Note: Color extraction from image is commented out
    # Uncomment and provide an image to extract colors dynamically
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
    
    # Predefined color palette for the dot painting
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
                  (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
                  (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
                  (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
                  (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
                  (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
                  (107, 127, 153), (174, 94, 97), (176, 192, 209)]

    t.colormode(255)
    tim6.speed("fastest")
    tim6.penup()
    tim6.hideturtle()

    # Position the turtle for drawing
    tim6.setheading(225)
    tim6.forward(300)
    tim6.setheading(0)
    number_of_dots = 100

    # Create a grid of colored dots
    for dot_count in range(1, number_of_dots + 1):
        tim6.dot(20, random.choice(color_list))
        tim6.forward(50)

        # Move to next row when reaching the end of current row
        if dot_count % 10 == 0:
            tim6.setheading(90)
            tim6.forward(50)
            tim6.setheading(180)
            tim6.forward(500)
            tim6.setheading(0)

def main():
    """
    Main function to run the drawing application.
    
    Handles the menu display, user input, and execution of selected drawing options.
    """
    game_is_running = True

    while game_is_running:
        menu()
        choice = int(input("What project do you want to run? "))

        if choice == 0:
            game_is_running = False
        elif 0 < choice < 7:
            # Create and configure turtle for drawing
            tim = t.Turtle()
            tim.shape("turtle")

            # Execute selected drawing option
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

            # Set up screen and wait for user click to exit
            screen = t.Screen()
            screen.exitonclick()
            game_is_running = False
        else:
            print("\n")
            print("That number isn't in the options menu!!")
            print("Please input a correct number.")
            print("\n\n")

if __name__ == "__main__":
    main()