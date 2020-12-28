# Q) Make the real estate program using the given code.

# (Print Example)
# There is 3 houses for sale.
# 강남 Apartment the value of price: 10억, 2010
# 마포 Studio a charter price: 5억, 2007
# 송파 Villa the rent per month price: 500/50, 2000

# [Code]
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass

#     def show_detail(self):
#         pass

# My answer
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(
            "{0} {1} {2}: {3}, {4}".format(
                self.location,
                self.house_type,
                self.deal_type,
                self.price,
                self.completion_year,
            )
        )


class Gangnam(House):
    def __init__(self):
        House.__init__(self, "강남", "Apartment", "the value of price(매매)", "10억", 2010)


class Mapo(House):
    def __init__(self):
        House.__init__(self, "마포", "Studio", "a charter price(전세)", "5억", 2007)


class Songpa(House):
    def __init__(self):
        House.__init__(
            self, "송파", "Villa", "the rent per month price(월세)", "500/50", 2000
        )


g1 = Gangnam()
m1 = Mapo()
s1 = Songpa()

house_for_sale = []
house_for_sale.append(g1)
house_for_sale.append(m1)
house_for_sale.append(s1)

print("There is {0} houses for sale.".format(len(house_for_sale)))
for house in house_for_sale:
    house.show_detail()

# 나도코딩 answer
class House2:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(
            self.location,
            self.house_type,
            self.deal_type,
            self.price,
            self.completion_year,
        )


house = []
house1 = House2("강남", "Apartment", "매매", "10억", 2010)
house2 = House2("마포", "Studio", "전세", "5억", 2007)
house3 = House2("송파", "Villa", "월세", "500/50", 2000)

house.append(house1)
house.append(house2)
house.append(house3)

print("There is {0} houses for sale.".format(len(house)))
for houses in house:
    houses.show_detail()
