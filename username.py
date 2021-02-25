count = 0
while True:
    if count == 3:
        print('exceeded maximum number of attempts')
        break

    name = input('Enter your username: ')
    password = input('Enter a password: ')
    if name == 'Michael' and password == 'password':
        print('Access Granted')
        break

    else:
        print('error...try again')
        count += 1