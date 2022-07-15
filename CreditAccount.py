from Account import Account

class CreditAccount(Account):
    def __init__(self,no,balance,owners,credit):
        super().__init__(no,balance,owners)
        self._credit = credit

    def __str__(self):
        msg = super().__str__() + " The credit: " + str(self._credit)
        return msg

    def withdraw(self,TakeMoney):
         if TakeMoney <= (self._balance + self._credit):
             super().withdraw(TakeMoney)
         else:
             print("You have not enough balance! ")


    def getCredit(self):
        return self._credit

    def setCredit(self, NewCredit):
        if NewCredit <= 0:
            print("The credit can not be too low")
        else:
            self._credit += NewCredit

def program1():
    namelist = ["Bluto","Popeye"]
    a3 = CreditAccount(3,100,namelist,1000)
    print(a3)
    a3.deposit(900)
    print(a3)
    a3.withdraw(1500)
    print(a3)
    a3.withdraw(600)
    print(a3)

program1()
