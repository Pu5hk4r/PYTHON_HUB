import torch

# Check if PyTorch is installed
print("PyTorch version:", torch.__version__)

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0])
print("Tensor x:", x)

# Perform a basic operation
y = x + 2
print("Tensor y (x + 2):", y)

# Check if CUDA (GPU support) is available
cuda_available = torch.cuda.is_available()
print("CUDA available:", cuda_available)

if cuda_available:
    # Create a tensor on the GPU
    device = torch.device("cuda")
    x_cuda = torch.tensor([1.0, 2.0, 3.0], device=device)
    print("Tensor x on GPU:", x_cuda)
