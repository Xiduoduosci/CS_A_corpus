import pandas as pd

# path1 = "C:/Users/Wenxi Wang/Desktop/disease.csv"
# ann = pd.read_csv(path1, header=None).values.tolist()
# lists = []
# copy_norepeat = []
# for i in range(len(ann)):
#     lists.append(ann[i][0])
#
# copy_norepeat = list(set(lists))
# print(copy_norepeat)
# pd.DataFrame(copy_norepeat).to_csv('disease.csv')
#
# print(len(copy_norepeat))

path1 = "C:/Users/Wenxi Wang/Desktop/symptom.csv"
ann = pd.read_csv(path1, header=None).values.tolist()
lists = []
copy_norepeat = []
for i in range(len(ann)):
    lists.append(ann[i][0])

copy_norepeat = list(set(lists))
print(copy_norepeat)
pd.DataFrame(copy_norepeat).to_csv('symptom.csv')
print(len(copy_norepeat))


