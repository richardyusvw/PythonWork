import pandas as pd
from efficient_apriori import apriori

pd.set_option('max_columns', None)
#数据加载
# header=None，不将第一行作为head
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
print(dataset)
print(dataset.shape) 
# shape为(7501,20)

transactions = []
#按行进行遍历
for i in range(0, dataset.shape[0]):
    #记录一行Transaction
    temp = []
    #按照列进行遍历
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i,j]) != 'nan':
          temp.append(dataset.values[i,j])
    #print(temp)
transactions.append(temp)

#数据关联分析
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.4)
print('频繁项集:', itemsets)
print('关联规则:', rules)

