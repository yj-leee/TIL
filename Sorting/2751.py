import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
print(num)

num.sort()

for i in num:
    print(i)
