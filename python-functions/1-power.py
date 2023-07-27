def pow(a, b):
    if a == 0 and b < 0:
        raise ValueError("Cannot raise 0 to a negative power")

    result = 1

    if b < 0:
        a = 1 / a
        b = -b

    def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result