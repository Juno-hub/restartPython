customer = "Thor"
index = 5
while index >= 1:
    print("{0}, Please take a coffee. {1} left alarm.".format(customer, index))
    index -= 1
    if index == 0:
        print("Sorry, coffee is disposed.")

customer = "Thor"
person = "Unknown"

while person != customer:
    print("{0}, Please take a coffee.".format(customer))
    person = input("What's your name? ")
