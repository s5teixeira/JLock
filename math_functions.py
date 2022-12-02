
# https://rosettacode.org/wiki/Modular_inverse#Python

""" this module involves computing Math -  iterations and error handling """
def extended_gcd(aa, bb):
    """ this function calculates mod """
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# https://rosettacode.org/wiki/Modular_inverse#Python
def modinv(a, m):
    """ this function computes modular multiplication inverse of a number """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
