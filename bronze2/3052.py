import sys
# from collections import Counter
# list = []
# for _ in range(10):
#     list.append(int(sys.stdin.readline())%42)
# print(len(Counter(list)))
s = set()
for _ in range(10):
    s.add(int(input())%42)
print(len(s))