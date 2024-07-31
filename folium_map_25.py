# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:28:44 2024

@author: yg175
"""

import folium
from geopy.distance import geodesic
import pandas as pd

file_path = 'C:/Users/YG175/Desktop/trip_25_map/2024_0402_trip_record.csv'
df = pd.read_csv(file_path)
latitudes = df['latitude'].tolist()
longitudes = df['longitude'].tolist()

total_distance = 0.0
for i in range(1, len(latitudes)):
    start_point = (latitudes[i-1], longitudes[i-1])
    end_point = (latitudes[i], longitudes[i])
    total_distance += geodesic(start_point, end_point).kilometers
        
print(f"Total distance: {total_distance:.2f} kilometers")

# 创建地图对象
m = folium.Map(location=[latitudes[0], longitudes[0]], zoom_start=13)

#加路径
path = list(zip(latitudes, longitudes))
folium.PolyLine(path, color="blue", weight=2.5, opacity=1).add_to(m)

# 添加起点和终点标记
folium.Marker(location=[latitudes[0], longitudes[0]], popup="Start", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(location=[latitudes[-1], longitudes[-1]], popup="End", icon=folium.Icon(color="red")).add_to(m)

# 保存地图为 HTML 文件
output_file = "path_map_25.html"
m.save(output_file)