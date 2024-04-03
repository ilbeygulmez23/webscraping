CREATE DATABASE IF NOT EXISTS petlebi;
USE petlebi;
DROP TABLE petlebi;
CREATE TABLE IF NOT EXISTS petlebi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_url VARCHAR(500),
    product_name VARCHAR(500),
    product_barcode VARCHAR(20),
    product_price VARCHAR(10),
    product_stock VARCHAR(10),
    product_images VARCHAR(20),
    product_description VARCHAR(1000),
    product_skt VARCHAR(20),
    product_category VARCHAR(500),
    product_id VARCHAR(20),
    product_brand VARCHAR(500)
);