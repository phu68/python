# tính diện tích hình tam giác
# Heron's formula
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

canh1 = float(input('Nhập cạnh 1: '))
canh2 = float(input('Nhập cạnh 2: '))
canh3 = float(input('Nhập cạnh 3: '))

s = (canh1 + canh2 + canh3) / 2

dien_tich = (s * (s - canh1) * (s - canh2) * (s - canh3)) ** 0.5

print("Dien tích hình tam giác {0} {1} {2} là: {3} ".format(canh1, canh2, canh3, dien_tich))
# print("Dien tich hinh tam giac: %0.1f" %dien_tich)