a, b = input().split()
a, b = int(a), int(b)
result = ''
for i in range(1, b+1):
    result += str(a) + ' '
print(result.strip())
