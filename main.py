from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

class CalcRequest(BaseModel):
    num1: float
    num2: float
    operation: str  # "add", "subtract", "multiply", "divide"

@app.post("/simple-calculate")
def calculate(request: CalcRequest):
    num1 = request.num1
    num2 = request.num2
    op = request.operation.lower()

    if op == "add":
        result = num1 + num2
    elif op == "subtract":
        result = num1 - num2
    elif op == "multiply":
        result = num1 * num2
    elif op == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation.")

    return {"result": result}

handler = Mangum(app)
