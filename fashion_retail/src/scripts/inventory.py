import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_inventory_data(products_df, inventory_percentage):
    product_id_list = products_df.sample(
        products_df.shape[0] * inventory_percentage // 100
    )["SKU"]
    inventory = []
    for p in products_df["SKU"]:
        stock = {
            "SKU": p,
            "Warehouse": faker.company(),
            "Stock_Level": random.randint(0, 500),
            "Reorder_Point": random.randint(20, 100),
            "Backorders": random.randint(0, 50),
        }
        inventory.append(stock)
    return pd.DataFrame(inventory)
