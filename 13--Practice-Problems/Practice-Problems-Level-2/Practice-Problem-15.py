class Buyer:
    def __init__(self, name, email_id):
        self.__name = name
        self.__email_id = email_id

    def get_name(self):
        return self.__name

    def get_email_id(self):
        return self.__email_id

    def purchase(self, item_name, quantity, emi):
        index = OnlinePortal.search_item(item_name)
        if index != -1:
            if OnlinePortal.quantity_list[index] >= quantity:
                return OnlinePortal.place_order(index, emi, quantity)
            else:
                return -1
        else:
            return -2


class OnlinePortal:
    item_list = ["iPhone 14", "Samsung Galaxy S23", "Google Pixel 7", "OnePlus 11"]
    quantity_list = [10, 15, 20, 8]
    price_list = [100000, 90000, 80000, 70000]

    @staticmethod
    def search_item(item):
        if item in OnlinePortal.item_list:
            return OnlinePortal.item_list.index(item)
        else:
            return -1

    @staticmethod
    def place_order(index, emi, quantity):
        OnlinePortal.quantity_list[index] -= quantity
        total_cost = OnlinePortal.price_list[index] * quantity
        if emi:
            total_cost *= 1.02
        else:
            total_cost *= 0.98
        return total_cost

    @staticmethod
    def add_stock(item_name, quantity):
        if item_name in OnlinePortal.item_list:
            index = OnlinePortal.item_list.index(item_name)
            if OnlinePortal.quantity_list[index] <= 10:
                OnlinePortal.quantity_list[index] += quantity
                return 1
            else:
                return -1
        else:
            return -2

    @staticmethod
    def add_item(item_name, price, quantity):
        if item_name not in OnlinePortal.item_list:
            OnlinePortal.item_list.append(item_name)
            OnlinePortal.price_list.append(price)
            OnlinePortal.quantity_list.append(quantity)
            return 1
        else:
            return -2


# Test the classes
buyer = Buyer("John Doe", "johndoe@example.com")
cost = buyer.purchase("iPhone 14", 5, True)
print("Total cost:", cost)