n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = b.copy()

a.sort()
c.sort(reverse=True)

result = 0
for i in range(n):
    result += a[i] * c[i]
    
print(result)


