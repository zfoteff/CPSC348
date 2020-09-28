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


def testAlgorithms ():
    key_sizes = [6,6,7,8,10,11,25,30,33,55,68,73,81]
    e_list =    [7,3,17,11,7,1319,20293957,293210035,5292724727,65537,65537,
                65537,65537]
    n_list =    [33,55,77,143,527,1717,24899297,660416987,26205577898256853,
                221000191580019839159,23800004200970185016117,
                17696857227996841252460893]
    d_list =    [3,27,53,11,343,0,17590093,0,0,9843735732800705,0,0,0]
    plaintext = [11,22,33,44,55,66,77,88,99,1010,1111,1212,1313]
    encrypted = [11,33,66,99,251,263,3851853,159810131,6516777357,
                9190603619039538,108834061316998845007,10290404458130915244793,
                1596396698114749970315290]

    # Repeat the test cases 13 times
    for case in range (0, 12):
        testOneAlgorithm (case, key_sizes[case], plaintext[case], encrypted[case], e_list[case], n_list[case], d_list[case])


def testOneAlgorithm (test_case, key_size, plaintext, ciphertext, e, n, d):
    start = time.time()
    d_actual_bf = crackRsaBruteForce(e, n)
    end = time.time()
    brute_force_time = '%.3f'%(end-start)

    start = time.time()
    d_actual_bf = crackRsaPrivateKey(e, n)
    end = time.time()
    cracking_time = '%.3f'%(end-start)

    print (" **************** Test Case "+str(test_case)+" - "+str(key_size)+" bits **************** \n")
    print ("d expected: "+str(d))
    print ("d actual: "+str(crackRsaPrivateKey(e, n)))
    print ("plaintext (expected): "+str(plaintext))
    print ("plaintext (actual): "+str(decryptRSA(d,n,ciphertext)))
    print ("ciphertext (expected): "+str(ciphertext))
    print ("ciphertext (actual): "+str(encryptRSA(e,n,plaintext)))
    print ("cracking took "+str(cracking_time)+" seconds")
    print ("brute force took "+str(brute_force_time)+" seconds")

def main():
    """ Main function """
    testAlgorithms()


main()
