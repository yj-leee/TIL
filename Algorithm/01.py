n = int(input())
print(-1 if n == 4 or n == 7 else n//5 + n%5//3 + n%5%3)