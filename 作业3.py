#Action3: 对汽车质量数据进行统计
import pandas as pd

#数据加载
df = pd.DataFrame()
df = pd.read_csv('./car_complain.csv')
#print(df)
#df.to_excel('./car_complain.xlsx',index=False)

#预处理
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#print(df)

#品牌投诉总数，车型投诉总数
df['brand'] = df['brand'].replace("一汽-大众","一汽大众")
result = df.groupby(['brand'])['id'].agg(['count'])
#print(result)

tags = df.columns[7:]
#print(tags)

result2 = df.groupby(['brand'])[tags].agg(['sum'])
#print(result2)

result2 = result.merge(result2, left_index=True, right_index=True, how='left')
#print(result2)

result2.reset_index(inplace=True)
#print(result2)

result2 = result2.sort_values('count', ascending = False)
#print(result2)

query = ('A11','sum')
result2.sort_values(query, ascending = False)[query]
print(result2)

#车型投诉总数
result = df.groupby(['car_model'])['id'].agg(['count'])
#print(result)

tags = df.columns[7:]
#print(tags)

result2 = df.groupby(['brand'])[tags].agg(['sum'])
#print(result2)

result2 = result.merge(result2, left_index=True, right_index=True, how='left')
#print(result2)

result2.reset_index(inplace=True)
#print(result2)

result2 = result2.sort_values('count', ascending = False)
#print(result2)

query = ('A11','sum')
result2.sort_values(query, ascending = False)[query]
#print(result2)

#哪个品牌的平均车型投诉最多
df = (df.groupby(['brand', 'car_model']).mean()
            .groupby('brand')[tags].mean())
print(df)

