# tìm giai thừa của một số

num = int(input("Input number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i

print("Factorial {} is {}".format(num, factorial))