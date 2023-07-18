def create_phone_number(n):
    #n = str(n)
    str1 = ""
    str2 = ""
    str3 = ""
    for i in range(0, len(n)):
        if 0 <= i < 3:
            str1 += str(n[i])
        elif 3 <= i < 6:
            str2 += str(n[i])
        else:
            str3 += str(n[i])
    print("(" + str1 + ") " + str2 + "-" + str3)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
