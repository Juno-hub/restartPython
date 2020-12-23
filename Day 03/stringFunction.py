python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

find = python.find("n")
print(find)
find = python.find("n", find + 1)
print(find)

# print(python.index("Java") -----> In this case, index() make an error.
# print(python.find("Java")) -----> In this case, find() return -1.

print(python.count("n"))