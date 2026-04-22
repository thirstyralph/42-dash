from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz", tags=["Health"])
def healthz() -> dict[str, str]:
    return {"status": "ok"}
