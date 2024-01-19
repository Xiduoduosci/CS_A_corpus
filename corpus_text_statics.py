import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
#统计语料库的规模大小

base_path = "F:/小论文1实验数据/corpus_final/acupoint corpus"
files = os.listdir(base_path)
sentence_count = 0
tokens_count = 0

for file in files:
    path = base_path+"/"+file
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            if len(line) == 0:
                continue
            number_of_sentence = sent_tokenize(line)
            number_of_words = word_tokenize(line)
            print(number_of_sentence)
            print(number_of_words)
            sentence_count = sentence_count + len(number_of_sentence)
            tokens_count = tokens_count + len(number_of_words)

print("总共有%s个句子" %sentence_count)
print("总共有%s个单词" %tokens_count)
