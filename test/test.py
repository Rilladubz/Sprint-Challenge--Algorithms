def test(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            print(j)
            sum += 1
    return sum


print(test(80))
