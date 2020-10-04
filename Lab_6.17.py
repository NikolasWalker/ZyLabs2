
get_password = input() + 'q*s' #gets password from user and concatenates q*s
password = ''

for x in get_password:
    if x == 'i':
        password += '!'

    elif x == 'a':
        password += '@'

    elif x == 'm':
        password += 'M'

    elif x == 'B':
        password += '8'

    elif x == 'o':
        password += '.'
    else:
        password += x

print(password)

