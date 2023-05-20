import random
import math


# Horner's algorithm for calculation of the polynomial in O(n) time
def horner(x, coeff, q):
    answer = 0
    for i in coeff:
        if i == '?':
            answer = (answer * x) % q  # ? is taken as zero
        else:
            answer = (answer * x + ord(i) - 65) % q
    return answer


# A power function which returns power % q while doing q bit operations at each step
def powq(x, m, q):
    ans = 1
    while m > 0:
        if m % 2 == 0:
            x = (x * x) % q
            m = m / 2
        else:
            ans = (ans * x) % q
            m = m - 1
    return ans


# To generate random prime less than N
def randPrime(N):
    primes = []
    for q in range(2, N + 1):
        if (isPrime(q)):
            primes.append(q)
    return primes[random.randint(0, len(primes) - 1)]


# To check if a number is prime
def isPrime(q):
    if (q > 1):
        for i in range(2, int(math.sqrt(q)) + 1):
            if (q % i == 0):
                return False
        return True
    else:
        return False


# pattern matching
def randPatternMatch(eps, p, x):
    N = findN(eps, len(p))
    q = randPrime(N)
    return modPatternMatch(q, p, x)


# pattern matching with wildcard
def randPatternMatchWildcard(eps, p, x):
    N = findN(eps, len(p))
    q = randPrime(N)
    return modPatternMatchWildcard(q, p, x)


# return appropriate N that satisfies the error bounds
def findN(eps, m):
    """
    Let f(p) mod q = s and f(x[i...(i+m-1)]) mod q = t
    Then s=t when (f(p)-f(x[i…(i+m-1)])) mod q = 0
    Thus q is a factor of f(p)- f(x[i…(i+m-1)])
    Maximum value of f(p)-f(x[i…(i+m-1)]) is 26**(m) – 1 and number of prime factors of 26**(m)-1 <= log(26**m)=mlog26 [Claim 1]
    Probability that s=t but f(p)!= f(x[i…(i+m-1)]) is thus mlog26/pi(N)<=eps, where pi(N) is the number of prime numbers <= N
    Using claim 2 we get the inequality
    N/logN >= 2*log26*(m/eps)
    Now, we use the following method to find N

    """
    y = m / eps * 2 * math.log(26, 2)
    if y == 0:
        return
    # y is greater than e
    # N/logN is increasing when N>e
    # Lets try using binary search to obtain the value of N
    f = lambda x: x / math.log(x, 2)
    Nmin = 3
    Nmax = int(y ** 2)  # As f(y**2)>y
    while Nmax - Nmin != 1:
        mid = int((Nmax + Nmin) / 2)
        if f(mid) > y:
            Nmax = mid
        else:
            Nmin = mid
    return Nmax
    '''
     Complexity of this function is O(2logy)=O(log(m/eps))
     This doesn't hamper the complexity bounds for the randPatternMatch mentioned in the assignment statement
     But, if we want this to run in O(1) time then we can choose N as int(kylogy) where k is a constant >1, eg. k=2. 
     However, the above algorithm provides a tighter bound for N. 
    '''


# Return sorted list of starting indices where p matches x
def modPatternMatch(q, p, x):
    if x == "":
        return []
    m = len(p)
    n = len(x)
    # Hash value for the pattern
    pattern_hash = horner(26, p, q)
    alpha = powq(26, (m - 1), q)  # Useful to store this otherwise complexity goes to O(mn)
    temp = horner(26, x[0: m], q)  # The first substring
    answers = []
    for i in range(n - m):
        if temp == pattern_hash:
            answers.append(i)
        temp = ((((temp - (ord(x[i]) - 65) * alpha) * 26) % q) + ord(x[i + m]) - 65) % q  # Shift to the next substring
    if temp == pattern_hash:
        answers.append(n - m)  # Check the last substring
    return answers


# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q, p, x):
    if x == "":
        return []
    # Two trivial cases:
    if p[0] == '?':
        return modPatternMatch(q, p[1:], x[1:])
    elif p[-1] == '?':
        return modPatternMatch(q, p[0:-1], x[0:-1])
    else:
        ques = p.find('?')  # index of question mark
        m = len(p)
        n = len(x)
        pattern_hash = horner(26, p, q)
        alpha = powq(26, (m - 1), q)  # Useful to store these otherwise complexity goes to O(mn)
        beta = powq(26, (m - ques - 2), q)
        temp = (horner(26, x[0: m], q) - 26 * beta * (
                ord(x[ques]) - 65)) % q  # The first substring, after removing character corresponding to ?
        answers = []
        for i in range(n - m):
            if temp == pattern_hash:
                answers.append(i)
            # Shift to the next substring, keeping in mind the shift corresponding to ?
            temp = ((((temp - (ord(x[i]) - 65) * alpha - (ord(x[i + ques + 1]) - 65) * beta + (
                    ord(x[i + ques]) - 65) * 26 * beta) * 26) % q) + ord(x[i + m]) - 65) % q
        if temp == pattern_hash:
            answers.append(n - m)  # Check the last substring
        return answers


# import time
#
# #
# t = time.time()
# print(modPatternMatch(1000000007, "CD", "ABCDE"))
# print(modPatternMatch(1000000007, "AA", "AAAAA"))
# print(modPatternMatch(2, 'AA', 'ACEGI'))
# print(modPatternMatchWildcard(1000000007, 'D?F', 'ABCDE'))
# print(modPatternMatchWildcard(1000000007, "D?", 'ABCDE'))
# print(modPatternMatch(1000000007, "", ""))
# print("Time", time.time() - t)
