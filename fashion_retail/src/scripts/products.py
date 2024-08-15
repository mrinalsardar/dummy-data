import random

import pandas as pd
from faker import Faker
from tqdm import tqdm

faker = Faker()


def generate_product_data(n=100):
    products = []
    categories = ["Tops", "Bottoms", "Dresses", "Outerwear", "Accessories"]
    for _ in tqdm(range(n)):
        product = {
            "SKU": faker.unique.ean(length=8),
            "Product_Name": faker.catch_phrase(),
            "Description": faker.text(max_nb_chars=200),
            "Size": random.choice(["XS", "S", "M", "L", "XL"]),
            "Color": faker.color_name(),
            "Category": random.choice(categories),
            "Material": random.choice(["Cotton", "Polyester", "Wool", "Silk", "Linen"]),
            "Season": random.choice(["Spring", "Summer", "Fall", "Winter"]),
        }
        products.append(product)
    return pd.DataFrame(products)
