http_status = 501

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad requet')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else:
    print('Unknown')

match http_status:
    case 200 | 201: #case replaces the statement "if", the pipe command is short-hand for "or"
        print('Success')
    case 400:
        print('Bad Request')
    case 500 | 501:
        print('Server Error')
    case _: #equivalent of "else"
        print('Unknown')