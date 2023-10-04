# class Public:

#     def first(self):
#         print('first function')

#     def display(self):
#         print('done',self)
#         self.first()
        

# firstObject = Public()
# firstObject.name = "himanshu"
# print(firstObject.display())

class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def display(self):
        print(f'Hello {self.name}, {self.balance} Rs left in your Account.')
    
    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance += amount


t = BankAccount('himanshu')

t.display()
t.withdraw(5)
t.deposit(10)
t.display()