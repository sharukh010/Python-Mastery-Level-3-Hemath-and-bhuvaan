## Practice Question: Single Inheritance in Python

Scenario: Employee Management System

A company wants to develop a simple employee management system using Python OOP and single inheritance.

### Requirements

1. Create a parent class called `Employee`.
   - Initialize the following attributes using a constructor:
     - `name`
     - `employee_id`
     - `basic_salary`
   - Create a method `display_details()` to display employee information.
   - Create a method `calculate_salary()` that returns the basic salary.
2. Create a child class called `Developer` that inherits from `Employee`.
   - Add an additional attribute `programming_language`.
   - Use the parent class constructor to initialize the inherited attributes.
   - Override the `calculate_salary()` method.
   - A developer receives a bonus of ₹5,000 in addition to their basic salary.
   - Create a method `display_developer_details()` to display all employee details, including programming language and final salary.
3. Create an object of the `Developer` class and demonstrate all the methods.

### Expected Output

```
Employee Name: Rahul
Employee ID: E101
Basic Salary: 40000

Programming Language: Python
Final Salary: 45000
```

### Constraints

- Use `super()` to call the parent constructor.
- Use method overriding.
- Do not duplicate inherited attributes in the child class.
- Follow proper OOP principles.

Difficulty: Medium

Bonus challenge: Modify the program so that the developer's bonus is calculated as 10% of their basic salary instead of a fixed ₹5,000.