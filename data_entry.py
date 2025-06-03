from datetime import datetime


date_format = "%d-%m-%Y"  # Define the date format to be used
CATEGORIES ={"I": "Income", "E": "Expense"}  # Define categories for income and expense


# Function to get a valid date from user input (Recursive Function)
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    else:
        try:
            valid_date=datetime.strptime(date_str, date_format)
            return valid_date.strftime(date_format)
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            return get_date(prompt, allow_default)

# Function to get a valid amount from user input (Recursive Function)
def get_amount():
    try:
        amount = float(input("Enter the amount : "))
        if amount<=0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category()

def get_description():
    return input("Enter the description (optional): ")
