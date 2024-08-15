import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_customer_interaction_data(n=500):
    interactions = []
    for _ in tqdm(range(n)):
        interaction = {
            "Interaction_ID": faker.unique.uuid4(),
            "Customer_ID": faker.unique.uuid4(),
            "Channel": random.choice(["Email", "Phone", "Chat", "In-Person"]),
            "Date": faker.date_this_year(),
            "Issue_Resolved": random.choice([True, False]),
            "Interaction_Length_minutes": random.randint(1, 60),
        }
        interactions.append(interaction)
    return pd.DataFrame(interactions)
