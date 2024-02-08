import verify as vy
class productList(): #used if user picks product
    def __init__(self):
        self.userList = []
        
    def printList(self): # prints user list to the console
        print("Your ordered products:")
        for item in self.userList:
            print(item)
    def infoToFile(self, days):# prints user list to the text file reciept
        fout = open("receipt.txt", 'w')
        fout.write("------Receipt------\n")
        fout.write("Item\n")
        for item in self.userList:
            fout.write(item+"\n")
        fout.write("Appointment in " + str(days) + " days\n")
        fout.write("------       ------\n")
        fout.close()
class service(): #parent of payed Agrement used if user does noy have an agreed upon price
    def __init__(self):
        self.name = None
        self.days = None
    def printServ(self): #prints the service that user choose
        print ("You Choose:", self.name, "service")
class payedAgreement(service): #used if user has an agreed upon price
    def __init__(self):
        super().__init__()
        self.price = None
        
numDays = 0 #used for telling the user how many days are left until order arrival/appointment date
price = ""
cont = "yes"
userProd = productList()
def lessThan(num): # checks to see if number inputed is less than 365
    while num >= 365:
        num = input("Enter a number of days less than 365: ")
        vy.verifyNumber(num)
        num = int(num)
    return int(num)
def printAppoint(name, days, cost):# prints an appointment to the text file
    fout = open("receipt.txt", 'w')
    fout.write("------Receipt------\n")
    fout.write("Service          Price\n")
    fout.write(name+"           " + cost + "\n")
    fout.write("Appointment in " + str(days) + " days\n")
    fout.write("------       ------\n")
    fout.close()
    
print ("products or services")
choice = input("1 for products 2 for services anything else to close program: ")
if choice == '1': #code for when user picks to purchase items
    userProd = productList()
    while cont.lower() == "yes":
        currentItem = input("Enter a product you wish to buy: (DO NOT INPUT ANY NUMBERS) ")
        vy.verifyText(currentItem)
        userProd.userList.append(currentItem)
        print("You ordered", currentItem)
        cont = input("Would you like to enter another product? (yes or no)")
        vy.verifyText(cont)
    numDays = input ("Enter a number of days within the year to have your products : ")
    vy.verifyNumber(numDays)
    numDays = lessThan(int(numDays))
    userProd.printList()
    userProd.infoToFile(numDays)
elif choice == '2': #code for when user picks a service
    priceKnown = input("Do you know the price of this service Y or N: ")
    if priceKnown.upper() == "N": #sets up an appointment without a price
        userService = service()
        userService.name = input("What is the name of Your Service? (DO NOT INPUT ANY NUMBERS) ")
        vy.verifyText(userService.name)
        userService.printServ()
        numDays = input ("Enter a number of days within the year to have your appointment: ")
        vy.verifyNumber(numDays)
        numDays = lessThan(int(numDays))
        
        userService.days = numDays
        print("Your appointment will be in", userService.days, "days")
        printAppoint(userService.name, userService.days, "N/A")
    elif priceKnown.upper() == "Y": #sets up an appointment with a price
        paidService = service()
        paidService.name = input("What is the name of Your Service? (DO NOT INPUT ANY NUMBERS) ")
        vy.verifyText(paidService.name)
        paidService.printServ()
        numDays = input ("Enter a number of days within the year to have your appointment: ")
        vy.verifyNumber(numDays)
        numDays = lessThan(int(numDays))
        paidService.days = numDays
        print("Your appointment will be in", paidService.days, "days")
        
        price = input("What is the price agreed upon the service: ")
        paidService.price = price
        printAppoint(paidService.name, paidService.days, paidService.price)
    else: # Used if user does not enter Y or N
        print ("Thank You Goodbye")
else: # Used if user does not enter 1 or 2
    print ("Thank You Goodbye")