from fastapi import FastAPI, Query
from pathlib import Path
from typing import Any
import healthz
import orjson
import api.games.games

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/")
def hello_() -> set[str]:
    return {"Hello"}


app.include_router(healthz.router)
app.include_router(api.games.games.router)


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hola mundo"}


def load_json_file(filename: str) -> Any:
    return orjson.loads((DATA_DIR / filename).read_bytes())


alpha = load_json_file("provider-alpha.json")
beta = load_json_file("provider-beta.json")
gamma = load_json_file("provider-gamma.json")


@app.get("/api/games")
def get_games(
    search: str | None = Query(default=None),
    name: str | None = Query(default=None),
    provider: str | None = Query(default=None),
    category: str | None = Query(default=None),
    enabled: bool | None = Query(default=None),
) -> dict[str, Any]:

    return {"alpha": alpha, "beta": beta, "gamma": gamma}
