lst= []
for i in range (1,10):
    lst.append(i)
    print (i)

lst= []
for i in range(1,10):
    if i%2!=0:
        lst.append (i)
        print (i)


lst= []
for i in range (65,91):
    lst.append(chr(i))
print (lst)


lst_ = [chr(i) for i in range(65, 91)]
print(lst_)


add = lambda x, y: x + y
sub = lambda x, y: x - y
print (add.__name__)
print (sub.__name__)

def add (a, b):
    return a + b

def sub (c, d):
    return d - c
def mult (e, f):
    return f(e)

def operate(x, y, fn):
    return fn(x, y)

val_sub = operate (5, 24, sub)
val_add = operate (5, 24, add)
# val_mult = operate (5, 24, mult)
print(val_add)
print(val_sub)
# print(val_mult)



val_sub = operate (5, 24, sub)
val_add = operate (5, 24, add)
val_divide = operate (5, 24, lambda x, y: y / x)
print(val_add)
print(val_sub)


def double(x, fn):
    return fn(x * x)

double = mult(3, lambda x: x * x)

print(double)





# # peoples = [
#     {"name:"Omosetan Omorele", "age": 30, "years_of_exp": 4, "language":["python", "java"]}
#     {"name:"JOHN DOE Omorele", "age": 25, "years_of_exp": 2, "language":["javascript", "c#"]}
#     {"name:"AMAMKA  STEPHEN", "age": 15, "years_of_exp": 4, "language":["python", "java"]}


map_object = map(lambda x: x**2, range(1, 10))
lst1 = list(map_object)
lst2 = list(map_object)
print ("1", lst1)
print("2",lst2)


from functools import reduce
fruits = ["Apple", "Pear", "Pineapples", "Banana","Cucumber", "Orange", ]
longest = reduce (lambda x, y: x if len(x) > len(y) else y, fruits)
print(longest)
print(max(fruits,key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))

def myfunc():
    global x
        x = "fantastic"













