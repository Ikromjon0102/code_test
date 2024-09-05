# Ikkita butun sonni kirish
A, B = map(int, input().split())

# Taqqoslash va natijani chop etish
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("=")
