#!/usr/bin/python3
"""
Main file for testing
"""
import time

start_time = time.time()

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))


end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
