# Chưa kịp add vào app chính

# Map cho report data

import plotly
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import io
import plotly.express as px
from geopy.geocoders import Nominatim, GoogleV3
import webbrowser
#print(plotly.__version__)
base_url= "https://maps.googleapis.com/maps/api/geocode/json?"
AUTH_KEY = 'AIzaSyA5y5AeQ-PE6Jr4L6z9_5sVuVEHu9LYFJI'
geolocator = GoogleV3(api_key=AUTH_KEY)
#File database realtime
data = 'data.txt'
df = pd.read_csv(data, header=None)
df.columns = ['Count', 'Address']
#df = pd.read_csv(io.StringIO(data))
df["loc"] = df["Address"].apply(geolocator.geocode)
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
df[['lat', 'lon', 'altitude']] = pd.DataFrame(list(df["point"]), index=df.index)
#m = folium.Map(location=df[["lat", "lon"]].mean().to_list(), zoom_start=13)
m = folium.Map(location=list(df[["lat", "lon"]].mean()), zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)
for i,r in df.iterrows():
  location = (r["lat"], r["lon"])
  folium.Marker(location=location,popup = str(r['Count']),tooltip=str(r['Count'])).add_to(marker_cluster)
m.save("map.html")
webbrowser.open("map.html")
'''def get_frame(url,width,height):
html = """ 
        <!doctype html>
    <html>
    <iframe id="myIFrame" width="{}" height="{}" src={}""".format(width,height,url) + """ frameborder="0"></iframe>
    <script type="text/javascript">
    var resizeIFrame = function(event) {
        var loc = document.location;
        if (event.origin != loc.protocol + '//' + loc.host) return;

        var myIFrame = document.getElementById('myIFrame');
        if (myIFrame) {
            myIFrame.style.height = event.data.h + "px";
            myIFrame.style.width  = event.data.w + "px";
        }
    };
    if (window.addEventListener) {
        window.addEventListener("message", resizeIFrame, false);
    } else if (window.attachEvent) {
        window.attachEvent("onmessage", resizeIFrame);
    }
    </script>
    </html>"""

popup = get_frame(url,
                  width,
                  height)

marker = folium.CircleMarker([lat,lon],
                             radius=radius,
                             color='#3186cc',
                             fill_color = '#3186cc',
                             popup=popup)

marker.add_to(map)



iframe = folium.element.IFrame(html=html,width=width,height=height)
popup = folium.Popup(iframe,max_width=width)
return popup'''
