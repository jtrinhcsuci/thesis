import torch
from torch.utils.data import Dataset, DataLoader, TensorDataset
import torchvision.transforms as T
import torchvision.datasets


import pandas as pd
data_points = pd.read_csv("Data_Points.csv")

batch_size = 256
train_data = data_points[:batch_size]

#print(data_points[:500])
# # Sample a fixed batch of 1024 validation examples
# val_x, val_l = zip(*list(data_points[i] for i in range(1024)))
# val_x = torch.stack(val_x, 0).cuda()
# val_l = torch.LongTensor(val_l).cuda()



# # Exclude the validation batch from the training data
# validation_data = data_points.data[1024:]

train_loader  = DataLoader(train_data, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True, drop_last=True)
# test_loader   = DataLoader(test_data,  batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True, drop_last=True)
