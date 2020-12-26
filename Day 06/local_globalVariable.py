gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[In function] gun: {0}".format(gun))


def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[In function] gun: {0}".format(gun))
    return gun


print("Total: {0}".format(gun))
# checkpoint(2)
checkpoint_ret(gun, 2)
print("Balance: {0}".format(gun))