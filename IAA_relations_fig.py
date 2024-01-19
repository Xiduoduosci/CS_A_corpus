import matplotlib.pyplot as plt
import numpy as np
#三轮迭代关系一致性分数分析

# 返回size个0-1的随机数

a = [50.38, 46.51, 53.72, 78.12, 47.44]
b = [52.94, 61.87, 62.35, 86.57, 51.10]
c = [80.16, 68.07, 69.37, 89.86, 71.86]

x = np.arange(5)
# 有a/b/c三种类型的数据，n设置为3
total_width, n = 0.9, 3
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2
x_data = ["Is_a", "Causes", "Is_synon", "Is_acron", "Is_anaphora"]
plt.xticks(x, x_data, fontsize=9, rotation=20)
# 画柱状图
plt.ylabel("IAA score")
ax.bar(x, a, width=width, label="first iteration", color='#f0833a')
for i, j in zip(x, a):
    plt.text(i, j+0.01, f'{j}%', ha="center", va="bottom", fontsize=6)

ax.bar(x + width, b, width=width, label="second iteration", color='#699d4c')
for i, j in zip(x + width, b):
    plt.text(i, j+0.01, f'{j}%', ha="center", va="bottom", fontsize=6)

ax.bar(x + 2*width, c, width=width, label="third iteration", color='#247afd')
for i, j in zip(x+2*width, c):
    plt.text(i, j+0.01, f'{j}%', ha="center", va="bottom", fontsize=6)


# 显示图例
plt.legend(loc='upper left',
           bbox_to_anchor=(0, 1.1),
           ncol=len(a))
# 显示柱状图
plt.show()