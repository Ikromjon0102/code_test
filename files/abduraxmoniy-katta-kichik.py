def taqqoslash(son1, son2):
    if son1 > son2:
        print(">")
    elif son1 < son2:
        print("<")
    elif son1 == son2:
        print("=")
son1, son2 = input(":").split()
taqqoslash(son1, son2)