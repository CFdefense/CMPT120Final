from graphics import *
from numpad import *
class buttons:
    """ This class refers to the construction of a button and a method to determine if it is clicked """
    def __init__(self,win,type,name,color,x1,y1,x2,y2):
        """Constructs a button"""
        #store variables
        self.name = name
        self.x1 = x1
        self.x2 = x2
        self.y1= y1
        self.y2 = y2
        #construct button
        button = Rectangle(Point(x1, y1), Point(x2, y2))
        button.setFill(color)
        button.draw(win)

        #due to the box sizes differing we check if its a num pad or a word and place text accordingly
        if type == "Num":
            buttonword = Text(Point(x1+20, y1+20),name).draw(win)
            buttonword.setStyle("bold")
        elif type == "Word":
            buttonword = Text(Point(x1+37, y1+20),name).draw(win)
            buttonword.setStyle("bold")

    #check if an input of x and y in within the objects x and y values return the name of the button it's within if so, else 'none
    def isclicked(self,x,y):
        if y >= self.y1 and y <= self.y2 and x >= self.x1 and x<= self.x2:
            return(self.name)
        else:
            return("none")