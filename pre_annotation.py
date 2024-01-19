import os
import pandas as pd
import re
from tqdm import tqdm
#加载疾病数据，进行语料库的预标注
df_disease = pd.read_csv("F:/小论文1实验数据/corpus_final/disease.csv", header=None, sep='\t', engine='python', error_bad_lines=False, encoding='gbk')
df_cyber_disease = pd.read_csv("F:/小论文1实验数据/corpus_final/cyber_syndrome_dic.csv", header=None, sep='\t', engine='python', error_bad_lines=False, encoding='gbk')
df_syndrome = pd.read_csv("F:/小论文1实验数据/corpus_final/symptom.csv", header=None, sep='\t', engine='python', error_bad_lines=False, encoding='gbk')
df_acupoint = pd.read_csv("F:/小论文1实验数据/corpus_final/acupoint.csv", header=None, sep='\t', engine='python', error_bad_lines=False, encoding='gbk')
#print(len(set(df_disease[0])))#确认没有重复的疾病名
disease_list=list(set(df_disease[0]))
cyber_syndrome_list = list(set(df_cyber_disease[0]))
syndrome_list = list(set(df_syndrome[0]))
acupoint_list = list(set(df_acupoint[0]))
#遍历每一个语料库文件
base_path="F:/小论文1实验数据/corpus_final/corpus"
disease_count = 0
cyber_syndrome_count = 0
syndrome_count = 0
acupoint_count = 0

for name in os.listdir(base_path):
    print("file_name-----%s"%name)#打印文件名
    file_path = base_path+"/"+name
    exist_disease_list = []
    exist_cyber_syndrome_list = []
    exist_syndrome_list = []
    exist_acupoint_list = []

    if re.search("\d", name):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines(): #遍历每一行,因为不同行之间是不同的句子。
                for disease in disease_list: #便利每个疾病
                    if disease.lower() in line.lower():
                        number = line.lower().count(disease) #判断这一行有几个该疾病
                        for i in range(number):
                            exist_disease_list.append(disease)
                    else:
                        pass

                for cyber_syndrome in cyber_syndrome_list:
                    if cyber_syndrome.lower() in line.lower():
                        cyber_number = line.lower().count(cyber_syndrome)
                        for i in range(cyber_number):
                            exist_cyber_syndrome_list.append(cyber_syndrome)
                    else:
                        pass

                for syndrome in syndrome_list:
                    if syndrome.lower() in line.lower():
                        syndrome_number = line.lower().count(syndrome)
                        for i in range(syndrome_number):
                            exist_syndrome_list.append(syndrome)
                    else:
                        pass

        # print('syndrome_count:%s'%len(syndrome_list))

    else:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = re.sub("\(.*\)", "", line)
                for acupoint in acupoint_list:
                    if acupoint.lower() in line.lower():
                        acupoint_number = line.lower().count(acupoint)
                        for i in range(acupoint_number):
                            exist_acupoint_list.append(acupoint)
                    else:
                        pass

                for disease in disease_list:  # 便利每个疾病
                    if disease.lower() in line.lower():
                        number = line.lower().count(disease)  # 判断这一行有几个该疾病
                        for i in range(number):
                            exist_disease_list.append(disease)
                    else:
                        pass

                for cyber_syndrome in cyber_syndrome_list:
                    if cyber_syndrome.lower() in line.lower():
                        cyber_number = line.lower().count(cyber_syndrome)
                        for i in range(cyber_number):
                            exist_cyber_syndrome_list.append(cyber_syndrome)
                    else:
                        pass

                for syndrome in syndrome_list:
                    if syndrome.lower() in line.lower():
                        syndrome_number = line.lower().count(syndrome)
                        for i in range(syndrome_number):
                            exist_syndrome_list.append(syndrome)
                    else:
                        pass

    for a in exist_acupoint_list:
        print("Acupoint-------%s" % a)
    for d in exist_disease_list:
        print("Disease---%s" % d)
    for c in exist_cyber_syndrome_list:
        print("Cyber-Syndrome----%s" % c)
    for s in exist_syndrome_list:
        print("Syndrome----%s" % s)

    acupoint_count = acupoint_count + len(exist_acupoint_list)
    disease_count = disease_count + len(exist_disease_list)
    cyber_syndrome_count = cyber_syndrome_count + len(exist_cyber_syndrome_list)
    syndrome_count = syndrome_count + len(exist_syndrome_list)

print('The total of the diseases:%s' %disease_count)
print('The total of the Cyber-Syndrome:%s' %cyber_syndrome_count)
print('The total of the Syndrome:%s'%syndrome_count)
print('The total of the Acupoint:%s'%acupoint_count)