## **Python OOP Challenge: Smart Vehicle Rental System**



Intermediate Level

Multilevel Inheritance

Exception Handling



### **Problem Statement**

Develop a **Smart Vehicle Rental System** using Python. The application should allow customers to rent different types of vehicles, calculate rental costs, and handle invalid inputs using exception handling.

### **1. Class Structure – Multilevel Inheritance**

Create the following inheritance hierarchy:

**Vehicle**

Base Class

- brand
- model
- rental_price

**RentalVehicle**

Intermediate Class

- vehicle_number
- is_available
- rent_vehicle()

**CustomerRental**

Derived Class

- customer_name
- rental_days
- calculate_bill()
- display_details()

### **2. Class Requirements**

**Class 1: Vehicle**

Create a constructor that accepts:

- `brand`
- `model`
- `rental_price`

Create a method `display_vehicle()` to display vehicle information.

**Class 2: RentalVehicle (inherits Vehicle)**

Add the following attributes:

- `vehicle_number`
- `is_available` (default: True)

Create a method:

\- `rent_vehicle()` – changes availability to False if the vehicle is available.

**Class 3: CustomerRental (inherits RentalVehicle)**

Add the following attributes:

- `customer_name`
- `rental_days`

Create the following methods:

1. `calculate_bill()` – calculate the total rental cost.
2. `display_details()` – display customer and vehicle details.
3. `return_vehicle()` – make the vehicle available again.

### **3. Exception Handling Requirements**

Implement the following exceptions:

| Scenario                                     | Exception to handle                           |
| -------------------------------------------- | --------------------------------------------- |
| Rental days are zero or negative             | ValueError                                    |
| Rental days contain text instead of a number | ValueError                                    |
| model is not string                  |Value error  |
| brand is not string                      |Value error |
| Invalid rental price                         | ValueError                                    |

Use:

- `try`
- `except`
- `else`
- `finally`
- `raise`
- Custom exception classes

### **4. Sample Execution**

```
========== VEHICLE RENTAL SYSTEM ==========

Enter customer name: Rahul
Enter vehicle brand: Toyota
Enter vehicle model: Fortuner
Enter rental price per day: 2500
Enter vehicle number: AP39AB1234
Enter rental days: 5

========== RENTAL DETAILS ==========

Customer Name: Rahul
Vehicle: Toyota Fortuner
Vehicle Number: AP39AB1234
Rental Days: 5
Price Per Day: Rs.2500

Total Rental Cost: Rs.12500

Vehicle successfully rented!
```

### **5. Important Constraints**

- Do not use multiple inheritance.
- Do not use global variables.
- Use `super()` to invoke parent constructors.
- Use meaningful method and variable names.
