import pandas as pd
import os
#疾病实体一致性分析
base_path1 = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v1/"
base_path2 = "F:/小论文1实验数据/corpus_final/corpus_annotation_zhao_v1/"
ann1_en = 0
ann2_en = 0
IAA_count = 0

for file_name in os.listdir(base_path1):
    file_count = 0
    url1 = base_path1 + file_name
    url2 = base_path2 + file_name
    ann1 = pd.read_csv(url1, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
    ann2 = pd.read_csv(url2, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')

    ann1_label = ann1[ann1[1].str.startswith('Disease')]
    ann2_label = ann2[ann2[1].str.startswith('Disease')]

    ann1_en = ann1_en + len(ann1_label)
    ann2_en = ann2_en + len(ann2_label)

    stand_label = ann1_label.values.tolist()
    constrast_label = ann2_label.values.tolist()

    for i in range(len(stand_label)):
        for j in range(len(constrast_label)):
            # print(stand_label[i],constrast_label[j])
            if stand_label[i][1] in constrast_label[j][1] and stand_label[i][2] in constrast_label[j][2]:
                IAA_count = IAA_count + 1
                file_count = file_count + 1
    print(file_name, file_count)

precison = IAA_count / ann2_en
recall = IAA_count / ann1_en
f1 = (2 * precison * recall) / (precison + recall)
print(precison)
print(recall)
print(f1)

