# Besides "+", ",", Way to use string format
# print("a" + "b")
# print("a", "b")

# Example 1
# %d treates only integer
print("나는 %d살입니다." % 20)
# %s treates string if you use %s, corresponding % 20, 20 becomes string.
print("나는 %s을 좋아합니다." % "파이썬")
print("I am %s years old." % 20)
# %c treates one letter of string
print("Apple은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아한다." % ("파란", "빨간"))

# Example 2
print("I am {} years old.".format(20))
print("I like {} and {}".format("red", "blue"))
print("I like {0} and {1}".format("red", "blue"))
print("I like {1} and {0}".format("red", "blue"))

# Example 3
print("I am {age} years old, I like {color}.".format(age=20, color="red"))

# Example 4 (Above Python version 3.6)
age = 20
color = "red"
print(f"I am {age} years old, I like {color}.")