import sqlite3

conn = sqlite3.connect("mibase.db")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE alumnos (nombre TEXT, cursos NUMERIC)")
except sqlite3.OperationalError:
    pass


nombre = input("Insert  name: ")
curso = input("Insert  course: ")
cursor.execute(f"INSERT INTO alumnos VALUES ('{nombre}', {curso})")

cursor.execute("INSERT INTO alumnos VALUES ('Matias', 3)")
cursor.execute("INSERT INTO alumnos VALUES ('Maria', 4)")
cursor.execute("INSERT INTO alumnos VALUES ('Mateo', 5)")
cursor.execute("INSERT INTO alumnos VALUES ('Manuel', 6)")
cursor.execute("INSERT INTO alumnos VALUES ('Melina', 7)")
cursor.execute("INSERT INTO alumnos VALUES ('Mauro', 4)")
cursor.execute("INSERT INTO alumnos VALUES ('Martin', 8)")
cursor.execute("INSERT INTO alumnos VALUES ('Merlin', 3)")

conn.commit()

cursor.execute("SELECT * FROM alumnos")
alumnos = cursor.fetchall()
for alumno in alumnos:
    print(alumnos)
conn.close()