
import numpy as np
import matplotlib.pyplot as plt
#三轮迭代实体一致性分数变化趋势
size = 6
# 返回size个0-1的随机数

a = [67.01, 89.64, 64.56, 98.25, 93.29, 52.13]
b = [73.31, 93.61, 76.42, 98.97, 95.15, 54.95]
c = [81.51, 95.04, 82.20, 99.01, 95.15, 75.93]

x = np.arange(6)
# 有a/b/c三种类型的数据，n设置为3
total_width, n = 0.9, 3
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
# 每种类型的柱状图宽度
width = total_width / n

# 重新设置x轴的坐标
x = x - (total_width - width) / 2
x_data = ["Disease", "Cyber-Syndrome", "Syndrome/Sign",  "Acupoint", "Meridians", "Anaphor"]

plt.xticks(x, x_data, fontsize=9, rotation=20)
plt.ylabel("IAA score")
# 画柱状图

ax.bar(x, a, width=width, label="first iteration", color='#f0833a')
for i, j in zip(x, a):
    plt.text(i, j+0.01, f'{j}%', ha="center", va="bottom", fontsize=6)

ax.bar(x + width, b, width=width, label="second iteration",color='#699d4c')
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