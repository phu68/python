#print all prime numbers in an interval
lower = 10
upper = 50

print("Danh sach so nguyen trong {} đến {}: ".format(lower, upper))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)