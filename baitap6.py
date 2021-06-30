#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.

soA = float(input("nhap so thap phan A: "))

so_can_lam_tron = int(input("nhap so can lam tron: "))


# print(round(soA,so_can_lam_tron))

print("{0}.{1}.format(soA,so_can_lam_tron)")