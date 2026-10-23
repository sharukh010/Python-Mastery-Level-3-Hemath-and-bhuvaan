# OOP Practice Question: Bank Account Management

Difficulty: Medium Topics: Classes, Objects, Getters, Setters, Action Methods, Encapsulation

## Problem Statement

Create a Python class called `BankAccount` to manage a customer's bank account. The class should store the account holder's name, account number, and current balance.

The balance must not be modified directly from outside the class. Instead, use getters, setters, and action methods to manage the account.

### Requirements

1\. Private attributes

Create the following attributes:

- `account_holder` — customer's name
- `account_number` — unique account number
- `balance` — initial account balance

Make all three attributes private using Python's double-underscore convention.

2\. Getter methods

Implement the following methods:

- `get_account_holder()` — returns the account holder's name.
- `get_account_number()` — returns the account number.
- `get_balance()` — returns the current balance.

3\. Setter methods

Implement the following methods:

- `set_account_holder(name)` — updates the account holder's name. Reject an empty name.
- `set_account_number(number)` — updates the account number. Reject an invalid account number.
- `set_balance(amount)` — updates the balance only if the amount is non-negative.

4\. Action methods

Implement the following methods:

- `deposit(amount)` — adds money to the account. Reject zero or negative deposits.
- `withdraw(amount)` — deducts money from the account. Reject invalid amounts and withdrawals exceeding the available balance.
- `display_account_details()` — displays the account holder's name, account number, and current balance.

## Sample execution

Your program should support operations similar to these:

```
account = BankAccount("Rahul", "ACC101", 5000)
print(account.get_account_holder())# Rahul
print(account.get_balance())# 5000
account.deposit(2000)
print(account.get_balance())# 7000
account.withdraw(1500)
print(account.get_balance())# 5500
account.set_account_holder("Rahul Sharma")
account.display_account_details()
```

Expected final output:

```
Account Holder: Rahul Sharma
Account Number: ACC101
Balance: 5500
```

## Additional test cases

Make sure your program handles these situations correctly.

| Operation   | Input                    | Expected behavior                                   |
| ----------- | ------------------------ | --------------------------------------------------- |
| Deposit     | `deposit(1000)`          | Balance increases by 1000                           |
| Deposit     | `deposit(-500)`          | Reject the transaction                              |
| Withdraw    | `withdraw(2000)`         | Balance decreases by 2000 if sufficient funds exist |
| Withdraw    | `withdraw(100000)`       | Reject insufficient funds                           |
| Set balance | `set_balance(-100)`      | Reject the update                                   |
| Set name    | `set_account_holder("")` | Reject the update                                   |
| Get balance | `get_balance()`          | Return the latest balance                           |
