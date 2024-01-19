import pandas as pd
import os
#语料总体的一致性分析
path1 = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v3/"
path2 = "F:/小论文1实验数据/corpus_final/corpus_annotation_zhao_v3/"

precision = 0
IAA_count = 0
total_en = 0
ann2_en = 0
label = []
co = 0

for file_name in os.listdir(path1):
    print(file_name)
    url1 = path1 + file_name
    ann1 = pd.read_csv(url1, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
    total_en = total_en + len(ann1)
    label = ann1.values.tolist()
    # print(url1)

    url2 = path2 + file_name
    ann2 = pd.read_csv(url2, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')

    ann2_en = ann2_en + len(ann2)
    contrast_label = ann2.values.tolist()

    glod_label = []
    con_label = []

    glod_relation_label = []
    con_relation_label = []

    stand_relation = []
    con_relation = []

    bi_stand_relation_label = []
    bi_con_relation_label = []

    bi_stand_relation = []
    bi_con_relation = []
    for i in range(len(label)):
        if label[i][0].startswith('T'):
            glod_label.append(label[i])
        if label[i][0].startswith('R'):
            glod_relation_label.append(label[i])
        if label[i][0].startswith('*'):
            bi_stand_relation_label.append(label[i])
    # print(glod_relation_label)
    # print(bi_stand_relation)

    for j in range(len(contrast_label)):
        if contrast_label[j][0].startswith('T'):
            con_label.append(contrast_label[j])
        if contrast_label[j][0].startswith('R'):
            con_relation_label.append(contrast_label[j])
        if contrast_label[j][0].startswith('*'):
            bi_con_relation_label.append(contrast_label[j])
    # print(con_relation_label)

    for m in range(len(glod_label)):
        for n in range(len(con_label)):
            if glod_label[m][1] == con_label[n][1]:
                if glod_label[m][2] == con_label[n][2]:
                    IAA_count = IAA_count + 1
    # print(IAA_count)
    for a in range(len(glod_relation_label)):
        # print(glod_relation_label[a])
        glod_process_label = glod_relation_label[a][1].split(' ')
        str1 = glod_process_label[1].split(':')[1]
        str2 = glod_process_label[2].split(':')[1]
        tokens1 = ann1[ann1[0] == str1].values.tolist()
        tokens2 = ann1[ann1[0] == str2].values.tolist()
        standard_str = tokens1 + tokens2
        stand_relation.append(standard_str)
        # print(standard_str)
    for b in range(len(con_relation_label)):
        constrast_process_label = con_relation_label[b][1].split(' ')
        constrast_str1 = constrast_process_label[1].split(':')[1]
        constrast_str2 = constrast_process_label[2].split(':')[1]
        constrast_tokens1 = ann2[ann2[0] == constrast_str1].values.tolist()
        constrast_tokens2 = ann2[ann2[0] == constrast_str2].values.tolist()
        constrast_str = constrast_tokens1 + constrast_tokens2
        con_relation.append(constrast_str)

    for c in range(len(stand_relation)):
        for d in range(len(con_relation)):
            print(con_relation[d])
            if stand_relation[c][0][1] == con_relation[d][0][1]:
                if stand_relation[c][0][2] == con_relation[d][0][2]:
                    if stand_relation[c][1][1] == con_relation[d][1][1]:
                        if stand_relation[c][1][2] == con_relation[d][1][2]:
                            IAA_count = IAA_count + 1
    # print(IAA_count)
    for e in range(len(bi_stand_relation_label)):
        bi_stand_process = bi_stand_relation_label[e][1].split(' ')
        # stand_temp = []
        bi_stand_str = []
        for f in range(1, len(bi_stand_process)):
            stand_temp = ann1[ann1[0] == bi_stand_process[f]].values.tolist()
            bi_stand_str = bi_stand_str + stand_temp
        bi_stand_relation.append(bi_stand_str)
    # print(bi_stand_relation)

    for x in range(len(bi_con_relation_label)):
        bi_con_process = bi_con_relation_label[x][1].split(' ')
        bi_con_str= []
        for y in range(1, len(bi_con_process)):
            con_temp = ann2[ann2[0] == bi_con_process[y]].values.tolist()
            bi_con_str = bi_con_str + con_temp
        bi_con_relation.append(bi_con_str)
    # print(bi_con_relation)

    for p in range(len(bi_stand_relation)):
        for q in range(len(bi_con_relation)):
            if len(bi_stand_relation[p]) == len(bi_con_relation[q]):
                # print(bi_stand_relation[p], bi_con_relation[q])
                # print(bi_stand_relation[p][0][1]+bi_stand_relation[p][0][2], bi_con_relation[q][0][1]+bi_con_relation[q][0][2])
                if bi_stand_relation[p][0][1] == bi_con_relation[q][0][1]:
                    if bi_stand_relation[p][0][2] == bi_con_relation[q][0][2]:
                        if bi_stand_relation[p][1][1] == bi_con_relation[q][1][1]:
                            if bi_stand_relation[p][1][2] == bi_con_relation[q][1][2]:
                                IAA_count = IAA_count + 1
                                co = co+1
            else:
                break
# print(co)


    # for e in range(len(bi_stand_relation)):
    #     for f in range(len(bi_con_relation)):
    #         bi_stand_process =



precision = IAA_count / ann2_en
recall = IAA_count / total_en
f1 = 2 * precision * recall / (precision + recall)
print('实体总数：%s' % total_en)
print('识别出：%s' % ann2_en)
print('标注一致的个数为：%s' % IAA_count)
print("准确率为：%s" % precision)
print("召回率为：%s" % recall)
print("f1-socre为：%s" % f1)