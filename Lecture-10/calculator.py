class CalculatorV1: 
    def __init__(self): 
        self.num1 = 0 
        self.num2 = 0 

    def set_values(self,num1,num2): 
        if isinstance(num1,(int,float)) and isinstance(num2,(int,float)): 
            self.num1 = num1 
            self.num2 = num2 
        else: 
            raise ValueError(f"num1 and num2 must be int or float. ({type(num1),type(num2)}) are given")

    def get_values(self): 
        return (self.num1,self.num2)

    def add(self): 
        return self.num1 + self.num2 

    def sub(self): 
        return self.num1 - self.num2 


class CalculatorV2(CalculatorV1):
    def __init__(self): 
        super().__init__()

    def mul(self): 
        return self.num1 * self.num2 

    def div(self): 
        if self.num2 == 0: 
            raise ZeroDivisionError("Cannot divide with 0")
        else: 
            return self.num1 / self.num2 

class CalculatorV3(CalculatorV2): 
    def __init__(self): 
        super().__init__()

    def power(self): 
        return self.num1 ** self.num2 

    def modulo_division(self): 
        return self.num1 % self.num2 


cal = CalculatorV3()

