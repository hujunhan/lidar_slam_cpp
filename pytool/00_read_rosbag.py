import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path=r'./data/imu.bag'
# read bag file
data=bagreader(file_path)

tp_table=data.topic_table
print(tp_table) 

imu=data.message_by_topic('/auk/fcu/imu')
df_imu = pd.read_csv(imu)

print(df_imu.head(10))

fig, ax = bagpy.create_fig(10)
ax[0].scatter(x = 'Time', y = 'orientation.x', data  = df_imu, s= 1, label = 'orientation.x')
ax[1].scatter(x = 'Time', y = 'orientation.y', data  = df_imu, s= 1, label ='orientation.y')
ax[2].scatter(x = 'Time', y = 'orientation.z', data  = df_imu, s= 1, label = 'orientation.z')
ax[3].scatter(x = 'Time', y = 'orientation.w', data  = df_imu, s= 1, label ='orientation.w')
ax[4].scatter(x = 'Time', y = 'angular_velocity.x', data  = df_imu, s= 1, label = 'angular_velocity.x')
ax[5].scatter(x = 'Time', y = 'angular_velocity.y', data  = df_imu, s= 1, label = 'angular_velocity.y')
ax[6].scatter(x = 'Time', y = 'angular_velocity.z', data  = df_imu, s= 1, label = 'angular_velocity.z')
ax[7].scatter(x = 'Time', y = 'linear_acceleration.x', data  = df_imu, s= 1, label = 'linear_acceleration.x')
ax[8].scatter(x = 'Time', y = 'linear_acceleration.y', data  = df_imu, s= 1, label = 'linear_acceleration.y')
ax[9].scatter(x = 'Time', y = 'linear_acceleration.z', data  = df_imu, s= 1, label = 'linear_acceleration.z')
for axis in ax:
    axis.legend()
    axis.set_xlabel('Time')

plt.show()