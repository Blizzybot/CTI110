# Terry Norman
# 03/01/2026
# P1HW2 - Travel Budget Calculator
# This program calculates the total travel expenses and remaining budget.

"""
Pseudocode:

1. Display program title
2. Ask user to enter their travel budget
3. Ask user to enter their travel destination
4. Ask user to enter amount for gas
5. Ask user to enter amount for accommodation
6. Ask user to enter amount for food
7. add up total expenses (gas + accommodation + food)
8.subtract total expenses from travel budget to get remaining budget
9. Display total expenses and remaining budget
"""
print("This Program calculates the total travel expenses and remaining budget.")
print("----- Travel Budget Calculator -----")
travel_budget = float(input("Enter your travel budget: $"))
travel_destination = input("Enter your travel destination: ")   
gas_expense = float(input("Enter the amount for gas: $"))
accommodation_expense = float(input("Enter the amount for accommodation: $"))     
food_expense = float(input("Enter the amount for food: $"))
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = travel_budget - total_expenses
print("\n----- Travel Expenses Summary -----")
print(f"Travel Location: {travel_destination}")
print(f"Initial Travel Budget: ${travel_budget:.2f}")
print()
print(f"Fuel Expense: ${gas_expense:.2f}")
print(f"Accommodation Expense: ${accommodation_expense:.2f}")
print(f"Food Expense: ${food_expense:.2f}")
print()
print(f"Total Expenses: ${total_expenses:.2f}") 
print(f"Remaining Budget: ${remaining_budget:.2f}") 
