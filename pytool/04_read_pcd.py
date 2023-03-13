import open3d
import numpy as np
file_path='/home/darkblue/code/oh_my_loam/data/test_csv/frame_00002.pcd'
file_path='/home/darkblue/code/oh_my_loam/data/nsh/1422133389.108526080.pcd'
pcd = open3d.io.read_point_cloud(file_path)

points=np.asarray(pcd.points)

print(f'mean: {np.mean(points, axis=0)}')