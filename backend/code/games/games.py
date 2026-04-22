from fastapi import APIRouter, Query
from pathlib import Path
from typing import Any
import orjson

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

def load_json_file(filename: str) -> Any:
    return orjson.loads((DATA_DIR / filename).read_bytes())
alpha = load_json_file("provider-alpha.json")
beta = load_json_file("provider-beta.json")
gamma = load_json_file("provider-gamma.json")

@router.get("/api/games")
def get_games(
    search: str | None = Query(default=None),
    name: str | None = Query(default=None),
    provider: str | None = Query(default=None),
    category: str | None = Query(default=None),
    enabled: bool | None = Query(default=None),
) -> dict[str, Any]:
    if all(value is None for value in (search, name, provider, category, enabled)):
        return {"results": get_all_games()}

    return {
        "results": get_games_filtered(
            search=search,
            name=name,
            provider=provider,
            category=category,
            enabled=enabled,
        )
    }



def get_games_by_name(name: str) -> list[dict[str, Any]]:
    return get_games_filtered(name=name)


def get_games_by_provider(provider: str) -> list[dict[str, Any]]:
    return get_games_filtered(provider=provider)


def get_all_games() -> list[dict[str, Any]]:
    return [*alpha, *beta, *gamma]


def get_games_filtered(
    search: str | None = None,
    name: str | None = None,
    provider: str | None = None,
    category: str | None = None,
    enabled: bool | None = None,
) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    normalized_search = search.lower() if search is not None else None
    normalized_name = name.lower() if name is not None else None
    normalized_provider = provider.lower() if provider is not None else None

    # category and enabled are accepted now to keep the function extensible.
    _ = (category, enabled)

    for game in alpha:
        search_ok = normalized_search is None or normalized_search in game["title"].lower()
        name_ok = normalized_name is None or game["title"].lower() == normalized_name
        provider_ok = normalized_provider is None or game["studio"].lower() == normalized_provider
        if search_ok and name_ok and provider_ok:
            matches.append(game)

    for game in beta:
        search_ok = normalized_search is None or normalized_search in game["gameName"].lower()
        name_ok = normalized_name is None or game["gameName"].lower() == normalized_name
        provider_ok = normalized_provider is None or game["providerName"].lower() == normalized_provider
        if search_ok and name_ok and provider_ok:
            matches.append(game)

    for game in gamma:
        attrs = game["data"]["attributes"]
        search_ok = normalized_search is None or normalized_search in attrs["displayName"].lower()
        name_ok = normalized_name is None or attrs["displayName"].lower() == normalized_name
        provider_ok = normalized_provider is None or attrs["label"].lower() == normalized_provider
        if search_ok and name_ok and provider_ok:
            matches.append(game)

    return matches

