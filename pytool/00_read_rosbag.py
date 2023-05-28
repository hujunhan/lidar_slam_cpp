import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# READ THE ROSBAG FILE FIRST TIME
# file_path=r'./data/imu.bag'
# # read bag file
# data=bagreader(file_path)

# tp_table=data.topic_table
# print(tp_table)

# read the imu date to dataframe
# save to csv file
# imu=data.message_by_topic('/imus/data_raw')


csv_file = r"./data/imu/imus-data_raw.csv"
df_imu = pd.read_csv(csv_file, sep=",", header=0)

acc_x = df_imu["linear_acceleration.x"]
acc_y = df_imu["linear_acceleration.y"]
acc_z = df_imu["linear_acceleration.z"]
ang_x = df_imu["angular_velocity.x"]
ang_y = df_imu["angular_velocity.y"]
ang_z = df_imu["angular_velocity.z"]

## plt the downsampled data
plt.scatter(range(len(acc_x[::100])), acc_x[::100], s=1)
plt.show()
