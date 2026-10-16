class Phone: 
    def __init__(self,
                 phone_type,
                 brand,
                 model_name,
                 storage): 
        self.phone_type = phone_type
        self.brand = brand 
        self.model_name = model_name
        self.storage = storage

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

my_phone = Phone(
    "Touch Screen",
    "Samsung",
    "Galaxy S1 Ultra",
    "256GB"
)