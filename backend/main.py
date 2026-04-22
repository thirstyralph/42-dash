from pathlib import Path
from typing import Any

import orjson
from fastapi import FastAPI, Query

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hola mundo"}



