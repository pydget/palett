from texting import COSP

from palett.fluo_vector import fluo_vector
from palett.presets import FRESH, PLANET

candidates = [
    [],
    ['Xx', 'Yy', 'Zz', 'e', 'd', 'c', '-', '1', 2, 3],
    [1, 1, 2, 3, 5, []],
    ['a', 'b', 'c', 'd', 'e'],
    [1, '1', 2.5, '3.5', 5, []],
    ['beijing', 'shanghai', 'wuhan', 'xiamen', 'changsha']
]


def test():
    for vec in candidates:
        fluoed = fluo_vector(vec, (FRESH, PLANET))
        print(f'[{COSP.join(fluoed)}]')


test()
