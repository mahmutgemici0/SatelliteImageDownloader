import pandas as pd

csv_file = 'airport-data.csv'
df = pd.read_csv('datasets_positive/airport-data.csv')

latitudes = df['ARP Latitude Sec']
longitudes = df['ARP Longitude Sec']

def lat_lon_converter(latitudes, longitudes):

    """
    Converts lat and long seconds to degree decimal.

    lat = 229559.8190N  ---->> 63.766616388888885
    lon = 0618238.0220W ---->> -171.73278388888886

    GoogleMapDownloader.py takes degree decimal
    """

    lat = []
    lon = []
    
    for i in latitudes:
        if i[-1] == "N":   # North
            i = i[:-1]
        elif i[-1] == "S": # South
            i = "-" + i[:-1]
            
        i = float(i)
        degree = i//3600
        remainder = i % 3600
        mins = remainder // 60
        secs = remainder % 60
        dd = degree + mins/60 + secs/3600
        lat.append(dd)

    for i in longitudes:
        if i[-1] == "E":   # East
            i = i[:-1]
        elif i[-1] == "W": # West 
            i = "-" + i[:-1]
        
        i = float(i)
        degree = i//3600
        remainder = i % 3600
        mins = remainder // 60
        secs = remainder % 60
        dd = degree + mins/60 + secs/3600
        lon.append(dd)

    return lat,lon


lat, lon = lat_lon_converter(latitudes, longitudes)

df["DD_Latitudes"] = lat
df["DD_Longitudes"] = lon

df.to_csv('datasets_positive/airport-data.csv')