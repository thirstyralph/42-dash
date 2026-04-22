from fastapi import FastAPI
import healthz
import api.games.games

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/")
def hello() -> set[str]:
    return {"Hello"}


app.include_router(healthz.router)
app.include_router(api.games.games.router)
