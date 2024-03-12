import psycopg2
import json

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="RickAndMorty",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Create the table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        status VARCHAR(20),
        species VARCHAR(50),
        type VARCHAR(50),
        gender VARCHAR(20),
        origin_name VARCHAR(50),
        location_name VARCHAR(50),
        image VARCHAR(100)
    )
''')

# Read data from the JSON file
with open('allCharsUpdated.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)

sorted_data_json = sorted(data_json, key=lambda x: x["id"])

# Insert the JSON data into the table
for data in sorted_data_json:
    cursor.execute('''
        INSERT INTO characters (
            name, status, species, type, gender,
            origin_name, location_name, image
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
            data['name'], data['status'], data['species'], data['type'], data['gender'],
            data['origin']['name'], data['location']['name'], data['image']
        ))

# Commit and close the connection
conn.commit()
conn.close()

print("Database successfully created!")
