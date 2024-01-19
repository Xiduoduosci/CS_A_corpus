import pandas as pd
import os
#cause关系一致性分析
base_path1 = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v1/"
base_path2 = "F:/小论文1实验数据/corpus_final/corpus_annotation_zhao_v1/"
ann1_en = 0
ann2_en = 0
IAA_count = 0

for file_name in os.listdir(base_path1):
    url1 = base_path1 + file_name
    url2 = base_path2 + file_name
    ann1 = pd.read_csv(url1, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
    ann2 = pd.read_csv(url2, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
    print(url2)
    ann1_label = ann1[ann1[1].str.startswith('Causes')]

    ann2_label = ann2[ann2[1].str.startswith('Causes')]
    print(ann2_label)
    ann1_en = ann1_en + len(ann1_label)
    ann2_en = ann2_en + len(ann2_label)

    str1 = ""
    str2 = ""
    stand_label = ann1_label.values.tolist()
    standard_str = ""

    constrast_label = ann2_label.values.tolist()
    constrast_str = ""

    glod_label = []
    con_label = []

    for i in range(len(stand_label)):
        process_label = stand_label[i][1].split(' ')
        str1 = process_label[1].split(':')[1]
        str2 = process_label[2].split(':')[1]
        tokens1 = ann1[ann1[0] == str1].values.tolist()
        tokens2 = ann1[ann1[0] == str2].values.tolist()
        standard_str = tokens1 + tokens2
        glod_label.append(standard_str)

    for i in range(len(constrast_label)):
        constrast_process_label = constrast_label[i][1].split(' ')
        constrast_str1 = constrast_process_label[1].split(':')[1]
        constrast_str2 = constrast_process_label[2].split(':')[1]
        constrast_tokens1 = ann2[ann2[0] == constrast_str1].values.tolist()
        constrast_tokens2 = ann2[ann2[0] == constrast_str2].values.tolist()
        constrast_str = constrast_tokens1 + constrast_tokens2
        con_label.append(constrast_str)

    # print(len(glod_label))
    for m in range(len(glod_label)):
        for n in range(len(con_label)):
            if glod_label[m][0][1] in con_label[n][0][1] and glod_label[m][0][2] in con_label[n][0][2] \
                    and glod_label[m][1][1] in con_label[n][1][1] and glod_label[m][1][2] in con_label[n][1][2]:
                IAA_count = IAA_count + 1
                print(glod_label[m], con_label[n])
    glod_label.clear()
    con_label.clear()

print(IAA_count)
print(ann1_en)
print(ann2_en)
precison = IAA_count / ann2_en
recall = IAA_count / ann1_en
f1 = (2 * precison * recall) / (precison + recall)
print(precison)
print(recall)
print(f1)

