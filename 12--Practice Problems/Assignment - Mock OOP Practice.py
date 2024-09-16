class Mart:
    item_name_list = ["Chocolate", "Perfume", "Bouquet", "Apparel"]
    item_price_list = [200, 400, 150, 300]
    item_quantity_list = [10, 20, 30, 40]

    def find_price_per_item(self, item_name):
        if item_name in Mart.item_name_list:
            index = Mart.item_name_list.index(item_name)
            return Mart.item_price_list[index]
        return -1


class OnlineMart(Mart):
    def __init__(self, order):
        self.__online_discount_percentage = None
        self.__order = order

    def identify_online_discount(self):
        if self.__order.get_payment_mode() == 'Prepaid':
            self.__online_discount_percentage = 5  # 5% discount
        elif self.__order.get_payment_mode() == 'COD':
            self.__online_discount_percentage = 2  # 2% discount
        else:
            self.__online_discount_percentage = -1

    def get_order(self):
        return self.__order

    # Method to find the price per item, including discount logic
    def find_price_per_item(self, item_name):
        initial_price = Mart.find_price_per_item(self, item_name)
        if initial_price == -1:
            return -1
        
        # Apply discount if applicable
        self.identify_online_discount()
        if self.__online_discount_percentage == -1:
            return -1

        # Calculate final price after discount
        discount = (initial_price * self.__online_discount_percentage) / 100
        final_price = initial_price - discount
        return final_price

    # Method to check if the item is available and quantity is sufficient
    def check_item_availability(self):
        item_name = self.__order.get_item_name()
        quantity_required = self.__order.get_quantity_required()

        if item_name not in Mart.item_name_list:
            return -1

        index = Mart.item_name_list.index(item_name)

        if Mart.item_quantity_list[index] < quantity_required:
            return -1

        # Deduct the required quantity from Mart's stock
        Mart.item_quantity_list[index] -= quantity_required
        return quantity_required

    # Method to ship the order
    def ship_order(self):
        # Step 1: Check item availability
        quantity = self.check_item_availability()
        if quantity == -1:
            self.__order.set_order_price(-1)
            self.__order.set_tracking_id("NA")
            return

        # Step 2: Find the price per item
        price_per_item = self.find_price_per_item(self.__order.get_item_name())
        if price_per_item == -1:
            self.__order.set_order_price(-1)
            self.__order.set_tracking_id("NA")
            return

        # Step 3: Calculate the total order price
        order_price = quantity * price_per_item
        self.__order.set_order_price(order_price)

        # Step 4: Generate the tracking ID
        self.__order.generate_tracking_id()


class Order():
    __counter = 1000  # Static variable to track order numbers

    def __init__(self, item_name, quantity_required, payment_mode):
        self.__tracking_id = None
        self.__item_name = item_name
        self.__quantity_required = quantity_required
        self.__payment_mode = payment_mode
        self.__order_price = None

    def get_tracking_id(self):
        return self.__tracking_id

    def set_tracking_id(self, tracking_id):
        self.__tracking_id = tracking_id

    def get_item_name(self):
        return self.__item_name

    def get_quantity_required(self):
        return self.__quantity_required

    def get_payment_mode(self):
        return self.__payment_mode

    def get_order_price(self):
        return self.__order_price

    def set_order_price(self, order_price):
        self.__order_price = order_price

    # Method to generate a tracking ID
    def generate_tracking_id(self):
        if self.__tracking_id is None:  # Only generate the ID if it's not already set
            self.__tracking_id = f"TR{Order.__counter}"
            Order.__counter += 1  # Increment the counter for the next order


# You may modify the below code for testing
order_obj = Order('Bouquet', 20, 'Prepaid')
online_mart_object = OnlineMart(order_obj)
online_mart_object.ship_order()
print('Tracking ID :', online_mart_object.get_order().get_tracking_id())
print('Order Price :', online_mart_object.get_order().get_order_price())