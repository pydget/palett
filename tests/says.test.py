from foba.dicts.dict_strings import dict_collection
from pyspare import deco_dict

from palett.enum.font_effects import BOLD, INVERSE
from palett.says import Says


def test():
    name, lex = dict_collection.flop_shuffle(7)
    print(name, deco_dict(lex))
    says = Says(BOLD)
    for key, value in lex.items():
        pal = says[key].asc
        pal(value)


test()
