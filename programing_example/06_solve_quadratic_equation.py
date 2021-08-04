# chương trình tìm nghiệm của phương trình bậc 3 với các hệ số a, b, c

#input

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# output
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / 2 * a


import cmath

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# tính số phân biệt
d = (b**2) - (4*a*c)

# tính kết quả
sol1 = (-b - cmath.sqrt(d))/(2*a)
sol2 = (-b + cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
