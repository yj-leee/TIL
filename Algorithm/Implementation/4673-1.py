""" set 자료구조 """

n = 10000

original_number = set([])

for i in range(1, n+1):
    original_number.add(i) 
    
generate_number = set([])

sum_number = 0
for i in range(1, n + 1):
    for j in range(str(i)):
        sum_number += int(j)
    if sum_number <= 10000:
        generate_number.add(sum_number)
        sum_number = 0

self_number = original_number-generate_number

for number in self_number:
    print(number)
