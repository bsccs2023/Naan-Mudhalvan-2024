class Customer:
    def __init__(self, customer_id, customer_name, address):
        # Store customer_id as an integer and not convert it to a string here
        self.__customer_id = customer_id  
        self.__customer_name = customer_name
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        # Convert customer_id to string only when validating
        customer_id_str = str(self.__customer_id)
        # Validate: customer_id should be a 6-digit number starting with '1'
        return customer_id_str.isdigit() and len(customer_id_str) == 6 and customer_id_str.startswith('1')


class Freight:
    counter = 198  # Initialize counter

    def __init__(self, from_customer, recipient_customer, weight, distance):
        self.__from_customer = from_customer
        self.__recipient_customer = recipient_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_id = None
        self.__freight_charge = 0

    def get_freight_id(self):
        return self.__freight_id

    def get_freight_charge(self):
        return self.__freight_charge

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def validate_distance(self):
        # Distance should be between 500 and 5000
        return 500 <= self.__distance <= 5000

    def validate_weight(self):
        # Weight should be a multiple of 5
        return self.__weight % 5 == 0

    def forward_cargo(self):
        if (self.__from_customer.validate_customer_id() and
            self.__recipient_customer.validate_customer_id() and
            self.validate_weight() and
            self.validate_distance()):

            # Generate freight_id (increment counter by 2 to make sure it's even)
            Freight.counter += 2
            self.__freight_id = Freight.counter

            # Calculate freight charge: 150 Rs/kg + 60 Rs/km
            self.__freight_charge = (self.__weight * 150) + (self.__distance * 60)
            
            # Output freight details
            print(f"Freight ID: {self.__freight_id}")
            print(f"Freight Charge: Rs.{self.__freight_charge}")
        else:
            self.__freight_charge = 0
            print("Error: Invalid data. Freight charge not calculated.")


# Example Usage
# Creating Customer objects
cust1 = Customer(123456, 'Jack', 'Mysore')
cust2 = Customer(198765, 'Jill', 'Bangalore')

# Creating Freight object
freight = Freight(cust1, cust2, 25, 1500)

# Forwarding cargo and displaying results
freight.forward_cargo()