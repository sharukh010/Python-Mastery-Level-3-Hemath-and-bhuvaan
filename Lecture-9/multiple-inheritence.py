import time 
class Watch: 
    def __init__(self,model,price):
        self.model = model 
        self.price = price 

    def get_time(self):
        raw_time = time.gmtime()
        formatted_time = time.strftime("%I:%M:%S",raw_time) 
        print(f"Current time is {formatted_time}")

    def get_date(self): 
        raw_time = time.gmtime()
        formatted_date = time.strftime("%d/%m/%Y",raw_time)
        print(f"Today's Date is {formatted_date}")

    def start_timer(self,minutes):
       print("Started")
       time.sleep(minutes*60)
       print("Ended")


class Mobile: 
    def __init__(self,model,price): 
        self.model = model 
        self.price = price 

    def get_notification(self): 
        print("Notifications...")
    def make_call(self,number): 
        print(f"Making call to {number}")
    def capture_picture(self):
        print("Capturing a picture..")

class SmartWatch(Watch,Mobile): 
    def __init__(self,model,price): 
        Watch.__init__(self,model,price)
        Mobile.__init__(self,model,price)

    def count_steps(self): 
        print("Counting steps...")

    def measure_heart_rate(self): 
        print("Measuring Heart rate..")

    def measure_O2(self): 
        print("Measuring O2...")


apple_watch = SmartWatch("apple",200)
# apple_watch.get_time()
# apple_watch.get_date()
# apple_watch.make_call("Bhuvan")
apple_watch.measure_heart_rate()

