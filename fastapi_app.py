from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, welcome to Databricks from Walmart, lets's begin to research weekly sales from weeks include holidays and non-holidays!"}

@app.get("/query")
async def query():
    """Execute a SQL query from Walmart database to search weekly sales that includes holidays and non-hoildays"""

    result = querydb()
    return {"Walmart weekly sales": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')