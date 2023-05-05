class customer:
    bank_name='TIMES BANK'
    def __init__(self,name, balance=0.0):
        self.name=name
        self.balance=balance
print('Welcome to', customer.bank_name)

name=input('Enter Your Name: ')
c=customer(name)
print('Hello',c.name,'Your account got created')
while True:
    print('D-Deposit\nW-Withdrawl\nE-Exit')
    option=input('Choose your option')
    
    
