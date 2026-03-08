from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     dbname = "calculator_db",
#     user = "sixpl",
#     host = "localhost"
# )

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS calculations (
#                id SERIAL PRIMARY KEY,
#                num1 INTEGER,
#                num2 INTEGER,
#                result INTEGER
#                );
# """)

# conn.commit()

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS calculations (
                id SERIAL PRIMARY KEY,
                a INTEGER,
                b INTEGER,
                result INTEGER
                )
    """)

    conn.commit()
    cur.close()
    conn.close()

create_table()

@app.get("/")
def home():
    return{"message": "App is running!"}

@app.get("/hello")
def say_hello():
    return{"status": "Working"}

@app.get("/add")
def sum_cal(a:int, b:int):
    result = a + b

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO calculations (a, b, result) VALUES (%s, %s, %s)",
        (a, b, result)
    )

    conn.commit()
    cur.close()
    conn.close()

    return{"Addition is": result }

# @app.get("/add")
# def sum_calculator(a: int, b: int):
#     result = a + b
#     cursor.execute(

#         "INSERT INTO calculations (num1, num2, result) VALUES (%s, %s, %s)",
#         (a, b, result)
#     )
#     conn.commit()

#     return{"result: ": result}

# @app.get("/history")
# def history():
#     cursor.execute("SELECT * FROM calculations")
#     rows = cursor.fetchall()
#     return{"data": rows}

@app.get("/subtract")
def subtraction_calculator(a: int, b: int):
    result = a - b
    return{"result: ": result}

@app.get("/multiply")
def multiply_calculator(a: int, b: int):
    result = a * b
    return{"result: ": result}

@app.get("/division")
def division_calculator(a: int, b: int):
    result = a / b
    return{"result: ": result}

@app.get("/history")
def get_history():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM calculations"
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()
    

    history_list = []

    for row in rows:
        history_list.append({
            "id": row[0],
            "a": row[1],
            "b": row[2],
            "result": row[3]
        })

    return history_list


