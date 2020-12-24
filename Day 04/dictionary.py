# Key has string as well as number.
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) ---> In this case, "hi" doesn't be returned and programm is exited like index()
# print(cabinet.get(5)) ---> In this case, None and "hi" are returned
print("hi")

# If cabinet[5] does not exist, return "available"
print(cabinet.get(5, "available"))

# Whether exist key in dictionary
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# New customer
cabinet[3] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# Customer leave
del cabinet[3]
print(cabinet)

# Return key of dictionary
print(cabinet.keys())

# Return value of dictionary
print(cabinet.values())

# Return key & value of dictionary
print(cabinet.items())

# Clear
cabinet.clear()
print(cabinet)