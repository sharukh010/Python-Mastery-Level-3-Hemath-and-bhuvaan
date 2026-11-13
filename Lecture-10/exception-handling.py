from calculator import CalculatorV2

try: 
    # it executes the code inside try block and if there is any error 
    # the control goes to except block 
    cal = CalculatorV2()
    cal.set_values(1,0)
    # cal.div()
    # print(games)
except Exception as e: # this is a generic exception handling 
    # here you will come when there is an exception
    print(e) 
# when ever you are using exception ladder the generic exception handling should be at last 
except ValueError as e: 
    print(e)
except ZeroDivisionError as e: 
    print(e)
# print(cal.add())
"""
Not ever exception can be handled 
ex: 
1. Logical errors 
"""