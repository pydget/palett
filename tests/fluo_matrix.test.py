from texting import COSP, LF, SP
from veho.enum.enum_matrix_directions import COLUMNWISE, POINTWISE, ROWWISE
from veho.matrix import init

from palett.fluo_matrix import fluo_matrix
from palett.presets import FRESH, PLANET

candidates = {
    'alphabetical': init(4, 7, lambda x, y: chr(63 + (x * 7) + y)),
    'another': [
        [1, 2, 3],
        [4, 5, 6],
        ['a', 'b', 'c']
    ]
}


def deco_row(row): return f'{SP}[{COSP.join(row)}]'


def deco_matrix(mx): return f'[{LF}{LF.join([deco_row(row) for row in mx])}{LF}]'


print('fluo_matrix')
for key, matrix in candidates.items():
    print(key)
    fluoed = fluo_matrix(matrix, POINTWISE, (FRESH, PLANET))
    print(deco_matrix(fluoed))

print()
print('fluo_rows')
for key, matrix in candidates.items():
    print(key)
    fluoed = fluo_matrix(matrix, ROWWISE, (FRESH, PLANET))
    print(deco_matrix(fluoed))

print()
print('fluo_columns')
for key, matrix in candidates.items():
    print(key)
    fluoed = fluo_matrix(matrix, COLUMNWISE, (FRESH, PLANET))
    print(deco_matrix(fluoed))
