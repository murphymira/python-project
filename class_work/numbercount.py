numbers=1
while numbers <= 100 :

    if numbers % 15 == 0:
        print("FIZZBUZZ")
    elif numbers % 5 == 0:
        print("BUZZ")
    elif numbers % 3 == 0:
        print("FIZZ")
    else:
        print(numbers)
    numbers+= 1

