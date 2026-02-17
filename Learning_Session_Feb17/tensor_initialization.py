import torch

# ====================================#

#         INITIALIZING TENSOR

# ====================================#

device = 'cuda' if torch.cuda.is_available() else 'cpu' 

print("Available device" , device)
my_tensor = torch.tensor([[1,2,3],
                          [4,5,6]] , 
                          dtype = torch.float32,
                          device = device,
                          requires_grad = True)

print(my_tensor)

print(my_tensor.dtype)

print(my_tensor.device)

print(my_tensor.shape)

print(my_tensor.requires_grad)



# ====================================#

#        OTHER INITIALIZING METHODS

# ====================================#

#Create tensor with required shape with un initialized data
x = torch.empty(size = (3,3))

print(x)


x = torch.zeros((3,3))


print(print(x))

x = torch.rand((3,3))
x = torch.ones((3,3))

#Identity Matrix , only diagonal 1 rest 0
x = torch.eye(5,5)

#Range start,stop , step

x = torch.arange(start = 1,end = 100,step = 2)

print(x)

x = torch.linspace(start = 0.1 , end = 1 , steps = 10)

print(x)


#makes the values normally distributed with mean 0 and std 1

x = torch.empty(size = (1,5)).normal_(mean = 0 , std = 1)

print(x)
#makes the values uniformly distributed

x = torch.empty(size = (1,5)).uniform_(0,1)

print(x)

x = torch.diag(torch.ones(3))

print(x)


tensor = torch.arange(4)

print(tensor.bool()) #boolen True / False
print(tensor.short()) #float 16
print(tensor.long()) #int 64
print(tensor.half()) #float 16

print(tensor.float()) #float 32

print(tensor.double()) #float 64


import numpy as np 


np_array = np.zeros((5,5))

tensor = torch.from_numpy(np_array)

print('numpy to torch -> : ' ,tensor , tensor.shape)
