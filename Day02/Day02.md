# 一、Python注释 提升代码可读性
```python
# 单行注释
print("Hello World from Python")  # 打印字符串 Hello World from Python

# 多行注释，可以注释多行内容
'''
print("Hello World from Python")
print("Hello World from Python")
print("Hello World from Python")
'''

```
# 二、Python变量
## 基本语法
:::info
变量名 = 变量值
:::
注意事项
> Python中的变量不能随意命名，要遵循规范：
> 1. 标识符，必须以字母、下画线（_）开头（数字不能打头），后面可以跟任意数目的字母、数字和下画线（_）。
> 2. 字母并不局限于 26 个英文字母，可以包含中文字符、日文字符等。
> 3. Python 语言是区分大小写的，因此 abc 和 Abc 是两个不同的标识符。
> 4. 标识符不能是 Python 关键字，但可以包含关键字。
> 5. 标识符不能包含空格。
> 6. Python 3 支持 UTF-8 字符集，因此 Python 3 的标识符可以使用 UTF-8 所能表示的多种语言的字符
> 7. Python 2.x 对中文支持较差，如果要在 Python 2.x 程序中使用中文字符或中文变量，则需要在 Python 源程序的第一行增加“#coding:utf-8”，当然别忘了将源文件保存为 UTF-8 字符集。

## 基本数据类型
![](https://cdn.nlark.com/yuque/0/2024/jpeg/40488635/1710569990133-d3e30ec2-7bbb-4461-97c4-e16bbbb6e3b5.jpeg)
```python
# 定义一个变量保存学生名字
StudentName = "张三"
# 定义一个变量保存年龄
StudentAge = 18

# 打印
print(StudentName)
print(StudentAge)

# 1. 定义一个整数变量
a = 100  # a变量就是一个整数类型的变量，int类型
print(type(a))

# 2. 定义一个浮点变量
b = 3.14  # b变量就是一个浮点类型的变量，float类型
print(type(b))

# 3. 定义一个布尔变量
c = True  # c变量就是一个布尔类型的变量，bool类型
print(type(c))

# 4. 定义一个字符串变量
d = "Hello World"
print(type(d))

# 5. 定义一个列表变量
e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(e))

# 6. 定义一个元组变量
f = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(f))

# 7. 定义一个字典变量
g = {"name": "张三", "age": 18}
print(type(g))

# 8. 定义一个集合变量
h = {1, 2, 3}
print(type(h))

```
# 三、格式化输出
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40488635/1710572110483-cc110956-7d3d-4499-ae57-e3d9a4b1b9cb.png#averageHue=%23eeeeec&clientId=uc158c504-027a-4&from=paste&height=584&id=u2d5f1543&originHeight=1168&originWidth=1666&originalType=binary&ratio=2&rotation=0&showTitle=false&size=195147&status=done&style=none&taskId=ue7a0dc23-bd71-4a3b-82d5-1158e83fd4a&title=&width=833)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40488635/1710572183960-293287db-f8a0-4adb-bd91-97a00c1e3651.png#averageHue=%23f5f3ee&clientId=uc158c504-027a-4&from=paste&height=186&id=u9ad1f8da&originHeight=372&originWidth=1664&originalType=binary&ratio=2&rotation=0&showTitle=false&size=54922&status=done&style=none&taskId=uf89b66f4-43e7-45ac-a6b7-f0290078172&title=&width=832)
> **^**, **<**, **>** 分别是居中、左对齐、右对齐，后面带宽度， **:** 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
> **+** 表示在正数前显示 **+**，负数前显示 **-**；** ** （空格）表示在正数前加空格
> b、d、o、x 分别是二进制、十进制、八进制、十六进制。
> 此外我们可以使用大括号 **{}** 来转义大括号

```python
"""
str.format()
基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序。
"""
str1 = "{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序

str2 = "{0} {1}".format("hello", "world")  # 设置指定位置

str3 = "{1} {0} {1}".format("hello", "world")  # 设置指定位置

print(str1)
print(str2)
print(str3)

# 也可以设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))  # 关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 数字格式化
print("{:.2f}".format(3.1415926))

```
