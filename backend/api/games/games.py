from fastapi import APIRouter

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.get("/")
def read_games() -> set[str]:
    return {"OK"}


@router.get("/{game_id}")
def return_id() -> set[str]:
    return {"OK {game_id}"}
