#!/usr/bin/python3

import numpy as np
import random

rng = np.random.default_rng()
arr1 = np.array(rng.integers(low=-100, high=100, size=random.randrange(1, 10)))

arr2 = np.copy(arr1) + 2

print(f"{list(arr1)}\n{list(arr2)}")
