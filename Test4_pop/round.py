def Round(x):
    if x+0.5 // 1 > x // 1:
        x = x+0.5
    x = x // 1
    return int(x)