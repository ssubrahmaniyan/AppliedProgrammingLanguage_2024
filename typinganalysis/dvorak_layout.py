keys = {
    # Number row (positions unchanged)
    '`': {'pos': (0, 4), 'start': 'a'},
    '1': {'pos': (1, 4), 'start': 'a'},
    '2': {'pos': (2, 4), 'start': 'o'},
    '3': {'pos': (3, 4), 'start': 'e'},
    '4': {'pos': (4, 4), 'start': 'u'},
    '5': {'pos': (5, 4), 'start': 'i'},
    '6': {'pos': (6, 4), 'start': 'd'},
    '7': {'pos': (7, 4), 'start': 'h'},
    '8': {'pos': (8, 4), 'start': 't'},
    '9': {'pos': (9, 4), 'start': 'n'},
    '0': {'pos': (10, 4), 'start': 's'},
    '[': {'pos': (11, 4), 'start': 's'},
    ']': {'pos': (12, 4), 'start': 's'},
    
    # Top letter row (positions unchanged)
    "'": {'pos': (1.5, 3), 'start': 'a'},
    ',': {'pos': (2.5, 3), 'start': 'o'},
    '.': {'pos': (3.5, 3), 'start': 'e'},
    'p': {'pos': (4.5, 3), 'start': 'u'},
    'y': {'pos': (5.5, 3), 'start': 'i'},
    'f': {'pos': (6.5, 3), 'start': 'd'},
    'g': {'pos': (7.5, 3), 'start': 'h'},
    'c': {'pos': (8.5, 3), 'start': 't'},
    'r': {'pos': (9.5, 3), 'start': 'n'},
    'l': {'pos': (10.5, 3), 'start': 's'},
    '/': {'pos': (11.5, 3), 'start': 's'},
    '=': {'pos': (12.5, 3), 'start': 's'},
    '\\': {'pos': (13.5, 3), 'start': 's'},
    
    # Home row (positions unchanged)
    'a': {'pos': (1.75, 2), 'start': 'a'},
    'o': {'pos': (2.75, 2), 'start': 'o'},
    'e': {'pos': (3.75, 2), 'start': 'e'},
    'u': {'pos': (4.75, 2), 'start': 'u'},
    'i': {'pos': (5.75, 2), 'start': 'i'},
    'd': {'pos': (6.75, 2), 'start': 'd'},
    'h': {'pos': (7.75, 2), 'start': 'h'},
    't': {'pos': (8.75, 2), 'start': 't'},
    'n': {'pos': (9.75, 2), 'start': 'n'},
    's': {'pos': (10.75, 2), 'start': 's'},
    '-': {'pos': (11.75, 2), 'start': 's'},
    
    # Bottom letter row (positions unchanged)
    ';': {'pos': (2.25, 1), 'start': 'a'},
    'q': {'pos': (3.25, 1), 'start': 'o'},
    'j': {'pos': (4.25, 1), 'start': 'e'},
    'k': {'pos': (5.25, 1), 'start': 'u'},
    'x': {'pos': (6.25, 1), 'start': 'i'},
    'b': {'pos': (7.25, 1), 'start': 'd'},
    'm': {'pos': (8.25, 1), 'start': 'h'},
    'w': {'pos': (9.25, 1), 'start': 't'},
    'v': {'pos': (10.25, 1), 'start': 'n'},
    'z': {'pos': (11.25, 1), 'start': 's'},
    
    # Special keys (positions unchanged)
    'Shift_L': {'pos': (0, 1), 'start': 'a'},
    'Shift_R': {'pos': (12.25, 1), 'start': 's'},
    'Ctrl_L': {'pos': (0, 0), 'start': 'a'},
    'Alt_L': {'pos': (1.5, 0), 'start': 'a'},
    'Space': {'pos': (4, 0), 'start': 'u'},
    'Alt_R': {'pos': (10, 0), 'start': 'h'},
    'Ctrl_R': {'pos': (11.5, 0), 'start': 's'},
}

