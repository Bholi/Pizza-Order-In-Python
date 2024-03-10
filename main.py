small = 15
medium = 20
large = 25
pepSmall = 2
pepBig = 3
cheese = 1
totalBill = 0

print('Welcome to Pizza Order System ! ')
size = input('Enter the size of pizza "S","M" or "L" : ')
add_peproni = input('Do you want to add some peproni ? "Y" or "N":  ')
add_cheese = input('Do you want to add some cheese ? "Y" or "N" : ')

if size == 'S':
    totalBill = small
    if add_peproni == 'Y':
        totalBill += pepSmall
    if add_cheese == 'Y':
        totalBill += cheese
    print(f'The total bill is ${totalBill}')
if size == 'M':
    totalBill = medium
    if add_peproni == 'Y':
        totalBill += pepBig
    if add_cheese == 'Y':
        totalBill += cheese
    print(f'The total bill is ${totalBill}')

if size == 'L':
    totalBill = large
    if add_peproni == 'Y':
        totalBill += pepBig
    if add_cheese == 'Y':
        totalBill += cheese
    print(f'The total bill is ${totalBill}')