
while True:
    try:
       age = int(input('enter your age : '))
       break
    except ValueError:
        print('you entered a string instead of number ,try again')
    except:
        print('unexpected error...')
     
if age <18:
    print('you can\'t play the game')
else:
    print('you can play this game')
       


# this code is correct 
# what if i enter the age in alphabets for instance 
# if i enter seven isntead of 7
# this is will raise error
# to avoid such mistakes we use try and exceptio method
# for that you guess in which line the error will occur 
# now we use infinite loop (while True)
# we have to break it otherwise it gonna run ,cant stop
# our main aim is to raise the error for that we will use the value error