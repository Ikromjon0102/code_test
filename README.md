Problem: Katta-kichik
Your Code:
a,b = input().split()
a,b = int(a), int(b)
if a == b:
  print('=')
elif a<b:
  print('>')
else:
  print('>')
Result: All tests 52 -> ❌ Error - 21 | ✅ Success - 31
Input: 0 0
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 34 43
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -34 -43
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 123 123
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: -50 -50
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 999 -999
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -1000 1000
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 1000000 999999
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -2000000000 2000000000
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 45 45
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: -56 -56
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 89 88
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -12 -13
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 74 74
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 67 68
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -99 -98
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 43 42
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -17 17
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 50 -50
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -50 50
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 23 23
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 1 2
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -1 -2
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 0 1
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 0 -1
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -1 0
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 1 0
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 78 78
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: -89 -90
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -90 -89
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 33 32
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 21 22
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 45 46
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -45 -44
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -44 -45
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 55 55
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: -100 100
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 100 -100
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -101 101
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 101 -101
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 75 75
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: -76 -75
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -75 -76
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 88 87
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 65 66
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: 77 76
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -78 -77
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -77 -78
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: 92 92
Expected: =
Output: =
Success: ✅ Success
------------------------------
Input: 13 14
Expected: <
Output: >
Success: ❌ Error
------------------------------
Input: -15 -16
Expected: >
Output: >
Success: ✅ Success
------------------------------
Input: -16 -15
Expected: <
Output: >
Success: ❌ Error
------------------------------
Total Success: 31
Total Errors: 21
