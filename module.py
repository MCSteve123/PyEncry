"""PyEncry的函数
   版本：v1.3.1

   对应程序：main.py"""


module_version = '1.3.1'

def encry(plaintext, key):  # 加密函数
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
    ciphertext = str(int(a) * key)

    """返回密文"""
    return ciphertext

def decry(ciphertext, key):  # 解密函数
    """解密字符串"""
    if ciphertext == '':
        return ''
    
    """除以密钥"""
    ciphertext = str(int(ciphertext) // key)
    for i in range(7 - len(ciphertext) % 7):
        ciphertext = '0' + ciphertext

    """调换顺序"""
    plaintext = ''
    for i in range(0, len(ciphertext), 7):
        plaintext += chr(int(ciphertext[i:i+7]))

    """返回明文"""
    return plaintext
