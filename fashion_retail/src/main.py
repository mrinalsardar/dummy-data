import logging
from pathlib import Path

from scripts.competitions import generate_competition_data
from scripts.customer_interactions import generate_customer_interaction_data
from scripts.customers import generate_customer_data
from scripts.financial import generate_financial_data
from scripts.inventory import generate_inventory_data
from scripts.marketing import generate_marketing_data
from scripts.operations import generate_operational_data
from scripts.products import generate_product_data
from scripts.sales import generate_sales_data
from scripts.supply_chain import generate_supply_chain_data

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# Parameter
scale_factor = 1 # Integer value


# Number of records
num_customers = 100 * max(scale_factor, 1)
num_products = 50 * max(scale_factor // 5, 1)
inventory_percentage = 95  # what percentage of products available
num_transactions = num_customers * 50
max_product_per_txn = 10
num_competitions = 20
num_interactions = num_customers // 2
num_marketings = num_customers * 10
num_financials = 12 * min(scale_factor, 5)
num_operations = num_customers // 50
num_supply_chains = num_customers // 50

current_dir = Path(__file__).absolute()
data_dir = Path(current_dir.parents[1], "data")


if __name__ == "__main__":
    log.info("Begin")

    log.debug("Creating customer data [%d customers]" % num_customers)
    customer_data = generate_customer_data(n=num_customers)
    customer_file = Path(data_dir, "customer_data.csv")
    log.debug("Storing customer data into %s" % customer_file)
    customer_data.to_csv(customer_file, index=False)

    log.debug("Creating products data [%d products]" % num_products)
    product_data = generate_product_data(n=num_products)
    product_file = Path(data_dir, "product_data.csv")
    log.debug("Storing product data into %s" % product_file)
    product_data.to_csv(product_file, index=False)

    log.debug("Creating inventory data [%d percent]" % inventory_percentage)
    inventory_data = generate_inventory_data(
        products_df=product_data, inventory_percentage=inventory_percentage
    )
    inventory_file = Path(data_dir, "inventory_data.csv")
    log.debug("Storing inventory data into %s" % inventory_file)
    inventory_data.to_csv(inventory_file, index=False)

    log.debug("Creating sales data [%d sales]" % num_transactions)
    sales_data = generate_sales_data(
        customers_df=customer_data,
        products_df=inventory_data,
        n_txn=num_transactions,
        max_product_per_txn=max_product_per_txn,
    )
    sales_file = Path(data_dir, "sales_data.csv")
    log.debug("Storing sales data into %s" % sales_file)
    sales_data.to_csv(sales_file, index=False)

    log.debug("Creating supply_chain data [%d supply_chains]" % num_supply_chains)
    supply_chain_data = generate_supply_chain_data(n=num_supply_chains)
    supply_chain_file = Path(data_dir, "supply_chain_data.csv")
    log.debug("Storing supply_chain data into %s" % supply_chain_file)
    supply_chain_data.to_csv(supply_chain_file, index=False)

    log.debug("Creating competition data [%d competitions]" % num_competitions)
    competition_data = generate_competition_data(n=num_competitions)
    competition_file = Path(data_dir, "competition_data.csv")
    log.debug("Storing competition data into %s" % competition_file)
    competition_data.to_csv(competition_file, index=False)

    log.debug("Creating interaction data [%d interactions]" % num_interactions)
    interaction_data = generate_customer_interaction_data(n=num_interactions)
    interaction_file = Path(data_dir, "customer_interaction_data.csv")
    log.debug("Storing interaction data into %s" % interaction_file)
    interaction_data.to_csv(interaction_file, index=False)

    log.debug("Creating marketing data [%d marketings]" % num_marketings)
    marketing_data = generate_marketing_data(n=num_marketings)
    marketing_file = Path(data_dir, "marketing_data.csv")
    log.debug("Storing marketing data into %s" % marketing_file)
    marketing_data.to_csv(marketing_file, index=False)

    log.debug("Creating operation data [%d operations]" % num_operations)
    operation_data = generate_operational_data(n=num_operations)
    operation_file = Path(data_dir, "operation_data.csv")
    log.debug("Storing operation data into %s" % operation_file)
    operation_data.to_csv(operation_file, index=False)

    log.debug("Creating financial data [%d financials]" % num_financials)
    financial_data = generate_financial_data(n=num_financials)
    financial_file = Path(data_dir, "financial_data.csv")
    log.debug("Storing financial data into %s" % financial_file)
    financial_data.to_csv(financial_file, index=False)

    log.info("End")
