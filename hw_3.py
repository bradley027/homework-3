# OCNG 689 Python for Geoscientists 
# Kelley Bradley
# HW 3

import netCDF4 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap 
import pandas as pd 

# Part1: Downloading netCDF data from URL & creates map 
# This map is specifically looking at the global SODA sst field in January of 1998. 
    
# loading in netcdf file & setting up variables 
nc = netCDF4.Dataset("http://apdrc.soest.hawaii.edu:80/dods/public_data/SODA/soda_pop2.2.4")
temp = nc.variables['temp'][1539,0,:,:]
lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

# setting up data into basemap with given projection 
lon, lat = np.meshgrid(lon, lat)
m = Basemap(llcrnrlon=100,llcrnrlat=-90,urcrnrlon=85,urcrnrlat=90,projection='robin',lon_0=180)
x,y = m(lon, lat)            

# drawing the map
fig = plt.figure()
m.fillcontinents(color='black',lake_color='black')
m.drawcoastlines(linewidth = 0.4)
m.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=8)
m.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=8)
m.drawmapboundary()

# plotting data on the map 
plt.contourf(x,y,temp,cmap=plt.cm.Spectral_r)
cb = plt.colorbar(orientation='horizontal')
cb.set_label(r'Sea Surface Temperature (deg C) Jan 1998',fontsize=14,style='italic')
plt.show()
plt.savefig('SST_globeplot_Hw3.png')

# Part 2: making pandas timeseries 

#setting up time for timeseries 
time = nc.variables['time']
temp_pac = nc.variables['temp'][:,0,200,400]
dates = netCDF4.num2date(time[:],time.units)
timeseries = pd.Series(temp_pac,index=dates)
data_frame = pd.DataFrame(timeseries)

#plotting pandas timeseries 
data_frame.plot(figsize=(25.0,5.0),color="blue",legend=False)
plt.title('SODA 2.2.4 SST Monthly Means')
plt.xlabel("Year")
plt.ylabel("Sea Surface Temp (deg C)")
plt.show()
plt.savefig('SST_timeseries_Hw3.png')