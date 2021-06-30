
>코드업 [기초-종합] 빛 섞어 색 만들기(설명)(py)

`
a, b, c=input().split()  
r = int(a)  
g = int(b)  
b = int(c)  

count = 0  

for i in range(r):  
    for j in range(g):  
        for k in range(b):  
            print("{} {} {}".format(i, j, k))  
            count += 1  
print(count)  
`
