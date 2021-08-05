
```
s = input()

result = s[0]
for i in range(1, len(s)):
    if int(result) * int(s[i]) > int(result) + int(s[i]):
        result = result * int(s[i])
    else:
        result = int(result) + int(s[i])
print(result)

```
