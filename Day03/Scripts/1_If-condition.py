"""
用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，
并提示：您的年龄是xx: 青少年/青年/中年/老年。
年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。
"""
age = int(input("请输入您的年纪："))
if 0 <= age <= 17:
    print("您的年龄是青少年。")
elif 18 <= age <= 35:
    print("您的年龄是青年。")
elif 36 <= age <= 59:
    print("您的年龄是中年。")
elif 60 <= age <= 99:
    print("您的年龄是老年。")

"""
制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：
登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。
提示：系统先验证验证码是否正确，正确后再验证用户名和密码。
"""
username = input("请输入用户名：")
password = input("请输入密码：")
captcha = input("请输入验证码：")
if captcha == "qwer":
    if username == "aaa" and password == "123456":
        print(f"欢迎：{username}")
    else:
        print("用户名或密码错误！")
else:
    print("验证码错误！")