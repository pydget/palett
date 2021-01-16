from pyspare import deco_vector
from texting import CO

from palett import DyeFactory, hex_hsl, hsl_hex
from palett.enum.color_spaces import HSL
from palett.enum.font_effects import BOLD
from palett.toner import hsl_toner

dye_factory = DyeFactory(HSL, BOLD)

color = hex_hsl('#FF0000')
print(color)
for i in range(10):
    color = hsl_toner(color, 0, 0, 5)
    dye = dye_factory(color)
    print(
        dye(hsl_hex(color).upper()),
        ':',
        dye(deco_vector(color, read=lambda x: f'{x:3.0f}', presets=None, delim=CO))
    )
