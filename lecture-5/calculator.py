class Calculator:
    def __init__(self,num1,num2): 
        # if you want to create variable inside a class 
        # you will create it here 
        self.num1 = num1 
        self.num2 = num2 
    # method 
    # self -> you are linking the class and the method 
    def add(self): 
        return self.num1 + self.num2 
    
    def sub(self): 
        return self.num1 - self.num2 
    
    def mul(self): 
        return self.num1 * self.num2 
    
    def div(self): 
        return self.num1 / self.num2 

def message(): 
    print("I'm inside calculator file")
    
