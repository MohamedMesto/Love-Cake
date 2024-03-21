# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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

        data_str = input("Enter your data here: ")
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

get_cake_sales_data()