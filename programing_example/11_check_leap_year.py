# Một năm nhuận chính xác là chia hết cho 4 
# ngoại trừ năm thế kỷ (năm kết thúc bằng 00). 
# Năm thế kỷ chỉ là năm nhuận nếu nó chia hết cho 400.

year =  int(input("Input year (19xx - 20xx): "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is leap year".format(year))
        else:
            print("{0} is not leap year".format(year))
    else:
        print("{0} is  leap year".format(year))
else:
    print("{0} is not leap year".format(year))
