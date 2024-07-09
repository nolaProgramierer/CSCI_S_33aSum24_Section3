import datetime

# Each of our pianos have the following characteristics:
# 1) finish
# 2) size
# 3) price
# 4) the date it was made

# Here's the class (blueprint)

class Piano:
    def __init__(self, finish, size, price, manufacture_date):
        self.finish = finish
        # size in cms
        self.size = size
        # price in US $
        self.price = price
        self.manufacture_date = manufacture_date

    
# 1) Let's build three pianos (instances of the class)

# 2) What would we have to do to display the values of these pianos to a user

# 3) Let's call the show method

# 4) Given that our pianos have a manufacture date, how would we 
#    determine whether a piano is new (less than 2 years old)

# 5) Find out if the 'Rosewood' piano is new
       

#--------------------------------------------------------------
print()
print()
# Here is a sub class of the Piano class which inherits all the
# Piano class instance variables and method, plus adds more 
# functionality without duplicating code from the superclass (Piano)
#--------------------------------------------------------------
class Bechstein(Piano):

    def __init__(self, finish, size, price, manufacture_date, line, features=None):
        self.brand = "Bechstein"
        self.line = line
        if features is None:
            features = []
        self.features = features
        super().__init__(finish, size, price, manufacture_date)


# 1) Instantiate 2 objects of the Bechstein subclass

# 2) Write a show method, as in the superclass, for the subclass

# 3) Show the values of the instance variable properties of each subclass object

# 4) Find out if the ebony Bechstein is new, using the method of the superclass

# 5) Return the line of the ebony Bechstein

# 6) Write a method to add features

# 7) Write a method to return features

# 8) Add 2 features to the walnut Bechstein

# 9) Return the features of the walnut Bechstein
