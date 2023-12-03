class Accounts:
    def __init__(self):
        """This class will deal with the storing of accounts and their information in addition to methods to access
        that information and to test if inputs match the information
        """
        #Recieve information

        File = open("Accounts.txt", "r").read().splitlines() #'first1 last1 number1 pin1 money1','first2 last2 number2 pin2 money2'

        #create blank lists to store information in
        self.Information = []
        self.listoffnames = []
        self.listofnumbers = []
        self.listofpins = []
        self.listofmoney = []

        #split information into list of lists
        for elem in File:
            filtered = elem.split("\t")
            self.Information.append(filtered) #[information for person1],[information or person2], [information for person3]

        #Sort through each set of data
        for elem in self.Information:
            name, number, pin, money = elem[:4]  # Extract the first 4 elements
            #for each set of data we take each datapoint and store it in its respective list
            self.listoffnames.append(name)
            self.listofnumbers.append(number)
            self.listofpins.append(pin)
            self.listofmoney.append(money)

        #now we remove all the $ in the list of money and make them ints, then store in new list
        self.newlistofmoney = []
        for x in self.listofmoney: #removes $
            withoutdollar = (x.replace('$', ''))
            self.newlistofmoney.append(int(withoutdollar))

    # returns list of card numbers to be matched
    def getnumbers(self):
        return(self.listofnumbers)

    # returns the pin at the position equal to the card
    def getpins(self,number):
        position =self.listofnumbers.index(number) # index of the card number
        return(self.listofpins[position])

    #returns the name at a certain index
    def getname(self,number):
        position = self.listofnumbers.index(number)
        return(self.listoffnames[position])

    #returns the balance at a certain index
    def getbalance(self,number):
        position = self.listofnumbers.index(number)
        return (self.newlistofmoney[position])

    #returns the new amount for both increase (true) and decrease (false)
    def update(self,number,type,amount):
        position = self.listofnumbers.index(number)
        amount = int(amount)
        currentamount = int(self.newlistofmoney[position])
        if type == True:
            newamount = currentamount + amount
            self.newlistofmoney[position] = newamount
            return newamount
        elif type == False:
            newamount = currentamount - amount
            self.newlistofmoney[position] = newamount
            return newamount

    #updates the file with the new amount, concatenate the changed data back together and write the new line over the old
    def updatefile(self,number):
        position = self.listofnumbers.index(number)
        name = str(self.listoffnames[position])
        number = str(number)
        pin = str(self.listofpins[position])
        balance = "$" + str(self.newlistofmoney[position])
        newline = name+"\t"+number+"\t"+pin+"\t"+balance

        # Read the existing content of the file
        File = open("Accounts.txt", "r")
        lines = File.readlines()

        # Update the desired line
        lines[position] = newline + '\n'

        # Write the modified content back to the file
        file = open("Accounts.txt", "w")
        file.writelines(lines)