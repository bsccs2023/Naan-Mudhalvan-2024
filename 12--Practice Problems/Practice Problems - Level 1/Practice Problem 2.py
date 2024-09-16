class Dog:
    # Static variables
    dog_breed_dict = {'Labrador Retriever': 5, 'German Shepherd': 12, 'Beagle': 10}
    counter = 100

    def __init__(self, breed_list, accessories_required):
        # Instance variables
        self.__breed_list = breed_list
        self.__dog_id_list = []  # Start with an empty list
        self.__price = 0
        self.__accessories_required = accessories_required  # Boolean value for accessories requirement

    def validate_breed(self):
        # Check if all breeds requested by the customer are available
        for breed in self.__breed_list:
            if breed not in Dog.dog_breed_dict:
                return False
        return True

    def validate_quantity(self):
        # Check if at least one dog is available for each breed requested
        for breed in self.__breed_list:
            if Dog.dog_breed_dict[breed] <= 0:
                return False
        return True

    def generate_dog_id(self, breed):
        # Generate dog ID using breed and the counter
        Dog.counter += 1
        dog_id = f"{breed[0].upper()}{Dog.counter}"
        self.__dog_id_list.append(dog_id)
        return dog_id  # Return the generated dog ID

    def get_dog_price(self, breed):
        # Return the price based on breed
        breed_price_dict = {'Labrador Retriever': 800, 'German Shepherd': 1230, 'Beagle': 650}
        return breed_price_dict.get(breed, 0)  # Default to 0 if breed not found

    def calculate_total_price(self):
        # Validate breed and quantity
        if not self.validate_breed():
            return -1  # Breed is not valid

        if not self.validate_quantity():
            return -2  # Quantity is not available

        # Calculate the total price for all breeds
        for breed in self.__breed_list:
            # Update quantity in dog_breed_dict
            Dog.dog_breed_dict[breed] -= 1
            
            # Generate dog ID and append to list
            generated_id = self.generate_dog_id(breed)
            
            # Calculate price for each breed
            breed_price = self.get_dog_price(breed)
            self.__price += breed_price

        # Add price for accessories if required
        if self.__accessories_required:
            self.__price += 350

        # Provide 5% discount if total price exceeds 1500
        if self.__price > 1500:
            self.__price *= 0.95  # Apply 5% discount

        return self.__price  # Return the total price

    # Getter methods
    def get_dog_id_list(self):
        return self.__dog_id_list

    def get_breed_list(self):
        return self.__breed_list

    def get_price(self):
        return self.__price

    def get_accessories_required(self):
        return self.__accessories_required


# Test the Dog class
dog1 = Dog(['Labrador Retriever', 'Beagle'], True)

# Calculate total price
total_price = dog1.calculate_total_price()
print("Total Price:", total_price)  # Print the total price

# Print the list of generated dog IDs
print("Dog IDs:", dog1.get_dog_id_list())  # Use getter method

# Print the list of requested breeds
print("Breed List:", dog1.get_breed_list())  # Use getter method

# Print the price
print("Price:", dog1.get_price())  # Use getter method

# Print if accessories are required
print("Accessories Required:", dog1.get_accessories_required())  # Use getter method

# Check the updated breed availability
print("Dog Breed Dictionary After Sale:", Dog.dog_breed_dict)