a, b = map(int, input().split())
# gcd = 1
# lcm = 1
# i = 2
# while True:
#     if a%i==0 and b%i==0:
#         gcd *= i
#         lcm *= i
#         a //= i
#         b //= i
#         i = 2
#         continue
#     else:
#         if i > min(a, b):
#             lcm *= a
#             lcm *= b
#             break
#         i += 1
        
# print(gcd)
# print(lcm)
def gcd(a, b):
    if b != 0:
        return gcd(b, a%b)
    else:
        return a
def lcm(a, b):
    return (a * b)//gcd(a, b)
print(gcd(a, b))
print(lcm(a, b))