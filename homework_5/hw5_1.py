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
SELECT product_name 
FROM products 
WHERE unit_price >= 3 AND unit_price < 7;
"""
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row[0])
cursor.close()
conn.close()