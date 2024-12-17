import psycopg2
conn = psycopg2.connect(
    dbname="nordwind",
    user="student",
    password="qweasd963",
    host="95.163.241.236",
    port="5432"
)
cursor = conn.cursor()
query = """
SELECT MIN(unit_price) AS min_price
FROM products
WHERE category_id = 1;
"""
cursor.execute(query)
result = cursor.fetchone()
print(f"Самая низкая цена в категории 1: {result[0]}")
cursor.close()
conn.close()