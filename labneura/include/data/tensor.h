#pragma once

#include <torch/torch.h>
#include <ATen/ATen.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>

namespace py = pybind11;

class Tensor {
public:
    // Constructors
    Tensor();
    Tensor(const py::array& numpy_array);
    Tensor(const std::vector<float>& list);
    Tensor(const at::Tensor& torch_tensor);

    // Convert Python objects to torch::Tensor
    at::Tensor from_numpy(const py::array& numpy_array);
    at::Tensor from_list(const std::vector<float>& list);
    at::Tensor from_pytorch_tensor(const at::Tensor& tensor);

    // Tensor operations
    Tensor add(const Tensor& other) const;
    Tensor multiply(const Tensor& other) const;

    // Return the internal tensor
    at::Tensor getTensor() const;

    // Helper function to detect available device and allocate tensor accordingly
    bool is_cuda_available() const;
    bool is_rocm_available() const;
    bool is_metal_available() const;

    at::Device get_device() const;

private:
    at::Tensor tensor_;
};