import datetime

class GarmentOrder:
    # Static variables
    garment_dict = {
        "shirt": [45, 400, 30],
        "trousers": [250, 500, 25],
        "saree": [500, 750, 10],
        "jersey": [750, 200, 5]
    }

    def __init__(self, cloth_type, no_of_piece):
        # Instance variables
        self.__cloth_type = cloth_type
        self.__no_of_piece = no_of_piece
        self.__order_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__delivery_date = None

    def get_cloth_type(self):
        return self.__cloth_type

    def get_no_of_piece(self):
        return self.__no_of_piece

    def get_order_date(self):
        return self.__order_date

    def get_delivery_date(self):
        return self.__delivery_date

    def take_order(self):
        if self.__cloth_type in GarmentOrder.garment_dict and GarmentOrder.garment_dict[self.__cloth_type][0] >= self.__no_of_piece:
            # Calculate amount
            amount = GarmentOrder.garment_dict[self.__cloth_type][1] * self.__no_of_piece

            # Update stock
            GarmentOrder.garment_dict[self.__cloth_type][0] -= self.__no_of_piece
            self.__delivery_date = (datetime.datetime.now() + datetime.timedelta(days=GarmentOrder.garment_dict[self.__cloth_type][2])).strftime("%d/%m/%Y")

            return amount
        else:
            return -1

    def calculate_amount(self):
        # This method is already defined in the take_order() method
        return self.take_order()

    def update_stock(self):
        # This method is already defined in the take_order() method
        return self.take_order()

# Test the GarmentOrder class
order1 = GarmentOrder("shirt", 10)

# Take the order and get the result
result = order1.take_order()
print("Order result:", result)

# Display order details
print("Cloth Type:", order1.get_cloth_type())
print("Number of Pieces:", order1.get_no_of_piece())
print("Order Date:", order1.get_order_date())
print("Delivery Date:", order1.get_delivery_date())

# Check the updated garment_dict
print("Garment Dictionary:", GarmentOrder.garment_dict)