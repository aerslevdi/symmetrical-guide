import sqlite3

conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")
except sqlite3.OperationalError:
    pass

cursor.execute("INSERT INTO productos VALUES (1, 'Teclado', 500)")
cursor.execute("INSERT INTO productos VALUES (2, 'Mouse', 350)")
cursor.execute("INSERT INTO productos VALUES (3, 'Monitor', 1500)")
cursor.execute("INSERT INTO productos VALUES (4, 'Parlantes', 1100)")

conn.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(productos)
conn.close()