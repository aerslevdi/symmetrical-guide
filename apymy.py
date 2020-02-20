import pymysql
conn = pymysql.connect(
    host = "instructor-606",
    user = "root",
    db = "base_python"
)
cursor = conn.cursor()
cursor.execute("INSERT INTO alumnos VALUES ('Gras', 3)")
conn.commit()

cursor.execute("SELECT * FROM alumnos")
alumnos = cursor.fetchall()
for alumno in alumnos:
    print(alumnos)
conn.close()