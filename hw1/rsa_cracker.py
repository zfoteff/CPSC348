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
import mpmath
from sympy.ntheory import factorint


def inverse_mod(a, m):
    """Return the inverse mod of a with respect to m."""
    g, x, y = extended_greatest_common_denominator(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def extended_greatest_common_denominator(a, b):
    """Return (g, x, y) such that a*x + b*y = g = greatest_common_denominator(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_greatest_common_denominator(b % a, a)
        return (g, x - (b // a) * y, y)

def encryptRSA(e, n , text):
    cyphertext = pow(text, e, n)
    return cyphertext

def decryptRSA(d, n, text):
    plaintext = pow(text, d, n)
    return plaintext

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

def crackRsaPrivateKey(e, n):
    """Given an RSA private key, return the private exponent."""
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
    d = inverse_mod(e, phi)
    return d

def testAlgorithms ():
    key_sizes = [6,6,7,8,10,11,25,30,33,55,68,73,81]
    e_list =    [7,3,17,11,7,1319,20293957,293210035,5292724727,65537,65537,65537,65537]
    n_list =    [33,55,77,143,527,1717,24899297,660416987,8093802337,26205577898256853,221000191580019839159,23800004200970185016117,1769685722799684125246893]
    d_list =    [3,27,53,11,343,0,17590093,0,0,9843735732800705,0,0,0]
    plaintext = [11,22,33,44,55,66,77,88,99,1010,1111,1212,1313]
    encrypted = [11,33,66,99,251,263,3851853,159810131,6516777357,9190603619039538,10883406131699884500660416987,7,10290404458130915244793,1596396698114749970315290]

    # Repeat the test cases 13 times
    for case in range (0, 13):
        printAlgorithmResults (case, key_sizes[case], plaintext[case], encrypted[case], e_list[case], n_list[case], d_list[case])

def printAlgorithmResults (test_case, key_size, plaintext, ciphertext, e, n, d):
    brute_force_time = -1

    if test_case < 7:
        start = time.time()
        d_actual_bf = crackRsaBruteForce(e, n)
        end = time.time()
        brute_force_time = '%.3f'%(end-start)

    start = time.time()
    d_actual = crackRsaPrivateKey(e, n)
    end = time.time()
    cracking_time = '%.3f'%(end-start)

    print (" **************** Test Case "+str(test_case+1)+" - "+str(key_size)+" bits **************** \n")
    print ("d expected: "+str(d))
    print ("d actual: "+str(d_actual))
    print ("plaintext (expected): "+str(plaintext))
    print ("plaintext (actual): "+str(decryptRSA(d_actual,n,ciphertext)))
    print ("ciphertext (expected): "+str(ciphertext))
    print ("ciphertext (actual): "+str(encryptRSA(e,n,plaintext)))
    print ("cracking took "+str(cracking_time)+" seconds")

    if brute_force_time == -1:
        print ("brute force took too long to complete\n")
    else:
        print ("brute force took "+str(brute_force_time)+" seconds\n")

def main():
    """ Main function """
    testAlgorithms()


main()
