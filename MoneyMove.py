# import modules used here -- sys is a very standard one
import sys
import locale
import os

locale.setlocale(locale.LC_ALL, 'en_US')

class Movement:

	def __init__(self):
		self.myList = [["Empty",0.0,"biweekly", "income"]]

	def add(self):
		print("add called")
		
	def remove(self):
		print("Remove called")

	def displayList(self):
		for i in self.myList:
			print("---------- "+ str(self.myList.index(i)) + " ----------")
			print(i)
	
	def displayMenu(self):
		
		os.system('clear')
		self.displayList()
		print("")
		print("Please select from the following options:")
		print("")
		print("       1 - Add")
		print("       2 - Remove")
		print("       0 - Back")
		print("")
		

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
		
	def calculate(self):
		return 1971

class Menu:
    

    def __init__(self, account):
    	self.accountBalance = account.getBalance()
    	
    def displayMain(self):
    	print("")
    	print("Welcome to MoneyMove v.1. Your account balance is " + locale.currency(self.accountBalance) + ".")
    	print("Please select from the following options:")
    	print("")
    	
    	
    	
    	print("       0 - Quit")
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
    
    movement = Movement()
    
    while (run != 0):
    	
    	mainMenu = Menu(account)
    	mainMenu.displayMain()
    
    	run = int(raw_input(">>>>>> "))
    	
    	if (run == 1):
    		account.setBalanceFromTerm()
    		
    	elif (run == 2):
    		movement.displayMenu()
    		
    		
    		
    		
    		
    		
    		
    	elif (run == 9):
    		print(str(account.calculate()))
		
    
    print ("Exiting. Thank you.")
    print("")




# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()