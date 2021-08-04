# swap 2 biến sử dụng biến tạm & không sử dụng biến tạm

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))


a, b, c = b, c, a

print('Gia gia a {}'.format(a))
print('Gia gia b {}'.format(b))
print('Gia gia c {}'.format(c))

