import sys
import random

def sampling_without_replacement(population, k):
    """
    从给定的总体中进行无放回抽样。

    参数:
    population: 总体，一个列表。
    k: 抽样数量。

    返回值:
    一个列表，包含从总体中抽取的 k 个样本。
    """
    return random.sample(population, k)

# 给定要抽取的样本数量
# k = 5

# 从命令行接收参数=要抽取的样本数量
k = int(sys.argv[1])

# 测试函数
# 给定要抽取的样本值 []
# population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 从命令行接收参数=样本值 int(x) for x in sys.argv[2:]
population = [int(x) for x in sys.argv[2:]]

print(sampling_without_replacement(population, k))