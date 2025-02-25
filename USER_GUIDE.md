# User Guide

## Menu Overview
This program provides a simple command-line interface (CLI) for managing income and expenses. Below is an overview of the available menu options and their functions.

### Main Menu ###
Upon running the program, you will be presented with the **Main Menu**, where you can choose from the following options:

1. **Enter an income** - Allows you to log a new income entry
2. **Enter an expense** - Enables you to record a new expense
3. **Display all income and expenses** - Summarises your financial transactions
4. **Access the Crypto Menu** - Opens the cryptocurrency tracking menu
5. **Exit the application** - Exits the application

## Income and Expenses Menu ##
Open pressing "3. Display all income and expenses", you will be presenting with the following options in the menu:

1. **Add Expense** - Allows you to enter a new expense, including the name, amount, category, and date.
2. **Add Income** - Enables you to log an income entry with details such as name, amount, category, and date.
3. **View Financial Summary** - Displays total income, expenses, and your overall financial position.
4. **Exit Program** - Closes the application.

### Adding an Expense
- You will be prompted to enter the **expense name** and **amount**.
- You must select a category from the following:
  - 🍔 Food
  - 🏠 Home
  - 🚗 Fuel
  - 🎸 Entertainment
  - 🌟 Misc
- The expense is then saved and recorded in the system.

### Adding an Income
- You will need to provide the **income name** and **amount**.
- Choose a category from the list below:
  - 💼 Salary
  - 🎁 Gift
  - 🤑 Investment Income
  - 🌟 Other Income
- The income is then recorded and saved.

### Viewing Financial Summary
- The program will display:
  - Total **income earned**
  - Total **expenses spent**
  - Your **financial position** (whether you have money left or are in debt)
- You will be prompted to press **Enter** to return to the Main Menu.

### Exiting the Program
- Selecting the exit option will safely close the application.

# Cryptocurrency Menu Guide

Upon accessing the cryptocurrency menu, users will be presented with the following options:

## 1. **Add/Remove BTC to Your Portfolio**
   - **What It Does**: This option allows the user to either add or remove BTC from their portfolio.
   - **How to Use**: 
     - When selecting option 1, the user will be prompted to enter the amount of BTC they want to add or remove. 
     - To remove BTC, users should input a negative number (e.g., `-0.5 BTC`). 
     - To add BTC, input a positive number (e.g., `0.5 BTC`).
     - If the amount entered is `0.0`, the program will display an error message.
   - **After Action**: The entered BTC amount will be saved in a CSV file (`crypto.csv`) with the current date.

## 2. **Display the Value of Your BTC Portfolio**
   - **What It Does**: This option calculates and displays the value of the user's BTC holdings in Australian Dollars (AUD).
   - **How to Use**: 
     - When selecting option 2, the program will fetch the current BTC price using the `btc.get_btc_price()` function.
     - It will then read the user's BTC portfolio from the `crypto.csv` file, calculate the total value in AUD, and display it.
     - The portfolio is also shown in a table format for the user's reference.
   - **After Action**: The value is displayed along with the current AUD value of the BTC holdings.

## 3. **Quit to the Main Menu**
   - **What It Does**: This option allows the user to exit the cryptocurrency menu and return to the main menu.
   - **How to Use**: Simply select option 3 to return to the main menu.

---

## Handling Errors and Invalid Inputs
- If an invalid input is entered, the program will prompt the user to try again. 
- If a non-numeric value is entered when asked for BTC amounts or menu choices, the program will display an error and ask for input again.

---

## Navigation Summary
- **Option 1**: Adds or removes BTC to/from the portfolio (requires entering a numeric value).
- **Option 2**: Displays the value of the BTC portfolio in AUD.
- **Option 3**: Exits to the main menu.

---
### Additional Features
- **Color-coded Text**: The application uses color formatting for better readability in the command line
- **Error Handling**: Provides user-friendly error messages for incorrect inputs
- **Crypto Tracking**: Integrates cryptocurrency-related financial operations

    For further details on each feature, refer to the relevant sections in this guide.

---
This guide ensures users can navigate and utilise the menu options effectively. If you encounter any issues, ensure that your inputs are correct, especially when entering numbers.
