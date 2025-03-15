def xyz(s):
    a, b, c = map(int, s.split())

    a, b, c = sorted([a, b, c])

    if (a + b + c) % 3 != 0:
        return -1

    return (c - a) // 2 + (c - b) // 2

print(xyz("3 5 2"))
print(xyz("4 4 4"))
print(xyz("2 4 6"))