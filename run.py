# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"
]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_cake')

 

# Get sales figures input from the user

def get_cake_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter cake sales data from the last market.")
        print("Data should be five numbers, separated by commas.")
        print("Example: 10,20,30,40,50\n")

        data_str = input("Enter your data here:/n")
        cake_sales_data = data_str.split(",")
        if validate_cake_data(cake_sales_data):
           print("Cake Data Insertion is valid!")
           break

    return cake_sales_data


 

# Get sales figures input from the user
    
def validate_cake_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 5 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

 



# Update cake sales worksheet, add new row with the list data provided

def update_cake_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating Cake sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Cake Sales worksheet updated successfully.\n")

# Update sales worksheet, add new row with the list data provided
    
def update_cake_surplus_worksheet(data):
    """
    # Update cake surplus worksheet, add new row with the list data provided
    """
    print("Updating Cake surplus worksheet...\n")
    cake_surplus_worksheet = SHEET.worksheet("surplus")
    cake_surplus_worksheet.append_row(data)
    print("Cake surplus worksheet updated successfully.\n")


# Comparison Method 
def calculate_cake_surplus_data(sales_row):
    """
  #  Compare sales with stock and calculate the cake surplus for each item type.

  #  The surplus is defined as the sales figure subtracted from the stock:
   # - Positive cake surplus indicates waste
   # - Negative cake surplus indicates extra made when stock was sold out.
    """
    print("Calculating cake surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # to only the last row in the stock
    stock_row = stock[-1]

 

    cake_surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        # change to integer
        surplus = int(stock) - sales
        cake_surplus_data.append(surplus)

    return cake_surplus_data


# get last 5 entriesof the cake sales
def get_last_5_entries_cake_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 6):
        column = sales.col_values(ind)
        columns.append(column[-4:])

    return columns



#  update worksheet
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

# calculate stock data
def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data



#  Run the main program functions
def main_cake_run():
    """
    Run the main program functions
    """
    data = get_cake_sales_data()
    cake_sales_data = [int(num) for num in data]
    update_worksheet(cake_sales_data, "sales")
    new_surplus_data = calculate_cake_surplus_data(cake_sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_cake_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")

 
if __name__ == '__main__':
    print("Welcome to Love Cake Data Automation")
    main_cake_run()