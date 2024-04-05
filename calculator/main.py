from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add_numbers(x: float, y: float):
    return {"result": x + y}

@app.get("/subtract")
def subtract_numbers(x: float, y: float):
    return {"result": x - y}

@app.get("/multiply")
def multiply_numbers(x: float, y: float):
    return {"result": x * y}

@app.get("/divide")
def divide_numbers(x: float, y: float):
    if y == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": x / y}

@app.get("/power")
def power(x: float, y: float):
    return {"result": x ** y}

@app.get("/sqrt")
def square_root(x: float):
    if x < 0:
        return {"error": "Square root of a negative number is not real"}
    return {"result": x ** 0.5}

@app.get("/convert")
def convert_units(value: float, from_unit: str, to_unit: str):
    conversion_rates = {"meters_to_feet": 3.28084, "feet_to_meters": 0.3048}
    conversion_key = f"{from_unit}_to_{to_unit}"
    if conversion_key not in conversion_rates:
        return {"error": "Conversion not supported"}
    converted_value = value * conversion_rates[conversion_key]
    return {"result": converted_value}

@app.get("/logical-and")
def logical_and(x: bool, y: bool):
    return {"result": x and y}

@app.get("/logical-or")
def logical_or(x: bool, y: bool):
    return {"result": x or y}

@app.get("/logical-not")
def logical_not(x: bool):
    return {"result": not x}



