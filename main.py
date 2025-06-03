import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "financial_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]

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

CSV.initialize_CSV()
CSV.add_entry(
    Date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # used the current date and time in the format YYYY-MM-DD HH:MM:SS
    Amount=100.0,  # example amount
    Category="Food",  # example category
    Description="Restaurant"  # example description
)   
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")
