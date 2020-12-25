# Set(집합)
# No reduplication, No sequence

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# Intersection
print(java & python)
print(java.intersection(python))

# Union
print(java | python)
print(java.union(python))

# Differce of sets
print(java - python)
print(java.difference(python))

# Increasing the number of python developer
python.add("김태호")
print(python)

# Decreasing the number of java developer
java.remove("김태호")
print(java)