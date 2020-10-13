Exam 1 Study Guide
===================

# Introduction to Computer Security
## Terms
* Vulnerability:
* Countermeasure: Protective, preventative, detective, responsive, or recovery
controls implemented to reduce or counteract threats to a system

## Security v. Usability
alalalal

## CIA
Confidentiality
* Data may only be viewed by authorized users
Integrity
* Data may be added, deleted, or modified only by authorized users and in legitimate
ways
Availability
* Data must be available a t all applicable times to all applicable users

## Security Design principles
Simplicity  
* Keep the design as small and as simple as possible (modularity)

Fail-safe defaults  
* By default, disallow, don't allow
* Every access to every object must be checked for authority
* Example: else blocks, catch blocks

Open Design
* Secret key v. Secret design
* Opposite: Security through Obscurity

Multi-factor authentication
* Don't just require a passcode
  * Verification Codes
  * Emails
  * Fingerprint\\Bioscanners
* Two-factor authentication
  * Authenticate something you know
  * Authenticate something you have
  * Authenticate something you are

Least Privilege
* Every program and user of the system should operate using the least set of privilege necessary to complete the job
* Not only per user but per action

Isolation
* Minimize the amount of mechanisms common to more than one user, and depended on by all users ... especially the ones involving shared variables
* Examples
    1. Global variables
    1. Virtual Machines
    1. Side-Channel attacks
    1. Unsecured networks
* Isolate
  * Public data and networks from private data and networks
  * Users/programs/processes from others in the system
  * Key security mechanisms from other mechanisms in the system
  * Encapsulation (OOP)

Usability
* Principle of least surprise

Computational Feasibility
* 'Work Factor'
* Not impossible, but unprofitable

Intrusion detection
* Compromise recording
* Redundancy: Multiple layers of security

# Cryptography

## Terms
* Computational Feasibility:
* Man in the middle attack:

## Cryptographic functions and their purposes
Asymmetric Encryption:
* Public key encryption
* Can guarantee authenticity
* Very slow
* Key = 2^124

Symmetric Encryption:
* Key has to be distributed
  * High potential for risk

Symmetric v. Asymmetric:
* Neither is more secure in principle
* Asymmetric is:
  * slower
  * doesn't work well for multi-way confidentiality
  * Relies on mysterious math
* Asymmetric needs to securely distribute public key

## Compare and contrast: Encryption and hashing
Encryption
* Takes plain text and turns it into ciphertext using a key
* Is slow by design
* Requires key
* Is reversible
* Key distribution: key needs to be shared while remaining secret
  * Attackers can:
    - Guess the key
    - Steal the key
    - Ignore the key

Hashing
* Irreversibly maps arbitrary-length data into a unique, fixed-length code
* Is fast
* Does not require key
* Is irreversible

## Key distribution
* The problem of key distribution in symmetric encryption is that the key has to be given in some form or anther to the user. If the transfer is unsecure, the users data could become compromised and could possibly compromise the data of others
* With Asymmetric encryption the key is already public knowledge. The user has their own private key that only they can use to decode the data

## Hashing function requirements and use cases
Hashing passwords before storing them in a database
* Hashing is used to ensure that is a databased is compromised, passwords are still secure for the time being
* Relies on irreversible and collision resistant hashes to ensure integrity and confidentiality

Hashing files/messages to ensure they haven't been tampered with
* Hashing ensures integrity of files because if a file is modified in any way it completely changes the outputted hash
* Relies on irreversible and collision resistant hashes to

## MACs
MAC: Message authentication code
* Ensures integrity (not confidentiality)
* To create a MAC
  1. Hash the message
  1. encrypt the hash
  1. Attack it to the message
* To check a MAC
  1. Hash the message
  1. Decrypt the MAC
  1. Compare

## Digital Signatures
A MAC, but with asymmetric encryption
* Ensures both integrity and authenticity (but not confidentiality)

## Public Key Certificates
Required for HTTPS websites
* Resolves fraudulent public keys
* Certificate authority: A trusted entity that manages and issues security certificates and public keys that are used for secure communication
* Server generates a certificate by generating a hash of the unsigned certificate, encrypts that hash code with CA's private key to form signature
* Client verifies certificate by decrypting signature with CA's public key to recover hash code

# Access Control
## Terms
Authentication: You are who you say you are
Authorization: You're allowed to do what you're trying to do
