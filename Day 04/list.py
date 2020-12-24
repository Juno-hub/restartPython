# List

# 10, 20, and 30 of people get on the subway by subway compartment
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#  What subway compartment is 조세호 gets on the subway?
print(subway.index("조세호"))

# 하하 takes a subway next station.
subway.append("하하")
print(subway)

# 정형돈 sits between 유재석 and 조세호
subway.insert(1, "정형돈")
print(subway)

# They get off the subway one person at a time
print(subway.pop())
print(subway)

# How many people have the same name in the subway?
subway.append("유재석")
print(subway.count("유재석"))

# Arrangement
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# Inverse
num_list.reverse()
print(num_list)

# Clear
num_list.clear()
print(num_list)

# Expansion
number_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

number_list.extend(mix_list)
print(num_list)