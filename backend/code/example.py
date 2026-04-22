from pathlib import Path
from typing import Any

import orjson
from fastapi import FastAPI, HTTPException

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/providers/{provider_name}")
def get_provider(provider_name: str) -> Any:
    file_path = DATA_DIR / f"provider-{provider_name}.json"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Provider '{provider_name}' no encontrado")

    try:
        return orjson.loads(file_path.read_bytes())
    except orjson.JSONDecodeError as exc:
        raise HTTPException(status_code=500, detail="JSON invalido") from exc
