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


def normalize_text(value: str) -> str:
    return "".join(value.lower().split())


def get_games_filtered(
    search: str | None = None,
    name: str | None = None,
    provider: str | None = None,
    category: str | None = None,
    enabled: bool | None = None,
) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    normalized_search = normalize_text(search) if search is not None else None
    normalized_name = normalize_text(name) if name is not None else None
    normalized_provider = normalize_text(provider) if provider is not None else None
    normalized_category = normalize_text(category) if category is not None else None

    for game in alpha:
        normalized_title = normalize_text(game["title"])
        normalized_studio = normalize_text(game["studio"])
        normalized_type = normalize_text(game["type"])
        search_ok = normalized_search is None or normalized_search in normalized_title
        name_ok = normalized_name is None or normalized_title == normalized_name
        provider_ok = normalized_provider is None or normalized_studio == normalized_provider
        category_ok = normalized_category is None or normalized_type == normalized_category
        enabled_ok = enabled is None or game["active"] is enabled
        if search_ok and name_ok and provider_ok and category_ok and enabled_ok:
            matches.append(game)

    for game in beta:
        normalized_game_name = normalize_text(game["gameName"])
        normalized_provider_name = normalize_text(game["providerName"])
        normalized_game_category = normalize_text(game["gameCategory"])
        search_ok = normalized_search is None or normalized_search in normalized_game_name
        name_ok = normalized_name is None or normalized_game_name == normalized_name
        provider_ok = normalized_provider is None or normalized_provider_name == normalized_provider
        category_ok = normalized_category is None or normalized_game_category == normalized_category
        enabled_ok = enabled is None or game["isEnabled"] is enabled
        if search_ok and name_ok and provider_ok and category_ok and enabled_ok:
            matches.append(game)

    for game in gamma:
        attrs = game["data"]["attributes"]
        classification = game["data"]["classification"]
        status = game["data"]["status"]
        normalized_display_name = normalize_text(attrs["displayName"])
        normalized_label = normalize_text(attrs["label"])
        normalized_category_name = normalize_text(classification["category"])
        search_ok = normalized_search is None or normalized_search in normalized_display_name
        name_ok = normalized_name is None or normalized_display_name == normalized_name
        provider_ok = normalized_provider is None or normalized_label == normalized_provider
        category_ok = normalized_category is None or normalized_category_name == normalized_category
        enabled_ok = enabled is None or status["enabled"] is enabled
        if search_ok and name_ok and provider_ok and category_ok and enabled_ok:
            matches.append(game)

    return matches

