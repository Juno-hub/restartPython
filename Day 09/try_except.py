try:
    print("It is a division calculator")
    nums = []
    nums.append(int(input("Type the first number : ")))
    nums.append(int(input("Type the second number : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error! Invalid literal")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Unknown err!")
    print(err)