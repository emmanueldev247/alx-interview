#!/usr/bin/python3
"""
Main file for testing
"""
import time

start_time = time.time()

isWinner = __import__('0-prime_game').isWinner

nums = [0] * 10000
for i in range(10000):
    nums[i] = i

print("Winner: {}".format(isWinner(10000, nums)))

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
