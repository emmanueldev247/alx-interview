#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that
    number and its multiples from the set. The player that cannot make a move
    loses the game. They play x rounds of the game, where n may be different
    for each round. Assuming Maria always goes first and both players play
    optimally, determine who the winner of each game is.

    Args:
        x (int): number of rounds
        nums (list): an array of n
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if primes[i]:
            for j in range(i, max_num + 1, i):
                prime_count[j] += 1

    players = {'Maria': 0, 'Ben': 0}

    for n in nums:
        if prime_count[n] % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return "Maria"
    elif players['Ben'] > players['Maria']:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(limit):
    """Implements the Sieve of Eratosthenes algorithm to find
        prime numbers up to a given limit.

    Args:
        limit: The upper limit for finding prime numbers.

    Returns:
        A list of prime numbers up to the given limit.
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes
