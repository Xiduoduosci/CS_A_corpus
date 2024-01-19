import requests
import json
import pandas as pd
import time
#疾病字典获取
def get_time():
    return 0
def get_content():
    root_url = "https://disease-ontology.org/query_tree?_dc=1684411319636&node=root"
    #                       网址前缀                        当前时间戳（毫秒） 请求目录的节点
    content = requests.get(root_url)
    root=json.loads(content.text)
    result_list=[]
    def digui(node_data,prex):
        if node_data["leaf"]==True:#为叶子结点    #递归出口
            result=prex+"||"+node_data['text']
            print(result)
            result_list.append([result])
        else:#不是叶子节点，仍然需要继续递归
            name=node_data["text"]
            id=node_data["id"]
            request_url="https://disease-ontology.org/query_tree?_dc="+str(get_time())+"&node="+id
            time.sleep(2)#休息2s
            request_data = json.loads(requests.get(request_url, timeout=10).text)
            for c in request_data:
                digui(c, prex+"||"+name)
    root_name=root[0]['text']
    root_children_list=root[0]['children']
    for child in root_children_list:
        digui(child,root_name)
    #存储
    pd.DataFrame(result_list).to_csv("带前缀的.csv")
    w_list=[]
    for r in result_list:
        print(r[0])
        w_list.append([r[0].split("||")[-1]])
    pd.DataFrame(w_list).to_csv("不带前缀的.csv")

    for r in result_list:
        w_list.append([r[0].split("||")[-1]])
        w_list.append([r[0].split("||")[-2]])
    pd.DataFrame(w_list).to_csv("disease.csv")

if __name__ == "__main__":
    get_content()