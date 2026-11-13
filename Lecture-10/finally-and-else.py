from calculator import CalculatorV3
"""
you are writting a program for a game now this game can have errors 
you wanted to print end message the at end of the game 
when can game end? 
1. if it is completed (no exceptions)
2. if there is an exception 
"""
# try: 
#     print("playing...")
#     raise ValueError("dummy error")
# except Exception as e: 
#     print("An error has occured")
# finally: 
#     # it gets excuted no matter if there is an exception or not 
#     print("Game over..")

cal = CalculatorV3()
try: 
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    cal.set_values(num1,num2)
    result = cal.div()
except ZeroDivisionError as e: 
    print("You cannot divide with zero")
else: 
    # this will get excuted only when there is no exception 
    print(f"Result: {result}")
finally: 
    print("Program ended")