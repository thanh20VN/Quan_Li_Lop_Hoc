def read_egfile(t):
    if t == "g":
        import json
        with open("./data/give.json", "r", encoding="utf-8") as f:
            teams = json.load(f)
        return teams
    if t == "e":
        import json
        with open("./data/errors.json", "r", encoding="utf-8") as f:
            teams = json.load(f)
        return teams