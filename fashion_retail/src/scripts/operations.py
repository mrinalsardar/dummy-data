import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_operational_data(n=100):
    operational = []
    for _ in tqdm(range(n)):
        operation = {
            "Store": faker.company(),
            "Employee_ID": faker.unique.uuid4(),
            "Employee_Name": faker.name(),
            "Role": random.choice(
                ["Cashier", "Manager", "Sales Associate", "Stock Associate"]
            ),
            "Hours_Worked": random.randint(0, 40),
            "Performance_Score": random.randint(1, 10),
        }
        operational.append(operation)
    return pd.DataFrame(operational)
