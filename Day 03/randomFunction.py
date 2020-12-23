from random import *

# Generate random number between 0.0 to 1.0 except for 1
print(random())

# Generate random number between 0.0 to 10.0 except for 10 because of multiplying by 10
print(random() * 10)

# Generate random number that is 0 or more and less than 10
print(int(random() * 10))

# Generate a random natural number that is 1 or more and 10 or less
print(int(random() * 10) + 1)

# Generate a lottery number
print(int(random() * 45) + 1)

# Same meanging above code
print(randrange(1, 46))

# Return random integer in range, including both end point
print(randint(1, 45))