class  PasswordTooShort(ValueError):
    pass


def validate(password):
    if len(password) < 8:
        raise PasswordTooShort('password is too short')

username = input('enter your password : ')
name = input('enter your name : ')
validate(username)
print(f'Hello {name}!!!')