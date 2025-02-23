# Help & Troubleshooting Guide

## Common Issues & Solutions

### 1. Virtual Environment Not Activating
**Issue:** Running `source .venv/bin/activate` does not activate the virtual environment.

**Solution:**
- Ensure you created the virtual environment by running:
  ```bash
  python3 -m venv .venv
  ```
- Try activating again:
    ```bash
    source .venv\Scripts\activate
    ```
- If activation still fails, ensure you have `python3-venv` installed:
    ```bash
    sudo apt install python3-venv
    ```

### 2. Dependencies Not Installing
**Issue:** Running `pip install -r requirements.txt` fails.

**Solution:**
- Ensure the virtual environment is activated:
    ```bash
    source .venv/bin/activate
    ```
- Try upgrading `pip` first:
    ```bash
    pip install --upgrade pip
    ```
- Then reinstall dependencies:
    ```bash
    pip install -r requirements.txt
    ```
**If an error mentions a missing package, install it manually:**
- Example: 
    ```bash
    pip install package-name
    ```

### 3. CoinMarketCap API Key Not Working
**Issue:** The application returns an error related to the API key.

**Solution:**
- Ensure you have correctly created a file called `secret.py` and then add your API key to it:
  ```python
  API_KEY = "YOUR_API_KEY"
  ```
- Verify that the API key is active by logging into your [CoinMarketCap API account](https://coinmarketcap.com/api/).
- Double-check that the key has no extra spaces or formatting issues.

### 4. Application Not Running
**Issue:** Running `python3 main.py` results in an error.

**Solution:**
- Ensure all dependencies are installed (solution above)
- If you see `ModuleNotFoundError`, manually install the missing module:
  ```bash
  pip install module-name
  ```
- Run the script with explicit Python version:
  ```bash
  python3.12 main.py
  ```

### 5. CSV File Not Saving Data
**Issue:** Transactions or crypto holdings are not being saved in the CSV files.

**Solution:**
- Ensure that the script has the correct file permissions:
  ```bash
  chmod +w transactions.csv holdings.csv
  ```
- Check that your Python script is correctly writing data by adding a print statement before saving:
  ```python
  print(data_to_save)
  ```
- If using Windows, try running the script in administrator mode.

## Need More Help?
If you continue to experience issues, refer to the documentation sources in the `README.md` file or seek help in Python developer communities like:
- [Stack Overflow](https://stackoverflow.com/)
- [Python Discord](https://pythondiscord.com/)
- [Reddit r/learnpython](https://www.reddit.com/r/learnpython/)

---
_Last updated: February 2025_
