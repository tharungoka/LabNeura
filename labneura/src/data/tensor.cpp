#include "data/tensor.h"

// Default constructor, initializes to an empty tensor on the appropriate device
Tensor::Tensor() {
    tensor_ = at::empty({0}, get_device());
}

// Constructor from numpy array
Tensor::Tensor(const py::array& numpy_array) {
    tensor_ = from_numpy(numpy_array);
}

// Constructor from list
Tensor::Tensor(const std::vector<float>& list) {
    tensor_ = from_list(list);
}

// Constructor from PyTorch tensor
Tensor::Tensor(const at::Tensor& torch_tensor) : tensor_(torch_tensor) {}

// Convert numpy array to torch tensor
at::Tensor Tensor::from_numpy(const py::array& numpy_array) {
    py::buffer_info buf_info = numpy_array.request();
    std::vector<int64_t> shape(buf_info.shape.begin(), buf_info.shape.end());
    return torch::from_blob(buf_info.ptr, shape, torch::kFloat).to(get_device()).clone();
}

// Convert list to torch tensor
at::Tensor Tensor::from_list(const std::vector<float>& list) {
    return torch::tensor(list, torch::kFloat).to(get_device());
}

// Convert tensor to torch tensor
at::Tensor Tensor::from_pytorch_tensor(const at::Tensor& tensor) {
    // Store the tensor in the appropriate device
    return tensor.to(get_device());
}

// Return the internal tensor
at::Tensor Tensor::getTensor() const {
    return tensor_;
}

// Addition of two tensors
Tensor Tensor::add(const Tensor& other) const {
    return Tensor(tensor_ + other.tensor_);
}

// Multiplication of two tensors
Tensor Tensor::multiply(const Tensor& other) const {
    return Tensor(tensor_ * other.tensor_);
}

// Check if CUDA is available
bool Tensor::is_cuda_available() const {
    return torch::cuda::is_available();
}

// Check if ROCm is available
bool Tensor::is_rocm_available() const {
    // PyTorch usually treats ROCm as a CUDA device, so this check works for ROCm as well
    return torch::cuda::is_available();
}

// Check if Metal (Apple's GPU API) is available
bool Tensor::is_metal_available() const {
    return at::hasMPS();
}

// Helper function to get the appropriate device (CUDA, ROCm, Metal, or CPU)
at::Device Tensor::get_device() const {
    if (is_cuda_available()) {
        return at::Device(at::kCUDA);
    } else if (is_rocm_available()) {
        return at::Device(at::kHIP);
    } else if (is_metal_available()) {
        return at::Device(at::kMPS);
    } else {
        return at::Device(at::kCPU);  // Default to CPU (works for both Intel and AMD CPUs)
    }
}