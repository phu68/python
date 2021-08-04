a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

# max = a
# if a < b:
#     if b > c:
#         max = b
#     elif a < c:
#         max = c
# elif a < c:
    # max = c
# print('Max is ',max)

if (a > b) and (a > c):
    print("Max is ", a)
elif (b > a) and (b > c):
    print("Max is ", b)
else:
    print("Max is ",c)