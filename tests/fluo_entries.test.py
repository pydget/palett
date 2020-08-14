from texting import COLF

from palett.fluo_entries import fluo_entries
from palett.presets import FRESH, PLANET

candidates = [
    # [],
    [('foo', 0), ('bar', 1), ('zen', 2)],
    [(0, 10), (1, 100), (2, 1000)]
]


def test():
    for vec in candidates:
        fluoed = fluo_entries(vec, (FRESH, PLANET))
        str_vec = [f'({k}, {v})' for k, v in fluoed]
        print(f'[{COLF.join(str_vec)}]')


test()
