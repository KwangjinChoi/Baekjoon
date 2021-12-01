import sys
import numpy as np
N = int(input())
cnt = 0
for _ in range(N):
    string = sys.stdin.readline()
    for i in string:
        tmp = np.where(string == i)
        