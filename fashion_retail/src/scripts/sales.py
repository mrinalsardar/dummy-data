import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_sales_data(
    customers_df,
    products_df,
    n_txn=10000,
    max_product_per_txn=5,
):
    rows = []
    for t in tqdm(range(n_txn)):
        customer_id = customers_df.sample(1).iloc[0]["Customer_ID"]
        product_id_list = products_df.sample(random.randint(1, max_product_per_txn))[
            "SKU"
        ]

        transaction_id = faker.unique.uuid4()
        store = faker.company()
        transaction_date = faker.date_this_year()

        for p in product_id_list:
            transaction = {
                "Transaction_ID": transaction_id,
                "Customer_ID": customer_id,
                "SKU": p,
                "Store": store,
                "Date": transaction_date,
                "Quantity": random.randint(1, 10),
                "Price": round(random.uniform(5.0, 200.0), 2),
                "Discount": round(random.uniform(0.0, 0.5), 2),
            }
            rows.append(transaction)

    return pd.DataFrame(rows)
