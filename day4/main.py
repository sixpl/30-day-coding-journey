from fastapi import FastAPI
# import psycopg2

app = FastAPI()

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

@app.get("/")
def home():
    return{"message": "App is running!"}

@app.get("/hello")
def say_hello():
    return{"status": "Working"}

@app.get("/add")
def sum_cal(a:int, b:int):
    result = a + b
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