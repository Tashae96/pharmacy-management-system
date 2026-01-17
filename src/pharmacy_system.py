from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Person"
    
 #polymorphism and inheritance   
class Customer(Person):
    def get_role(self):
        return "Customer"
    
class Pharmacist(Person):
    def get_role(self):
        return "Pharmacist"
    
#polymorphism    
people = [Customer("A"), Pharmacist("B")]
for p in people:
    print (p.get_role())

class Medicine:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock  # private

    def reduce_stock(self, quantity):
        if quantity > self.__stock:
            raise ValueError("Insufficient stock")
        self.__stock -= quantity

    def get_stock(self):
        return self.__stock
  
class Inventory:
    def __init__(self):
        self._medicines = []

    def add_medicine(self, medicine):
        self._medicines.append(medicine)

    def find_medicine(self, name):
        for med in self._medicines:
            if med.name == name:
                return med
        return None

class Prescription:
    def __init__(self, customer, medicine, quantity):
        self.customer = customer
        self.medicine = medicine
        self.quantity = quantity

    def total_price(self):
        return self.medicine.price * self.quantity
    
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} in cash"


class MobilePayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} via mobile money"



class PharmacySystem:
    def __init__(self):
        self.inventory = Inventory()

    def process_prescription(self, prescription, payment_method):
        prescription.medicine.reduce_stock(prescription.quantity)
        total = prescription.total_price()
        return payment_method.pay(total)



