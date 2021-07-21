
import datetime
now = datetime.datetime.now()

ten = input("Nhap ten: ")
tuoi = input("Nhap tuoi hien tai: ")

tuoi = int(tuoi)


def namsinh(tuoi):
	return now.year - tuoi
	pass

namtuonglai = input("Nam tuong lai muon tinh tuoi: ")

namtuonglai = int(namtuonglai)

tuoituonglai = namtuonglai - namsinh(tuoi)

print("Nam " + str(namtuonglai) + " tuoi cua ban la " + str(tuoituonglai))