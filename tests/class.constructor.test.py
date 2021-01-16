from ject import oneself


class Point:
    def __init__(self, *ks):
        print(ks)
        pass


p = Point()
print(p)

a = 0
if a:
    print('yes')
else:
    print('no')
