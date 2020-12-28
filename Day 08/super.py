class Unit:
    def __init__(self):
        print("Unit Constructor")


class Flyable:
    def __init__(self):
        print("Flyable Constructor")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()  # No support multiple inheritance
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()