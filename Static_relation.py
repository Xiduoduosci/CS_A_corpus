import pandas as pd
import os
import matplotlib.pyplot as plt
#关系统计
Is_a_en = 0
Causes_en = 0
Is_synon_en = 0
Is_acron_en = 0
Is_anaphora_en = 0
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

path = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v3/"
for file_name in os.listdir(path):
    url = path+file_name
    label = pd.read_csv(url, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')

    Is_a_label = label[label[1].str.startswith('Is_a')]
    Is_a_en = Is_a_en + len(Is_a_label)

    Causes_label = label[label[1].str.startswith('Causes')]
    Causes_en = Causes_en + len(Causes_label)

    Is_synon_label = label[label[1].str.startswith('Is_synon')]
    Is_synon_en = Is_synon_en + len(Is_synon_label)

    Is_acron_label = label[label[1].str.startswith('Is_acron')]
    Is_acron_en = Is_acron_en + len(Is_acron_label)

    Is_anaphora_label = label[label[1].str.startswith('Is_anaphora')]
    Is_anaphora_en = Is_anaphora_en + len(Is_anaphora_label)

#准备数据
x_data = ['Is_a', 'Causes', 'Is_synon', 'Is_acron', 'Is_anaphora']
y_data = [Is_a_en, Causes_en, Is_synon_en, Is_acron_en, Is_anaphora_en]

plt.rcParams["font.serif"] = ["Times New Roman"]

#画图
width = 0.5
for i in range(len(x_data)):
    ax.bar(x_data[i], y_data[i], label=x_data[i], width=width)

for i, v in enumerate(y_data):
    plt.annotate(str(v), xy=(i, v), ha='center', va='bottom')

plt.xticks(fontsize=9, rotation=20)
# plt.legend(loc='upper left',
#            bbox_to_anchor=(-0.1,-0.15),
#            ncol=len(x_data))
plt.legend()
# plt.xlabel("Relations")
plt.ylabel("Number of relations annotated")
plt.savefig(fname="relation_static.png", dpi=100)
plt.show()

print(Is_a_en)
print(Causes_en)
print(Is_synon_en)
print(Is_acron_en)
print(Is_anaphora_en)