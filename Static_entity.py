import pandas as pd
import os
import matplotlib.pyplot as plt
entity_count = 0
Disease_en = 0
Cyber_Syndrome_en = 0
Syndrome_en = 0
Sign_en = 0
Acupoint_en = 0
Meridian_en = 0
Anaphor_en = 0
#实体统计
path = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v3/"
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
for file_name in os.listdir(path):
    url = path+file_name
    # print(url)
    label = pd.read_csv(url, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
    lable_T = label[label[0].str.startswith('T')]
    entity_count = entity_count + len(lable_T)
    print(url+"处理完毕！")
    Disease_label = label[label[1].str.startswith('Disease')]
    Disease_en = Disease_en + len(Disease_label)

    Cyber_Syndrome_label = label[label[1].str.startswith('Cyber')]
    Cyber_Syndrome_en = Cyber_Syndrome_en + len(Cyber_Syndrome_label)

    Syndrome_lable = label[label[1].str.startswith('Sy')]
    Syndrome_en = Syndrome_en + len(Syndrome_lable)

    Sign_label = label[label[1].str.startswith('Sign')]
    Sign_en = Sign_en + len(Sign_label)

    Acupoint_lable = label[label[1].str.startswith('A')]
    Acupoint_en = Acupoint_en + len(Acupoint_lable)

    Meridian_label = label[label[1].str.startswith('M')]
    Meridian_en = Meridian_en + len(Meridian_label)

    Anaphor_lable = label[label[1].str.startswith('Anaphor')]
    Anaphor_en = Anaphor_en + len(Anaphor_lable)

#准备数据
x_data = ["Disease", "Cyber-Syndrome", "Symptom", "Sign", "Acupoint", "Meridians", "Anaphor"]
y_data = [Disease_en, Cyber_Syndrome_en, Syndrome_en, Sign_en, Acupoint_en, Meridian_en, Anaphor_en]

plt.rcParams["font.serif"] = ["Times New Roman"]

total_width, n = 0.8, 3
width = total_width / n

#画图
for i in range(len(x_data)):
    ax.bar(x_data[i], y_data[i], label=x_data[i])

for i, v in enumerate(y_data):
    plt.annotate(str(v), xy=(i,v), ha='center', va='bottom')

plt.xticks(fontsize=9, rotation=20)
# plt.xlabel("Number of entities annotated")
plt.ylabel("Number of entities annotated")
# plt.legend(loc='upper left',
#             bbox_to_anchor=(-0.1,-0.15),
#             ncol=len(x_data))
plt.legend()
plt.savefig(fname="entity_static.png", dpi=100)
plt.show()


print(Disease_en)
print(Cyber_Syndrome_en)
print(Syndrome_en)
print(Sign_en)
print(Acupoint_en)
print(Meridian_en)
print(Anaphor_en)

print(entity_count)