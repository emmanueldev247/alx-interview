#!/usr/bin/python3
"""
Main file for testing
"""
import time

start_time = time.time()
isWinner = __import__('0-prime_game').isWinner

nums = [0] * 100
for i in range(100):
    nums[i] = i * i

print("Winner: {}".format(isWinner(100, nums)))

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
