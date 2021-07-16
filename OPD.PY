import webbrowser

import numpy as np
import pandas as pd
import folium
from folium import plugins

latitude = 28.5382
longitude = -81.3792


df_crimes =pd.read_excel("C:\\Users\\Aavak\\Desktop\\Everything You Need\\Excel Doc's for Python\\OPD_Crimes.xlsx")
df_crimes.dropna(inplace=True)

limit = 100
df_crimes = df_crimes.iloc[0:limit, :]


orl_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(orl_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_crimes.Y, df_crimes.X, df_crimes['Case Offense Category']):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)

path="C:\\Users\\Aavak\\Desktop\\Everything You Need\\Excel Doc's for Python\\"
filename = 'OrlPDcrimes.html'
orl_map.save(path+filename)






def auto_open(path):
    html_page = f'{path}'
    orl_map.save(html_page)
    # open in browser.
    new = 2
    webbrowser.open(html_page, new=new)

auto_open(path+filename)


