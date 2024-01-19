from graphviz import Digraph
#树型语料库构建与展示
# # 创建树状结构
# dot = Digraph(comment='pidancode.com')   # 创建图形对象
# dot.node('dir1')
# dot.node('dir2')
# dot.edge('pidancode.com', 'dir1')
# dot.edge('pidancode.com', 'dir2')
# dot.node('file1')
# dot.node('file2')
# dot.node('file3')
# dot.edge('dir1', 'file1')
# dot.edge('dir1', 'file2')
# dot.edge('dir2', 'file3')
#
# # 生成图形
# dot.render('pidancode_tree', view=True)

import numpy as np
import nltk
nltk.download()
from nltk.tokenize import word_tokenize
import os, re
import pandas as pd

def show_tree_dir(father_name, children_list):
    dir_str ="├──"
    dir_str += father_name+"\n"
    for c in children_list:
        dir_str += "  └──"+c+"\n"

    dot = Digraph(comment='pidancode.com')
    dot.node(father_name)

    for s in range(len(children_list)):
        dot.node(children_list[s])
        dot.edge(father_name, children_list[s])
    dot.render("../CS_A_Tree_show/CS-A_"+father_name, view=True)
    return dir_str

def get_word_vector(s1, s2):  # 将文本转换为词向量
    cut1 = word_tokenize(s1)
    cut2 = word_tokenize(s2)

    #列出所有的词，取并集
    key_word = list(set(cut1+cut2))
    # print(key_word)
    # 给定形状和类型的用0填充的矩阵存储向量 初始化矩阵
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))

    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(cut1)):
            if key_word[i] == cut1[j]:
                word_vector1[i] += 1
        for k in range(len(cut2)):
            if key_word[i] == cut2[k]:
                word_vector2[i] += 1

    # 输出向量
    # print("s1词向量矩阵：")
    # print(word_vector1)
    # print("s2词向量矩阵：")
    # print(word_vector2)
    return word_vector1, word_vector2

def cos_dist(vec1, vec2):
    dist1 = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
    return dist1

if __name__ == '__main__':
    base_path1 = "F:/小论文1实验数据/corpus_final/corpus_annotation_wang_v3/"
    acu_list = []
    cyber_syndrome_list = []
    treats_count = 0
    for file_name in os.listdir(base_path1):
        if re.search(r'\d', file_name):
            cyber_syndrome_list.append(file_name)
        else:
            acu_list.append(file_name)

    # disease_symtom = []
    for i in range(len(cyber_syndrome_list)):
        children_acu_list = []
        dist1 = 0
        max = 0.8
        url1 = base_path1 + cyber_syndrome_list[i]
        print(url1)
        father_name = cyber_syndrome_list[i]
        disease_symtom = []
        ann1 = pd.read_csv(url1, header=None, sep='\t', engine='python', error_bad_lines=False, encoding='utf-8')
        ann1_label = ann1[ann1[1].str.startswith('S')]
        for item in ann1_label[2]:
            disease_symtom.append(item.lower())
        disease_symtom = list(set(disease_symtom))
        print(disease_symtom)

        cyber_label = ann1[ann1[1].str.startswith('Cyber')]
        search_cyber_syndrome = []
        for element in cyber_label[2]:
            search_cyber_syndrome.append(element.lower())
        search_cyber_syndrome = set(search_cyber_syndrome)
        # print(search_cyber_syndrome)
        for j in range(len(acu_list)):
            search_acu = []
            search_cyber_acu = []
            acu_url = base_path1 + acu_list[j]
            acu_data = pd.read_csv(acu_url, header=None, sep='\t', engine='python', error_bad_lines=False,
                                   encoding='utf-8')
            acu_label = acu_data[acu_data[1].str.startswith('S')]
            cyber_acu_label = acu_data[acu_data[1].str.startswith('Cyber')]
            for temp in acu_label[2]:
                search_acu.append(temp.lower())
            search_acu = list(set(search_acu))
            # print(search_acu)

            for item in cyber_acu_label[2]:
                search_cyber_acu.append(item.lower())
            search_cyber_acu = list(set(search_cyber_syndrome))

            for cyber_item in search_cyber_syndrome:
                if cyber_item in search_acu:
                    children_acu_list.append(acu_list[i])

            for m in range(len(disease_symtom)):
                for n in range(len(search_acu)):
                    vec1, vec2 = get_word_vector(disease_symtom[m], search_acu[n])
                    dist1 = cos_dist(vec1, vec2)  # 将矩阵传入
                    if dist1 >= max:
                        children_acu_list.append(acu_list[j])
                        print(disease_symtom[m], search_acu[n], dist1, acu_list[j])
        children_acu_list = list(set(children_acu_list))
        treats_count = treats_count + len(children_acu_list)
        dir_str = show_tree_dir(father_name, children_acu_list)
        write_file = open('output.txt', mode='a+')
        write_file.write(dir_str)
        write_file.write('\n')
        print(dir_str)
        write_file.close()
        print(treats_count)