create or replace table products (
    sku varchar(8) primary key,
    product_name varchar(100),
    description varchar(2000),
    size varchar(5),
    color varchar(20),
    category varchar(20),
    material varchar(50),
    season varchar(20)
);