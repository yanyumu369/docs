class person(object):
    address = '中国'  # 类属性，没个实例的公共属性

    def __init__(self, name, sex, age):  # 相当于java中的构造方法
        self.name = name  # 实例属性
        self.sex = sex  # 实例属性
        self.age = age  # 实例属性

    def dance(self):  # 方法
        print(self.name, '跳了一场舞')

hong = person('小红', '女', 18)  # 实例化小红，将实例化的对象赋值给变量hong
ming = person('小明', '男', 26)
hua = person('小花', '女', 22)
