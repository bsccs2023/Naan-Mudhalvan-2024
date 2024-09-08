class Parrot:
    # Static variable to keep track of the unique number
    __counter = 7000
    
    def __init__(self, name, color):
        # Set the instance variables
        self.__name = name
        self.__color = color
        Parrot.__counter += 1
        self.__unique_number = Parrot.__counter
    
    def get_name(self):
        """Getter method for the parrot's name."""
        return self.__name
    
    def get_color(self):
        """Getter method for the parrot's color."""
        return self.__color
    
    def get_unique_number(self):
        """Getter method for the parrot's unique number."""
        return self.__unique_number
    
    def display_info(self):
        """Display the parrot's information."""
        print(f"Name: {self.__name}")
        print(f"Color: {self.__color}")
        print(f"Unique Number: {self.__unique_number}")

# Test cases
def test_parrot_class():
    # Create instances of Parrot
    parrot1 = Parrot("Polly", "Green")
    parrot2 = Parrot("Coco", "Red")
    parrot3 = Parrot("Kiwi", "Blue")
    parrot4 = Parrot("Rio", "Yellow")

    # Display information of each parrot
    parrot1.display_info()
    print()
    parrot2.display_info()
    print()
    parrot3.display_info()
    print()
    parrot4.display_info()

# Execute the test
test_parrot_class()