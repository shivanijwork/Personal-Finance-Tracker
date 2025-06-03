import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "financial_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    date_format = "%d-%m-%Y"

    @classmethod
    def initialize_CSV(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)  # created a pandas dataframe with these four columns
            df.to_csv(cls.CSV_FILE, index=False)    # converted this file into a csv file with name Financial_data.csv

    @classmethod
    def add_entry(cls, Date, Amount, Category, Description):
        new_entry = {           #created a new dictionary with all the data we wanted to add 
            "Date": Date,
            "Amount": Amount,
            "Category": Category,
            "Description": Description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:    # opened the csv file in append mode
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)    # created a csv writer object with the column names
            writer.writerow(new_entry)      # wrote the new entry to the csv file
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["Date"]=pd.to_datetime(df["Date"], format=cls.date_format)  # converted the date column to datetime format
        start_date=datetime.strptime(start_date, CSV.date_format)
        end_date=datetime.strptime(end_date, CSV.date_format)
        
        mask=(df["Date"]>=start_date) & (df["Date"]<=end_date)  # created a mask to filter the dataframe based on the date range
        filtered_df=df.loc[mask]
        if filtered_df.empty:
            print("No transactions found in the specified date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}:")
            print(filtered_df.to_string(index=False, formatters={'Date': lambda x: x.strftime(CSV.date_format)}))

        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
        print("\nSummary:")
        print(f"Total Income: {total_income:.2f}")
        print(f"Total Expense: {total_expense:.2f}")
        print(f"Net Saving: {total_income - total_expense:.2f}")

        return filtered_df

def add():
    CSV.initialize_CSV()
    Date = get_date("Enter the date (DD-MM-YYYY) or press Enter for today: ", allow_default=True)
    Amount = get_amount()
    Category = get_category()
    Description = get_description()
    CSV.add_entry(Date, Amount, Category, Description)

def plot_transactions(df):
    df.set_index("Date", inplace=True)

    income_df=df[df["Category"]=="Income"].resample("D").sum().reindex(df.index, fill_value=0) #makes sure that there is data for each day
    expense_df=df[df["Category"]=="Expense"].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="green")
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="red")
    plt.title("Income and Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add a new transaction")
        print("2. View transactions and a summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (DD-MM-YYYY): ")
            end_date = get_date("Enter the end date (DD-MM-YYYY): ")
            df=CSV.get_transactions(start_date, end_date)
            if input("Do you want to plot the transactions? (y/n): ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()