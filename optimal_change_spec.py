from optimal_change import optimal_change

# Write your tests here!
print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print("3:", optimal_change(0.01, 999) == "The optimal change for an item that costs $0.01 with an amount paid of $999 is 9 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, 3 quarters, 2 dimes, and 4 pennies.")

print("4:", optimal_change(50, 50.01) == "The optimal change for an item that costs $50 with an amount paid of $50.01 is 1 penny.")

print("5:", optimal_change(100, 100) == "The optimal change for an item that costs $100 with an amount paid of $100 is no change given.")

print("6:", optimal_change(29.41, 34.76) == "The optimal change for an item that costs $29.41 with an amount paid of $34.76 is 1 $5 bill, 1 quarter, and 1 dime.")

print("7:", optimal_change(1.98, 1.00) == "Not enough money for this item.")

print("8:", optimal_change(29.41, 34.76) == "The optimal change for an item that costs $29.41 with an amount paid of $34.76 is 1 $5 bill, 1 quarter, and 1 dime.")
