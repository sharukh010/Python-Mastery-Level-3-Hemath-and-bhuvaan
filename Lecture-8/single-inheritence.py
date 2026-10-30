"""
In single inheritence there will be one parent and one child 
and the child will inherit from the parent 
"""
class Car: 
    def __init__(self,fuel_type,company_name): 
        self.fuel_type = fuel_type 
        self.company_name = company_name 

    def run_on_fuel(self): 
        print("Running on Fuel...")

class HybridCar(Car): 
    def __init__(self,fuel_type,company_name,battery_life): 
        # call parent class constructor 
        super().__init__(fuel_type,company_name) # calling parent class 
        self.battery_life = battery_life 

    def run_on_electricity(self): 
        print("Running on Electricity...")

bmw = Car("Diesel","BMW")
tesla = HybridCar("Petrol","Tesla",15)
# print(bmw.fuel_type)
# bmw.run_on_fuel()
# bmw.run_on_electricity() # this will give you error 
# inheritence is uni directionaly i.e, parent -> child 
# tesla.run_on_fuel()
# tesla.run_on_electricity()
print(tesla.battery_life)