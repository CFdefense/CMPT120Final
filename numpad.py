from buttons import *
class Numpad:
    def __init__(self,win):
        '''This class will deal with the visual creation of the numpad as well as a method to identify which
        button was pressed'''

        numpadborder = Rectangle(Point(140,420),Point(430,670)) #create numpad rectangle border
        numpadborder.setFill("black")  # set color to black
        numpadborder.draw(win)
        numpadwindow = Rectangle(Point(150,430),Point(420,660)) #create numpad rectangle
        numpadwindow.setFill("darkgray") #set color to dark gray
        numpadwindow.draw(win) # draw to win

        self.buttonlist = []
        self.button1 = buttons(win,"Num","1","grey",165,440,205,480)
        self.buttonlist.append(self.button1)
        self.button2 = buttons(win,"Num","2","grey",220,440,260,480)
        self.buttonlist.append(self.button2)
        self.button3 = buttons(win,"Num","3","grey",275,440,315,480)
        self.buttonlist.append(self.button3)
        self.button4 = buttons(win,"Num","4","grey",165,495,205,535)
        self.buttonlist.append(self.button4)
        self.button5 = buttons(win,"Num","5","grey",220,495,260,535)
        self.buttonlist.append(self.button5)
        self.button6 = buttons(win,"Num","6","grey",275,495,315,535)
        self.buttonlist.append(self.button6)
        self.button7 = buttons(win,"Num","7","grey",165,550,205,590)
        self.buttonlist.append(self.button7)
        self.button8 = buttons(win,"Num","8","grey",220,550,260,590)
        self.buttonlist.append(self.button8)
        self.button9 = buttons(win,"Num","9","grey",275,550,315,590)
        self.buttonlist.append(self.button9)
        self.button0 = buttons(win,"Num","0","grey",220,605,260,645)
        self.buttonlist.append(self.button0)
        self.buttonc = buttons(win,"Word","cancel","red",330,440,405,480)
        self.buttonlist.append(self.buttonc)
        self.buttonb = buttons(win,"Word","delete","yellow",330,495,405,535)
        self.buttonlist.append(self.buttonb)
        self.buttono = buttons(win,"Word","confirm","green",330,605,405,645)
        self.buttonlist.append(self.buttono)
    def findclick(self,x,y):
        result = self.button1.isclicked(x,y)
        i = 1
        while result == "none":
            if i >= len(self.buttonlist):
                break
            else:
                result = self.buttonlist[i].isclicked(x,y)

            i=i+1
        return result