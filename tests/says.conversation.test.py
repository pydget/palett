from pyspare import deco_dict

from palett.enum.font_effects import BOLD
from palett.says import Says

says = Says(BOLD)

says.chef.to(says.aboyeur).to(says.worker)('what to do')
says.worker.asc.to(says.chef)('how would i know')
says.worker('i\'ll be there tmr')
says.tournant.asc.asc('anything i can do for you')
says.aboyeur('no,\n but you just stand by, \nand wait for order')
says.tournant('yes')

print()
print('registered roster')
print(deco_dict(says.roster()))
