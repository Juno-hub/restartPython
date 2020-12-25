# Q) Your shcool holds python hackathon.
# They progress comment participation event in order to attendance.
# One gets a chicken coupon, three people get coffee coupons by drawing lots.
# Code drawing lots programm

# rule 1: The number of comment is 20 and their ID are 1 ~ 20.
# rule 2: No reduplication
# rule 3: You use random module(shuffle, sample)

# (Example)
#  -- Winner --
#  Chicken winner: 1
#  Coffee winner: [2, 3, 4]
#  -- Congratulations! --

#  (Use Example)
#  from ramdom import *
#  lst = [1, 2, 3, 4, 5]
#  print(lst)
#  shuffle(lst)
#  print(lst)
#  print(sample(lst, 1))

# My answer
from random import *

id = set(range(1, 21))
winner_ck = set(sample(id, 1))
id = id - winner_ck
winner_cf = set(sample(id, 3))
id = id - winner_cf
winner_ck = list(winner_ck)
winner_cf = list(winner_cf)
print(
    """
    -- Winner --
     Chicken winner:""",
    winner_ck,
    """
     Coffee winner:""",
    winner_cf,
    """
    -- Congratulations! --
    """,
)

# 나도코딩 answer
from random import *

users = range(1, 21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print(" -- Winner -- ")
print("Chicken winner: {0}".format(winners[0]))
print("Coffee winner: {0}".format(winners[1:]))
print(" -- Congratulations! -- ")

# # Debriefing
# First of all, I don't stay true to the question.
# I don't use shuffle() and I return list of chicken winner.
# I don't know that it existes that range of all classes because I did't check range of type.
# I don't think of way to draw 4 people and divide.