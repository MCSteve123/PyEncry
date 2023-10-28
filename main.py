"""一个可以抹去信息统计学特征的加密工具

   使用库/模块：
       module   （自制）
       tkinter
       random-randint
       pyperclib-copy, paste         （需安装）

   操作方式：GUI
   语言：Python
   版本：v1.6

   注：此工具仅可在有人监听但无法修改的前提下运作（如微信群）
   作者：MCSteve123/根号谈(GitHub/Bilibili)               """

from module import *
from tkinter import *
from random import randint
from pyperclip import copy,paste


VER = '1.6'

"""初始化GUI"""
root = Tk()
root['bg'] = 'white'
root.title('PyEncry    工具版本：v' + VER + '  模块库版本：v' + MODULE_VER + '  作者：根号谈')
root.geometry('550x450+150+150')


"""定义StringVar变量"""
plaintext = StringVar()
ciphertext = StringVar()
decry_key = StringVar()
warning = StringVar()
cipher = StringVar()
plain = StringVar()


"""定义随机密钥"""
KEY = randint(10000000, 99999999)
sha = sha256(str(KEY))
THE_KEY = '%i %s %s %s' %(KEY,sha,VER,MODULE_VER)


"""五个函数（由于不知名原因（似乎是Tk的问题），一行的代码也只能做成函数）"""
def enc():
    """加密函数"""

    cipher.set(encry(plaintext.get(), KEY))

def dec():
    """解密函数"""

    a = decry_key.get().split()
    
    """警告部分"""
    if len(a) != 4:
        warning.set('警告：密钥验证失效，请重新索要密钥或检查对方工具是否低于v1.2、模块库低于v1.1')
        return
    if sha256(a[0]) != a[1]:
        warning.set('警告：密钥损坏或被修改，请重新索要')
        return
    if a[2] != VER:
        warning.set('警告：双方工具版本不同，请更换版本。您的版本：%s，对方版本：%s'%(VER, a[2]))
        return
    if a[3] != MODULE_VER:
        warning.set('警告：双方模块库版本不同，请更换版本。您的版本：%s，对方版本：%s'%(MODULE_VER, a[3]))
        return
    warning.set('')

    plain.set(decry(ciphertext.get(), int(a[0])))

def paste_cipher():
    ciphertext.set(paste())

def copy_cipher():
    copy(cipher.get())

def paste_key():
    decry_key.set(paste())

def copy_key():
    copy(str(THE_KEY))


"""GUI"""
Label(root, text='-------------------------------------------------  加密区  -------------------------------------------------', fg='green', bg='white').place(x=0, y=0)
Entry(root, textvariable=plaintext, fg='blue', bg='white', width=75).place(x=0, y=25)
Label(root, text='您的密钥:' + str(KEY), fg='SkyBlue', bg='white').place(x=220, y=53)
Button(root,text='复制密钥（请务必点这里）',command=copy_key,fg='black',bg='white').place(x=333,y=50)
Button(root, text='加密', fg='red', bg='white', command=enc).place(x=493, y=50)
Label(root, text='密文：', fg='orange', bg='white').place(x=0, y=88)
Entry(root, textvariable=cipher, fg='black', bg='white', width=75).place(x=0, y=110)
Button(root, text='复制密文', fg='black', bg='white', command=copy_cipher).place(x=400, y=133)

Label(root, text='-------------------------------------------------  解密区   -------------------------------------------------', fg='green', bg='white').place(x=0, y=225)
Label(root,textvariable=warning,fg='red',bg='white').place(x=0,y=200)
Entry(root, textvariable=ciphertext, fg='black', bg='white', width=75).place(x=0, y=250)
Button(root,text='粘贴密文',command=paste_cipher,fg='black',bg='white').place(x=100,y=275)
Label(root, text='对方密钥:', fg='SkyBlue', bg='white').place(x=215, y=279)
Entry(root, textvariable=decry_key, fg='SkyBlue', bg='white', width=8).place(x=275, y=281)
Button(root,text='粘贴密钥',command=paste_key,fg='black',bg='white').place(x=350,y=275)
Button(root, text='解密', fg='red', bg='white', command=dec).place(x=450, y=275)
Label(root, text='明文：', fg='orange', bg='white').place(x=0, y=313)
Entry(root, textvariable=plain, fg='blue', bg='white', width=75).place(x=0, y=335)

Label(root, text='在这里输入一串字符以标记通信者（不写也没事）-->', bg='white').place(x=110, y=398)
Entry(root, bg='white', width=15).place(x=400, y=400)


root.mainloop()  # 启动GUI
