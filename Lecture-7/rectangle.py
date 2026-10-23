class Rectangle: 
    def __init__(self): 
        self.length = 0 
        self.breadth = 0 
    # you are not going to add setter or getters for every property 
    # sometimes you want to keep a property from chaning the value 
    # ex: gender - this you will pass while creating the object 
    def set_length(self,new_length): 
        self.length = new_length 
    
    def set_breadth(self,new_breadth): 
        self.breadth = new_breadth 
    
    def get_length(self): 
        return self.length 
    
    def get_breadth(self): 
        return self.breadth 

    def perimeter(self): 
        return 2 * (self.length + self.breadth)

    def area(self): 
        return self.length * self.breadth 

rectangle = Rectangle()
rectangle.set_length(10)
rectangle.set_breadth(20)
print(f"Lenght: {rectangle.get_length()}")
print(f"Breadth: {rectangle.get_breadth()}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")