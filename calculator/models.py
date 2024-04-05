from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class ArithmeticOperation(BaseModel):
    operation: str
    x: float
    y: float

@app.post("/calculate")
def calculate(operation_info: ArithmeticOperation):
    operation = operation_info.operation
    x = operation_info.x
    y = operation_info.y
    
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = x / y
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}
class ConvertTemperature(BaseModel):
    cloud = str
    kelvin: float
    Fahrenheit: float
    celcius: float


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    raise HTTPException(status_code=400, detail="Invalid temperature conversion")

@app.get("/convert/temperature")
def convert_temperature_endpoint(value: float = Query(..., gt=0), from_unit: str = Query(..., regex="^(Celsius|Fahrenheit|Kelvin)$"), to_unit: str = Query(..., regex="^(Celsius|Fahrenheit|Kelvin)$")):
    converted_value = convert_temperature(value, from_unit, to_unit)
    return {"result": converted_value}
