from fastapi import FastAPI
from schemas import Course
import mysql.connector

app = FastAPI()

db_config = {
    "host": "100.27.52.36",
    "port": 8005,
    "user": "root",
    "password": "utec",
    "database": "api_cursos"
}

@app.post("/cursos")
def add_course(course: Course):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO cursos (nombre_del_curso, descripcion, id_profesor) VALUES (%s, %s, %s)"
    val = (course.nombre_del_curso, course.descripcion, course.id_profesor)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Course added successfully"}

@app.get("/cursos")
def get_courses():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos")
    courses = cursor.fetchall()
    conn.close()
    return {"courses": courses}

@app.get("/cursos/{id}")
def get_course(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos WHERE id = %s", (id,))
    course = cursor.fetchone()
    conn.close()
    return {"course": course}

@app.put("/cursos/{id}")
def update_course(id: int, course: Course):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "UPDATE cursos SET nombre_del_curso=%s, descripcion=%s, id_profesor=%s WHERE id=%s"
    val = (course.nombre_del_curso, course.descripcion, course.id_profesor, id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Course updated successfully"}

@app.delete("/cursos/{id}")
def delete_course(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cursos WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return {"message": "Course deleted successfully"}
