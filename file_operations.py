import csv

class FileOperations:
    """
    File operations involving saving data to the income/expense csv files is done here
    """
    def __init__(self, expense_path ='expense_data.csv', income_path='income_data.csv'):

        self.expense_path = expense_path
        self.income_path = income_path

    # In the below method, the 'data' argument is the income/expense class being passed 
    def save_data(self, data, data_type, path):

        fieldnames = ['Name', 'Category', 'Amount', 'Date']

        try:
            with open(path, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({
                    'Name': f'{data.name}',
                    'Category': f'{data.category}',
                    'Amount': f'{data.amount}',
                    'Date': f'{data.date}'
                })
            print(f'Successfully saved {data_type} data to {path}')
        except PermissionError:
            print(f"You don't have permission to access {path}")
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    def save_income(self, income):
        """ Saves income data passed from financial_operations.py """
        self.save_data(income, "income", self.income_path)
    
    def save_expense(self, expense):
        """ Saves expense data passed from financial_operations.py"""
        self.save_data(expense, "expense", self.expense_path)
