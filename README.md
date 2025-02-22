# Budget Manager with Bitcoin Tracking

This is a personal finance application that helps you manage your income, expenses, and crypto investments.

## Features:

- **Income and Expense Tracking:** Manually input your income and expenses, categorised for easy budgeting.
- **CSV File Storage:** Data is saved securely in CSV files for future reference and analysis.
- **Top Spending Category:** See which category you're spending the most on to optimise your budget.
- **Crypto Investment Tracking:** Track your Bitcoin (BTC) purchases and holdings.
- **Real-time BTC Price Check:** View the current value of your BTC wallet based on CoinmarketCap API.

## Setting Up

1. **Create a Virtual Environment:**

    - Open your linux-based terminal
    - CD into the root folder of this application
    - Run the following command to create a virtual environment called '.venv'

        ```bash
        python3 -m venv .venv
        ```
    - Activate the virtual environment

        ```bash
        source .venv/bin/activate
        ```

2. **Install Dependancies**
    
    - Inside the activated virtual environment, run the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. **Get your CoinMarketCap API Key:**

    - Create an account on the [CoinMarketCap API Page](https://coinmarketcap.com/api/).
    - Create a new API key and copy it.

4. **Create a Secret File:**

    - Create a new file in the index of the program called 'secret.py'
    - Inside 'secret.py', add the following line, replacing 'YOUR_API_KEY' with your new CoinMarketCap API key:

        ```python
        API_KEY = "YOUR_API_KEY"
        ```

## Running the Application

1. Make sure that the virtual environment is activated
2. Run the application by typing the following in terminal:

    ```bash
    python3 main.py
    ```

## Usage

The application will run you through adding income, expenses and BTC amounts.

## Third-Party Libraries and Licenses

This project uses the following third-party libraries:

*   **certifi:** Mozilla Public License 2.0 (MPL-2.0) [https://www.mozilla.org/en-US/MPL/2.0/](https://www.mozilla.org/en-US/MPL/2.0/)
*   **charset-normalizer:** MIT License [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
*   **color50:** MIT License [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
*   **idna:** BSD License (typically a 3-clause BSD) [https://opensource.org/licenses/BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
*   **requests:** Apache License 2.0 [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
*   **tabulate:** MIT License [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)
*   **urllib3:** MIT License [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

Since all the libraries used are permissive licenses, their use in my project is generally considered ethical.

These libraries are used under their respective open-source licenses.

## References

- **DK.** (2020). Beginner's Step-by-Step Coding Course. Penguin Random House Australia.

- **freeCodeCamp.org.** (2022). Python for Beginners - Full Course [Free and Complete]. [online] Available at: https://www.youtube.com/watch?v=f3GfkvfpVAE [Accessed 10 Dec. 2024].

- **Tech With Tim.** (2019). Python Tutorial for Beginners - Full Course in 11 Hours [2023]. [online] Available at: https://www.youtube.com/watch?v=p71SWzjeqtk [Accessed 10 Dec. 2024].

- **CoinMarketCap.** (n.d.). Cryptocurrency Quotes Latest. [online] Available at: https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest [Accessed 12 Dec. 2024].

- **GeeksforGeeks.** (2023). How to Install Requests in Python for Windows, Linux, Mac? [online] Available at: https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/#google_vignette [Accessed 12 Dec. 2024].

- **NetworkChuck.** (2021). Learn Python in 1 Hour - NEVER Give Up. [online] Available at: https://www.youtube.com/watch?v=q5uM4VKywbA [Accessed 12 Dec. 2024].

- **Python.org.** (n.d.). venv — Creation of virtual environments. [online] Available at: https://docs.python.org/3/library/venv.html [Accessed 12 Dec. 2024].

- **Color50.** (n.d.). Color50 Documentation. [online] Available at: https://color50.readthedocs.io/en/latest/index.html [Accessed 19 Dec. 2024].

- **Python.org.** (n.d.). csv — CSV File Reading and Writing. [online] Available at: https://docs.python.org/3/library/csv.html#module-contents [Accessed 15 Dec. 2024].
