import folium

# 创建地图
m = folium.Map(location=[39.9, 116.4], zoom_start=12)

# 添加节点
folium.GeoJson('nodes.geojson',
              style_function=lambda x: {'fillColor': '#ff7800', 'color': '#000'}).add_to(m)

# 添加边
folium.GeoJson('edges.geojson',
              style_function=lambda x: {'color': 'gray', 'weight': 2}).add_to(m)

# 保存地图
m.save('map.html')