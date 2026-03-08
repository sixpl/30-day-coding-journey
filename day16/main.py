from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)

def home():
    html_content = """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>30 Days Python Training</title>
        </head>
        <body>
            <h1>
                Calculator
            </h1>
            <form action="/add" method="post">
                <label>
                    Enter number a:
                </label>
                <br>
                <input type="text" name="num1"  />
                <br><br>
                <label> Enter number b:</label>
                <br>
                <input type="text" name="num2" />
                <br><br>

                <button type="submit">Add Numbers</button>
            </form>
        </body>
    </html>

    """
    return html_content

@app.post("/add", response_class=HTMLResponse)
def add_numbers(num1: int = Form(...), num2: int = Form(...)):
    result = num1 + num2
    result_html = f"""
    
    <html>
        <head>
            <title>Result</title>
        </head>
        <body>
            <h1>Addition</h1>
            <p> {num1} + {num2} = {result} </p>
            <a href="/">Go Back</a>
        </body>
    </html>
    """
    return result_html