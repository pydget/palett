from pyspare.deco.deco_crostab import deco_crostab

from palett.enum.color_spaces import RGB, HSL, HEX
from palett.tabular import palett_crostab

crostab = palett_crostab(space=HEX, dyed=True)
print(deco_crostab(crostab, ansi=True))
