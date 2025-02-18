# OLED Display
Not enough screen space? Add a display to your keyboard!

This documentation concerns the recommended OLED extension.

*Note:*
Driving an OLED display can bind up a considerable amount of CPU time and RAM.
Be aware of the performance degradation that can occur.

## Preparation
First of all you need to download a few libraries that will make it possible for your OLED to work.
You can get them with the [Adafruit CircuitPython Libraries bundle](https://circuitpython.org/libraries).
Make sure you to choose the one that matches your version of CircuitPython.

Create a `lib` directory under the CircuitPython drive and copy the following
from the library bundle there:
* `adafruit_display_text/`
* `adafruit_displayio_ssd1306.mpy`

## Configuration
Here's how you may initialize the extension:

```python
import board
import busio
from kmk.extensions.oled import Oled, TextEntry, ImageEntry

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

oled = Oled(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
    width=128, # screen size
    height=64, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    dim_time=10, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=0, # time in seconds to turn off screen
    brightness=1, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)
```
Also shown are all the options with their default values.
Customize them to fit your screen and preferences.


## Images
Images have to be monochromatic bitmaps with same resolution as your display and
have to be placed in the root of the CircuitPython drive.
**Placing it in separate a seperate directory may cause issues.**

```python
oled.entries = [
    ImageEntry(image="1.bmp", x=0, y=0),
]
keyboard.extensions.append(oled)
```

You can also make your images appear only on specific layers,

```python
oled.entries = [
    ImageEntry(image="1.bmp", x=0, y=0, layer=0),
    ImageEntry(image="2.bmp", x=0, y=0, layer=1),
]
keyboard.extensions.append(oled)
```

and/or side of your split keyboard.

```python
oled.entries = [
    ImageEntry(image="L1.bmp", x=0, y=0, side="L"),
    ImageEntry(image="R1.bmp", x=0, y=0, side="R"),
]
keyboard.extensions.append(oled)
```

## Text
You're able to freely positon your text to place it wherever you want just by changing x and y values.

```python
oled.entries = [
    TextEntry(text="Layer = 1", x=0, y=0),
    TextEntry(text="Macros", x=0, y=12),
    TextEntry(text="Hey there!", x=0, y=24),
]
keyboard.extensions.append(oled)
```

### X and Y anchors
Anchor points define the "origin" or `(0, 0)` position within a text label.
Example: for text in top right corner you need to set its anchor points Top Right and move text to far right position.
The values can be set "T" for top, "M" for middle and "B" for bottom on the X
axis and "L" for left, "M" for middle and "R, for right on the Y axis.

For more infos about anchors check the [Adafruit docs](https://learn.adafruit.com/circuitpython-display-support-using-displayio/text).
Notable difference: KMK uses strings ("T", "M","B" and "L", "M", "R") instead of numbers.

```python
oled.entries = [
    TextEntry(text="Layer = 1", x=128, y=0, x_anchor="R", y_anchor="T"), # text in Top Right corner
    TextEntry(text="Macros", x=128, y=64, x_anchor="R", y_anchor="B"), # text in Bottom Right corner
    TextEntry(text="Hey there!", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
]
keyboard.extensions.append(oled)
```

### Split
Same as with images you can change displaying according to current layer or side of split keyboard.

```python
oled.entries = [
    TextEntry(text="Longer text that", x=0, y=0, layer=0),
    TextEntry(text="has been divided", x=0, y=12, layer=0, side="L"),
    TextEntry(text="for an example", x=0, y=24, layer=0, side="R"),
]
keyboard.extensions.append(oled)
```

### Inverting
Inverts colours of your text. Comes in handy, for example, as a good layer indicator.

```python
oled_ext = Oled(
    entries=[
        TextEntry(text='0 1 2 4', x=0, y=0),
        TextEntry(text='0', x=0, y=0, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=0, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=0, inverted=True, layer=2),
    ],
)
```

# Example Code
```python
import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.oled import Oled, TextEntry, ImageEntry

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)

i2c_bus = busio.I2C(board.GP21, board.GP20)
oled = Oled(
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='NUM', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    i2c=i2c_bus,
    device_address=0x3C,
    width=128,
    height=64,
    dim_time=10,
    dim_target=0.1,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(oled)
```
