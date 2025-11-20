#!/usr/bin/python3

import numpy as np
import random

rng = np.random.default_rng()
arr = np.array(rng.integers(low=-100, high=100, size=random.randrange(1, 10)))

print(list(arr))
