def squareperi(side_lenght):
    perimeter = 4 * side_lenght
    print("The perimeter of a square is", perimeter)

def rectperi(l,b):
    perimeter_r = 2 * (l + b)
    print("The perimeter of a rectangle is", perimeter_r)

def circle_circumfrence(radius):
    circumfrence = 2 * 3.14 * radius
    print("The circumfrence of a circle is", circumfrence)

radius = int(input("Enter a radius for the circle :"))
circle_circumfrence(radius)

l = int(input("Enter a lenght for the rectangle :"))
b = int(input("Enter a breath for the rectangle :"))
rectperi(l,b)

side_lenght = int(input("Enter a side lenght for the square :"))
squareperi(side_lenght)