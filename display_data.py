from file_operations import * # Description required
import financial_operations as fin_ops # Description required
import csv # Description required
import crypto_operations # Description required
from tabulate import tabulate # type: ignore # Description required
from color50 import rgb, constants # type: ignore # Description required
from colors import * # Description required

def main_menu():
    
    """
    The main menu that users see upon starting the application. It provides options for managing income, expenses, and cryptocurrency.
    """

    print(f"{primary_text}\nWelcome to the Budget Manager!")
    print(f"------------------------------{constants.RESET}")
    print(f"{secondary_text}1. Enter an income")
    print(f"2. Enter an expense")
    print(f"3. Display all income and expenses")
    print(f"4. Access Crypto Menu")
    print(f"5. Exit the application")
    print(f"-------------------------------{constants.RESET}")

    choice = input(heading + f"Please type in a number from the options above: {constants.RESET}")

    if choice == "1":
        fin_ops.Income.add_income()
    elif choice == "2":
        fin_ops.Expense.add_expense()
    elif choice =="3":
        display_data()
    elif choice == "4":
        crypto_operations.crypto_menu()
    elif choice == "5":
        quit()
    else:
        print(f"{error_text}\nYour choice is invalid, try again!{constants.RESET}\n")
        input(f"{primary_text}----Press Enter to Continue----")

def display_csv_as_table(path):
    """
    Reads data from a CSV file and displays it as a table using the 'tabulate' library.

    Args:
        path (str): Path to the CSV file to display.
    """
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [row for row in reader]
    
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_data():
    """
    Provides the user with options to view income and expense data or perform summary calculations.
    """

    while True:

        print(f"{primary_text}\nWelcome to the Budget Summary Menu!")
        print(f"------------------------------{constants.RESET}")
        print(f"{secondary_text}1. View all income")
        print("2. View all expenses")
        print("3. How am I doing for the month?")
        print("4. What category am I spending the most on?")
        print(f"5. Return to the main menu{constants.RESET}")
        print(f"{primary_text}-------------------------------{constants.RESET}")

        choice = input(f"{primary_text}Please type in a number from the options above: ")

        if choice == "1":
            display_csv_as_table('income_data.csv')
            total = summarise_totals('income_data.csv')
            print(f'The total amount is: ${total:.2f}!')
            input("------Please press Enter to continue----")
        elif choice == "2":
            display_csv_as_table('expense_data.csv')
            total = summarise_totals('expense_data.csv')
            print(f'The total amount is: ${total:.2f}!')
            input("------Please press Enter to continue----")
        elif choice == "3":
            income_summary = summarise_totals('income_data.csv')
            fin_ops.income_expense_calc()
        elif choice == "4":
            max_category = max_category_spending()
            print(f'\nYour max category is {max_category[0]} with an amount of ${max_category[1]:.2f}!\n')
            input("--------Press Enter to continue-------")
        elif choice == "5":
            main_menu()
        else:
            print(f"{error_text}Your choice is invalid, try again!")
            input(f'{primary_text}----Press Enter to Continue----')


def summarise_totals(path):
    
    """
    Calculates the total amount for either income or expenses by reading the specified CSV file.

    Args:
        path (str): Path to the CSV file (either 'income_data.csv' or 'expense_data.csv').

    Returns:
        float: The total amount calculated from the data in the CSV file.
    """

    total = 0.0

    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total += float(row['Amount'])
    
    return total

def max_category_spending():
    
    """
    Identifies the category in which the most money has been spent based on the expense data.

    Returns:
        tuple: The category with the highest spending and the total amount spent in that category.
    """

    category_totals = {}
    with open('expense_data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            category_totals[category] = category_totals.get(category, 0) + amount

    max_category = None
    max_amount = 0
    for category, amount in category_totals.items():
        if amount > max_amount:
            max_category = category
            max_amount = amount
    
    return max_category, max_amount