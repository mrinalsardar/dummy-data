import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_supply_chain_data(n=50):
    supply_chain = []
    for _ in tqdm(range(n)):
        supplier = {
            "Supplier_ID": faker.unique.uuid4(),
            "Supplier_Name": faker.company(),
            "Lead_Time_days": random.randint(7, 30),
            "Shipping_Cost": round(random.uniform(100.0, 1000.0), 2),
            "Location": faker.country(),
        }
        supply_chain.append(supplier)
    return pd.DataFrame(supply_chain)
