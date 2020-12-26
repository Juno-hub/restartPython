def open_account():
    print("Create a new account.")


def deposit(balance, money):
    print("Complete deposit. Your balance is ${0}".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("Complete withdraw. Your balance is ${0}".format(balance - money))
        return balance - money
    else:
        print("Not enough balance. Your balance is ${0}".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 1
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 100)
balance = withdraw(balance, 40)
commission, balance = withdraw_night(balance, 40)
print("Commission is ${0} , Your balance is ${1}".format(commission, balance))