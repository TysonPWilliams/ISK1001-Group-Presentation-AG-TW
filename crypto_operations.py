import display_data
import csv
import btc_calculations as btc
from datetime import datetime
from colors import *

path = 'crypto.csv'

def crypto_menu():
    """
    Displays the cryptocurrency menu and handles user interactions for managing BTC in the portfolio.
    """
    while True:

        print(f"{primary_text}\n\n------Cryptocurrency Main Menu--------{constants.RESET}")
        print(f"{secondary_text}1. Add/Remove BTC to your portfolio")
        print(f"{secondary_text}2. Display the value of your BTC portfolio")
        print(f"{secondary_text}3. Quit to the main menu")
        print(f"{primary_text}---------------------------------------")

        try:
            choice = int(input(f"Please enter a number from the above menu: {constants.RESET}"))
        except ValueError:
            print(f"{error_text}Error: Please enter a whole number: ie. 2{constants.RESET}")
            input(f"{primary_text}---Press Enter to Continue---")
            crypto_menu()
        except Exception as e:
            print(f"{error_text}An unexpected error occured: {e}{constants.RESET}")
            input(f"{primary_text}---Press Enter to Continue---{constants.RESET}")
            crypto_menu()
        
        if choice == 1:
            add_crypto()

        elif choice == 2:
            print(f"{primary_text}------------------------------------")
            print(f"Calculating the value of you BTC holdings\n{constants.RESET}")
            try:
                btc_price = btc.get_btc_price()
                btc_holdings = btc.read_csv_data('crypto.csv')
                total_aud_value = btc.calculate_aud_value(btc_price, btc_holdings)
                display_data.display_csv_as_table('crypto.csv')
                print(f"{secondary_text}Your BTC holdings are worth approximately AUD ${total_aud_value:.2f}{constants.RESET}")
            except Exception as e:
                print(f'{error_text}An unexpected error occured: {e}{constants.RESET}')
            finally:
                input(f"{primary_text}------Press Enter to Continue-------")

        elif choice == 3:
            display_data.main_menu()
        else:
            print(f"{error_text}\n\nYou have entered an invalid option, try again!{constants.RESET}")

def add_crypto():
    """
    Allows the user to add or remove BTC from their portfolio by modifying the 'crypto.csv' file.
    """
    print(f"{primary_text}-------------------------------")
    print("Adding/Removing BTC to your portfolio!")
    print(f"If removing BTC, add a '-' minus sign to your amount!{constants.RESET}")

    try:
        BTC_added = float(input(f"{secondary_text}How much BTC are you adding/removing: "))
        if BTC_added == 0.0:
            print(f"{error_text}The BTC added can't be 0{constants.RESET}")
            input(f"{primary_text}----Press Enter to Continue----{constants.RESET}")
            crypto_menu()
    except ValueError:
        print('Please enter a number')
        input("----Press Enter to Contine----")
        add_crypto()
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        input('----Press Enter to Continue----')
        crypto_menu()

    print("-------------------------------")
    print(f'Adding {BTC_added} BTC to your portfolio!{constants.RESET}')

    with open(path, 'a', newline='') as file:
        fieldnames = ['BTC', 'Date Added']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        current_date = datetime.now().strftime('%Y-%m-%d')
        writer.writerow({'BTC': BTC_added, 'Date Added': current_date})
        input(f"{primary_text}------Press Enter to Continue------")


    