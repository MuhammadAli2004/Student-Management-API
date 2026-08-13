# Student Management API

A beginner-friendly REST API built with **FastAPI** and **Pydantic** to learn how APIs, HTTP methods, request bodies, validation, path parameters, and CRUD operations work.

This project is part of my process of learning backend development with Python.

## Features

* Create students
* Get all students
* Get a student by ID
* Update a student
* Delete a student
* Validate request data with Pydantic
* Interactive API documentation with Swagger UI
* REST API endpoints using HTTP methods

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
student_api/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd student_api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

OpenAPI specification:

```text
http://127.0.0.1:8000/openapi.json
```

## Endpoints

| Method | Endpoint                 | Description                 |
| ------ | ------------------------ | --------------------------- |
| GET    | `/`                      | Check if the API is running |
| GET    | `/students`              | Get all students            |
| GET    | `/students/{student_id}` | Get a student by ID         |
| POST   | `/students`              | Create a student            |
| PUT    | `/students/{student_id}` | Replace a student           |
| DELETE | `/students/{student_id}` | Delete a student            |

## Creating a Student

Send a `POST` request to:

```text
/students
```

Example request:

```json
{
  "name": "Muhammad Ali",
  "age": 22,
  "course": "Computer Science",
  "enrolled": true
}
```

Example response:

```json
{
  "id": 1,
  "name": "Muhammad Ali",
  "age": 22,
  "course": "Computer Science",
  "enrolled": true
}
```

## Pydantic Validation

The `Student` model defines the expected structure and data types:

```python
class Student(BaseModel):
    name: str
    age: int
    course: str
    enrolled: bool = True
```

FastAPI uses this model to validate incoming JSON before passing the data to the endpoint.

For example, `age` must be an integer.

## Important Note

This project currently stores students in a Python list:

```python
students = []
```

This means the data is stored only in memory.

If the server is restarted, the students are lost.

A future version will replace the Python list with a database such as SQLite or PostgreSQL.

## What I Learned

Through this project I practiced:

* Creating FastAPI applications
* Creating API routes
* HTTP GET, POST, PUT and DELETE methods
* Path parameters
* JSON request bodies
* Pydantic models
* Request validation
* CRUD operations
* Swagger/OpenAPI documentation
* Running an API with Uvicorn
* Using virtual environments
* Understanding the client-server relationship

## Future Improvements

* Add a database
* Add proper HTTP status codes
* Add response models
* Add error handling
* Add query parameters
* Add authentication
* Add a separate API client
* Add automated tests
