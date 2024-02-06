import numpy as np
import matplotlib.pyplot as plt

# 定义均值和标准差
mu = 0  # 均值
sigma = 1  # 标准差

# 生成随机样本
data = np.random.normal(mu, sigma, 1000)

# 绘制直方图
plt.hist(data, bins=30, density=True, alpha=0.5, color='b', label='Histogram')

# 添加标题和标签
plt.title('Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
