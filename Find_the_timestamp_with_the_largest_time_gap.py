import pandas as pd
import folium
from geopy.distance import geodesic
import os
from datetime import datetime

# 文件路径
file_path = 'C:/Users/YG175/Desktop/cleaned_cmp_data.csv'
output_folder = 'C:/Users/YG175/Desktop/time_difference'

# 读取数据
df = pd.read_csv(file_path)
df = df.dropna(subset=['natural_index', 'latitude', 'longitude','occurrence_date_time_beijing'])

timestamp_col = 'occurrence_date_time_beijing'
df[timestamp_col] = pd.to_datetime(df[timestamp_col])

# 过滤出 natural_index=29 的数据
subset = df[df['natural_index'] == 29]

# 确保数据按照时间戳排序
subset = subset.sort_values(by=timestamp_col)   

print(df.timestamp)

# 计算相邻时间戳之间的差距
time_diffs = subset[timestamp_col].diff().dt.total_seconds().dropna()

# 找出最大的时间差
max_time_diff = time_diffs.max()

# 找出最大的时间差的索引
max_time_diff_index = time_diffs.idxmax()

# 获取相应的时间戳
max_time_diff_start = subset.loc[max_time_diff_index - 1, 'occurrence_date_time_beijing']
max_time_diff_end = subset.loc[max_time_diff_index, 'occurrence_date_time_beijing']

print(f"Largest time difference: {max_time_diff} seconds between {max_time_diff_start} and {max_time_diff_end}")

