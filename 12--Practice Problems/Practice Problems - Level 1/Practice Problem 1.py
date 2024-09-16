class Purchase:
    # Static variables
    list_of_items = ['Cake', 'Soap', 'Jam', 'Cereal', 'Hand Sanitizer', 'Biscuits', 'Bread', 'Chocolates']
    list_of_count_of_each_item_sold = [0] * len(list_of_items)
    
    def __init__(self):
        # Private attributes
        self.__items_purchased = []
        self.__item_on_offer = None
    
    def get_items_purchased(self):
        # Accessor method to get items purchased
        return self.__items_purchased
    
    def get_item_on_offer(self):
        # Accessor method to get the item on offer
        return self.__item_on_offer
    
    def provide_offer(self):
        # Check if "Soap" (case-insensitive) is in the purchased items
        if any(item.lower() == 'soap' for item in self.__items_purchased):
            # Increment the count of Hand Sanitizer
            hand_sanitizer_index = self.list_of_items.index('Hand Sanitizer')
            self.list_of_count_of_each_item_sold[hand_sanitizer_index] += 1
            # Set the item on offer
            self.__item_on_offer = 'HAND SANITIZER'
    
    def sell_items(self, list_of_items_to_be_purchased):
        # Reset the purchased items list for each call to reset state
        self.__items_purchased = []
        
        for item in list_of_items_to_be_purchased:
            # Find the matching item from list_of_items in a case-insensitive way
            for i, list_item in enumerate(self.list_of_items):
                if list_item.lower() == item.lower():
                    # Update count for the matched item
                    self.list_of_count_of_each_item_sold[i] += 1
                    # Append the original case item from the input to items_purchased
                    self.__items_purchased.append(item)
                    break  # Stop searching after the first match
        
        # Check for offers
        self.provide_offer()
    
    @staticmethod
    def find_total_items_sold():
        return sum(Purchase.list_of_count_of_each_item_sold)

# Testing the Purchase class

# Creating an object of the Purchase class
purchase1 = Purchase()

# Customer purchases items
purchase1.sell_items(['JAM', 'CHOcolates', 'Soap'])

# Display the details for the sample test case
print("Sample Test Case - Items Purchased:", purchase1.get_items_purchased())  # Access via getter
print("Sample Test Case - Item on Offer:", purchase1.get_item_on_offer())      # Access via getter
print("Sample Test Case - Total Items Sold:", Purchase.find_total_items_sold())

# For Purchase::self.__item_on_offer, expected output is N/A
# Since it is a private attribute, there is no direct output expected from it.