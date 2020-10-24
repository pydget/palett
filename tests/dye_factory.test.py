from palett.cards import amber
from palett.dye import DyeFactory
from palett.enum.color_space import HEX
from palett.enum.font_effects import INVERSE

dyeFactory = DyeFactory(HEX, INVERSE)
dye_fn = dyeFactory(amber.base)
print(dye_fn('something'))
