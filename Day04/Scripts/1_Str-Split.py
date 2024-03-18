"""
现有字符串如下，请使用切片提取出ceg
words = "abcdefghi"
"""
words = "abcdefghi"
newStr = words[2: 7: 2]
print(newStr)

# 创建列表 => [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list = [(i, j) for i in range(1, 3) for j in range(0, 3)]
print(list)

numstr = '0123456789'
# 1、从2到5开始切片，步长为1
print(numstr[2:5:1])
print(numstr[2:5])
# 2、只有结尾的字符串切片：代表从索引为0开始，截取到索引为5的位置（不包含索引为5的数据）
print(numstr[:5])
# 3、只有开头的字符串切片：代表从起始位置开始，已知截取到字符串的结尾
print(numstr[1:])
# 4、获取或拷贝整个字符串
print(numstr[:])
# 5、调整步阶：类似求偶数
print(numstr[::2])
# 6、把步阶设置为负整数：类似字符串翻转
print(numstr[::-1])
# 7、起始位置与结束位置都是负数
print(numstr[-4:-1])
# 8、结束字符为负数，如截取012345678
print(numstr[:-1])