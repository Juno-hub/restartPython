class BigNumError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("It can only calculate an one digit number.")
    num1 = int(input("Type the first number : "))
    num2 = int(input("Type the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumError("Input Value: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("You typed a wrong number. Type an one digit number")
except BigNumError as err:
    print("Error! Type an one digit number")
    print(err)
finally:
    print("Thank you for using my calculator!")