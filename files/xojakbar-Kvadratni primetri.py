
A = 5
B = 1
list = [1,2,3,]

try:
    print(a / b)
    print(list[0])
    print(1 + 'ikki')


except ZeroDivisionError:
    print('Nolga bo\'lish mumkin emas')
except IndexErrorError:
    print('siz bergan index elementi mavjud emas')

except (Exception, IndexError, TypeError) as e:
except BaseException as e:
    print(e)