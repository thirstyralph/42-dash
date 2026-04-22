from fastapi import FastAPI
import healthz
import games

app = FastAPI(title="Dash QTech API", version="0.1.0")


@app.get("/")
def hello_() -> set[str]:
    return {"Hello"}


app.include_router(healthz.router)
app.include_router(games.router)


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hola mundo"}


if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("BACKEND_PORT", 3000))

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
