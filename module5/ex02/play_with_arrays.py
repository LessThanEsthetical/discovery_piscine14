#!/usr/bin/python3

import numpy as np
import random

rng = np.random.default_rng()
arr1 = np.array(rng.integers(low=-100, high=100, size=random.randrange(1, 10)))

arr2 = np.copy(arr1)
arr2 = np.where(arr2 > 5, arr2 + 2, arr2)
arr2 = np.extract(arr2 > 5, arr2)

print(list(arr1), list(arr2), sep="\n")
