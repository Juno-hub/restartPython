# Q) There is the popular chicken restaurant with waiting guest everyday.
# The restaurant makes an automatic order system to cut off waiting time.
# Check the code, make a proper except syntax.

# rule 1: If input value is lower than 1 or not number, You should deal with ValueError
#         Massage: "You typed a wrong input value."
# rule 2: Total available chicken of waiting guest is ten chickens.
#         If it is sold out, You use custom exception error [SoldOutError].
#         Massage: "We does not take an order because of exhaustion inventory."

# [Code]
# chicken = 10
# waiting = 1
# while True:
#     print("[Available chicken: {0}]".format(chicken))
#     order = int(input("How many chicken would you like to order? "))
#     if order > chicken:
#         print("Not enough ingredient")
#     else:
#         print(
#             "[Waiting number: {0}] Complate to order. The number of ordered chicken is {1}".format(
#                 waiting, order
#             )
#         )
#         waiting += 1
#         chicken -= order

# My answer
# class SoldOutError(Exception):
#     def __init__(self, massage):
#         self.massage = massage

#     def __str__(self):
#         return self.massage


# try:
#     chicken = 10
#     waiting = 1
#     while True:
#         print("[Available chicken: {0}]".format(chicken))
#         order = int(input("How many chicken would you like to order? "))
#         if order < 1 or type(order) != int:
#             raise ValueError

#         if order > chicken:
#             raise SoldOutError(
#                 "We does not take an order because of exhaustion inventory."
#             )
#         else:
#             print(
#                 "[Waiting number: {0}] Complate to order. The number of ordered chicken is {1}".format(
#                     waiting, order
#                 )
#             )
#             waiting += 1
#             chicken -= order
# except ValueError:
#     print("You typed a wrong input value.")
# except SoldOutError as err:
#     print(err)

# 나도코딩 answer
# class SoldOutError(Exception):
#     pass


# chicken = 10
# waiting = 1
# while True:
#     try:
#         print("[Available chicken: {0}]".format(chicken))
#         order = int(input("How many chicken would you like to order? "))
#         if order > chicken:
#             print("Not enough ingredient")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print(
#                 "[Waiting number: {0}] Complate to order. The number of ordered chicken is {1}".format(
#                     waiting, order
#                 )
#             )
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("You typed a wrong input value.")
#     except SoldOutError:
#         print("We does not take an order because of exhaustion inventory.")
#         break

# Debriefing
class SoldOutError(Exception):
    def __init__(self, massage):
        self.massage = massage

    def __str__(self):
        return self.massage


chicken = 10
waiting = 1
while True:
    try:
        print("[Available chicken: {0}]".format(chicken))
        order = int(input("How many chicken would you like to order? "))
        if order > chicken:
            print("Not enough ingredient")
        elif order < 1:
            raise ValueError
        else:
            print(
                "[Waiting number: {0}] Complate to order. The number of ordered chicken is {1}".format(
                    waiting, order
                )
            )
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError(
                "We does not take an order because of exhaustion inventory."
            )
    except ValueError:
        print("You typed a wrong input value.")
    except SoldOutError as err:
        print(err)
        break

# When I make a custom exception, I can deal with that in "pass".
# It should be better to use "elif".
# You should use "break", if it has to be under "while".
# I did not consider of exhaustion inventory. Just I code that order is more than chicken. I should been consideration both them.
