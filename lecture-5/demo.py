from matrix_multiplication import matrix_multiplication
import calculator 
# importing everything from calculator file 
a = [[1,2],[3,4]]
b = [[1],[3]]
# print(matrix_multiplication(a,b))
# calculator.message()
# how to create a object 
c1 = calculator.Calculator(10,20) # this will call __init__
c2 = calculator.Calculator(30,40)
# print(c1.add())
# print(c1.mul())
print(c1.num1)
print(c1.num2)
print(c2.num1)
print(c2.num2)