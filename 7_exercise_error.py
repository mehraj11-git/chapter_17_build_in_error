def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print('number must be in integer or floats')
        # print(err)
    except:
        print('unexpected error')
    else:
        return result   


print(divide(10,7))
