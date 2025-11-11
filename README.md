# FastAPI Starter Application

A simple FastAPI application with a hello world endpoint and a calculator endpoint.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
.\venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Hello World
- **URL**: `/`
- **Method**: GET
- **Response**: 
```json
{
  "message": "Hello World"
}
```

### 2. Calculator
- **URL**: `/calculator`
- **Method**: POST
- **Request Body**:
```json
{
  "operation": "add",
  "num1": 10,
  "num2": 5
}
```
- **Supported Operations**: `add`, `subtract`, `multiply`, `divide`
- **Response**:
```json
{
  "operation": "add",
  "num1": 10,
  "num2": 5,
  "result": 15
}
```

## Interactive API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

```bash
# Hello World
curl http://localhost:8000/

# Calculator - Addition
curl -X POST http://localhost:8000/calculator \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "num1": 10, "num2": 5}'

# Calculator - Division
curl -X POST http://localhost:8000/calculator \
  -H "Content-Type: application/json" \
  -d '{"operation": "divide", "num1": 20, "num2": 4}'
```
