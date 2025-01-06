import torch
import numpy as np
arr=np.ones((3,3))
print("arr的数据类型为："+str(arr.dtype))
t=torch.tensor(arr)
print(t)

