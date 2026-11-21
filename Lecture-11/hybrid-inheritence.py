class Human: 
    def __init__(self,name,age): 
        self.name = name 
        self.age = age 

    def info(self): 
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Male(Human): 
    def __init__(self,name,age): 
        super().__init__(name,age)
        self.gender = "male"

    def info_v2(self): 
        self.info()
        print(f"Gender: {self.gender}")


class Female(Human): 
    def __init__(self,name,age): 
        super().__init__(name,age)
        self.gender = "female"

    def info_v2(self): 
        self.info()
        print(f"Gender: {self.gender}")

# human -> male -> teen male (heirarchy + multilevel)
class TeenMale(Male): 
    def __init__(self,name,age,height): 
        super().__init__(name,age)
        self.height = height 

    def who_am_i(self): 
        print("Teenager")