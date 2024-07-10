import datetime

class Piano:
    def __init__(self, finish, size, price, manufacture_date):
        self.finish = finish
        # size in cms
        self.size = size
        # price in US $
        self.price = price
        self.manufacture_date = manufacture_date

    # Question #2
    def show(self):
        print(f"This piano has a {self.finish}, is {self.size} in length and costs ${self.price} US")
        print()

    # Question #4
    def is_new(self):
        now = datetime.datetime.now()
        date = now.date()
        if date.year - 2 > self.manufacture_date:
            print(f"The piano is new")
        else:
            print("The piano is not new")
        print()


# Question #1
p1 = Piano("ebony", 165, 75000, 2018)
p2 = Piano("rosewood", 210, 85000, 2022)
p3 = Piano("white", 285, 285000, 2023)

# Question #3
p1.show()

# Question #4
p2.is_new()
p3.show()


class Bechstein(Piano):

    def __init__(self, finish, size, price, manufacture_date, line, features=None):
        self.brand = "Bechstein"
        self.line = line
        if features is None:
            features = []
        self.features = features
        super().__init__(finish, size, price, manufacture_date)

    # Question #2
    def details(self):
        print(f"This {self.brand} is of the {self.line} line and at ${self.price} is priced accordingly")
        print()

    # Question #6
    def add_features(self, feature):
        self.features.append(feature)

    # Question #7
    def list_features(self):
        feature_list = []
        for feature in self.features:
            feature_list.append(feature)
        print(feature_list)
        print()


# Question #1
b1 = Bechstein("walnut", 210, 95000, 2019, "concert")
b2 = Bechstein("ebony", 215, 125000, 1998, "parlor")

# Question #3
b1.details()
b2.details()

# Question #4
b2.is_new()

# Question #5
print(f'The line of the ebony Bechstein is {b1.line}')

# Question #8
b1.add_features("singing tone")
b1.add_features("warm sound")

# Question #9
b1.list_features()