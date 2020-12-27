print("Python", "Java", sep=", ", end="?")
print("Which the language for fun?")

import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# The exam marks
scores = {"Math": 0, "English": 50, "Coding": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# Waiting Number
# 001, 002, 003 ...
for num in range(1, 21):
    print("Waiting Number: " + str(num).zfill(3))

answer = input("Fill out anything : ")  # input() makes any value string type.
print("Do you fill out '" + answer + "' ?")
