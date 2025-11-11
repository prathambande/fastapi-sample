from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def hello_world():
    """Simple hello world endpoint"""
    return {"message": "Hello World"}


class CalculatorRequest(BaseModel):
    """Request model for calculator operations"""
    operation: str  # add, subtract, multiply, divide
    num1: float
    num2: float


@app.post("/calculator")
async def calculator(request: CalculatorRequest):
    """
    Calculator endpoint that performs basic arithmetic operations.
    
    Operations supported: add, subtract, multiply, divide
    """
    operation = request.operation.lower()
    num1 = request.num1
    num2 = request.num2
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2
    else:
        return {"error": f"Invalid operation: {operation}. Use: add, subtract, multiply, or divide"}
    
    return {
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    }
