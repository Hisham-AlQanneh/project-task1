import sqlite3
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")
logger = logging.getLogger()

def db():
    conn = sqlite3.connect("employee.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = db()
conn.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL
)
""")
conn.commit()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Employee(BaseModel):
    name: str
    department: str
    salary: float
    hire_date: str


@app.get("/employees")
def get_all():
    conn = db()
    rows = conn.execute("SELECT * FROM employees").fetchall()
    return [dict(r) for r in rows]

@app.get("/employees/{emp_id}")
def get_one(emp_id: int):
    conn = db()
    row = conn.execute(
        "SELECT * FROM employees WHERE employee_id=?",
        (emp_id,)
    ).fetchone()
    if not row:
        raise HTTPException(404, "Not found")
    return dict(row)

@app.post("/employees")
def add(emp: Employee):
    conn = db()
    conn.execute(
        "INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)",
        (emp.name, emp.department, emp.salary, emp.hire_date)
    )
    conn.commit()
    logger.info(f"Added employee {emp.name}")
    return {"message": "added"}

@app.put("/employees/{emp_id}")
def update(emp_id: int, emp: Employee):
    conn = db()
    conn.execute(
        "UPDATE employees SET name=?, department=?, salary=?, hire_date=? WHERE employee_id=?",
        (emp.name, emp.department, emp.salary, emp.hire_date, emp_id)
    )
    conn.commit()
    logger.info(f"Updated employee {emp_id}")
    return {"message": "updated"}

@app.delete("/employees/{emp_id}")
def delete(emp_id: int):
    conn = db()
    conn.execute(
        "DELETE FROM employees WHERE employee_id=?",
        (emp_id,)
    )
    conn.commit()
    logger.info(f"Deleted employee {emp_id}")
    return {"message": "deleted"}
