#!/usr/bin/python3

import sys
import numpy as np

if len(sys.argv) == 3:
	print(list(np.arange(int(sys.argv[1]), int(sys.argv[2]) + 1)))
else:
	print("None")
