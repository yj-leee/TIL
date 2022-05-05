n = 10000

natural_num = set(range(1, 10001))    
generate_num = set()

for i in range(1, n + 1):
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_number = sorted(natural_num-generate_num)

for number in self_number:
    print(number)
