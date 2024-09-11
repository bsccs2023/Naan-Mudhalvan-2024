class Vehicle:
    def __init__(self):
        # Initializing mileage and fuel_left
        self.mileage = None
        self.fuel_left = None

    # Method to calculate distance travelled based on initial fuel
    def identify_distance_travelled(self, initial_fuel):
        distance_travelled = (initial_fuel - self.fuel_left) * self.mileage
        return distance_travelled

    # Method to calculate the distance that can still be traveled
    def identify_distance_that_can_be_travelled(self):
        initial_fuel = 15  # Assuming the tank starts with 15 units of fuel
        distance_travelled = self.identify_distance_travelled(initial_fuel)
        
        if self.fuel_left > 5:
            # Calculates the distance that can be travelled if there's more than 5 units of fuel left
            return (self.fuel_left - 5) * self.mileage
        else:
            # If fuel is less than or equal to 5, no additional distance can be traveled
            return 0

# Example usage
v1 = Vehicle()
v1.mileage = 10     # Setting mileage as 10 units per fuel
v1.fuel_left = 20   # Setting the current fuel left in the vehicle

print(v1.identify_distance_that_can_be_travelled())  # Output: Distance that can be traveled