# chương trình chuyển đổi km -> dặm

# conversion factor
conv_fac = 0.621371

kilometers = float(input("Input kilometers: "))

# tính ra dặm
miles = kilometers * conv_fac

print("%0.2f kilimeters is equal  to %0.2f miles" %(kilometers, miles))