n = 10000
number = set(range(n))

generate_number = set()
a = 0
for i in range(1, n + 1):
    a = 0
    for j in str(i):
        a += int(j)
    b = i + a
    generate_number.add(b)
    


self_number =  number - generate_number
s = sorted(self_number)
for i in s:
    print(i)
    