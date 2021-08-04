
# Python Program to Find the Square Root || tìm căn bậc 2

# Find square root of real or complex numbers
# Importing the complex math module
import cmath

# num = 1+2j

# To take input from the user
num = eval(input('Enter a number: ')) # eval để tính số thực có dạng (a + bj)

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))


# num_sqrt.real = phần thực
# num_sqrt.imag = phần ảo

'''
Trong chương trình này, chúng tôi sử dụng hàm sqrt () trong mô-đun cmath (toán phức hợp).
'''

'''
Phương thức eval() có thể được sử dụng để chuyển đổi các số phức 
làm đầu vào cho các đối tượng phức tạp trong Python. 
'''
