# Q) Find standard weight.

# * standard weight: proper weight by individual height

# (Formula by gender)
# Male: height(m) * height(m) * 22
# Female: height(m) * height(m) * 21

# rule 1: Calculate the standard weight using function.
#             * Function Name: std_weight
#             * Argument: hegiht, gender
# rule 2: Standard weight should be displayed up to second decimal point.

# (Output Example)
# 175cm, Male's the standard weight is 67.38kg.

# My answer
def std_weight(height, gender):
    if gender == "Male" or "Man":
        weight = pow(height / 100, 2) * 22
        print(
            "{0}cm, {1}'s the standard weight is {2:.2f}kg".format(
                height, gender, weight
            )
        )
    elif gender == "Female" or "Women":
        weight = pow(height / 100, 2) * 21
        print(
            "{0}cm, {1}'s the standard weight is {2:.2f}kg".format(
                height, gender, weight
            )
        )


height = int(input("What's your height(cm)? "))
gender = input("What's your gender? ")
std_weight(height, gender)

# 나도코딩 answer
def std_weight2(height, gender):
    if gender == "Male":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "Male"
weight = round(std_weight2(height / 100, gender), 2)
print("{0}cm, {1}'s the standard weight is {2}kg".format(height, gender, weight))

# Debriefing(My second answer)
# I want to return weight using 'return'. I think that a sencond code is more clear than a first code.
def std_weight3(height, gender):
    if gender == "Male" or "Man":
        return pow(height / 100, 2) * 22
    elif gender == "Female" or "Women":
        return pow(height / 100, 2) * 22


height = int(input("What's your height(cm)? "))
gender = input("What's your gender? ")
weight = std_weight3(height, gender)
print("{0}cm, {1}'s the standard weight is {2:.2f}kg".format(height, gender, weight))