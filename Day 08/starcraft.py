from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}, good to go sir.".format(name))

    def move(self, location):
        print(
            "{0} move at the {1} o'clock. [Speed: {2}]".format(
                self.name, location, self.speed
            )
        )

    def damaged(self, damage):
        print("{0} get damaged {1}.".format(self.name, damage))
        self.hp -= damage
        print("{0}'s HP is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is dead.".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(
            "{0} attack enemy at the {1} o'clock. [Damage: {2}]".format(
                self.name, location, self.damage
            )
        )


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} go to fly at the {1} o'clock. [Speed: {2}]".format(
                name, location, self.flying_speed
            )
        )


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # Ground speed is 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} use the stimpack. (Decrease HP 10)".format(self.name))
        else:
            print("Not enough {0}'s HP.".format(self.name))


class Tank(AttackUnit):
    siege_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Seige Tank", 150, 1, 35)
        self.seige_mode = False

    def set_seige_mode(self):
        if Tank.siege_developed == False:
            return

        if self.seige_mode == False:
            print("{0} convert the siege mode.".format(self.name))
            self.damage *= 2
            self.seige_mode = True
        else:
            print("{0} unlock the siege mode.".format(self.name))
            self.damage /= 2
            self.seige_mode = False


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print("{0} use the clocking.".format(self.name))
            self.clocked = True
        else:
            print("{0} unlock the clocking.".format(self.name))
            self.clocked = False


def game_start():
    print("[Alarm] Start the new game.")


def game_over():
    print("Player: GG")
    print("[Player] has left the game.")


# Game Start!
game_start()
# Generate 3 Marine
m1 = Marine()
m2 = Marine()
m3 = Marine()
# Generate 2 Seige Tank
t1 = Tank()
t2 = Tank()
# Generate 1 Wraith
w1 = Wraith()
# Control all unit
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# Move all unit
for unit in attack_units:
    unit.move("one")

# Develope the siegie mode
Tank.siege_developed = True
print("[Alarm] Complete to develope the siege mode")

# Prepare attack (Marine: Stimpack, Tank: Seige mode, Wraith: Clocking)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seige_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
# Attack
for unit in attack_units:
    unit.attack("one")
# Damage
for unit in attack_units:
    unit.damaged(randint(5, 21))  # Untis get damaged at random between 5 and 20
# Game Over
game_over()
