TEAM_DATA = {
    "Adelaide": {"short": "ADEL", "color": (255, 0, 0)},
    "Brisbane Lions": {"short": "BRIS", "color": (128, 0, 128)},
    "Carlton": {"short": "CARL", "color": (0, 80, 160)},
    "Collingwood": {"short": "COLL", "color": (0, 0, 0)},
    "Essendon": {"short": "ESS", "color": (255, 80, 0)},
    "Fremantle": {"short": "FREM", "color": (128, 0, 128)},
    "Geelong Cats": {"short": "GEEL", "color": (0, 100, 255)},
    "Gold Coast Suns": {"short": "GC", "color": (255, 165, 0)},
    "GWS Giants": {"short": "GWS", "color": (0, 150, 0)},
    "Hawthorn": {"short": "HAW", "color": (139, 0, 0)},
    "Melbourne": {"short": "MELB", "color": (0, 120, 255)},
    "North Melbourne": {"short": "NM", "color": (0, 150, 0)},
    "Port Adelaide": {"short": "PORT", "color": (0, 0, 0)},
    "Richmond": {"short": "RICH", "color": (255, 20, 20)},
    "St Kilda": {"short": "STK", "color": (0, 0, 0)},
    "Sydney": {"short": "SYD", "color": (255, 165, 0)},
    "West Coast": {"short": "WCE", "color": (255, 200, 0)},
    "Western Bulldogs": {"short": "WB", "color": (0, 80, 160)},
}

def get_team_info(name):
    name_str = str(name)
    for key in TEAM_DATA:
        if key.lower() in name_str.lower() or name_str.lower() in key.lower():
            return TEAM_DATA[key]
    return {"short": name_str[:6].upper(), "color": (200, 200, 200)}
