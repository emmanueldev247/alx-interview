#!/usr/bin/python3
import time

start_time = time.time()

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 4, 3])))

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
