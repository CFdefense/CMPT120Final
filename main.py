from graphics import *
from ATM import *
from numpad import *
from Screen import *
from Accounts import *

def main():

    # create window and ATM graphic
    win = GraphWin("ATM MACHINE", 750, 750)

    # call the creation of an ATM
    ATM = createATM(win)

    # call the creation of the numpad
    numpad = Numpad(win)

    # call the function sequence of the program
    Screen = screen(win, numpad)

main()