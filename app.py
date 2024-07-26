import torch

data = [[1,2,3,4], [3,4,5,6]]

x_data = torch.tensor(data)

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(x_rand)