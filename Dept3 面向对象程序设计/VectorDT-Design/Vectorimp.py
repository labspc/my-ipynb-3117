from ast import main


class Vector:
    def __init__(self, x, y):
        self.x = x # 实例变量：x、y
        self.y = y
    

    def add(self, other):
        """求和运算"""
        return Vector(self.x + other.x, self.y + other.y)

    def scalar_multiply(self, scalar):
        """数乘运算"""
        return Vector(self.x * scalar, self.y * scalar)

    def dot_product(self, other):
        """点乘运算"""
        return self.x * other.x + self.y * other.y

    def get_x(self):
        """获取 x 分量"""
        return self.x

    def get_y(self):
        """获取 y 分量"""
        return self.y


# 示例用法
if __name__ == "__main__":
    main()