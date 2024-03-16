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
