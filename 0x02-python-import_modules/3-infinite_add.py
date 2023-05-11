#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0")
else:
    result = 0
    for arg in sys.argv[1:]:
        result += int(arg)
    print(result)