from palett.enum.font_effects import BOLD
from palett.presets import FRESH
from palett.projector import ProjectorFactory
from texting import COSP

projectorCandidates = [
    [1, 2, 3, 4, 5]
]


def test():
    for vec in projectorCandidates:
        bound = dict(min=1, max=5)
        projector = ProjectorFactory(bound, FRESH, BOLD)
        colored = [projector(x)(x) for x in vec]
        print(colored)
        print(f'[{COSP.join(colored)}]')


test()
