"""
Class: CPSC 348-01
Zac Foteff
09/28/20
GU Username: zfoteff
File Name: rsa_cracker.py
    File contains two algorithms for cracking RSA encryption keys. One algorithm
    uses various libraries to accompish this task in a fast manner, and the
    other algorithm uses a slower brute force approach

"""

from math import sqrt, floor
import time
from libnum import invmod
from sympy import factorint

def main():
    """ Main function """
    print(crackRsaPrivateKey(7, 33))
    print(crackRsaBruteForce(7, 33))


def getFirstFactor (n):
    """
    Find the first factor of a given number

    Keyword Arguments:
    n -- integer to find first factor of

    """
    # Start with iterator = 2
    i = 2

    while i < sqrt(n):
        # If n % i is, then the first factor has been found
        if n % i == 0:
            return i

        i += 1

    # Return -1 if somehow a factor isn't found
    return -1


def crackRsaPrivateKey (e, n):
    """
    Finds private key in an RSA encyption cypher using a fast algorithm

    Keyword Arguments:
    e -- public key
    n -- modulus
    """
    factorsOfN = factorint(n)

    # since n is the product of two primes, we know its only factors are those two primes
    # if this is not the case, n is invalid (i.e., not the product of two primes)
    factorsAreValid = len(factorsOfN) == 2 and all(multiplicity == 1 for multiplicity in factorsOfN.values())
    if (not factorsAreValid):
        raise Exception(f"{n} is not a valid n value.")

    factorsList = list(factorsOfN)
    p = factorsList[0]
    q = factorsList[1]

    phi = (p - 1) * (q - 1)
    d = invmod(e, phi)
    return d

def crackRsaBruteForce (e, n):
    """
    Finds private key in an RSA encyption cypher using a brute force attack

    Keyword Arguments:
    e -- public key
    n -- modulus
    """
    p = getFirstFactor(n)
    q = n/p
    phi = (p-1)*(q-1)

    d = 1
    while d < phi:
        # If the public key times the private key % phi = 1, then you have found
        # the correct private key
        if (e*d) % phi == 1:
            return d

        d += 1

    return -1

main()
