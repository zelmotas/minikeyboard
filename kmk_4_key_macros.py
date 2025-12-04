# Import all the IOs of the board
import board

# Imports from the KMK library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Main keyboard instance
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your GPIO pins for the 4 keys
PINS = [board.D1, board.D2, board.D3, board.D4]  # Updated: keys on GPIO 1, 2, 3, 4  # Keys on GPIO 8, 9, 10, 11  # Updated: keys on GPIO 8, 9, then your remaining two

# Tell KMK that this is a simple keypad, not a matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# --- MACRO DEFINITIONS ---
# 1) Screenshot on Windows → Win + Shift + S
screenshot_macro = KC.MACRO(
    Press(KC.LGUI), Press(KC.LSHIFT), Tap(KC.S), Release(KC.LSHIFT), Release(KC.LGUI)
)

# 2) Open Canvas (UBC) → Win + R, type URL, press Enter
open_canvas_macro = KC.MACRO(
    Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),  # Open Run dialog
    Tap(KC.H), Tap(KC.T), Tap(KC.T), Tap(KC.P), Tap(KC.S), Tap(KC.DOT),
    Tap(KC.C), Tap(KC.A), Tap(KC.N), Tap(KC.V), Tap(KC.A), Tap(KC.S),
    Tap(KC.DOT), Tap(KC.U), Tap(KC.B), Tap(KC.C), Tap(KC.DOT), Tap(KC.A), Tap(KC.DOT),
    Tap(KC.C), Tap(KC.A),  # types "https://canvas.ubc.ca/"
    Tap(KC.ENTER)
)

# 3) Copy → Ctrl + C
copy_macro = KC.MACRO(
    Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)
)

# 4) Paste → Ctrl + V
paste_macro = KC.MACRO(
    Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)
)

# --- KEYMAP ORDER ---
# Key 1 → Screenshot
# Key 2 → Open Canvas
# Key 3 → Copy
# Key 4 → Paste
keyboard.keymap = [
    [
        screenshot_macro,
        open_canvas_macro,
        copy_macro,
        paste_macro,
    ]
]

# Start KMK
def __main__():
    keyboard.go()

if __name__ == '__main__':
    __main__()
