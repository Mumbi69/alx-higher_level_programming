# Simple rectangle
* Write an empty class Rectangle that defines a rectangle:
> * You are not allowed to import any module

# Real definition of a rectangle
* Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
> * Private instance attribute: width:
> * Private instance attribute: height:
> * Instantiation with optional width and height: def __init__(self, width=0, height=0):

> * You are not allowed to import any module

# Area and Perimeter
* Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

> * Private instance attribute: width:
> * Private instance attribute: height:
> * Instantiation with optional width and height: def __init__(self, width=0, height=0):

> * Public instance method: def area(self): that returns the rectangle area

> * Public instance method: def perimeter(self): that returns the rectangle perimeter:

> * You are not allowed to import any module

#  String representation
* Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

> * Private instance attribute: width:
> * Private instance attribute: height:
> * Instantiation with optional width and height: def __init__(self, width=0, height=0):

> * Public instance method: def area(self): that returns the rectangle area

> * Public instance method: def perimeter(self): that returns the rectangle perimeter:

> * You are not allowed to import any module

# Eval is magic
* Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
> * Instantiation with optional width and height: def __init__(self, width=0, height=0):

> * Public instance method: def area(self): that returns the rectangle area
> * Public instance method: def perimeter(self): that returns the rectangle perimeter:
> * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)

> * You are not allowed to import any module

# Detect instance deletion
* Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)


# How many instances
* Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)


#  Change representation 
* Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)

> * Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
> * You are not allowed to import any module

#  Compare rectangles
* Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
> * Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
> * You are not allowed to import any module

# A square is a rectangle
* Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

> * Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size


# N queens
* The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens proble

> * Usage: nqueens N
> > * If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
> * where N must be an integer greater or equal to 4
> > * If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
> > * If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
> * The program should print every possible solution to the problem
> > * One solution per line
> * You don’t have to print the solutions in a specific order
> * You are only allowed to import the sys module
