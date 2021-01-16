from pyspare.deco.deco_crostab import deco_crostab

from palett.enum.color_degrees import readable
from palett.enum.color_groups import rainbow
from palett.enum.color_spaces import RGB, HSL, HEX
from palett.tabular import palett_crostab

crostab = palett_crostab(space=HEX,
                         colors=rainbow,
                         degrees=readable,
                         dyed=True)
print(deco_crostab(crostab, ansi=True))
