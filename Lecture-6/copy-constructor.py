class Phone: 
    def __init__(self,
                 phone): 
        if phone == None: 
            self.phone_type = ""
            self.brand = ""
            self.model_name = ""
            self.storage = ""
        else: 
            self.phone_type = phone.phone_type
            self.brand = phone.brand 
            self.model_name = phone.model_name
            self.storage = phone.storage

    def connect_wifi(self): 
        print("Connected to Wi-Fi")

    def torch(self): 
        print("Torch is on")

    def open(self,app): 
        print(f"Opening {app}...")

    def close(self,app): 
        print(f"Closing {app}...")

    def power_on(self): 
        print("Powering on...")
    def power_off(self): 
        print("Powering off...")

    def display(self): 
        print(f"Phone Type: {self.phone_type}")
        print(f"Brand Name: {self.brand}")
        print(f"Model Name: {self.model_name}")
        print(f"Storage Capacity: {self.storage}")

original = Phone(None)
original.phone_type = "Foldable"
original.brand = "Samsung"
original.model_name = "Z Fold"
original.storage = "256GB"
original.display()
copy = Phone(original)
copy.display()