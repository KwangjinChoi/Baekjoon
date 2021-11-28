import sys

dict = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    input = sys.stdin.readline().split('\n')[0]
    if input == '#':
        break
    res = 0
    for i in range(len(input)):
        res += dict[input[i]]*(8**(len(input)-i-1))
    print(res)
    