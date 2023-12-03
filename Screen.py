from graphics import *
from numpad import *
from Accounts import *
from numpad import *
class screen:
    def __init__(self,win,numpad):
        """Class Screen's purpose is to generate the program sequence, call and recieve information and manipulate the
        stored data"""

        #create the initial text
        self.numpad = numpad
        accounts = Accounts() # Create accounts object which stores all the data. Create so we can call and siphon data
        welcome = Text(Point(375, 250), "Welcome").draw(win) # draw text to window
        welcome.setSize(20)  # Set the font size
        welcome.setStyle("bold")  # Set the font style
        con2pro = Text(Point(375, 300), '"Confirm to Continue"').draw(win) #draw text to window
        con2pro.setSize(15) # set font size
        con2pro.setStyle("italic") # set font style

        #check for 'confirm' pressed
        win1 = win.getMouse() #wait and find where next click is
        check = self.numpad.findclick(win1.getX(),win1.getY()) #call method findclick to find if and which button clicked
        while check != "confirm": # check if button confirm is clicked
            win1 = win.getMouse()
            check = numpad.findclick(win1.getX(), win1.getY())
        welcome.undraw()
        con2pro.undraw()

        #draw new messages including an invisible message that we will update as numbers are pressed
        welcome = Text(Point(375, 250), "Enter Your Card Number").draw(win)
        welcome.setSize(20)  # Set the font size
        welcome.setStyle("bold")  # Set the font style
        con2pro = Text(Point(375, 350), '"Confirm to Continue"').draw(win)
        con2pro.setSize(15)
        con2pro.setStyle("italic")
        cardstrdraw = Text(Point(375, 300), "")
        cardstrdraw.setSize(20)
        cardstrdraw.setStyle("bold")

        #read which number is pressed, update and display the current string
        win1 = win.getMouse() #record mouse input
        check = self.numpad.findclick(win1.getX(),win1.getY()) # find if click is within a buttons area
        self.cardstr = "" #set card number to empty

        #continue to check which button if any are pressed and update the current string
        while check != "confirm":
            if check == "none":
                self.cardstr = self.cardstr
            elif check == "delete":
                self.cardstr = self.cardstr[:-1]
            elif check == "cancel":
                win.close()
            else:
                self.cardstr = self.cardstr + check
            cardstrdraw.undraw()
            cardstrdraw = Text(Point(375, 300), self.cardstr).draw(win)
            win1 = win.getMouse()
            check = self.numpad.findclick(win1.getX(), win1.getY())

        #check if the number is within the list of documented account numbers

        Success = False
        if self.cardstr in Accounts.getnumbers(accounts):
            Success = True

        if Success == False: # if it does not exist then we close after stating invalid
            cardstrdraw.undraw()
            cardstrdraw = Text(Point(375, 300), "Invalid Card Number").draw(win)
            time.sleep(3)
            win.close()

        #undraw the number and the "enter card number" and state success and new "enter pin number"
        cardstrdraw.undraw()
        cardstrdraw = Text(Point(375, 300), "Success").draw(win)
        win1 = win.getMouse()
        check = self.numpad.findclick(win1.getX(), win1.getY()) # check for confirm
        while check != "confirm":
            win1 = win.getMouse()
            check = numpad.findclick(win1.getX(), win1.getY())
        welcome.undraw()
        cardstrdraw.undraw()
        welcome = Text(Point(375, 250), "Enter Your Pin Number").draw(win)
        welcome.setSize(20)  # Set the font size
        welcome.setStyle("bold")  # Set the font style

        #check for which buttons are pressed while pin being entered
        win1 = win.getMouse()
        check = self.numpad.findclick(win1.getX(),win1.getY())
        self.numstr = ""
        while check != "confirm":
            if check == "none":
                self.numstr = self.numstr
            elif check == "delete":
                self.numstr = self.numstr[:-1]
            elif check == "cancel":
                win.close()
            else:
                self.numstr = self.numstr + check
            cardstrdraw.undraw()
            cardstrdraw = Text(Point(375, 300), self.numstr).draw(win)
            win1 = win.getMouse()
            check = self.numpad.findclick(win1.getX(), win1.getY())

        #check if inputted pin matches the card number account pin
        if self.numstr != Accounts.getpins(accounts,self.cardstr):
            cardstrdraw.undraw()
            cardstrdraw = Text(Point(375, 300), "Invalid Pin Number").draw(win)
            time.sleep(3)
            win.close()
        cardstrdraw.undraw()
        cardstrdraw = Text(Point(375, 300), "Success").draw(win)

        #check for confirm before continuing
        win1 = win.getMouse()
        check = self.numpad.findclick(win1.getX(), win1.getY())  # check for confirm
        while check != "confirm":
            win1 = win.getMouse()
            check = numpad.findclick(win1.getX(), win1.getY())
        #undraw all previous text as we continue
        cardstrdraw.undraw()
        welcome.undraw()
        con2pro.undraw()

        #create new screen graphics and pull numbers from data to display
        welcome = Text(Point(375, 150), "Welcome "+Accounts.getname(accounts,self.cardstr)).draw(win)
        welcome.setSize(20)
        welcome.setStyle('bold')
        balance = Text(Point(375,200),"Balance: $"+str(Accounts.getbalance(accounts,self.cardstr))).draw(win)
        balance.setStyle('bold')
        withdrawal = Text(Point(300,250),"Withdrawal")
        withdrawal.setStyle('bold')
        withdrawal.draw(win)
        deposit = Text(Point(450, 250), "Deposit")
        deposit.setStyle('bold')
        deposit.draw(win)
        withdrawalop = Text(Point(300, 275), '"delete" to select').draw(win)
        withdrawalop.setStyle('italic')
        withdrawalop.setSize(8)
        depositop = Text(Point(450, 275), '"confirm" to select').draw(win)
        depositop.setStyle('italic')
        depositop.setSize(8)

        #check for confirm before continuing
        win1 = win.getMouse()
        check = self.numpad.findclick(win1.getX(), win1.getY())
        while check != "confirm" and check != "delete":
            win1 = win.getMouse()
            check = self.numpad.findclick(win1.getX(), win1.getY())

        #undraw all before continuing
        welcome.undraw()
        withdrawalop.undraw()
        depositop.undraw()
        withdrawal.undraw()
        deposit.undraw()
        balance.undraw()

        #if were withdrawling "delete" entered and we do below
        if check == "delete":
            balancegraphic = Text(Point(375, 200), "Current Balance $:" + str(Accounts.getbalance(accounts, self.cardstr))).draw(win)
            balancegraphic.setStyle('bold')
            withdrawalgraphic = Text(Point(375, 150), "Withdrawal ").draw(win)
            withdrawalgraphic.setStyle('bold')
            withdrawalgraphic.setSize(20)
            questiongraphic = Text(Point(375, 250), "Enter Withdrawal Amount ").draw(win)
            questiongraphic.setStyle('bold')
            con2pro = Text(Point(375, 275), "Confirm to Submit ").draw(win)
            con2pro.setStyle('italic')
            con2pro.setSize(8)
            win1 = win.getMouse()
            check = self.numpad.findclick(win1.getX(), win1.getY())
            self.input = ""
            while check != "confirm":
                if check == "none":
                    self.input = self.input
                elif check == "delete":
                    self.input = self.input[:-1]
                elif check == "cancel":
                    win.close()
                else:
                    self.input = self.input + check
                cardstrdraw.undraw()
                cardstrdraw = Text(Point(375, 300), self.input).draw(win)
                win1 = win.getMouse()
                check = self.numpad.findclick(win1.getX(), win1.getY())
            if Accounts.getbalance(accounts, self.cardstr) < int(self.input): #Insufficient funds
                cardstrdraw.undraw()
                cardstrdraw = Text(Point(375, 300), "Insufficient Funds").draw(win)
                time.sleep(3)
                win.close()
            else:
                newamount = accounts.update(self.cardstr,False,self.input)
                cardstrdraw.undraw()
                accounts.updatefile(self.cardstr)
                cardstrdraw = Text(Point(375, 300), "Updated Balance: $"+str(newamount)).draw(win)

        #check if depositing and "confirm" and do the following
        elif check == "confirm":
            balancegraphic = Text(Point(375, 200), "Available Balance: $" + str(Accounts.getbalance(accounts, self.cardstr))).draw(win)
            balancegraphic.setStyle('bold')
            depositgraphic = Text(Point(375, 150),"Deposit").draw(win)
            depositgraphic.setStyle('bold')
            depositgraphic.setSize(20)
            questiongraphic = Text(Point(375, 250),"Enter Deposit Amount ").draw(win)
            questiongraphic.setStyle('bold')
            con2pro = Text(Point(375, 275),"Confirm to Submit ").draw(win)
            con2pro.setStyle('italic')
            con2pro.setSize(8)
            win1 = win.getMouse()
            check = self.numpad.findclick(win1.getX(), win1.getY())
            self.input = ""
            while check != "confirm":
                if check == "none":
                    self.input = self.input
                elif check == "delete":
                    self.input = self.input[:-1]
                elif check == "cancel":
                    win.close()
                else:
                    self.input = self.input + check
                cardstrdraw.undraw()
                cardstrdraw = Text(Point(375, 300), self.input).draw(win)
                win1 = win.getMouse()
                check = self.numpad.findclick(win1.getX(), win1.getY())
            newamount = accounts.update(self.cardstr, True, self.input)
            cardstrdraw.undraw()
            accounts.updatefile(self.cardstr)
            cardstrdraw = Text(Point(375, 300), "Updated Balance: $" + str(newamount)).draw(win)
        win1 = win.getMouse()


