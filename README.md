# Assessment 1: Algorithms
- **Change Maker**

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of any other student/individual.

## Requirements
- This assessment should be completed using Python.

## Challenge
You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost. Write a function called `optimal_change` that takes in two arguments: `item_cost` and `amount_paid`. The function should return a string describing the optimal change which follows the following convention:

```
print(optimal_change(62.13, 100))
> "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

print(optimal_change(31.51, 50))
> "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
```

Some helpful notes:
- Valid denominations: 1 cent (penny), 5 cents (nickel), 10 cents (dime), 25 cents (quarter), $1, $5, $10, $20, $50, $100
- Your algorithm should compute the **optimal** change. Obviously, you can give the change in pennies, but we're looking for the most optimal (least amount of) change possible.
- You should only consider *common* monetary denominations (i.e. ignore any denomination larger than $100-bill, ignore $2-bills, half-dollars, etc...)
- You should fully understand the data types of your input and output
- You need to account for proper plural denominations (i.e., quarters, dimes, pennies, bills) and proper punctuation (i.e., commas, using "and", and the period at the end of a sentence).
- You need to account for for edge cases and special cases! We haven't specified what to return for special cases, so decide what you think is most sensible. 
- You should not worry too much about floating point rounding errors (but see if you can handle it if you know how to). 

Testing is important for any application that is written. We want to make sure that you attempt to test your code with some sensible and varied test cases. In addition to submitting a correct algorithm, we want you to write at least 5-6 additional test cases in the `optimal_change_spec.py` file, simply using the `print()` function that accurately tests your solution. Feel free to start with the two examples below. Make sure you test various parts of your algorithm (common cases, edge cases, special cases, etc...)

Sample test cases:
```python

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
```
