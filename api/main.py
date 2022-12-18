from fastapi import FastAPI
from endpoints.cheques import router as cheques
from endpoints.persons import router as persons
from endpoints.positions import router as positions
from endpoints.transactions import router as transactions
from endpoints.results import router as results

app = FastAPI()
app.include_router(cheques, tags=['cheques'])
app.include_router(persons, tags=['persons'])
app.include_router(positions, tags=['positions'])
app.include_router(transactions, tags=['transaction'])
app.include_router(results, tags=['results'])


@app.get("/")
def main():
    return {"content": "Hello World!"}
