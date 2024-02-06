import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 从用户那里获取均值和标准差
mu = float(input("请输入均值mu: "))
sigma = float(input("请输入标准差sigma: "))

# 生成随机样本
data = np.random.normal(mu, sigma, 1000)

# 计算概率密度函数
pdf_values = norm.pdf(data, mu, sigma)

# 绘制直方图和概率密度函数图
plt.hist(data, bins=30, density=True, alpha=0.5, color='b', label='Histogram')
plt.plot(data, pdf_values, color='r', label='PDF')
plt.title('Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()