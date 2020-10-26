from texting import RT

from palett import DyeFactory
from palett.convert import hex_rgb, hsl_rgb, rgb_hex, rgb_hsl
from palett.enum.color_spaces import HEX
from palett.enum.font_effects import BOLD

lex = {
    'black': '#3B4252',
    'red': '#BF616A',
    'green': '#A3BE8C',
    'yellow': '#EBCB8B',
    'blue': '#81A1C1',
    'magenta': '#B48EAD',
    'cyan': '#88C0D0',
    'white': '#E5E9F0',
}

dye_factory = DyeFactory(HEX, BOLD)


def test():
    for (key, hex_color) in lex.items():
        hex_color = hex_color.lower()
        rgb = hex_rgb(hex_color)
        hsl = rgb_hsl(rgb)
        rgb2 = hsl_rgb(hsl)
        hex2 = rgb_hex(rgb2)
        print(
            dye_factory(hex_color)(key),
            RT,
            dye_factory(hex_color)(hex_color),
            rgb,
            hsl,
            rgb2,
            dye_factory(hex2)(hex2)
        )


test()