characters = {
    # Lowercase letters
    'a': ('a',), 'b': ('b',), 'c': ('c',), 'd': ('d',), 'e': ('e',),
    'f': ('f',), 'g': ('g',), 'h': ('h',), 'i': ('i',), 'j': ('j',),
    'k': ('k',), 'l': ('l',), 'm': ('m',), 'n': ('n',), 'o': ('o',),
    'p': ('p',), 'q': ('q',), 'r': ('r',), 's': ('s',), 't': ('t',),
    'u': ('u',), 'v': ('v',), 'w': ('w',), 'x': ('x',), 'y': ('y',),
    'z': ('z',),
    
    # Uppercase letters
    'A': ('Shift_R', 'a'), 'B': ('Shift_R', 'b'), 'C': ('Shift_R', 'c'),
    'D': ('Shift_R', 'd'), 'E': ('Shift_R', 'e'), 'F': ('Shift_R', 'f'),
    'G': ('Shift_R', 'g'), 'H': ('Shift_L', 'h'), 'I': ('Shift_L', 'i'),
    'J': ('Shift_L', 'j'), 'K': ('Shift_L', 'k'), 'L': ('Shift_L', 'l'),
    'M': ('Shift_L', 'm'), 'N': ('Shift_L', 'n'), 'O': ('Shift_R', 'o'),
    'P': ('Shift_R', 'p'), 'Q': ('Shift_R', 'q'), 'R': ('Shift_L', 'r'),
    'S': ('Shift_L', 's'), 'T': ('Shift_L', 't'), 'U': ('Shift_R', 'u'),
    'V': ('Shift_L', 'v'), 'W': ('Shift_L', 'w'), 'X': ('Shift_R', 'x'),
    'Y': ('Shift_R', 'y'), 'Z': ('Shift_L', 'z'),
    
    # Numbers and their shifted symbols (unchanged)
    '1': ('1',), '!': ('Shift_R', '1'),
    '2': ('2',), '@': ('Shift_R', '2'),
    '3': ('3',), '#': ('Shift_R', '3'),
    '4': ('4',), '$': ('Shift_R', '4'),
    '5': ('5',), '%': ('Shift_R', '5'),
    '6': ('6',), '^': ('Shift_L', '6'),
    '7': ('7',), '&': ('Shift_L', '7'),
    '8': ('8',), '*': ('Shift_L', '8'),
    '9': ('9',), '(': ('Shift_L', '9'),
    '0': ('0',), ')': ('Shift_L', '0'),
    
    # Other symbols
    '`': ('`',), '~': ('Shift_R', '`'),
    '[': ('[',), '{': ('Shift_R', '['),
    ']': (']',), '}': ('Shift_R', ']'),
    '\\': ('\\',), '|': ('Shift_R', '\\'),
    "'": ("'",), '"': ('Shift_R', "'"),
    ',': (',',), '<': ('Shift_R', ','),
    '.': ('.',), '>': ('Shift_R', '.'),
    'p': ('p',), 'P': ('Shift_R', 'p'),
    'y': ('y',), 'Y': ('Shift_R', 'y'),
    'f': ('f',), 'F': ('Shift_R', 'f'),
    'g': ('g',), 'G': ('Shift_R', 'g'),
    'c': ('c',), 'C': ('Shift_R', 'c'),
    'r': ('r',), 'R': ('Shift_L', 'r'),
    'l': ('l',), 'L': ('Shift_L', 'l'),
    '/': ('/',), '?': ('Shift_R', '/'),
    '=': ('=',), '+': ('Shift_R', '='),
    'o': ('o',), 'O': ('Shift_R', 'o'),
    'e': ('e',), 'E': ('Shift_R', 'e'),
    'u': ('u',), 'U': ('Shift_R', 'u'),
    'i': ('i',), 'I': ('Shift_L', 'i'),
    'd': ('d',), 'D': ('Shift_R', 'd'),
    'h': ('h',), 'H': ('Shift_L', 'h'),
    't': ('t',), 'T': ('Shift_L', 't'),
    'n': ('n',), 'N': ('Shift_L', 'n'),
    's': ('s',), 'S': ('Shift_L', 's'),
    '-': ('-',), '_': ('Shift_R', '-'),
    ';': (';',), ':': ('Shift_R', ';'),
    'q': ('q',), 'Q': ('Shift_R', 'q'),
    'j': ('j',), 'J': ('Shift_L', 'j'),
    'k': ('k',), 'K': ('Shift_L', 'k'),
    'x': ('x',), 'X': ('Shift_R', 'x'),
    'b': ('b',), 'B': ('Shift_R', 'b'),
    'm': ('m',), 'M': ('Shift_L', 'm'),
    'w': ('w',), 'W': ('Shift_L', 'w'),
    'v': ('v',), 'V': ('Shift_L', 'v'),
    'z': ('z',), 'Z': ('Shift_L', 'z'),
    
    # Space (unchanged)
    ' ': ('Space',),
}
