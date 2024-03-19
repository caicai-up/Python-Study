"""
a.定义一个Star类(明星类)，包含初始化init方法：
成员属性：明星姓名, 明星的电影
成员方法：playing() 打印：“xxx出演了yyy，非常好看”
打印对象时显示“xxx是我的偶像，我非常喜欢他的电影yyy”
删除对象提示“xxx我不再喜欢了”
xxx为明星姓名，yyy是电影的名字
b.键盘循环输入五个Star对象的姓名和电影名。
c.分别调用输入Star对象的playing方法和打印对象
"""


class Star:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __str__(self):
        return f'{self.name}是我的偶像，我非常喜欢他的电影{self.movie}'

    def __del__(self):
        print(self.name + "我不再喜欢了")

    def playing(self):
        print(self.name + "出演了" + self.movie + "，非常好看")


stars = []
for _ in range(5):
    starName = input("请输入明星的姓名：")
    starMovie = input("请输入明星的电影：")
    stars.append(Star(starName, starMovie))

for star in stars:
    star.playing()
    print(star)

stars.clear()

"""
搬家具规则：
1. 家具分不同的类型，并占用不同的面积
2. 输出家具信息时，显示家具的类型和家具占用的面积
3. 房子有自己的地址和占用的面积
4. 房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功；否则提示添加失败
5. 输出房子信息时，可以显示房子的地址、占地面积、剩余面积
"""


class Furniture:
    def __init__(self, fType, area):
        self.fType = fType
        self.area = area

    def __str__(self):
        return f'{self.fType}占据面积{self.area}'


class House:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.unUsedArea = area
        self.items = []

    def addFurniture(self, furniture):
        if self.unUsedArea >= furniture.area:
            self.items.append(furniture)
            self.unUsedArea -= furniture.area
            print(f"添加{furniture.fType}成功")
        else:
            print(f"添加{furniture.fType}失败")

    def __str__(self):
        return f'地址：{self.address}，面积：{self.area}，空闲面积：{self.unUsedArea}'


home = House("北京", 120)
print(home)
bed = Furniture("床", 10)
print(bed)
airCondition = Furniture("空调", 10)
print(airCondition)
home.addFurniture(bed)
print(home)
home.addFurniture(airCondition)
print(home)
