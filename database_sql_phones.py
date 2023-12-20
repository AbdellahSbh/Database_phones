# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:42:43 2023

@author: abdellah
"""
import sqlite3
import random
# Connect to SQLite database 
conn = sqlite3.connect('store_database.db')

# Create a cursor object using the cursor method
cursor = conn.cursor()
conn.commit()

# SQL command to create a Phones table
create_phones_table_command = '''
CREATE TABLE IF NOT EXISTS phones (
    phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    release_year INTEGER,
    operating_system TEXT,
    screen_size TEXT,
    cpu TEXT,
    ram TEXT,
    storage_capacity TEXT,
    camera_resolution TEXT,
    battery_capacity TEXT,
    price INTEGER
);
'''

# SQL command to create a Customers table
create_customers_table_command = '''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    email TEXT UNIQUE,
    phone_number TEXT,
    phone_id INTEGER,
    store TEXT,
    FOREIGN KEY (phone_id) REFERENCES phones(phone_id)
    
);
 '''
   
create_stores_table_command = '''
CREATE TABLE IF NOT EXISTS stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT,
    location TEXT
);
'''

create_stock_table_command = '''
CREATE TABLE IF NOT EXISTS stock (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id INTEGER,
    phone_id INTEGER,
    quantity_in_stock INTEGER,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (phone_id) REFERENCES phones(phone_id)
);
'''

create_purchases_table_command = '''
CREATE TABLE IF NOT EXISTS purchases (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    phone_id INTEGER,
    store_id INTEGER,
    purchase_date DATE,
    quantity_purchased INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (phone_id) REFERENCES phones(phone_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);
'''

# Execute the commands
cursor.execute(create_phones_table_command)
cursor.execute(create_customers_table_command)
cursor.execute(create_stores_table_command)
cursor.execute(create_stock_table_command)
cursor.execute(create_purchases_table_command)

# Commit the changes
conn.commit()


# Example data for a few phone models
phones_data = [
    ('Apple', 'iPhone 13 Pro Max', 2021, 'iOS 15', '6.7 inches', 'A15 Bionic', '6 GB', '128 GB', '12 MP', '4352 mAh', 1099),
    ('Samsung', 'Galaxy S21 Ultra', 2021, 'Android 11', '6.8 inches', 'Exynos 2100', '12 GB', '128 GB', '108 MP', '5000 mAh', 1199),
   ('Google', 'Pixel 6 Pro', 2021, 'Android 12', '6.7 inches', 'Google Tensor', '12 GB', '128 GB', '50 MP', '5003 mAh', 899),
   ('OnePlus', '9 Pro', 2021, 'Android 11', '6.7 inches', 'Snapdragon 888', '8 GB', '128 GB', '48 MP', '4500 mAh', 969),
   ('Xiaomi', 'Mi 11 Ultra', 2021, 'Android 11', '6.81 inches', 'Snapdragon 888', '12 GB', '256 GB', '50 MP', '5000 mAh', 1299),
   ('Huawei', 'P40 Pro', 2020, 'Android 10', '6.58 inches', 'Kirin 990 5G', '8 GB', '256 GB', '50 MP', '4200 mAh', 999),
 ('Motorola', 'Edge Plus', 2020, 'Android 10', '6.7 inches', 'Snapdragon 865', '12 GB', '256 GB', '108 MP', '5000 mAh', 999),
  ('Sony', 'Xperia 1 III', 2021, 'Android 11', '6.5 inches', 'Snapdragon 888', '12 GB', '256 GB', '12 MP', '4500 mAh', 1299),
  ('Oppo', 'Find X3 Pro', 2021, 'Android 11', '6.7 inches', 'Snapdragon 888', '12 GB', '256 GB', '50 MP', '4500 mAh', 1149),
  ('LG', 'Wing', 2020, 'Android 10', '6.8 inches', 'Snapdragon 765G', '8 GB', '256 GB', '64 MP', '4000 mAh', 999),
  ('Asus', 'ROG Phone 5', 2021, 'Android 11', '6.78 inches', 'Snapdragon 888', '8 GB', '128 GB', '64 MP', '6000 mAh', 999),
  ('Realme', 'GT', 2021, 'Android 11', '6.43 inches', 'Snapdragon 888', '8 GB', '128 GB', '64 MP', '4500 mAh', 599),
  ('Nokia', '8.3 5G', 2020, 'Android 10', '6.81 inches', 'Snapdragon 765G', '8 GB', '128 GB', '64 MP', '4500 mAh', 699),
  ('HTC', 'U12+', 2018, 'Android 8', '6 inches', 'Snapdragon 845', '6 GB', '128 GB', '12 MP', '3500 mAh', 799),
  ('BlackBerry', 'Key2', 2018, 'Android 8.1', '4.5 inches', 'Snapdragon 660', '6 GB', '64 GB', '12 MP', '3500 mAh', 649),
  ('Apple', 'iPhone 12', 2020, 'iOS 14', '6.1 inches', 'A14 Bionic', '4 GB', '64 GB', '12 MP', '2815 mAh', 799),
  ('Samsung', 'Galaxy Note 20 Ultra', 2020, 'Android 10', '6.9 inches', 'Exynos 990', '12 GB', '128 GB', '108 MP', '4500 mAh', 1299),
  ('Google', 'Pixel 5', 2020, 'Android 11', '6 inches', 'Snapdragon 765G', '8 GB', '128 GB', '12.2 MP', '4080 mAh', 699),
  ('OnePlus', '8T', 2020, 'Android 11', '6.55 inches', 'Snapdragon 865', '12 GB', '256 GB', '48 MP', '4500 mAh', 749),
  ('Xiaomi', 'Redmi Note 10 Pro', 2021, 'Android 11', '6.67 inches', 'Snapdragon 732G', '6 GB', '128 GB', '108 MP', '5020 mAh', 279),
  ('Huawei', 'Mate 40 Pro', 2020, 'Android 10', '6.76 inches', 'Kirin 9000 5G', '8 GB', '256 GB', '50 MP', '4400 mAh', 1199),
  ('Motorola', 'Razr 5G', 2020, 'Android 10', '6.2 inches', 'Snapdragon 765G', '8 GB', '256 GB', '48 MP', '2800 mAh', 1399),
  ('Sony', 'Xperia 5 II', 2020, 'Android 10', '6.1 inches', 'Snapdragon 865', '8 GB', '128 GB', '12 MP', '4000 mAh', 949),
  ('Oppo', 'Reno 6 Pro 5G', 2021, 'Android 11', '6.55 inches', 'MediaTek Dimensity 1200', '12 GB', '256 GB', '64 MP', '4500 mAh' , 799),
  ('LG', 'G8 ThinQ', 2019, 'Android 9.0', '6.1 inches', 'Snapdragon 855', '6 GB', '128 GB', '12 MP + 16 MP', '3500 mAh', 850),
  ('Nokia', '9 PureView', 2019, 'Android 9.0', '5.99 inches', 'Snapdragon 845', '6 GB', '128 GB', '5x 12 MP', '3320 mAh', 700),
  ('Google', 'Pixel 4 XL', 2019, 'Android 10', '6.3 inches', 'Snapdragon 855', '6 GB', '64 GB', '12.2 MP + 16 MP', '3700 mAh', 899),
  ('Samsung', 'Galaxy A50', 2019, 'Android 9.0', '6.4 inches', 'Exynos 9610', '4 GB', '64 GB', '25 MP + 8 MP + 5 MP', '4000 mAh', 349),
  ('Huawei', 'P30 Pro', 2019, 'Android 9.0', '6.47 inches', 'Kirin 980', '8 GB', '128 GB', '40 MP + 20 MP + 8 MP', '4200 mAh', 900),
  ('OnePlus', '7 Pro', 2019, 'Android 9.0', '6.67 inches', 'Snapdragon 855', '6 GB', '128 GB', '48 MP + 8 MP + 16 MP', '4000 mAh', 669),
  ('Xiaomi', 'Mi 9', 2019, 'Android 9.0', '6.39 inches', 'Snapdragon 855', '6 GB', '64 GB', '48 MP + 12 MP + 16 MP', '3300 mAh', 445),
  ('Apple', 'iPhone 11', 2019, 'iOS 13', '6.1 inches', 'A13 Bionic', '4 GB', '64 GB', '12 MP + 12 MP', '3110 mAh', 699),
  ('Sony', 'Xperia 1', 2019, 'Android 9.0', '6.5 inches', 'Snapdragon 855', '6 GB', '128 GB', '12 MP + 12 MP + 12 MP', '3330 mAh', 950),
  ('Motorola', 'Moto G7', 2019, 'Android 9.0', '6.2 inches', 'Snapdragon 632', '4 GB', '64 GB', '12 MP + 5 MP', '3000 mAh', 299),
  ('Asus', 'Zenfone 6', 2019, 'Android 9.0', '6.4 inches', 'Snapdragon 855', '6 GB', '64 GB', '48 MP + 13 MP', '5000 mAh', 499),
  ('Realme', 'X2 Pro', 2019, 'Android 9.0', '6.5 inches', 'Snapdragon 855+', '8 GB', '128 GB', '64 MP + 13 MP + 8 MP + 2 MP', '4000 mAh', 469),
  ('HTC', 'U12 Life', 2018, 'Android 8.1', '6 inches', 'Snapdragon 636', '4 GB', '64 GB', '16 MP + 5 MP', '3600 mAh', 349),
  ('BlackBerry', 'KEY2 LE', 2018, 'Android 8.1', '4.5 inches', 'Snapdragon 636', '4 GB', '32 GB', '13 MP + 5 MP', '3000 mAh', 449),
  ('Apple', 'iPhone XS', 2018, 'iOS 12', '5.8 inches', 'A12 Bionic', '4 GB', '64 GB', '12 MP + 12 MP', '2658 mAh', 999),
  ('Samsung', 'Galaxy S10', 2019, 'Android 9.0', '6.1 inches', 'Exynos 9820', '8 GB', '128 GB', '12 MP + 12 MP + 16 MP', '3400 mAh', 899),
  ('Google', 'Pixel 3a', 2019, 'Android 9.0', '5.6 inches', 'Snapdragon 670', '4 GB', '64 GB', '12.2 MP', '3000 mAh', 399),
  ('OnePlus', '6T', 2018, 'Android 9.0', '6.41 inches', 'Snapdragon 845', '6 GB', '128 GB', '16 MP + 20 MP', '3700 mAh', 549),
  ('Xiaomi', 'Redmi Note 7', 2019, 'Android 9.0', '6.3 inches', 'Snapdragon 660', '4 GB', '64 GB', '48 MP + 5 MP', '4000 mAh', 200),
  ('Huawei', 'Mate 20 Pro', 2018, 'Android 9.0', '6.39 inches', 'Kirin 980', '6 GB', '128 GB', '40 MP + 20 MP + 8 MP', '4200 mAh', 999),
  ('Apple', 'iPhone 14 Pro', 2023, 'iOS 16', '6.1 inches', 'A16 Bionic', '6 GB', '128 GB', '12 MP', '4400 mAh', 1199),
  ('Samsung', 'Galaxy Z Fold4', 2023, 'Android 12', '7.6 inches', 'Snapdragon 8 Gen 1', '12 GB', '256 GB', '108 MP', '4400 mAh', 1799),
  ('Google', 'Pixel 7', 2023, 'Android 13', '6.3 inches', 'Google Tensor G2', '8 GB', '128 GB', '50 MP', '4600 mAh', 999),
  ('OnePlus', '10T', 2023, 'Android 12', '6.7 inches', 'Snapdragon 8 Gen 1', '8 GB', '128 GB', '50 MP', '4800 mAh', 649),
  ('Xiaomi', 'Mi 12', 2023, 'Android 12', '6.28 inches', 'Snapdragon 8 Gen 1', '8 GB', '128 GB', '50 MP', '4500 mAh', 749),
  ('Huawei', 'P50 Pro', 2023, 'HarmonyOS', '6.6 inches', 'Kirin 9000', '8 GB', '256 GB', '50 MP', '4360 mAh', 1199),
  ('Motorola', 'Edge 30', 2023, 'Android 12', '6.5 inches', 'Snapdragon 8 Gen 1', '8 GB', '128 GB', '50 MP', '5000 mAh', 699),
  ('Sony', 'Xperia 5 IV', 2023, 'Android 12', '6.1 inches', 'Snapdragon 8 Gen 1', '8 GB', '128 GB', '12 MP', '5000 mAh', 999),
  ('Oppo', 'Find X5 Pro', 2023, 'Android 12', '6.7 inches', 'Snapdragon 8 Gen 1', '12 GB', '256 GB', '50 MP', '5000 mAh', 1199),
  ('LG', 'Velvet 2 Pro', 2023, 'Android 11', '6.8 inches', 'Snapdragon 888', '8 GB', '128 GB', '64 MP', '4300 mAh', 599),
  ('Asus', 'Zenfone 9', 2023, 'Android 12', '5.9 inches', 'Snapdragon 8 Gen 1', '8 GB', '128 GB', '64 MP', '4300 mAh', 699),
  ('Realme', 'GT Neo 3', 2023, 'Android 12', '6.7 inches', 'Dimensity 8100', '8 GB', '128 GB', '50 MP', '5000 mAh', 499)
]


customers_data = [
    ('Emma Smith', 'USA', 'emma.smith@email.com', '+10123456001', 1, 'Amazon'),
    ('Liam Johnson', 'Canada', 'liam.johnson@email.com', '+11023456002', 2, 'Samsung Store'),
    ('Marco Polo', 'Italy', 'marco.polo@email.com', '+39123456003', 3, 'Apple Store'),
    ('Lucas Moore', 'Germany', 'lucas.moore@email.com', '+49123456048', 4, 'Fnac'),
    ('Mia Thompson', 'Spain', 'mia.thompson@email.com', '+34123456049', 5, 'Carrefour'),
    ('Lionel Gauthier', 'Switzerland', 'lionel.gauthier@email.com', '+4123456001', 6, 'Amazon'),
    ('Jacob Taylor', 'France', 'jacob.taylor@email.com', '+33123456050', 7, 'Boulanger'),
    ('Sophia Martinez', 'Mexico', 'sophia.martinez@email.com', '+52123456008', 8, 'Mercado Libre'),
    ('Ethan Brown', 'Australia', 'ethan.brown@email.com', '+61123456009', 9, 'JB Hi-Fi'),
    ('Isabella Clark', 'New Zealand', 'isabella.clark@email.com', '+64123456010', 10, 'Noel Leeming'),
    ('Mason Rodriguez', 'India', 'mason.rodriguez@email.com', '+91123456011', 11, 'Reliance Digital'),
    ('Ava White', 'South Africa', 'ava.white@email.com', '+27123456012', 12, 'Takealot'),
    ('Oliver Harris', 'Nigeria', 'oliver.harris@email.com', '+234123456013', 13, 'Jumia'),
    ('Mia Martin', 'Brazil', 'mia.martin@email.com', '+55123456014', 14, 'Americanas'),
    ('James Lee', 'South Korea', 'james.lee@email.com', '+82123456015', 15, 'Gmarket'),
    ('Charlotte Walker', 'Russia', 'charlotte.walker@email.com', '+7123456016', 16, 'M.Video'),
    ('Harper Hall', 'Japan', 'harper.hall@email.com', '+81123456017', 17, 'Rakuten'),
    ('Evelyn Young', 'Turkey', 'evelyn.young@email.com', '+90123456018', 18, 'Hepsiburada'),
    ('Ahmed Al Maktum', 'United Arab Emirates', 'ahmed.almaktum@email.com', '+97123456019', 19, 'Sharaf DG'),
    ('Lucas Wright', 'Singapore', 'lucas.wright@email.com', '+65123456020', 20, 'Courts'),
    ('Amelia Green', 'Malaysia', 'amelia.green@email.com', '+60123456021', 21, 'Lazada'),
    ('Henry Adams', 'Thailand', 'henry.adams@email.com', '+66123456022', 22, 'Central Online'),
    ('Ava Martinez', 'Brazil', 'ava.martinez@email.com', '+55123456041', 41, 'Americanas'),
    ('Mason Hernandez', 'Argentina', 'mason.hernandez@email.com', '+54123456042', 42, 'Frávega'),
    ('Ethan King', 'Japan', 'ethan.king@email.com', '+81123456043', 43, 'Bic Camera'),
    ('Harper Lee', 'South Korea', 'harper.lee@email.com', '+82123456044', 44, 'Gmarket'),
    ('Matthew Clark', 'India', 'matthew.clark@email.com', '+91123456045', 45, 'Flipkart'),
    ('Elizabeth Lewis', 'Russia', 'elizabeth.lewis@email.com', '+74123456046', 46, 'M.Video'),
    ('Jackson Young', 'Turkey', 'jackson.young@email.com', '+90123456047', 47, 'Trendyol'),
    ('Charlotte Robinson', 'Germany', 'charlotte.robinson@email.com', '+49123456048', 48, 'MediaMarkt'),
    ('Henry Clark', 'Mexico', 'henry.clark@email.com', '+52123456049', 49, 'Walmart'),
    ('Amelia Lewis', 'France', 'amelia.lewis@email.com', '+33123456050', 50, 'Fnac'),
    ('Noah Anderson', 'Italy', 'noah.anderson@email.com', '+39123456051', 3, 'Apple Store'),
    ('Aria Martin', 'Spain', 'aria.martin@email.com', '+34123456052', 5, 'Carrefour'),
    ('Logan White', 'USA', 'logan.white@email.com', '+10123456053', 1, 'Amazon'),
    ('Isaac Johnson', 'Canada', 'isaac.johnson@email.com', '+11023456054', 2, 'Samsung Store'),
    ('Zoe King', 'Mexico', 'zoe.king@email.com', '+52123456055', 49, 'Walmart'),
    ('Liam Smith', 'Japan', 'liam.smith@email.com', '+81123456056', 17, 'Rakuten'),
    ('Grace Lee', 'South Korea', 'grace.lee@email.com', '+82123456057', 15, 'Gmarket'),
    ('Oliver Brown', 'Germany', 'oliver.brown@email.com', '+49123456058', 48, 'MediaMarkt'),
    ('Ella Davis', 'France', 'ella.davis@email.com', '+33123456059', 50, 'Fnac'),
    ('Mia Wilson', 'Australia', 'mia.wilson@email.com', '+61123456060', 9, 'JB Hi-Fi'),
    ('Ethan Harris', 'UK', 'ethan.harris@email.com', '+44123456061', 3, 'Apple Store'),
    ('Olivia Martinez', 'USA', 'olivia.martinez@email.com', '+52123456062', 49, 'Walmart'),
    ('Aiden Lee', 'South Korea', 'aiden.lee@email.com', '+82123456063', 15, 'Gmarket'),
    ('Emma Thompson', 'Canada', 'emma.thompson@email.com', '+11023456064', 2, 'Samsung Store'),
    ('Sophia Robinson', 'USA', 'sophia.robinson@email.com', '+10123456065', 1, 'Amazon'),
    ('Jackson Clark', 'Germany', 'jackson.clark@email.com', '+49123456066', 48, 'MediaMarkt'),
    ('Ava Hernandez', 'Spain', 'ava.hernandez@email.com', '+34123456067', 5, 'Carrefour'),
    ('Mason Wright', 'Italy', 'mason.wright@email.com', '+39123456068', 3, 'Apple Store'),
    ('Lily Evans', 'France', 'lily.evans@email.com', '+33123456069', 50, 'Fnac'),
    ('Noah White', 'Australia', 'noah.white@email.com', '+61123456070', 9, 'JB Hi-Fi'),
    ('Mia Johnson', 'Canada', 'mia.johnson@email.com', '+11023456071', 2, 'Samsung Store'),
    ('Lucas Brown', 'USA', 'lucas.brown@email.com', '+10123456072', 1, 'Amazon'),
    ('Chloe Green', 'UK', 'chloe.green@email.com', '+44123456073', 3, 'Apple Store'),
    ('Isabella Garcia', 'USA', 'isabella.garcia@email.com', '+52123456074', 49, 'Walmart'),
    ('Gabriel Martinez', 'Brazil', 'gabriel.martinez@email.com', '+55123456075', 14, 'Americanas')
    
]

store_names = set(customer[-1] for customer in customers_data)  # Extract unique store names
stores_data = [(name, 'Various Locations') for name in store_names]
store_data = {name: {'sales': 0, 'stock': 0} for name in store_names}


stock_data = []
for store_id, store in enumerate(stores_data, start=1):
    for phone_id in range(1, len(phones_data) + 1):
        quantity_in_stock = random.randint(0, 100)
        stock_data.append((store_id, phone_id, quantity_in_stock))
        store_data[store[0]]['stock'] += quantity_in_stock
        
        
purchases_data = []
for customer_id, customer in enumerate(customers_data, start=1):
    phone_id = customer[4]  # Assuming phone_id is the 5th element in customer data
    store_id = random.randint(1, len(stores_data))  # Random store selection
    purchase_date = f"2023-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    quantity_purchased = random.randint(1, 3)  # Random purchase quantity
    purchases_data.append((customer_id, phone_id, store_id, purchase_date, quantity_purchased))
    store_name = stores_data[store_id - 1][0]
    store_data[store_name]['sales'] += 1

for _, _, store_id, _, _ in purchases_data:
    store_name = next((customer[-1] for customer in customers_data if customer[4] == store_id), None)
    if store_name:
        store_data[store_name]['sales'] += 1

for store_id, _, quantity in stock_data:
    store_name = next((name for name, _ in stores_data if store_id == stores_data.index((name, _)) + 1), None)
    if store_name:
        store_data[store_name]['stock'] += quantity


def insert_phone_data(data):
    # Check if the phone already exists in the database
    cursor.execute('''
    SELECT * FROM phones WHERE model = ?
    ''', (data[1],))  # Use the model name as the unique identifier
    exists = cursor.fetchone()
    
    # If the phone does not exist, insert it
    if not exists:
        cursor.execute('''
        INSERT INTO phones (brand, model, release_year, operating_system, screen_size, cpu, ram, storage_capacity, camera_resolution, battery_capacity, price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()


def insert_customer_data(data):
    cursor.execute('''
    INSERT INTO customers (name, location, email, phone_number, phone_id, store)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    
def insert_store_data(data):
    cursor.execute('''
    INSERT INTO stores (store_name, sales_count, total_stock)
    VALUES (?, ?, ?)
    ''', data)
    conn.commit()

def insert_stock_data(data):
    cursor.execute('''
    INSERT INTO stock (store_id, phone_id, quantity_in_stock)
    VALUES (?, ?, ?)
    ''', data)
    conn.commit()

def insert_purchase_data(data):
    cursor.execute('''
    INSERT INTO purchases (customer_id, phone_id, store_id, purchase_date, quantity_purchased)
    VALUES (?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    
for phone in phones_data:
    insert_phone_data(phone)

for customer in customers_data:
    insert_customer_data(customer)

for store in stores_data:
    insert_store_data(store)

for stock in stock_data:
    insert_stock_data(stock)

for purchase in purchases_data:
    insert_purchase_data(purchase)

# Close the connection
conn.close()

    





