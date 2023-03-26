import geopandas as gpd
import folium

# Read the shapefile
gdf = gpd.read_file('guangdong.shp', encoding='utf-8')

# Set the CRS of the GeoDataFrame
gdf = gdf.set_crs('EPSG:4326')

# Create a new map
m = folium.Map(location=[23.5, 116.5], zoom_start=7)

# Add the shapefile to the map
folium.GeoJson(gdf).add_to(m)

# Save the map as an HTML file
m.save('map.html')



# %%

import geopandas as gpd
import matplotlib.pyplot as plt

# Read the shapefile
gdf = gpd.read_file('guangdong.shp', encoding='utf-8')

# Plot the map
gdf.plot()

# Show the plot
plt.show()

# %%
import shapefile
import matplotlib.pyplot as plt

# Read the shapefile
sf = shapefile.Reader("guangdong.shp")

# Plot the map
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x, y)

# Show the plot
plt.show()

# %%
import shapefile
import matplotlib.pyplot as plt

# Read the shapefile
sf = shapefile.Reader("guangdong.shp")

# Plot the map
for shape in sf.shapeRecords():
    x, y = zip(*shape.shape.points)
    plt.plot(x, y)

# Show the plot
plt.show()




