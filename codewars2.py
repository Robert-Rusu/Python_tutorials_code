def get_sum(a, b):
    result = 0
    while a <= b:
        print(a)
        result = result + a
        a += 1
    print(result)


get_sum(1,4)