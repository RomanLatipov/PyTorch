import torch

# 5x3 tensor of zeros
z = torch.zeros(5, 3)
print(z)
print(z.dtype)

# 5x3 tensor of ones
i = torch.ones((5, 3), dtype=torch.int16)
print(i)

#tensors with the same seed create the same tensor
torch.manual_seed(1729)
r1 = torch.rand(2, 2)
print('A random tensor:')
print(r1)

r2 = torch.rand(2, 2)
print('\nA different random tensor:')
print(r2) # new values

torch.manual_seed(1729)
r3 = torch.rand(2, 2)
print('\nShould match r1:')
print(r3)

# combining tensors
ones = torch.ones(2, 3)
print(ones)

twos = torch.ones(2, 3) * 2 # twos = ones * 2
print(twos)

# add the values of 2 tensors of the same size
threes = ones + twos 
print(threes)              
print(threes.shape)

#tensors must be the same size; will cause error
# r1 = torch.rand(2, 3)
# r2 = torch.rand(3, 2)
# r3 = r1 + r2

# values between -1 and 1
r = torch.rand(2, 2) - 0.5 * 2  
print('A random matrix, r:')
print(r)

# common mathematical operations
print('\nAbsolute value of r:')
print(torch.abs(r))

# statistical and aggregate operations:
print('\nAverage and standard deviation of r:')
print(torch.std_mean(r))

print('\nMaximum value of r:')
print(torch.max(r))