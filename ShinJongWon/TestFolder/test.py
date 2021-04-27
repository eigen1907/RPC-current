import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import random as rd


x = np.zeros([10000])
t = np.zeros([10000])

for i in range(10000):
    x[i] = rd.uniform(0, 10)
    t[i] = rd.uniform(0, 10)
z = np.sin(x + t)


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

plt.plot(x, t, z, ".")
plt.show()