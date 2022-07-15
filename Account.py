class Account:
    def __init__(self,no,balance,owners):
        self._number = no
        self._balance = balance
        self._owners = owners

    def __str__(self):
        return 'The number account: '+ str(self._number) + ' The owners: ' + str(self._owners) + ' The balance: ' + str(self._balance)

    def deposit(self,NewMoney):
        if NewMoney > 0:
            self._balance += NewMoney

    def withdraw(self,TakeMoney):
        if TakeMoney > 0:
            self._balance -= TakeMoney

    def getNum(self):
        return self._number

    def getBalance(self):
        return self._balance

    def getOwners(self):
        return self._owners

# def program1():
    # nameList = ['Minnie Mouse','Mickey Mouse']
    # nameList1 = ['Donald Duck']
    # a1 = Account(1, 100, nameList)
    # a2 = Account(2, 200, nameList1)
    # print(a1)
    # print(a2)
    # a1.deposit(200)
    # a2.deposit(200)
    # print(a1)
    # print(a2)
    # a1.withdraw(500)
    # a2.withdraw(500)
    # print(a1)
    # print(a2)

# program1()




