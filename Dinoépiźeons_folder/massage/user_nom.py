import socket
import random

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

def la17_hux(input_str):
    numbers = input_str.split(".")
    hex17_list = []
    base17_chars01 = "bcdfghjklmnpqrstvwxz"  # 用于个位的字符集
    base17_chars10 = "àâèêôûùüÿåäö"         # 用于十位的字符集

    for number in numbers:
        decimal_number = int(number)
        hex17_value = ""
        is_ten_digit = False  # 用于标记当前处理的是个位还是十位
        while decimal_number > 0:
            remainder = decimal_number % 20
            if is_ten_digit:
                hex17_digit = base17_chars10[remainder]
            else:
                hex17_digit = base17_chars01[remainder]
            hex17_value = hex17_digit + hex17_value
            decimal_number //= 20
            is_ten_digit = not is_ten_digit  # 切换到下一个位
        hex17_list.append(hex17_value)
    
    return hex17_list

hux17_ip = la17_hux(local_ip)

vowels = "aeiou"
separator = random.choice(vowels)
result_str = separator.join(hux17_ip)
str20_ip = result_str.upper()

def user_name(text):
    text = text.replace("à", "a")
    text = text.replace("â", "ao")
    text = text.replace("è", "e")
    text = text.replace("ê", "eu")
    text = text.replace("ù", "u")
    text = text.replace("ü", "eu")
    text = text.replace("ÿ", "y")
    text = text.replace("q", "qu")
    return text

name = user_name(result_str)
name = name.upper()
print(name)
