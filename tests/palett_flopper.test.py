import sys

from palett.dye import DyeFactory
from palett.enum.color_spaces import HEX
from palett.enum.font_effects import INVERSE
from palett.flopper import palett_flopper


def test():
    gen = palett_flopper(exhausted=False)
    dye_factory = DyeFactory(HEX, INVERSE)
    prev = ''
    while True:
        try:
            hex_color = next(gen)
            print(dye_factory(hex_color)(hex_color))
            if hex_color == prev: raise StopIteration
            prev = hex_color
        except StopIteration:
            print('exception StopIteration')
            sys.exit()


test()
