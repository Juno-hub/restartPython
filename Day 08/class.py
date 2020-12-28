# -- class & __init__ --


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[Move ground unit]")
        print(
            "{0} move at the {1} o'clock. [Speed: {2}]".format(
                self.name, location, self.speed
            )
        )


# # -- Member variable --

# wraith2 = Unit("Mind control Wraith", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} is clocking now.".format(wraith2.name))

# -- Method & Inheritance--
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

    def damaged(self, damage):
        print("{0} get damaged {1}.".format(self.name, damage))
        self.hp -= damage
        print("{0}'s HP is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is dead.".format(self.name))


# firebat1 = AttackUnit("Firebat", 50, 16)
# firebat1.attack("five")
# firebat1.damaged(25)
# firebat1.damaged(25)


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(
            "{0} go to fly at the {1} o'clock. [Speed: {2}]".format(
                name, location, self.flying_speed
            )
        )


# -- Method Overloading --
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # Ground speed is 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[Move flyer unit]")
        self.fly(self.name, location)


# vulture = AttackUnit("Vulture", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("Battlecrusier", 500, 25, 3)

# vulture.move("eleven")
# battlecruiser.move("nine")

# -- Super --
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


supply_dipot = BuildingUnit("Supply depot", 500, "seven")

# -- Pass --
# def game_start():
#     print("[Alarm] Start the new game.")


# def game_over():
#     pass


# game_start()
# game_over()