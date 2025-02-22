import csv

class FileOperations:
    
    """
    Handles file operations for saving income and expense data to CSV files.
    
    This class provides methods to save financial transaction data (income and expenses)
    into separate CSV files, ensuring structured and organised data storage.

    Methods:
        __init__(): Initialises the FileOperations class with file paths for storing income and expense
        save_data(): Saves income or expense data to the specified CSV files
        save_income(): Saves income to the designated income CSV file
        save_expense(): Saves expense data the the designated expense CSV file
    """

    def __init__(self, expense_path ='expense_data.csv', income_path='income_data.csv'):
        
        """
        Initialises the FileOperations class with default file paths for expenses and income.
        
        Args:
            expense_path (str): The file path where expense data will be stored. Defaults to 'expense_data.csv'.
            income_path (str): The file path where income data will be stored. Defaults to 'income_data.csv'.
        """

        self.expense_path = expense_path
        self.income_path = income_path

    # In the below method, the 'data' argument is the income/expense class being passed 
    def save_data(self, data, data_type, path):
        
        """
        Saves income or expense data to the specified CSV file.
        
        Args:
            data (object): An instance of an income or expense class containing financial details.
            data_type (str): Specifies whether the data being saved is "income" or "expense".
            path (str): The file path where the data should be stored.
        
        The method writes the financial data (name, category, amount, date) into a CSV file.
        If an error occurs, it handles permission errors and general exceptions.
        """

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
        """
        Saves income data to the designated income CSV file.
        
        Args:
            income (object): An instance of the income class containing financial details.
        
        Calls the 'save_data' method, passing the income object and the income file path.
        """
        self.save_data(income, "income", self.income_path)
    
    def save_expense(self, expense):
        """
        Saves expense data to the designated expense CSV file.
        
        Args:
            expense (object): An instance of the expense class containing financial details.
        
        Calls the 'save_data' method, passing the expense object and the expense file path.
        """
        self.save_data(expense, "expense", self.expense_path)
