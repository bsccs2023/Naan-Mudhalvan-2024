# Assignment 2
#Assignment on OOP Basics & List - Level 2


class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None
    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount
        
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        amt=0
        for i in range(0,len(quantity_list)):
            amt += quantity_list[i]*price_list[i]
            self.__bill_amount=consultation_fees+amt
    
b1=Bill(12,"abc")
b1.calculate_bill_amount(200,[2,3],[20,50])
print(b1.get_patient_name(),b1.get_bill_id(),b1.get_bill_amount())