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
    for key, value in dict(sorted(status_code_count.items())).items():
        print(f'{key}: {value}')


def handle_sigint(signal, frame):
    """
      Function to handle signt sgnal (CTRL + C)
      Arguments:
          signal: signal
          frame: frame where the signal was sent from
      Return: None
    """
    statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

# Entry point
total_size = 0
status_code_count = {}
log_pattern = r'\S+ \- \[.*?\] \".*?\" (\d{3}) (\d+)'
buffer_count = 0
for line in sys.stdin:
    log = line.strip()
    if re.fullmatch(log_pattern, log):
        buffer_count += 1

        total_size += int(log.split()[8])
        status_code = log.split()[7]

        if status_code in status_code_count:
            status_code_count[status_code] += 1
        else:
            status_code_count[status_code] = 1

    if buffer_count == 10:
        statistics()
        buffer_count = 0
