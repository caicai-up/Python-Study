"""
现有字典dict1 = {'name':'张三','age':18}
  要求：1.删除age：18这个键值对
       2.将整个字典里面的所有键值对，清空
"""
dict1 = {'name': '张三', 'age': 18}
print(dict1)
del dict1['age']
print(dict1)
dict1.clear()
print(dict1)

"""
现有字典dict1 = {'name':'张三','age':18}
要求：1.使用循环将字典中所有的键输出到屏幕上
    2.使用循环将字典中所有的键输出到屏幕上
    3.使用循环将字典中所有的键值对输出到屏幕上
      输出方式：  name：张三
                 age:18
"""
dict1 = {'name': '张三', 'age': 18}

for key in dict1.keys():
    print(key)

for val in dict1.values():
    print(val)

for key, value in dict1.items():
    print(f"{key}：{value}")

"""
有一个列表list1 = [1,2,3,4,3]
请完成去重复的功能，并且最后依然是列表
"""
list1 = [1, 2, 3, 4, 3]
set1 = set(list1)
list1 = list(set1)
print(list1)

"""
有这样的一个列表
product=[
{"name":"电脑","price":7000},
{"name":"鼠标","price":30},
{"name":"usb电动小风扇","price":20},
{"name":"遮阳伞","price":50}
]，然后小明一共有8000块钱，那么他能不能买下这所有商品？
如果能，请输出“能”，否则输出“不能”
"""
product=[
    {"name":"电脑","price":7000},
    {"name":"鼠标","price":30},
    {"name":"usb电动小风扇","price":20},
    {"name":"遮阳伞","price":50}
]

# 定义一个变量，如sums，用于存储所有商品的总价格
sums = 0
for i in product:
    for key, value in i.items():
        if isinstance(value, int):
            sums += value
if 8000 > sums:
    print('能')
else:
    print('不能')
