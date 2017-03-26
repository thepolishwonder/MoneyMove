# import modules used here -- sys is a very standard one
import sys
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

#class Movement:
#    def quack(self): return self.strings['quack']
#    def bark(self): return self.strings['bark']

class Account:
	
	def __init__(self):
		self.accountName = "StubName"
		self.accountBalance = 0.0
		
	def setBalance(self, balance):
		self.accountBalance = balance
	
	def setBalanceFromTerm(self):
		self.accountBalance = float(raw_input("Enter balance: "))
	
	def getBalance(self):
		return self.accountBalance
	
	def setName(self,name):
		self.accountName = name
	
	def getName(self):
		return self.accountName	
		

class Menu:
    

    def __init__(self, account):
    	self.accountBalance = account.getBalance()
    	
    def display(self):
    	print("")
    	print("Welcome to MoneyMove v.1. Your account balance is " + locale.currency(self.accountBalance) + ".")
    	print("Please select from the following options:")
    	print("")


# Gather our code in a main() function
def main():
    # print 'Hello there', sys.argv[1]
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    
    run = 1
    
    account = Account()
    account.setName("Recurring")
    account.setBalance(0)
    
    while (run != 0):
    	
    	mainMenu = Menu(account)
    	mainMenu.display()
    
    	run = int(raw_input("Enter something: "))
    	
    	if (run == 1):
    		account.setBalanceFromTerm()
    		
    	elif (run == 2):
    		print("Made it to 2")
		
    
    print ("Exiting now")




# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()