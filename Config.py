---

### **2. `config.py`**
```python
YEAR = 2026
BRIGHTNESS = 60
REFRESH_SECONDS = 25
FAVORITE_TEAM = None   # Change to e.g. "Geelong Cats" to show only your team

MATRIX_OPTIONS = {
    "rows": 32,
    "cols": 64,
    "chain_length": 1,
    "parallel": 1,
    "hardware_mapping": "regular",
    "brightness": BRIGHTNESS,
    "gpio_slowdown": 3,           # Good starting value for Pi Zero W
    "led_rgb_sequence": "RGB",
}
