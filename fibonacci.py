
def funcFibo(i):
	if i < 0:
		return -1
	elif i ==0 or i == 1:
		return i
	else:
		return funcFibo(i-1) + funcFibo(i-2)
i = 0
while i < 20:
	print(funcFibo(i),end="\t")
	i+=1



