class Name: 
    def __init__(self,first_name,last_name,middle_name=None): 
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name 

    def __str__(self): 
        result = f"First Name: {self.first_name}\n"
        result += f"Middle Name: {self.middle_name}\n"
        result += f"Last Name: {self.last_name}"
        return result 

    def __add__(self,other): 
        updated_name = Name(self.first_name,other.last_name,self.middle_name)
        return updated_name


name1 = Name("Peter","Parker")
name2 = Name("Mary","Jane")
# wife + husband name -> wife's last names will be updated with 
# husbands last name 
name2 = name2 + name1 
print(name2)