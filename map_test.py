import folium

# 创建一个 Folium 地图对象
m = folium.Map(location=[39.9, 116.4], zoom_start=13)

# 保存生成的 HTML
m.save("map.html")
