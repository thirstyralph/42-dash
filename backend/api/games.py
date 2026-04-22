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


def get_games_by_name(name: str) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []

    for game in alpha:
        if game["title"].lower() == name.lower():
            matches.append(game)

    for game in beta:
        if game["gameName"].lower() == name.lower():
            matches.append(game)

    for game in gamma:
        if game["data"]["attributes"]["displayName"].lower() == name.lower():
            matches.append(game)

    return matches
