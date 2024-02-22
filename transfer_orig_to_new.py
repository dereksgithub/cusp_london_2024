import pandas as pd

c1 = pd.read_csv('./data/merged_journeys_new.csv')
joined = pd.read_csv('station_borough_all.csv')

# 将df_boroughs转换为地点到borough的映射字典
borough_dict = joined.set_index('Station')['borough'].to_dict()
# print(borough_dict)

# 切片原始数据集的station数据
stat1 = (c1['Start station'].str.split(',', expand=True)).iloc[:,1]
stat2 = (c1['Start station'].str.split(',', expand=True)).iloc[:,1]

# 使用.map()函数替换df_data中的地点为对应的borough
# print(stat.map(borough_dict))
c1['Start borough'] = stat1.map(borough_dict)
c1['End borough'] = stat2.map(borough_dict)
c1.to_csv('./data/merged_journeys_new_with_borough.csv', index=False)
