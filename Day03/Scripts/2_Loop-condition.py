"""
    编写代码模拟用户登陆。要求：用户名为 python，密码 123456，
    如果输入正确，打印“欢迎光临”，程序结束，
    如果输入错误，提示用户输入错误并重新输入
"""
# while True:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == "python" and password == "123456":
#         print("欢迎光临")
#         break
#     else:
#         print("输入错误并重新输入!")

"""
设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字，
如果遇见7和7的倍数则打印“哈~”跳过本次循环。
"""
for i in range(1,101):
    if i % 7 == 0:
        print("哈~")
        continue
    print(f"{i} ")


