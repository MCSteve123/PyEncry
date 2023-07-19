"""一个可以抹去信息统计学特征的加密工具

   使用库/模块：
       Encry_and_Decry   （自制）
       tkinter
       random-randint
       pyperclib         （需安装）
    
   操作方式：GUI
   语言：Python
   版本：v1.2

   注：此工具仅可在有人监听但无法修改的前提下运作（如微信群）
   作者：MCSteve123/根号谈(GitHub/Bilibili)                                              """

from Encry_and_Decry import *
from tkinter import *
from pyperclip import copy,paste
from random import randint


"""版本号"""
version = '1.2'
module_version = retrun_version()


"""初始化GUI"""
root = Tk()
root['bg'] = 'white'
root.title('对称加解密工具    工具版本：v' + version + '  模块库版本：v' + module_version + '  作者：根号谈')
root.geometry('550x450+150+150')


"""定义六个StringVar变量"""
plaintext = StringVar()
ciphertext = StringVar()
decry_key = StringVar()
warning = StringVar()
warning.set('')
cipher = StringVar()
plain = StringVar()


"""定义随机密钥"""
key = randint(1024, 8192)
the_key = str(key) + '/' + str(hash(str(key))) + '/' + version + '/' + module_version


"""五个函数"""
def enc():
    """加密函数"""
    global key
    global plaintext

    cipher.set(encry(plaintext.get(), key))

def dec():
    """解密函数"""
    global ciphertext
    global decry_key
    global warning
    global version

    a = decry_key.get().split('/')
    
    """警告部分"""
    if len(a) != 4:
        warning.set('警告：密钥验证失效，请重新索要密钥或检查对方工具是否低于v1.2、模块库低于v1.1')
        return
    elif str(hash(a[0])) != a[1]:
        warning.set('警告：密钥被修改或损坏，请重新索要密钥')
        return
    elif float(a[2]) > float(version):
        warning.set('警告：对方工具版本较高，请更新加密工具')
        return
    elif float(a[2]) < float(version):
        warning.set('警告：对方工具版本较低，请让对方更新加密工具')
        return
    elif float(a[3]) > float(module_version):
        warning.set('警告：对方模块库版本较高，请更新模块库')
        return
    elif float(a[3]) < float(module_version):
        warning.set('警告：对方模块库版本较低，请让对方更新模块库')
        return
    else:
        warning.set('')

    plain.set(decry(ciphertext.get(), int(a[0])))

def paste_cipher():
    global ciphertext
    ciphertext.set(paste())

def paste_key():
    global decry_key
    decry_key.set(paste())

def copy_key():
    global the_key
    copy(str(the_key))


"""GUI"""
Label(root, text='加密区：', fg='green', bg='white').place(x=0, y=0)
Entry(root, textvariable=plaintext, fg='blue', bg='white', width=75).place(x=0, y=25)
Label(root, text='您的密钥:' + str(key), fg='SkyBlue', bg='white').place(x=250, y=53)
Button(root,text='复制密钥到剪贴板',command=copy_key,fg='black',bg='white').place(x=333,y=50)
Button(root, text='加密', fg='red', bg='white', command=enc).place(x=450, y=50)
Label(root, text='密文：', fg='orange', bg='white').place(x=0, y=88)
Entry(root, textvariable=cipher, fg='black', bg='white', width=75).place(x=0, y=110)

Label(root, text='解密区：', fg='green', bg='white').place(x=0, y=225)
Label(root,textvariable=warning,fg='red',bg='white').place(x=50,y=225)
Entry(root, textvariable=ciphertext, fg='black', bg='white', width=75).place(x=0, y=250)
Button(root,text='粘贴密文',command=paste_cipher,fg='black',bg='white').place(x=100,y=275)
Label(root, text='对方密钥:', fg='SkyBlue', bg='white').place(x=250, y=278)
Entry(root, textvariable=decry_key, fg='SkyBlue', bg='white', width=4).place(x=305, y=279)
Button(root,text='粘贴密钥',command=paste_key,fg='black',bg='white').place(x=350,y=275)
Button(root, text='解密', fg='red', bg='white', command=dec).place(x=450, y=275)
Label(root, text='明文：', fg='orange', bg='white').place(x=0, y=313)
Entry(root, textvariable=plain, fg='blue', bg='white', width=75).place(x=0, y=335)


root.mainloop()  # 启动GUI
