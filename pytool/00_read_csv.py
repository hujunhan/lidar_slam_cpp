## Script to read a large csv file and print the first 10 lines

import csv
import numpy as np
import open3d as o3d

csv_path = "/home/darkblue/Downloads/outdoor.csv"

## Read the first 10 lines
read_lines = 3

## count total lines
# total_lines = sum(1 for line in open(csv_path, 'r'))
# print(f'Total lines: {total_lines}')

for i, line in enumerate(csv.reader(open(csv_path, "r"))):
    if i == read_lines:
        break
    print(line)

row_item_num = len(line)

## use numpy to read the csv file as a buffer
# every time read 32000 lines

total_frames = 2400
reader = open(csv_path, "r")
reader.readline()
buffer_size = 32000
data = np.empty((buffer_size, row_item_num))
for i in range(10):
    print(f"current frame {i}")
    data = np.genfromtxt(
        reader,
        delimiter=",",
        max_rows=buffer_size,
        missing_values=None,
        filling_values=0,
        usecols=range(0, 5),
    )
    print(np.mean(data[:, 0], axis=0))
