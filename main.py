def calc_egs52_01_03(seed):
    """
    Seed key algorithm for 27 01/27 02 requests

    Seed - 2 bytes
    Key - 2 bytes
    """
    print("Seed:", int.to_bytes(seed, 2, 'big').hex(' '))
    res = ((seed << 8) & 0xFFFF) | (seed >> 8)
    res ^= 0x5aa5
    res *= 0x5aa5
    res &= 0xFFFF
    print("Key: ", int.to_bytes(res, 2, 'big').hex(' '))
    return res


def calc_egs52_05(seed):
    """
    Seed key algorithm for 27 05 requests

    Seed - 4 bytes
    Key - 4 bytes
    """
    print("Seed:", int.to_bytes(seed, 4, 'big').hex(' '))
    res = seed
    res ^= 0x5AA5A5A5
    res *= 0x5AA5A5A5
    res &= 0xFFFF_FFFF
    print("Key: ", int.to_bytes(res, 4, 'big').hex(' '))
    return res


def test_calc_egs52_01_03():
    assert(calc_egs52_01_03(0x650c) == 0x69c0)


def test_calc_egs52_05():
    assert(calc_egs52_05(0xc88c8676) == 0xfd9a15ff)
