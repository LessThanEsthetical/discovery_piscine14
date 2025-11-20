#!/usr/bin/python3

import sys
print("\n".join(sys.argv[1:][::-1])) if int(len(sys.argv)) > 2 else print("None")
