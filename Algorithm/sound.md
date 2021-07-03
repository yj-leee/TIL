>코드업 [기초-종합] 소리 파일 저장용량 계산하기(py)

```
a, b, c, d =input().split()

h = int(a)
b = int(b)
c = int(c)
s = int(d)

change = round((h * b * c * s)/8/1024/1024, 1)
print("{} {}".format(change, "MB"))
```
