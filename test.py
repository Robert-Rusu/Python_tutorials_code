def approx_equals(a, b):
    val = False
    c = a - b
    if abs(c)<= 0.001:
        val = True
        print(val)
    else:
        print(val)


approx_equals(4.6262, 4.6270)


a = 4.333
round(a, 3)
print(a)