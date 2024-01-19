import requests
import json
import pandas as pd
import time
import random
from urllib import parse
#症状字典获取
def get_time():
    return 0
def get_content():
    root_url = "https://www.ebi.ac.uk/ols4/api/v2/ontologies/symp/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSYMP_0000462/hierarchicalChildren?size=100&lang=en&includeObsoleteEntities=undefined"
    #https://www.ebi.ac.uk/ols/api/ontologies/symp/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSYMP_0000461/jstree/children/184278196_child_5?lang=en
    #https://www.ebi.ac.uk/ols/api/ontologies/symp/terms/http%253A%252F%252Fpurl.obolibrary.org%252obo%252SYMP_0000461/jstree/children/184278196_child_5?lang=en
    content = requests.get(root_url)
    root_data = json.loads(content.text)
    result_list = []
    output = []
    def digui(node_data, prex):
        if node_data["hasDirectChildren"] == 'false':#递归出口
            output.append(node_data['label'])
            result = prex + "||" + node_data['label']
            print(result)
            result_list.append([result])
        else:
            #id = node_data["id"]
            iri = node_data["iri"]
            name = node_data["label"]
            output.append(name)
            #print(name)
            new_iri = iri.replace("://", "%253A%252F%252F").replace("/", '%252F')
            child_url = 'https://www.ebi.ac.uk/ols4/api/v2/ontologies/symp/classes/' + new_iri + "/hierarchicalChildren?size=100&lang=en&includeObsoleteEntities=undefined"
            #print(child_url)
            #print(node_data["hasDirectChildren"])
            time.sleep(2)  # 休息2s
            child_content= json.loads(requests.get(child_url).text)
            for child in child_content['elements']:
                digui(child, prex+"||"+name)


    for child in root_data['elements']:
        digui(child, "symptom")

    #存储
    pd.DataFrame(result_list).to_csv("symptom_带前缀的.csv")
    w_list=[]
    for r in result_list:
        w_list.append([r[0].split("||")[-1]])
    pd.DataFrame(w_list).to_csv("symptom_不带前缀的.csv")

    for r in result_list:
        w_list.append([r[0].split("||")[-1]])
        w_list.append([r[0].split("||")[-2]])
    pd.DataFrame(w_list).to_csv("symptom.csv")

if __name__ == "__main__":
    get_content()