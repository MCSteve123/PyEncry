# Py加密工具（PyEncry）
## 介绍
此工具是一个可以加密文本的Python程序，使用一个8位数字作为密钥。 <br>
此工具会持续更新。（虽然可能几个月不更） <br>
<br>
（众求一个较快速的Python质数筛选器，这对以后的开发很有用，如果有的话请在issues里反馈一下！）

## 使用方法

### 发送密钥
程序拥有一个8位密钥，这是内容的加解密工具。<br>
您应当使用“复制密钥到剪贴板”按钮复制<u>有核验标记的密钥</u>，并将其发送出去，但不能让其他人知道这是密钥。<br>
（<u>不应</u>将无核验标记的密钥直接发送给对方，这将导致工具无法识别！）<br>

### 加密
_在加密前，您需要确保您执行了[发送密钥部分](#发送密钥)的内容。_<br>
将需加密的内容输入**加密框**（“加密区”下的第一个长输入框），点击“加密”按钮，您会看到**加密输出框**（“加密区”下的第二个长输入框）中输出了一串数字，这就是密文。<br>
您可以复制密文，再将其发送出去。<br>

### 解密
将对方发送过来的密钥<u>原封不动</u>地输入**密钥框**（“解密区”下的唯一短输入框）。<br>
再将需解密的内容输入**解密框**（“解密区”下的第一个长输入框），点击“解密”按钮，您会看到**解密输出框**（“解密区”下的第二个长输入框）中输出了文字，这就是原内容。<br>
_如果显示了“警告”，请看此处：[为什么点击解密按钮会产生警告？](#一)_<br>

### 示意图
![示意图](<image.jpg>)
注：v1.4的GUI更新并无实质作用，因此没有修改示意图
<br>
<br>


## 最新更新
（注意！工具和模块库版本号不一定相同，具体请看“适配说明”）

### 主程序
#### 2023.10.14（v1.6）【适配模块库v1.4, v1.5】
1. 查明了上一个版本的`hash()`函数问题，替换为sha256加密

### 模块库
#### 2023.10.14（v1.5）【适配工具v1.6】
1. 在[这里](https://github.com/MCSteve123/PyEncry-API)开源了

## 历史版本
[所有版本列表](https://github.com/MCSteve123/PyEncry/releases)<br>
### 版本
[Release1.0版本](https://github.com/MCSteve123/PyEncry/releases/tag/Release1.0)<br>
[Release1.1版本](https://github.com/MCSteve123/PyEncry/releases/tag/Release1.1)<br>
[Release1.2版本](https://github.com/MCSteve123/PyEncry/releases/tag/Release1.2)<br>
[Release1.2.1版本](https://github.com/MCSteve123/PyEncry/releases/tag/Release1.2.1)<br>
[ReLease1.3版本](https://github.com/MCSteve123/PyEncry/releases/tag/Release1.3)
### 附注
从Release1.3开始，不提供任何.exe文件，直到能够保证Pyinstaller不抽风为止<br>
在此之前要求拥有Python环境者才可使用<br>
依赖库安装请在cmd或powershell使用此命令：`pip install <依赖库名称>`
<br>
<br>

## Q & A
### 一、
Q:<br>
为什么点击解密按钮会产生警告？<br>
A:<br>
这有3种可能：
1. 密钥验证失效，请重新索要密钥或检查对方工具是否低于v1.2、模块库低于v1.1:<br>
这是因为对方的密钥不完整（说了点按钮复制密钥，非不听）或版本过低导致的<br><br>
2. 密钥已损坏，请重新索要:<br>
这是因为密钥被修改或漏输入导致的，当然也有可能是你当时的剪贴板里存的不是密钥<br><br>
3. 双方\[工具/模块库\]版本不同:<br>
这是因为双方版本不同导致的，需要更新版本<br>

### 二、
Q:<br>
为什么有些包和程序的版本号是X.X，有些是X.X.X？<br>
A:<br>
1.如果版本号是X.X格式的，使用的是Release版本，比较稳定，代码打包格式为“ReleaseX.X”，可直接在GitHub上的Release菜单中下载。更建议使用此类版本。<br>
2.如果是X.X.X格式的，使用的是beta版本或snapshot版本，可能会有各种BUG，beta版打包格式为“BetaX.X”，也可直接在GitHub上的Release菜单中下载。snapshot版本不打包，只在版本库里开放，更新后就无了。

### 三、
Q:<br>
beta版本和snapshot版本有何区别？<br>
A:<br>
beta版本更新内容多，snapshot版本更新内容少。（就这点区别，别问我为啥，实在是没啥区别了...）

## 关于作者
[B站主页-根号谈](https://space.bilibili.com/1098123879)<br>
[GitHub主页-MCSteve123](https://github.com/MCSteve123)<br>
[GitHub仓库-PyEncry](https://github.com/MCSteve123/PyEncry)
