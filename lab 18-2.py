class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance #private variable
    def deposit(self, amount):
        self.__balance += amount
    def widthdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -=amount
        else:
            print("Not enough funds")
    def get_balance(self):
        return self.__balance
account = Bankaccount(100)#start at balance :100
account.deposit(200) #deposit 200
print(account.get_balance()) #balance now is 300

account.widthdraw(150) #widthdraw 150
print(account.get_balance())  #now the balance is 150 

account.widthdraw(400) #fails to widthdraw 
print(account.get_balance())#still 150



