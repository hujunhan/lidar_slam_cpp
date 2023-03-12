## Script to read a large csv file and print the first 10 lines

import csv
import numpy as np
import open3d as o3d
csv_path = '/Users/hu/Downloads/C16_v4.0.0_2023-03-11-13-02_660Frame.csv'

## Read the first 10 lines
read_lines = 3

## count total lines
# total_lines = sum(1 for line in open(csv_path, 'r'))
# print(f'Total lines: {total_lines}')

for i, line in enumerate(csv.reader(open(csv_path, 'r'))):
    if i == read_lines:
        break
    print(line)

row_item_num = len(line)

## Use numpy to read the first 32000 lines (exclude the first line)
data = np.genfromtxt(csv_path, delimiter=',', skip_header=1+32000*5, max_rows=32000,missing_values=None)

print(data.shape)

print(data[:10,0])
print(data[-10:,0])

point_cloud=data[:,2:5]
print(point_cloud.shape)

## Use open3d to visualize the point cloud
pcl=o3d.geometry.PointCloud()
pcl.points=o3d.utility.Vector3dVector(point_cloud)
o3d.visualization.draw_geometries([pcl])