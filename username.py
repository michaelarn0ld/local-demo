count = 0
while True:
    if count == 3:
        print('exceeded maximum number of attempts')
        break

    name = input('Enter your username: ')
    if name == 'Michael':
        print('Access Granted')
        break

    else:
        print('error...try again')
        count += 1