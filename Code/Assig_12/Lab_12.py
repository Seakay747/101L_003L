########################################################################
##
## CS 101 Lab
## Program #11
## Charles Keys
## CKBMD@umsystem.edu
##
## PROBLEM : Create a program that uses the class object to keep time
##
## ALGORITHM : 
##      1. Set up the super class
##      2. Set up the the child classes
##      3. Set up the grandchild classes
##      4. Set up input codelines and object assignment
## 
## ERROR HANDLING:
##      coords must be coords, colors must be colors
##
## OTHER COMMENTS:
##      Any special comments
##              
######################################################################## 
import turtle

class Point(object):
    def __init__(self, x1, y1, color):
        self.x1 = x1
        self.y1 = y1
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

    def get_x1(self):
        return self.x1
    
    def get_y1(self):
        return self.y1
    
    def set_x1(self, a):
        self.x1 = a

    def set_y1(self, a):
        self.y1 = a

class Box(Point):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(x1, y1,color)
        self.x2 = x2
        self.y2 = y2
    
    def draw_action(self):
        turtle.goto(self.x2, self.y1)
        turtle.goto(self.x2, self.y2)
        turtle.goto(self.x1, self.y2)
        turtle.goto(self.x1, self.y1)
    
    def get_x2(self):
        return self.x2
    
    def get_y2(self):
        return self.y2
    
    def set_x2(self, a):
        self.x2 = a

    def set_y2(self, a):
        self.y2 = a

class FilledBox(Box):
    def __init__(self, x1, y1, x2, y2, color, fillcolor):
        super().__init__(x1, y1, x2, y2, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()
    
    def get_fillcolor(self):
        return self.fillcolor
    
    def set_fillcolor(self, a):
        self.fillcolor = a

class Circle(Point):
    def __init__(self, x1, y1, r, color):
        super().__init__(x1, y1, color)
        self.r = r
    
    def draw_action(self):
        turtle.circle(self.r)
    
    def get_r(self):
        return self.r
    
    def set_r(self, a):
        self.r = a

class FilledCircle(Circle):
    def __init__(self, x1, y1, r, color, fillcolor):
        super().__init__(x1, y1, r, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
    
    def get_fillcolor(self):
        return self.fillcolor
    
    def set_fillcolor(self, a):
        self.fillcolor = a


p = Point(-100, 100, "blue")
p.draw()

x = input('Press enter to continue')

b = Box(0, 0, 100, 100, "red")
b.draw()

x = input('Press enter to continue')

fb = FilledBox(-100, -100, 0, 0, 'black', 'yellow')
fb.draw()

x = input('Press enter to continue')

c = Circle(50, -100, 50, 'purple')
c.draw()

x = input('Press enter to continue')

cf = FilledCircle(0,-5,10,'black','orange')
cf.draw()

x = input('Press enter to end program')