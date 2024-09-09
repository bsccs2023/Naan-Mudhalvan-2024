class Vehicle:
    def __init__(self): #,vehicle_cost,vehicle_type,vehicle_id,premium_amount
        self.__vehicle_type=None
        self.__vehicle_id=None
        self.__vehicle_cost=None
        self.__premium_amount=None

    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=(2/100)*self.__vehicle_cost
        if self.__vehicle_type== "Four Wheeler":
            self.__premium_amount=(6/100)*self.__vehicle_cost
        else:
            print("Invalid Vehicle Type")

    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount

    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount

    def display_vehicle_details(self):
        print(self.__vehicle_cost,self.__premium_amount,self.__vehicle_type,self.__vehicle_id)

v1 = Vehicle()
v1.set_vehicle_id(10)
v1.set_vehicle_type("Four Wheeler")
v1.set_vehicle_cost(500000)
v1.calculate_premium()
v1.display_vehicle_details()

