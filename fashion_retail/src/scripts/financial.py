"""This is not being used"""

import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_financial_data(n=12):
    financials = []
    for _ in tqdm(range(n)):
        financial = {
            "Month": faker.date_this_year().strftime("%B"),
            "Revenue": round(random.uniform(10000.0, 100000.0), 2),
            "Expenses": round(random.uniform(5000.0, 80000.0), 2),
            "Profit": round(random.uniform(1000.0, 50000.0), 2),
            "Budget": round(random.uniform(10000.0, 100000.0), 2),
        }
        financials.append(financial)
    return pd.DataFrame(financials)
