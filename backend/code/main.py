from fastapi import FastAPI
from . import healthz
from . import games

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/")
def hello_() -> set[str]:
    return {"Hello"}


app.include_router(healthz.router)
app.include_router(games.router)


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hola mundo"}
