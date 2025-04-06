# Turtle Graphics Drawing Application

A Python application that demonstrates various drawing capabilities using the Turtle graphics library. This project is perfect for learning Python graphics programming and geometric concepts.

## Features

The application offers six different drawing options:

1. **Square Drawing** - Draws a simple square
2. **Dashed Line** - Creates a dashed line pattern
3. **Various Shapes** - Draws multiple shapes from triangle to decagon with different colors
4. **Random Walk** - Creates a random walk pattern with changing colors
5. **Spirograph** - Generates a spirograph pattern with changing colors
6. **Dot Painting** - Creates a grid-based dot painting using predefined colors

## Requirements

- Python 3.x
- turtle (built-in Python library)
- random (built-in Python library)
- colorgram (optional, for image color extraction)

## Installation

1. Clone this repository or download the source code
2. Ensure you have Python 3.x installed
3. (Optional) Install colorgram if you want to use the image color extraction feature:
   ```
   pip install colorgram.py
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Select a drawing option by entering a number (0-6):
   - 1: Draw a Square
   - 2: Draw a Dashed Line
   - 3: Draw various shapes
   - 4: Random Walk
   - 5: Spirograph
   - 6: Draw Dots painting
   - 0: Exit

3. After selecting an option, the drawing will be created
4. Click anywhere on the screen to exit the drawing

## Drawing Options Explained

### 1. Square Drawing
Draws a simple square with sides of 100 units.

### 2. Dashed Line
Creates a dashed line with 10 segments, each segment is 10 units long with a 10-unit gap.

### 3. Various Shapes
Draws shapes from triangle (3 sides) to decagon (10 sides), each with a different color from a predefined palette.

### 4. Random Walk
Creates a random walk pattern with 200 steps, changing direction randomly (right, up, left, down) and color at each step.

### 5. Spirograph
Generates a spirograph pattern with circles of radius 100 units, rotating by 5 degrees between each circle.

### 6. Dot Painting
Creates a 10x10 grid of colored dots using a predefined color palette extracted from an image.

## Code Structure

- `main.py` - Contains all the drawing functions and the main application logic
- Each drawing option is implemented as a separate function
- The application uses a menu-driven interface for user interaction

## Customization

You can customize the drawings by modifying parameters in the code:

- Change colors in the predefined color lists
- Adjust sizes, angles, and counts in the drawing functions
- Uncomment and use the colorgram feature to extract colors from your own images

## Learning Resources

This project is great for learning:
- Python's Turtle graphics library
- Basic geometric concepts
- Color theory and RGB color model
- Menu-driven application design
- User input handling

## License

This project is open source and available for educational and personal use.


## Acknowledgments

- Python Turtle Graphics Library
- Colorgram.py for color extraction capabilities 