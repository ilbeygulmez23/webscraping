import mysql.connector
import json

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
)
cursor = connection.cursor()
# Create database SQL query. --> petlebi_create.sql
# I could have read the query from the file, but I wrote query on IDE first.
# The files are created only to meet the requirements.
cursor.execute("CREATE DATABASE IF NOT EXISTS petlebi")
cursor.execute("USE petlebi")
cursor.execute("DROP TABLE petlebi")
cursor.execute("""CREATE TABLE IF NOT EXISTS petlebi (
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
)""")
with open('petlebi_products.json', 'r', encoding='latin-1') as f:
    # Read each line (which contains a single JSON object) and process it
    products = []
    jsons = f.read().split("endjson")
    try:
        for jsonK in jsons:
            products.append(json.loads(jsonK))
    except json.decoder.JSONDecodeError:
        pass

    for product in products:
        # Insert SQL query --> petlebi_insert.sql
        sql = """INSERT INTO petlebi (product_url, product_name, product_barcode, 
        product_price, product_stock, product_images, product_description, product_skt, product_category, 
        product_id, product_brand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (product["product_url"],
                  product["product_name"],
                  product["product_barcode"],
                  product["product_price"],
                  product["product_stock"],
                  product["product_images"],
                  product["product_description"][0],
                  product["product_skt"],
                  product["product_category"],
                  product["product_id"],
                  product["product_brand"])
        cursor.execute(sql, params)

    # Commit changes and close connection
    connection.commit()
    cursor.close()
    connection.close()
