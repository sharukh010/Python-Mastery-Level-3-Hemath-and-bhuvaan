"""
len(list)
len(string)
len(tuple)
function with same name but different parameter types , different number of parameters
- Compile time polymorphism 
- you will know which function is going to run during the compile 
- within a class 

Run time polymorphism (Method overriding): 
this actually happens in the child class 
we will redefine the method from the parent class 
"""
class Polymorphism: 

    def display(self,*names): 
        for name in names: 
            print(name)

class Parent: 
    def display(self,name): 
        print(f"Parent Name: {name}")
    def hello(self): 
        print("hello")

class Child(Parent): 
    def display(self,name): 
        print(f"Child Name: {name}")

# demo = Polymorphism()
# #method overloading
# demo.display("alex","bob","charlie")
# demo.display("david")

parent = Parent()
parent.display("Alex")
child = Child()
child.display("Bob")
child.hello()
