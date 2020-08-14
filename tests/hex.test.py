from palett.convert import hex_int


def test():
    hex_candidates = {
        'black': '#000',
        'white': 'FFF',
        'red': '#ff0000',
        'green': '00ff00',
        'blue': '0000ff',
        'magenta': 'ff00ff',
        'cyan': '00ffff',
        'yellow': 'ffff00',
        'grey': '808080'
    }
    for key, hex_str in hex_candidates.items():
        print(key, hex_str, '->', hex_int(hex_str))


test()