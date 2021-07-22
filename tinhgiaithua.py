def giaithua(n):
	if n < 2:
		return 1
	else:
		return n * giaithua(n-1)

num = int(input("Nhap so can tinh giai thua: "))
print(giaithua(num))