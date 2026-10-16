class Phone: 
    # class is blue print and object is real world entity of that blue print 
    def __init__(self): # inti -> initialization # this constructor is also called as default constructor 
        # self is link between function and class 
        # self will give you access to class variables and methods 
        # type -> keypad / touch screen 
        # brand -> apple/samsung 
        # model name 
        # storage this are all variables / properties 
        # methods 
        # connect wifi 
        # torch 
        # open
        # close 
        # power on 
        # power off 
        self.type = "touch screen"
        self.brand = "apple"
        self.model_name = "Iphone 17 Pro"
        self.storage = "128GB"

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

my_phone = Phone() # this will internally call __init__ method 
my_phone.model_name = "Iphone 18 Pro"
# print(my_phone.type)
# print(my_phone.brand)
# print(my_phone.model_name)
# print(my_phone.storage)
# my_phone.connect_wifi()
# my_phone.torch()
# my_phone.open("Google meet")
# my_phone.close("Google meet")
# my_phone.power_off()
# my_phone.power_on()

my_samsung = Phone()
my_samsung.brand = "Samsung"
my_samsung.model_name = "Galaxy Ultra S1"
my_samsung.storage = "256GB"