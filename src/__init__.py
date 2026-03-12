"""
Just a whole bunch of random functions made by me!

I'll find out how to organize this better but for
now I'll just put everything here.
"""

# Standard imports
import math

def prime_numbers_up_to(n: int) -> list[int]:
    """
    Finds and returns every prime number up to any value, n.

    Parameters:
    `n: int` Up to value (exclusive). !MUST BE GREATER THAN 1 OR AN
    EMPTY LIST IS RETURNED!

    Returns:
    `primes: list[int]` List of every prime number up to param `n`.

    Example:
    >>> print(prime_numbers_up_to(20))
    [1, 2, 3, 5, 7, 11, 13, 17, 19]
    """

    # The value should be no less than 1
    n = max(1, n)

    # The list of prime numbers up to n.
    primes: list[int] = []

    # Find if every number from 1 to n - 1 is divisible
    # by a number in primes. If so, add it to primes.
    for i in range(1, n):
        if primes:
            is_prime = True
            for prime in primes:
                if i % prime == 0 and prime != 1:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        else:
            primes.append(i)

    return primes


def subfactorial(n: int) -> float:
    """
    Finds the subfactorial of a number, n.
    A subfactorial is the number of permutations of a number, n,
    objects where no objects are in their original location
    (derangements). It is calculated by using this formula:
             n
    !n = n!( Σ ((-1)^k/k!))
            k=0

    Parameters:
    `n: int` Number to find the factorial of. !MUST BE A
    POSITIVE INTEGER OR ELSE IT RAISES A ValueError!

    Returns:
    `subf: float` The subfactorial of n.

    Example:
    >>> print(subfactorial(5))
    44.0
    """

    # The subfactorial of n.
    subf: float = 0.0

    # Find the summation of n!((-1)^k/k!), where k is a sequence from 0 to n.
    for k in range(n + 1):
        # Because exponentiating -1 by any number gives itself, this
        # is necessary.
        neg_value = -1
        if k % 2 == 0:
            neg_value *= neg_value
        sigma_value = math.factorial(n)*(neg_value / math.factorial(k))
        subf += sigma_value
    
    return subf
