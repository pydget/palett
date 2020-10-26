from pyspare import deco

from palett import DyeFactory
from palett.cards import amber, teal, blue, pink
from palett.enum.color_spaces import HEX
from palett.enum.font_effects import BOLD
from palett.structs.preset import Preset

candidates = {
    'blue.darken_1': blue.darken_1,
    'teal.accent_2': teal.accent_2,
    'amber.accent_3': amber.accent_3,
    'pink.lighten_1': pink.lighten_1
}
dye_factory = DyeFactory(HEX, BOLD)

for key, hex_color in candidates.items():
    print(key, dye_factory(hex_color)(hex_color), end=' ')
    preset = Preset.rand(hex_color)
    print(deco({k: dye_factory(v)(v) for k, v in vars(preset).items()}))
