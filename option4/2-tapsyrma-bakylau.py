lst = [3, 7, 11, 15]

if len(lst) < 3:
    print(True)
else:
    d = lst[1] - lst[0]
    ok = True
    for i in range(2, len(lst)):
        if lst[i] - lst[i-1] != d:
            ok = False
            break
    print(ok) 