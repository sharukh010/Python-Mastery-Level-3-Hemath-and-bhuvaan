"""
Parent class: one 
child classes: many 

ex: 
Human -> parent class 
Male, Female -> child classes 

ex: 
mamals -> parent class 
reptials , animals , fishes -> child classes 
"""

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


male = Male("Alex",30)
female = Female("Barb",24)
male.info_v2()
female.info_v2()
