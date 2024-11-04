# # in this chapter we gonna learn about:
# # built in error
# # exception ,how to handle them 
# # raise our errors, debugging , etc.... 

# # types of error :-

# # SyntaxError 
# # for ex you define a func but you forget to put paranthesis( )
#  def func:
#     pass
# name = "mehraj"*

# # indentation error 
# # its means that space error 
# # this is intendation error look at 1 and 2
# def func():
#   print('mehraj') #1
# print('khan') #2

# # name error 
# # if you didnt define the name variable but you print it 
# # it will raise the name error
#  print(name)

# # TypeError 
# # suppose if you add integar with string
# # this will raise the type error 
# # but you can use multiply there 
# print(5+'mehraj')

# # index error
# # if you call the index position which is not available on that list 
# # this will raise the error
# l = [1,2,4]
# print(l[4])

# # value error
# # this error will raise when you put the correct the data perhaps the wrong the value
# # abc is not a number but we try to convert it with int method 
# # if i put numbers and try to use the int method, its work
# s  = 'abc'
# print(int(s))

# # attribute error
# # for ex if you use such func or method which isnot predefine method 
# # there is no push method
# l = [1,2,3]
# l.push(20)

# # KeyError
# # suppose if you dict and yu dont have the age key in that key
# # this will raise error 
# d = {"name":"mehraj"}
# print(d['age'])

