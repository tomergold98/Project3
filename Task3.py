from Account import Account
from CreditAccount import CreditAccount

def getAccountDetails():
    NumAcc = int(input("Enter number account: "))
    Bal = int(input("Enter the balance of the account: "))
    NameOwn = input("Enter the name of owner: ")
    return NumAcc, Bal, NameOwn

def createAccountAC():
    NumAcc, Bal, NameOwn = getAccountDetails()
    return Account(NumAcc,Bal,NameOwn)

def createAccountCR():
    NumAcc, Bal, NameOwn = getAccountDetails()
    Cred = int(input("Enter the credit of the account: "))
    return CreditAccount(NumAcc, Bal, NameOwn, Cred)

def program3():
    a4 = createAccountAC()
    a5 = createAccountCR()
    a6 = createAccountAC()
    a7 = createAccountCR()
    a8 = createAccountAC()
    listAccount = [a4, a5, a6, a7, a8]
    for account in listAccount:
        print(account)
        if type(account) is CreditAccount:
            account.setCredit(1000)
        account.withdraw(2000)
        print(account)

program3()
