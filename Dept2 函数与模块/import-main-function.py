# main.py
import math_operations

# 使用 math_operations 模块中的函数
result_add = math_operations.add(5, 3)
result_subtract = math_operations.subtract(5, 3)
result_multiply = math_operations.multiply(5, 3)

# 定义另一个函数，不会与 math_operations 模块中的函数冲突
def add(x, y):
    return x + y + 1

# 调用 main.py 中定义的函数
result_custom_add = add(5, 3)

print("Result of addition:", result_add)
print("Result of subtraction:", result_subtract)
print("Result of multiplication:", result_multiply)
print("Result of custom addition:", result_custom_add)
