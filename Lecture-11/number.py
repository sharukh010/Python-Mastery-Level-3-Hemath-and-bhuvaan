class Number: 
    def __init__(self,value=0):
        if value == 0:  
            self.value = value 
        elif isinstance(value,(int,float)): 
            self.value = value 
        else: 
            raise ValueError(f"cannot store {type(value)}. only (int,float) are supported")
    def __add__(self,other): 
        if isinstance(other,(int,float)): 
            return Number(self.value + other)
        return Number(self.value + other.value)

    def __sub__(self,other):
        if isinstance(other,(int,float)): 
            return Number(self.value - other) 
        return Number(self.value - other.value)

    def __mul__(self,other): 
        if isinstance(other,(int,float)): 
            return Number(self.value * other.value)
        return Number(self.value * other.value)

    def __truediv__(self,other): 
        if isinstance(other,(int,float)):
            if other == 0: 
                raise ZeroDivisionError("cannot divide with zero") 
            return Number(self.value / other)
        if  other.value == 0: 
            raise ZeroDivisionError("cannot divide with zero")
        return Number(self.value / other.value)

    def __mod__(self,other): 
        if isinstance(other,(int,float)): 
                    return Number(self.value % other)
        return Number(self.value % other.value)

    def __floordiv__(self, other):
        if isinstance(other,(int,float)): 
            return Number(self.value // other)
        return Number(self.value // other.value)

    def __pow__(self, other):
        if isinstance(other,(int,float)): 
            return Number(self.value ** other)
        return Number(self.value ** other.value)

    # comparision operators -> returns boolean values  
    def __eq__(self, other): # ==
        return self.value == other.value 

    def __ne__(self,other): # != 
        return self.value != other.value 

    def __lt__(self,other): # < 
        return self.value < other.value 

    def __gt__(self,other): # > 
        return self.value > other.value 

    def __le__(self,other): 
        return self.value <= other.value 

    def __ge__(self,other): 
        return self.value >= other.value 
    
    def __str__(self): 
        return str(self.value)

num1 = Number(10)
num2 = Number(20)
# print(num1,num2)
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 // num2)
# print(num1 ** num2)
# print(num1 == num2)
# print(num1 != num2)
# print(num1 < num2)
# print(num1 <= num2)
# print(num1 > num2)
# print(num1 >= num2)
print(num1 / 4)
