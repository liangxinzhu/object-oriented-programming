from math_utils import isprime


def test_isprime_value():
    for i, f in enumerate([2, 19, 23, 97]):
        assert isprime(f) == 'True'
    for i, f in enumerate([15, 20, 34, 50]):
        assert isprime(f) == 'False'
