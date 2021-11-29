str = input().strip()
if not str:
    print(0)
else:
    print(len(str.split(' ')))