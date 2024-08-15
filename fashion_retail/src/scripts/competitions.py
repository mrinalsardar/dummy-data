import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_competition_data(n=50):
    competitive = []
    for _ in tqdm(range(n)):
        competitor = {
            "Competitor": faker.company(),
            "Product": faker.catch_phrase(),
            "Price": round(random.uniform(5.0, 200.0), 2),
            "Market_Share": round(random.uniform(0.1, 20.0), 2),
            "Trend": random.choice(["Rising", "Stable", "Declining"]),
        }
        competitive.append(competitor)
    return pd.DataFrame(competitive)
