class Laptop:
    def __init__(self, grcode='GR777', expiry=False):
        self.__grcode = grcode  # Private attribute
        self.__expiry = expiry  # Private attribute

    # Getter method for grcode
    def get_grcode(self):
        return self.__grcode

    # Getter method for expiry
    def get_expiry(self):
        return self.__expiry

class Scanner:
    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict  # Private attribute

    def validate_expiry_date(self, laptop):
        # Returns True if allocation has not expired, False if it has expired
        return not laptop.get_expiry()

    def scan(self, empid, laptop):
        # Check if the employee ID is in the dictionary
        if empid in self.__emp_laptop_dict:
            # Check if the laptop assigned to this employee matches the given laptop's grcode
            if self.__emp_laptop_dict[empid].get_grcode() == laptop.get_grcode():
                # Validate the expiry date
                return self.validate_expiry_date(laptop)
        return False

# Creating Laptop objects
laptop1 = Laptop(grcode="GR777", expiry=False)
laptop2 = Laptop(grcode="QR002", expiry=True)
laptop3 = Laptop(grcode="QR003", expiry=False)

# Creating a dictionary to store employee ID and their corresponding Laptop object
emp_laptop_dict = {
    "E001": laptop1,
    "E002": laptop2,
    "E003": laptop3
}

# Creating a Scanner object
scanner = Scanner(emp_laptop_dict)

# Testing the scanner with different employees and laptops
print(scanner.scan(empid="E001", laptop=laptop1))  # Output: True
print(scanner.scan(empid="E002", laptop=laptop2))  # Output: False (allocation expired)
print(scanner.scan(empid="E003", laptop=laptop1))  # Output: False (wrong laptop)