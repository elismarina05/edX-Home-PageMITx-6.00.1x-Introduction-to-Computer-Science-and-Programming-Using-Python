'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  0.25∗n∗s2tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This
function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.

hint: Which library should you be importing at the beginning of your code in
order to call the tan function and to get the pi constant?
'''


def polysum(n,s):
    """
    n=number of sides
    s=side length
    """
    from math import tan, pi
    area = (0.25*(n)*(s**2))/(tan(pi/n))
    perim = (n*s)
    ans = area + perim**2
    return round(ans,4)
