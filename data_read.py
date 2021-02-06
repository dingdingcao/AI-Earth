# -*- coding：utf-8 -*-
from constants import *
import netCDF4 as nc
import matplotlib.pyplot as plt
import seaborn as sns

FILES_DATA=["CMIP_train.nc","SODA_train.nc"]
# print(FILES_DATA)

CMIP_train=nc.Dataset(FILES_DATA[0]) #CMIP_train.nc的路径
SODA_train=nc.Dataset(FILES_DATA[1]) #SODA_train.nc的路径
#查看，.nc文件的数据格式
# print(SODA_train)

#查看.nc文件中的变量
# print(f'variables的type:{type(SODA_train.variables)}')
# print(f'keys of dict:{SODA_train.variables.keys()}')
# keys_of_dict=['sst', 't300', 'ua', 'va', 'year', 'month', 'lat', 'lon']
#海表温度异常(SST)，热含量异常(T300)，纬向风异常（Ua），经向风异常（Va），数据维度为（year,month,lat,lon）

# print(CMIP_train.variables['lat']) #current shape=(24,)
# # print('---')
# # print(CMIP_train.variables['lat'].ncattrs()) #['_FillValue', 'axis', 'units', 'long_name', 'standard_name']
#
# print(SODA_train.variables['sst']) #current shape=(100,36,24,72)
# print('---')
# print(SODA_train.variables['sst'].ncattrs()) #['_FillValue']

# print(SODA_train.variables['year'][:]) #100年
# print("----")
# print(SODA_train.variables['lat'][:]) #-55到60

sst = SODA_train.variables['sst'][:]
# print(type(sst))
# print(sst.shape) #(100,36,24,72)
# print(sst.shape[1])

n = sst.shape[1]
plt.figure(figsize=(20,300),dpi=50)
for i in range(n):
    plt.subplot(n,1,i+1)
    sns.heatmap(sst[0,i,:,:], square=True, cbar=False, xticklabels=False, yticklabels=False)
# plt.savefig("./1.png",format="png",transparent=True,dpi=200)
plt.show()
