#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import sys


def statistics():
    """
      Function to display the statistics from the log parser
      Arguments: None
      Return: None
    """
    print(f'File size: {total_size}')
    for key, value in sorted(cache.items()):
        if value != 0:
            print(f'{key}: {value}')


# Entry point
# possible status code
cache = {
    '200': 0, '301': 0,
    '400': 0, '401': 0,
    '403': 0, '404': 0,
    '405': 0, '500': 0
}

total_size = 0
buffer_count = 0

try:
    for line in sys.stdin:
        try:
            log = line.split()
            total_size += int(log[-1])
            status_code = log[-2]
            if status_code in cache.keys():
                cache[status_code] += 1
        except:
            pass
        buffer_count += 1
        if buffer_count == 10:
            buffer_count = 0
            statistics()
except Exception:
    pass

finally:
    statistics()
