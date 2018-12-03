"""
This function returns the bands to be comopsited.
"""



def banded(s):
    return int(s[s.index("band") + 4:s.index('.')])



if __name__ == '__main__':
    import doctest
    doctest.testmod()
