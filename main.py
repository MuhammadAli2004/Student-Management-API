from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str
    enrolled: bool = True


students = []


@app.get("/")
def home():
    return {"message": "Student API is running"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}


@app.post("/students")
def create_student(student: Student):

    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "enrolled": student.enrolled
    }

    students.append(new_student)

    return new_student


@app.put("/students/{student_id}")
def replace_student(student_id: int, student: Student):

    for index, existing_student in enumerate(students):

        if existing_student["id"] == student_id:

            updated_student = {
                "id": student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "enrolled": student.enrolled
            }

            students[index] = updated_student

            return updated_student

    return {"message": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            deleted_student = students.pop(index)

            return deleted_student

    return {"message": "Student not found"}