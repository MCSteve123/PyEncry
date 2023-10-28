"""PyEncry的函数
   版本：v1.4

   对应程序：main.py"""

from hashlib import sha256 as sha

MODULE_VER = '1.4'

def encry(plaintext: str, key: int) -> str:  # 加密函数
    """加密字符串"""
    if plaintext == '':
        return ''

    """替换字符"""
    a = ''
    for i in plaintext:
        b = str(ord(i))
        for i in range(7 - len(b)):
            b = '0' + b
        a += b

    """乘以随机密钥"""
    a = str(int(a) * key)

    """倒置字符"""
    ciphertext = ''
    for i in a:
        ciphertext = i + ciphertext

    """返回密文"""
    return ciphertext

def decry(ciphertext: str, key: int) -> str:  # 解密函数
    """解密字符串"""
    if ciphertext == '':
        return ''
    
    """倒置字符"""
    a = ''
    for i in ciphertext:
        a = i + a
    
    """除以密钥"""
    a = str(int(a) // key)
    for i in range(7 - len(a) % 7):
        a = '0' + a

    """调换顺序"""
    plaintext = ''
    for i in range(0, len(a), 7):
        plaintext += chr(int(a[i:i+7]))

    """返回明文"""
    return plaintext

def sha256(text: str) -> str:
    sh = sha()
    sh.update(text.encode())

    return sh.hexdigest()
