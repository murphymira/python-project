number = 1
while number < 11:
    if number == 5:
        break
    print(number)
    number += 1
else:
    print("All went well")


n = 1221
n = str(n)
print(n == n[::-11])
