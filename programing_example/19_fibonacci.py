# in dãy số fibonacci
# 1 1 2 3 5 8 13 21 34
nterms = int(input('Enter terms: '))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print('Please enter a positive interger')
elif nterms == 1:
    print('Fibonacci sequence upto', nterms, ':')
    print(n1)
else:
    print('Fibonacci sequence upto', nterms, ':')
    while count < nterms:
        print(n1, end ='\t')
        n_next = n1 + n2
        #update n1, n2
        n1 = n2
        n2 = n_next
        count += 1
