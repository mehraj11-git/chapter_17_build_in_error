def func(a,b):
    return a+b
print(func(2,3))  #1
print(func('2','3'))  #2


# if i print 1 it will give 5
# if i print 2 it will give 23 bcz its  a string 
# and if i raise an error simple i will write the raise instead of the return
# you can raise any error but you should select the one which is suits your code condition
# here i used type error
def add(a,b):
    if type(a)==int and type(b)==int:
        return a+b
    raise TypeError ("opps you are passing a wrong data type ")
print(add('2','3'))
print(add(2,3))     