from Vectorimp import Vector

# 创建两个向量
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# 求和运算
sum_vector = v1.add(v2)
print("Sum:", sum_vector.get_x(), sum_vector.get_y())

# 数乘运算
scaled_vector = v1.scalar_multiply(2)
print("Scalar Multiply:", scaled_vector.get_x(), scaled_vector.get_y())

# 点乘运算
dot_product = v1.dot_product(v2)
print("Dot Product:", dot_product)


# python Client.py
#
# Sum: 6 8
# Scalar Multiply: 4 6
# Dot Product: 23