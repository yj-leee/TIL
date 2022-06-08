
reguler_number =  set(range(1, 10001))

generate_number = set([])
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generate_number.add(i)

self_number = sorted(reguler_number - generate_number)
for i in self_number:
    print(i)

