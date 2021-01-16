from crostab import Table
from pyspare.deco.deco_tabular.deco_table import deco_table

from palett import DyeFactory, hex_int
from palett.enum.color_spaces import HEX
from palett.enum.font_effects import BOLD

candidates = {
    'black': '#000000',
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'magenta': '#FF00FF',
    'cyan': '#00FFFF',
    'white': '#FFFFFF',
}

dye_factory = DyeFactory(HEX, BOLD)
table = Table(head=['name', 'hex', 'int'], rows=[
    [key, (dye := dye_factory(color))(color), dye(hex_int(color))] for key, color in candidates.items()
])

print(deco_table(table, ansi=True))
