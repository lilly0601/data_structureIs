lst = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]

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
