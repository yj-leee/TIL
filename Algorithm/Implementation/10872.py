n = int(input())

"""
0 = 1
1 = 1
2 = 2 X 1
3 = 3 X 2 X 1 

n! = (n - 1)! X n
"""

memo = [1]
for i in range(1, n + 1):
    memo.append(memo[i - 1] * i)
    
print(memo[n])


def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))