import requests
import time
import sys
import argparse
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from config import *
from teams import get_team_info

# Command line arguments (good for Pi Zero W)
parser = argparse.ArgumentParser(description="AFL LED Scoreboard")
parser.add_argument("--led-gpio-slowdown", type=int, default=3, help="GPIO slowdown (2-4 for Pi Zero W)")
parser.add_argument("--led-brightness", type=int, default=BRIGHTNESS)
args = parser.parse_args()

# ============= MATRIX SETUP =============
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = MATRIX_OPTIONS["hardware_mapping"]
options.brightness = args.led_brightness
options.gpio_slowdown = args.led_gpio_slowdown
options.led_rgb_sequence = MATRIX_OPTIONS.get("led_rgb_sequence", "RGB")

matrix = RGBMatrix(options=options)

# ============= FONT SETUP =============
font = graphics.Font()
font_loaded = False
font_paths = ["fonts/5x8.bdf", "fonts/4x6.bdf", "fonts/tom-thumb.bdf"]

for path in font_paths:
    try:
        font.LoadFont(path)
        font_loaded = True
        print(f"Loaded font: {path}")
        break
    except:
        continue

if not font_loaded:
    print("Warning: Could not load font. Display may be limited.")

# ============= DATA FETCH =============
def get_games():
    try:
        url = f"https://api.squiggle.com.au/?q=games;year={YEAR}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return r.json().get('games', [])
    except Exception as e:
        print(f"API Error: {e}")
        return []

# ============= DRAWING =============
def draw_game(canvas, game, y):
    hteam = game.get('hteam', 'Home')
    ateam = game.get('ateam', 'Away')
    hinfo = get_team_info(hteam)
    ainfo = get_team_info(ateam)

    hscore = f"{game.get('hgoals',0)}.{game.get('hbehinds',0)}"
    ascore = f"{game.get('agoals',0)}.{game.get('abehinds',0)}"
    status = str(game.get('timestr', 'Upcoming'))[:13]

    # Home team
    graphics.DrawText(canvas, font, 1, y, graphics.Color(*hinfo["color"]), hinfo["short"])
    graphics.DrawText(canvas, font, 1, y + 9, graphics.Color(255, 255, 255), hscore)

    # Away team
    graphics.DrawText(canvas, font, 35, y, graphics.Color(*ainfo["color"]), ainfo["short"])
    graphics.DrawText(canvas, font, 35, y + 9, graphics.Color(255, 255, 255), ascore)

    # Status
    graphics.DrawText(canvas, font, 1, y + 19, graphics.Color(160, 160, 160), status)

# ============= MAIN LOOP =============
offscreen_canvas = matrix.CreateFrameCanvas()
print("🚀 AFL Scoreboard Started on Pi Zero W - Press Ctrl+C to stop")

try:
    while True:
        games = get_games()
        
        # Filter by favorite team if set
        if FAVORITE_TEAM:
            games = [g for g in games if FAVORITE_TEAM.lower() in str(g.get('hteam','')).lower() or 
                                           FAVORITE_TEAM.lower() in str(g.get('ateam','')).lower()]

        offscreen_canvas.Clear()
        y = 7
        count = 0

        for game in games[:2]:          # Max 2 games on small screen
            draw_game(offscreen_canvas, game, y)
            y += 27
            count += 1

        if count == 0:
            graphics.DrawText(offscreen_canvas, font, 4, 18, graphics.Color(255, 255, 100), "No Games")

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep(REFRESH_SECONDS)

except KeyboardInterrupt:
    print("\n👋 Scoreboard stopped.")
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
