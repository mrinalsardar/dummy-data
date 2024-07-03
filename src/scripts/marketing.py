import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_marketing_data(n=200):
    marketing = []
    for _ in tqdm(range(n)):
        campaign = {
            "Campaign_ID": faker.unique.uuid4(),
            "Channel": random.choice(["Email", "Social Media", "TV", "Radio", "Print"]),
            "Start_Date": faker.date_this_year(),
            "End_Date": faker.date_this_year(),
            "Budget": round(random.uniform(1000.0, 100000.0), 2),
            "Spent": round(random.uniform(500.0, 80000.0), 2),
            "ROI": round(random.uniform(0.5, 5.0), 2),
        }
        marketing.append(campaign)
    return pd.DataFrame(marketing)
