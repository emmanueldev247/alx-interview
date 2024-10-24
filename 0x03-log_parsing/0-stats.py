#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import re
import signal
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

    """
    print(f'File size: {total_size}')
    for key, value in dict(sorted(status_code_count.items())).items():
        print(f'{key}: {value}')
    """


def handle_sigint(signal, frame):
    """
      Function to handle signt sgnal (CTRL + C)
      Arguments:
          signal: signal
          frame: frame where the signal was sent from
      Return: None
    """
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

# Entry point
# possible status code
cache = {
    '200':0, '301':0,
    '400':0, '401':0,
    '403':0, '404':0,
    '405':0, '500':0
}

total_size = 0
log_pattern = r'\S+ \- \[.*?\] \".*?\" (\d{3}) (\d+)'
buffer_count = 0

try:
    for line in sys.stdin:
        log = line.strip()
        if re.fullmatch(log_pattern, log):
            buffer_count += 1

            total_size += int(log.split()[8])
            status_code = log.split()[7]

        if status_code in cache.keys():
            cache[status_code] += 1

        if buffer_count == 10:
            buffer_count = 0
            statistics()
except Exception:
    pass

finally:
    statistics()
