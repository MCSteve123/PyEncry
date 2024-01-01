"""   PyEncryAPI   v1.5"""

# The API of PyEncry
# Copyright (C) 2024 MCSteve123
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

from hashlib import sha256 as sha

MODULE_VER = '1.5'

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
    try:
        plaintext = ''
        for i in range(0, len(a), 7):
            plaintext += chr(int(a[i:i+7]))
    except:
        return ValueError

    """返回明文"""
    return plaintext

def sha256(text: str) -> str:
    sh = sha()
    sh.update(text.encode())

    return sh.hexdigest()
