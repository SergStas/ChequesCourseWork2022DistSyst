from fastapi import FastAPI
from endpoints.cheques import router as cheques
from endpoints.persons import router as persons
from endpoints.positions import router as positions

app = FastAPI()
app.include_router(cheques, tags=['cheques'])
app.include_router(persons, tags=['persons'])
app.include_router(positions, tags=['positions'])


@app.get("/")
def main():
    return {"content": "Hello World!"}
