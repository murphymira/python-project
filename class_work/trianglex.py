for i in range(1, 11, 1):
    print('*' * i)

for i in range(10, 0, -1):
    print('*' * i)

star = "*"
for i in range (1,11):
    print(f"{star * i:<10}  { star *(11-1):>10}  {star * i:>10}")