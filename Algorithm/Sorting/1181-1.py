n = int(input())

word = dict()
for i in range(n):
    word[len(i)].append(i)
    word[len(i)].sort()
    

    

for i in range(0, 50):
    if word[i]:
        for j in word[i]:
            print(j)
