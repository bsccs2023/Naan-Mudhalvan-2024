# Object Oriented Programming using Python

# Abstraction & Encapsulation

# Exercise on Access Specifiers - Level 1

class Athlete:
    def __init__(self, name, gender):
        self.__name = name      # Private attribute
        self.__gender = gender  # Private attribute

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    # Method to make the athlete run
    def running(self):
        if self.__gender == "girl":
            print("150mtr running")
        else:
            print("200mtr running")

# Representing Maria, the runner
maria = Athlete(name="Maria", gender="girl")

# Maria starts running
maria.running()