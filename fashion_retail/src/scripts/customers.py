import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_customer_data(n=500):
    customers = []
    for _ in tqdm(range(n)):
        customer = {
            "Customer_ID": faker.unique.uuid4(),
            "Name": faker.name(),
            "Age": random.randint(18, 70),
            "Gender": random.choice(["Male", "Female"]),
            "Location": faker.city(),
            "Join_Date": faker.date_this_decade(),
            "Loyalty_Points": random.randint(0, 1000),
            "Customer_Segment": random.choice(["Regular", "VIP", "Employee"]),
        }
        customers.append(customer)
    df = pd.DataFrame(customers)
    df["Email"] = (
        df["Name"].str.replace(" ", ".") + f"{random.randint(0, 1000)}@example.com"
    )

    return df
