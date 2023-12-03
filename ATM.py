from graphics import *

#class ATM creates an ATM in a window
class createATM:
    def __init__(self,win):

        """Creates an atm window minus the keypad"""

        # creates grey atm box outline
        atmBaseb = Rectangle(Point(90, 90), Point(660, 710))  # create the rectangle
        atmBaseb.setFill("black")  # set color to black
        atmBaseb.draw(win)  #draw
        # creates grey atm box
        atmBase = Rectangle(Point(100,100),Point(650,700)) #create the rectangle
        atmBase.setFill("gray") # set color to gray
        atmBase.draw(win) #draw

        # outline for red rectangle at top
        atmhead = Rectangle(Point(210, 100), Point(540, 10))  # create the rectangle
        atmhead.setFill("black")  # set color to red
        atmhead.draw(win)  # draw

        #red rectangle at the top of the atm
        atmhead = Rectangle(Point(220,90),Point(530,20)) # create the rectangle
        atmhead.setFill("red") # set color to red
        atmhead.draw(win) #draw

        #Word ATM at the top of the atm
        atmword = Text(Point(375, 60), "ATM") #create the rectangle
        atmword.setSize(36)  # Set the font size
        atmword.setStyle("bold")  # Set the font style
        atmword.draw(win) #draw in window

        #ATM window
        atmborder = Rectangle(Point(140,120),Point(615,390)) #create border before window so window override
        atmborder.setFill("black") #set border color to black
        atmborder.draw(win) #draw border
        atmwin = Rectangle(Point(150,130),Point(605,380)) #create window
        atmwin.setFill("lightblue") #set window to light blue
        atmwin.draw(win) #draw window

        #ATM money slot border
        atmslotb = Rectangle(Point(450,620),Point(630,670)) #create rectangle
        atmslotb.setFill("black")  # set color to black
        atmslotb.draw(win) #draw to window

        #ATM money slot
        atmslot = Rectangle(Point(460, 630), Point(620, 660)) #create rectangle
        atmslot.setFill("darkgray")  # set color to darkgray
        atmslot.draw(win) # draw to window

        # ATM money slot inside
        atmsloti = Rectangle(Point(475, 643), Point(605, 647)) #create rectangle
        atmsloti.setFill("black")  # set color to black
        atmsloti.draw(win)