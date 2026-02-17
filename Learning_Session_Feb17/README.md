# 🎯 PyTorch Tensor Initialization - Learning Session
**Date:** February 17, 2026  
**Topic:** Understanding PyTorch Tensor Creation and Initialization  
**Status:** ✅ Completed

---

## 📚 Overview
Today's session focused on mastering tensor initialization in PyTorch, understanding different methods to create tensors, and learning about tensor properties and type conversions.

---

## 🔑 Key Concepts Covered

### 1. **Basic Tensor Creation**
Creating tensors manually with specific data and properties:
```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
my_tensor = torch.tensor([[1,2,3], [4,5,6]], 
                          dtype=torch.float32,
                          device=device,
                          requires_grad=True)
```

**Key Properties:**
- `dtype` - Data type (float32, int64, etc.)
- `device` - CPU or GPU computation location
- `requires_grad` - Enable gradient tracking for backpropagation
- `shape` - Tensor dimensions
- `device` - Current device location

---

### 2. **Specialized Tensor Initialization Methods**

#### **Empty & Zero Initialization**
```python
torch.empty(size=(3,3))      # Uninitialized data
torch.zeros((3,3))            # All zeros
torch.ones((3,3))             # All ones
```

#### **Random Initialization**
```python
torch.rand((3,3))             # Uniform distribution [0,1)
torch.normal_(mean=0, std=1)  # Normal distribution (mean=0, std=1)
torch.uniform_(0, 1)          # Uniform distribution
```

#### **Range & Sequence Creation**
```python
torch.arange(start=1, end=100, step=2)      # Range with step
torch.linspace(start=0.1, end=1, steps=10)  # 10 evenly spaced values
```

#### **Special Matrices**
```python
torch.eye(5, 5)               # Identity matrix (diagonal = 1, rest = 0)
torch.diag(torch.ones(3))     # Diagonal matrix
```

---

### 3. **Data Type Conversions**
Converting tensors between different data types:

| Method | Data Type | Bit Width |
|--------|-----------|-----------|
| `.bool()` | Boolean | 1 bit |
| `.short()` | int16 | 16 bits |
| `.long()` | int64 | 64 bits |
| `.half()` | float16 | 16 bits |
| `.float()` | float32 | 32 bits |
| `.double()` | float64 | 64 bits |

```python
tensor = torch.arange(4)
tensor.float()    # Convert to float32
tensor.double()   # Convert to float64
tensor.long()     # Convert to int64
```

---

### 4. **Tensor ↔ NumPy Conversion**
Seamless conversion between NumPy arrays and PyTorch tensors:

```python
import numpy as np

# NumPy to PyTorch
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)

# PyTorch to NumPy
np_array_back = tensor.numpy()
```

---

## 💡 Important Notes

### Device Management
- **CPU:** Suitable for testing and development (`device = 'cpu'`)
- **GPU:** CUDA for fast computation on compatible hardware
- **Check Availability:** `torch.cuda.is_available()`

### Dtype Considerations
- **float32 :** Default, good balance of precision and memory
- **float64 (double) :** Higher precision, more memory
- **float16 (half) :** Lower precision, less memory, useful for GPUs

### In-place Operations
- Methods ending with `_` modify tensor in-place (e.g., `.normal_()`, `.uniform_()`)
- More memory efficient than creating new tensors

---

## 🎓 Learning Outcomes

✅ Understand tensor creation methods and when to use each  
✅ Master tensor properties (dtype, device, shape, requires_grad)  
✅ Convert between different data types efficiently  
✅ Work with NumPy ↔ PyTorch conversions  
✅ Device-aware tensor initialization (CPU/GPU)  

---

## 📁 Files in This Session

| File | Purpose |
|------|---------|
| `tensor_initialization.py` | Complete examples and demonstrations |
| `README.md` | This comprehensive guide |

---

## 🔄 Review Checklist

- [ ] Understand device selection and availability
- [ ] Know all tensor initialization methods
- [ ] Can convert between data types
- [ ] Can work with NumPy arrays
- [ ] Understand requires_grad and its purpose

---

## 🚀 Next Steps

1. **Tensor Operations:** Learn element-wise operations, matrix multiplication
2. **Shape Manipulation:** Reshape, transpose, and view operations
3. **Indexing & Slicing:** Access and modify tensor elements
4. **Broadcasting:** Understand automatic dimension expansion
5. **Gradient Computation:** Backpropagation and autograd

---

## 📖 Quick Reference

```python
import torch

# Device setup
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Basic creation
t = torch.tensor([[1,2],[3,4]], dtype=torch.float32, device=device)

# Initialization methods
empty = torch.empty(3,3)
zeros = torch.zeros(3,3)
ones = torch.ones(3,3)
identity = torch.eye(3,3)
random = torch.rand(3,3)
normal = torch.randn(3,3)
range_t = torch.arange(0, 10, 2)

# Type conversion
t.float()   # → float32
t.double()  # → float64
t.long()    # → int64

# NumPy conversion
import numpy as np
np_arr = np.zeros(5)
torch_t = torch.from_numpy(np_arr)
```

---

**Happy Learning! 🎉**

