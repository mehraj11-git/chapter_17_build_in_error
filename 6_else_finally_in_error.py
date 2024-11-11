
while True:

    try:
      age = int(input('enter your age : '))
    except ValueError:
        print('you entered a string !!')
    except:
        print('unexpected error')   
    else:
        print(f'user input = {age}')
        break
    finally:
        print('finally block.....')




#  we can add statements in try method
# but this is not good to add too many statements in try method 
# for that we use else method        #  
# finally method will work whether the errors occur or not
# it will run
# think!!!! here the break loop works aftr the finally method