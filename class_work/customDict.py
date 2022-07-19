class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of bounds")
        return super().__getitem__(index - 1)

    def __setitem__(self, index, value):
        pass

        if index <= 0:
            raise IndexError("index out of bounds")

        return super().__setitem__(index -1, value)



a = CustomList()
a.append(10)
a.append(20)
a.append(30)
print(a)
a[1] = 50
print(a)







