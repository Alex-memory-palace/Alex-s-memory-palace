import pandas as pd
import folium
from geopy.distance import geodesic
import os


file_path = 'C:/Users/YG175/Desktop/cleaned_cmp_data.csv'
output_folder = 'C:/Users/YG175/Desktop/trip_demonstration'


df = pd.read_csv(file_path)
df = df.dropna(subset=['natural_index', 'latitude', 'longitude'])
df['natural_index'] = df['natural_index'].astype(int)
natural_indices = sorted(df['natural_index'].unique())
total_distances = []


for index in natural_indices:
    subset = df[df['natural_index'] == index]
    latitudes = subset['latitude'].tolist()
    longitudes = subset['longitude'].tolist()

    total_distance = 0.0
    for i in range(1, len(latitudes)):
        start_point = (latitudes[i-1], longitudes[i-1])
        end_point = (latitudes[i], longitudes[i])
        total_distance += geodesic(start_point, end_point).kilometers

    total_distances.append((index, total_distance))

    
    m = folium.Map(location=[latitudes[0], longitudes[0]], zoom_start=13)

    
    path = list(zip(latitudes, longitudes))
    folium.PolyLine(path, color="blue", weight=2.5, opacity=1).add_to(m)

    
    folium.Marker(location=[latitudes[0], longitudes[0]], popup="Start", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(location=[latitudes[-1], longitudes[-1]], popup="End", icon=folium.Icon(color="red")).add_to(m)

    
    output_file = os.path.join(output_folder, f"path_map_{index}.html")
    m.save(output_file)


total_distances_sorted = sorted(total_distances, key=lambda x: x[0])
print(total_distances_sorted)


