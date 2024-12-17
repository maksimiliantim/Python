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
SELECT supplier_id, MAX(unit_price) AS max_price
FROM products
WHERE supplier_id IN (1, 3, 5)
GROUP BY supplier_id
ORDER BY supplier_id;
"""
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(f"Поставщик ID: {row[0]}, Максимальная цена: {row[1]}")
cursor.close()
conn.close()