#Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó ở hệ bát phân.

#xu ly ngoai le

try:
	so_thap_phan = int(input("nhap so thap phan: "))
	print("so thap phan %d trong he bat phan là %o" %(so_thap_phan,so_thap_phan))
except:
	print("nhap lieu ko hop le")