import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "financial_data.csv"

    @classmethod
    def initialize_CSV(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = ["Date", "Amount", "Category", "Description"])  # created a pandas dataframe with these four columns
            df.to_csv(cls.CSV_FILE, index=False)    # converted this file into a csv file with name Financial_data.csv 

CSV.initialize_CSV()