#TViết chương trình tính và hiển thị ra màn hình tổng hai số nguyên được nhập bất kỳ từ bàn phím (Có xử lý ngoại lệ đầu vào).


num1 = input("Nhap so thu 1: ")
num2 = input("Nhap so thu 2: ")


def tinhtong(num1,num2):
	return num1 + num2


try:
	num1 = int(num1)
	num2 = int(num2)
	print(tinhtong(num1,num2))
except Exception as e:
	print("co loi trong nhap lieu")
else:
	pass
finally:
	pass