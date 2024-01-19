import re
#穴位语料的获取
import requests
from bs4 import BeautifulSoup

#爬取英文穴位语料

url = "https://tcmwiki.com/wiki/acupoints"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
response = requests.get(url, headers)
soup = BeautifulSoup(response.content, 'html.parser')
acupoint_list = soup.find_all("li")

acupoint_file_name = []
pattern = re.compile("[a-zA-Z]")
path = []
for i in range(13, 374):
    tmp_name = acupoint_list[i].text
    acupoint_file_name.append("".join(re.findall(pattern, tmp_name)))



for i in range(len(acupoint_file_name)):
    path.append("https://tcmwiki.com/wiki/"+acupoint_file_name[i].lower())

for i in range(len(path)):
    res = requests.get(path[i], headers)
    sp = BeautifulSoup(res.content, 'html.parser')
    pattern = re.compile("1 #")
    for content in sp.find_all("div", {"class": "col s12 p_content"}):
        sentence = content.text
        ss = re.sub(pattern, "", sentence)
        with open("C:/Users/Wenxi Wang/Desktop/acu_en/"+acupoint_file_name[i]+".txt", 'w+', encoding='utf-8') as f:
            f.write(ss)
        f.close()






