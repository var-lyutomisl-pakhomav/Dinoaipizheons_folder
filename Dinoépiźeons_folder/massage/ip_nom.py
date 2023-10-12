# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:13:31 2023

@author: user
"""

import socket
import random
from flask import Flask

app = Flask(__name__)
@app.route("/")

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        elif char.isdigit():
            encrypted_char = chr(((ord(char) - ord('0') + key) % 10) + ord('0'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            elif char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        elif char.isdigit():
            decrypted_char = chr(((ord(char) - ord('0') - key) % 10) + ord('0'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

letter_list_fr = "nabcdefghijklmopqrstuvwxyz"
letter_list_sd = "aeiouywlrn"

def room_num_codetor(local_ip):
    key = ord(random.choice(letter_list_fr + letter_list_sd))
    ip_unencrypt = ""
    
    numbers = local_ip.split(".")
    for number in numbers:
        if len(number) == 1:
            vol_ip = "00" + number
        elif len(number) == 2:
            vol_ip = "0" + number
        else:
            vol_ip = number
        
        num1 = vol_ip[0:2]
        nom1 = letter_list_fr[int(num1)]
        num2 = vol_ip[2:3]
        nom2 = letter_list_sd[int(num2)]
        nom = nom1 + nom2
        
        ip_unencrypt += nom

    ip_encrypt = encrypt(ip_unencrypt, key) + chr(key)
    return ip_encrypt

def room_num_decode(ip_encrypt):
    key = ord(ip_encrypt[8:9])
    ip_unencrypt = ""
    ip_encrypt = decrypt(ip_encrypt, key)
    
    for i in range(1, 8, 2):
        num1 = str(letter_list_fr.find(ip_encrypt[(i-1):i]))
        num2 = str(letter_list_sd.find(ip_encrypt[i:(i+1)]))
        if num1 == "0":
            num1 = ""
        nom = num1 + num2
        
        ip_unencrypt += "." + nom
    
    ip_unencrypt = ip_unencrypt[1:]
    return ip_unencrypt

recieve_massage = "0"

if recieve_massage == "0":
    resend_massage = room_num_codetor(local_ip) #加密IP輸出
else :
    resend_massage = room_num_decode(recieve_massage) #輸入以解密IP

print(resend_massage)
