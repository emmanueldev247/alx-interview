#!/usr/bin/python3
"""N Queens"""

import sys

if len(sys.argv) !=  2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except Exception:
        print("N must be a number")
        sys.exit(1)


queens
