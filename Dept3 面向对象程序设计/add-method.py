class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 重载加法运算符 +
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# 创建两个向量对象
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# 使用加法运算符进行向量相加
result = v1 + v2

print("Result:", result)  # 输出：Result: (6, 8)
