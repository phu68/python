

## CHUONG TRINH TINH CAN CHI THEO NAM

namsinh = int(input("Nhap nam sinh: "))

lsCan = ["Giap", "At", "Binh", "Dinh", "Mau", "Ky", "Canh", "Tan", "Nham", "Quy"]
lsChi = ["Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui", "Than", "Dau", "Tuat", "Hoi"]

# luachon = int(input("Nhap lua chon"))

def tinhsodu(sochia,sobichia):
	ketqua = sochia - int((sochia/sobichia))*sobichia
	return ketqua
	pass


def tinhcan(namsinh):
	socan = tinhsodu(namsinh,10)
	return socan

def tinhchi(namsinh):
	sochi = tinhsodu(namsinh,12)
	return sochi

def tinhcanchi(namsinh):
	lsCan = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
	lsChi = ["Than", "Dau", "Tuat", "Hoi", "Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui"]
	can = tinhcan(namsinh)
	chi = tinhchi(namsinh)
	# print(tinhsodu(namsinh,10))
	# print(tinhsodu(namsinh,12))
	print("Can Chi Nam " + str(namsinh) + " la " + str(lsCan[can]) + " " + str(lsChi[chi]))


tinhcanchi(namsinh)