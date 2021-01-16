from types import SimpleNamespace as Object

from pyspare import deco

import palett.cards as cards
from palett.cards import amber, orange


def module_to_dict(module): return {k: getattr(module, k) for k in dir(module) if not k.startswith('_')}


print(type(cards))

print(deco(module_to_dict(cards)))


class SimpleNamespacePseudo:
    def __init__(self, /, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Ob(list):

    def __init__(self, *args, **kw):
        super().__init__()
        self[:] = list(args)
        setattr(self, '__dict__', kw)


ob_collection = Ob(amber=amber, orange=orange)

print(deco(ob_collection))

card_collection = Object(amber=amber, orange=orange)

print(deco(card_collection))
print(deco(vars(card_collection)))
