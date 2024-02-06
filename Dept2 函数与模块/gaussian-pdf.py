import numpy as np
import matplotlib.pyplot as plt

# 定义高斯分布的概率密度函数
def gaussian_pdf(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

# 从用户处获取 mu 和 sigma 值
mu = float(input("请输入均值（mu）: "))
sigma = float(input("请输入标准差（sigma）: "))

# 生成一组 x 值
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# 计算对应 x 值的概率密度函数值
pdf_values = gaussian_pdf(x_values, mu, sigma)

# 绘制概率密度函数图
plt.plot(x_values, pdf_values, label='Gaussian PDF')

# 添加标题和标签
plt.title('Gaussian Probability Density Function')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()

# 显示图形
plt.show()
