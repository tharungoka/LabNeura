#pragma once
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "data/list.h"
#include "data/queue.h"
#include "data/stack.h"
#include "data/vector.h"
#include "data/deque.h"
#include "data/forward_list.h"
#include "data/set.h"
#include "data/map.h"
#include "data/unordered_set.h"
#include "data/unordered_map.h"
#include "data/tensor.h"

namespace py = pybind11;

void bind_tensor(py::module& m) {
    py::class_<Tensor>(m, "Tensor")
        .def(py::init<>())  // Default constructor
        .def(py::init<const py::array&>())  // Numpy array constructor
        .def(py::init<const std::vector<float>&>())  // List constructor
        .def(py::init<const at::Tensor&>())  // PyTorch tensor constructor
        
        // Methods
        .def("get_tensor", &Tensor::getTensor)
        .def("add", &Tensor::add)
        .def("multiply", &Tensor::multiply)
        .def("is_cuda_available", &Tensor::is_cuda_available)
        .def("is_rocm_available", &Tensor::is_rocm_available)
        .def("is_metal_available", &Tensor::is_metal_available)
        
        // Static methods for convenience
        .def("from_numpy", &Tensor::from_numpy)
        .def("from_list", &Tensor::from_list)
        .def("from_pytorch_tensor", &Tensor::from_pytorch_tensor);
}


template <typename T>
void bind_vector_wrapper(py::module &m) {
    py::class_<VectorWrapper<T>>(m, "Vector")
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::vector<T>>())

        .def("size", &VectorWrapper<T>::size)
        .def("max_size", &VectorWrapper<T>::max_size)
        .def("resize", &VectorWrapper<T>::resize)
        .def("capacity", &VectorWrapper<T>::capacity)
        .def("empty", &VectorWrapper<T>::empty)
        .def("reserve", &VectorWrapper<T>::reserve)
        .def("shrink_to_fit", &VectorWrapper<T>::shrink_to_fit)

        .def("at", &VectorWrapper<T>::at)
        .def("__getitem__", &VectorWrapper<T>::operator[])
        .def("__len__", &VectorWrapper<T>::__len__)
        .def("front", &VectorWrapper<T>::front)
        .def("back", &VectorWrapper<T>::back)
        .def("data", &VectorWrapper<T>::getData, py::return_value_policy::reference_internal)

        .def("push_back", &VectorWrapper<T>::push_back)
        .def("pop_back", &VectorWrapper<T>::pop_back)
        .def("insert", &VectorWrapper<T>::insert)
        .def("erase", &VectorWrapper<T>::erase)
        .def("clear", &VectorWrapper<T>::clear)
        .def("swap", &VectorWrapper<T>::swap)

        .def("find", &VectorWrapper<T>::find)

        .def("__iter__", [](VectorWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](VectorWrapper<T> &v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_vector(py::module &m, const std::string &typestr) {
    py::class_<VectorWrapper<T>>(m, ("Vector" + typestr).c_str())
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::vector<T>>())

        .def("size", &VectorWrapper<T>::size)
        .def("max_size", &VectorWrapper<T>::max_size)
        .def("resize", &VectorWrapper<T>::resize)
        .def("capacity", &VectorWrapper<T>::capacity)
        .def("empty", &VectorWrapper<T>::empty)
        .def("reserve", &VectorWrapper<T>::reserve)
        .def("shrink_to_fit", &VectorWrapper<T>::shrink_to_fit)

        .def("at", &VectorWrapper<T>::at)
        .def("__getitem__", &VectorWrapper<T>::operator[])
        .def("__len__", &VectorWrapper<T>::__len__)
        .def("front", &VectorWrapper<T>::front)
        .def("back", &VectorWrapper<T>::back)
        .def("data", &VectorWrapper<T>::getData, py::return_value_policy::reference_internal)

        .def("push_back", &VectorWrapper<T>::push_back)
        .def("pop_back", &VectorWrapper<T>::pop_back)
        .def("insert", &VectorWrapper<T>::insert)
        .def("erase", &VectorWrapper<T>::erase)
        .def("clear", &VectorWrapper<T>::clear)
        .def("swap", &VectorWrapper<T>::swap)

        .def("find", &VectorWrapper<T>::find)

        .def("__iter__", [](VectorWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](VectorWrapper<T> &v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_deque_wrapper(py::module &m) {
    py::class_<DequeWrapper<T>>(m, "Deque")
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::deque<T>>())

        .def("size", &DequeWrapper<T>::size)
        .def("max_size", &DequeWrapper<T>::max_size)
        .def("resize", &DequeWrapper<T>::resize)
        .def("empty", &DequeWrapper<T>::empty)
        .def("shrink_to_fit", &DequeWrapper<T>::shrink_to_fit)
        .def("at", &DequeWrapper<T>::at)
        .def("__getitem__", &DequeWrapper<T>::operator[])
        .def("data", &DequeWrapper<T>::getData, py::return_value_policy::reference_internal)
        .def("front", &DequeWrapper<T>::front)
        .def("back", &DequeWrapper<T>::back)

        .def("push_back", &DequeWrapper<T>::push_back)
        .def("push_front", &DequeWrapper<T>::push_front)
        .def("pop_back", &DequeWrapper<T>::pop_back)
        .def("pop_front", &DequeWrapper<T>::pop_front)
        .def("insert", &DequeWrapper<T>::insert)
        .def("erase", &DequeWrapper<T>::erase)
        .def("clear", &DequeWrapper<T>::clear)
        .def("swap", &DequeWrapper<T>::swap)

        .def("find", &DequeWrapper<T>::find)

        .def("__iter__", [](DequeWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](DequeWrapper<T> &v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>())
        .def("__len__", &DequeWrapper<T>::__len__);
}

template <typename T>
void bind_deque(py::module &m, const std::string &type) {
    py::class_<DequeWrapper<T>>(m, ("Deque" + type).c_str())
         .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::deque<T>>())

        .def("size", &DequeWrapper<T>::size)
        .def("max_size", &DequeWrapper<T>::max_size)
        .def("resize", &DequeWrapper<T>::resize)
        .def("empty", &DequeWrapper<T>::empty)
        .def("shrink_to_fit", &DequeWrapper<T>::shrink_to_fit)
        .def("at", &DequeWrapper<T>::at)
        .def("__getitem__", &DequeWrapper<T>::operator[])
        .def("data", &DequeWrapper<T>::getData, py::return_value_policy::reference_internal)
        .def("front", &DequeWrapper<T>::front)
        .def("back", &DequeWrapper<T>::back)

        .def("push_back", &DequeWrapper<T>::push_back)
        .def("push_front", &DequeWrapper<T>::push_front)
        .def("pop_back", &DequeWrapper<T>::pop_back)
        .def("pop_front", &DequeWrapper<T>::pop_front)
        .def("insert", &DequeWrapper<T>::insert)
        .def("erase", &DequeWrapper<T>::erase)
        .def("clear", &DequeWrapper<T>::clear)
        .def("swap", &DequeWrapper<T>::swap)

        .def("find", &DequeWrapper<T>::find)

        .def("__iter__", [](DequeWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](DequeWrapper<T> &v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>())
        .def("__len__", &DequeWrapper<T>::__len__);
}

template <typename T>
void bind_list_wrapper(py::module &m) {
    py::class_<ListWrapper<T>>(m, "List")
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::list<T>>())

        .def("size", &ListWrapper<T>::size)
        .def("empty", &ListWrapper<T>::empty)

        .def("push_back", &ListWrapper<T>::push_back)
        .def("push_front", &ListWrapper<T>::push_front)
        .def("pop_back", &ListWrapper<T>::pop_back)
        .def("pop_front", &ListWrapper<T>::pop_front)
        .def("clear", &ListWrapper<T>::clear)
        .def("insert", &ListWrapper<T>::insert)
        .def("erase", &ListWrapper<T>::erase)

        .def("front", &ListWrapper<T>::front)
        .def("back", &ListWrapper<T>::back)
        .def("data", &ListWrapper<T>::getData)
        .def("find", &ListWrapper<T>::find)

        .def("__len__", &ListWrapper<T>::size)  // Python's len() function
        .def("__iter__", [](ListWrapper<T>& v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](ListWrapper<T>& v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_list(py::module &m, const std::string &type) {
    py::class_<ListWrapper<T>>(m, ("List" + type).c_str())
        .def(py::init<>())
        .def(py::init<size_t>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::list<T>>())

        .def("size", &ListWrapper<T>::size)
        .def("empty", &ListWrapper<T>::empty)

        .def("push_back", &ListWrapper<T>::push_back)
        .def("push_front", &ListWrapper<T>::push_front)
        .def("pop_back", &ListWrapper<T>::pop_back)
        .def("pop_front", &ListWrapper<T>::pop_front)
        .def("clear", &ListWrapper<T>::clear)
        .def("insert", &ListWrapper<T>::insert)
        .def("erase", &ListWrapper<T>::erase)

        .def("front", &ListWrapper<T>::front)
        .def("back", &ListWrapper<T>::back)
        .def("data", &ListWrapper<T>::getData)
        .def("find", &ListWrapper<T>::find)

        .def("__len__", &ListWrapper<T>::size)  // Python's len() function
        .def("__iter__", [](ListWrapper<T>& v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__reversed__", [](ListWrapper<T>& v) { return py::make_iterator(v.rbegin(), v.rend()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_forward_list_wrapper(py::module &m) {
    py::class_<ForwardListWrapper<T>>(m, "ForwardList")
        .def(py::init<>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::forward_list<T>>())
        .def("empty", &ForwardListWrapper<T>::empty)
        .def("front", &ForwardListWrapper<T>::front)
        .def("push_front", &ForwardListWrapper<T>::push_front)
        .def("pop_front", &ForwardListWrapper<T>::pop_front)
        .def("clear", &ForwardListWrapper<T>::clear)
        .def("insert_after", &ForwardListWrapper<T>::insert_after)
        .def("erase_after", &ForwardListWrapper<T>::erase_after)
        .def("data", &ForwardListWrapper<T>::getData)
        .def("find", &ForwardListWrapper<T>::find)

        .def("__iter__", [](ForwardListWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__len__", [](const ForwardListWrapper<T> &v) { return std::distance(v.begin(), v.end()); });
}

template <typename T>
void bind_forward_list(py::module &m, const std::string &type) {
    py::class_<ForwardListWrapper<T>>(m, ("ForwardList" + type).c_str())
        .def(py::init<>())
        .def(py::init<size_t, const T&>())
        .def(py::init<std::forward_list<T>>())
        .def("empty", &ForwardListWrapper<T>::empty)
        .def("front", &ForwardListWrapper<T>::front)
        .def("push_front", &ForwardListWrapper<T>::push_front)
        .def("pop_front", &ForwardListWrapper<T>::pop_front)
        .def("clear", &ForwardListWrapper<T>::clear)
        .def("insert_after", &ForwardListWrapper<T>::insert_after)
        .def("erase_after", &ForwardListWrapper<T>::erase_after)
        .def("data", &ForwardListWrapper<T>::getData)
        .def("find", &ForwardListWrapper<T>::find)

        .def("__iter__", [](ForwardListWrapper<T> &v) { return py::make_iterator(v.begin(), v.end()); },
             py::keep_alive<0, 1>())
        .def("__len__", [](const ForwardListWrapper<T> &v) { return std::distance(v.begin(), v.end()); });
}

template <typename T>
void bind_set_wrapper(py::module &m) {
    py::class_<SetWrapper<T>>(m, "Set")
        .def(py::init<>())
        .def(py::init<const std::set<T>&>())
        .def("size", &SetWrapper<T>::size)
        .def("empty", &SetWrapper<T>::empty)
        .def("insert", &SetWrapper<T>::insert)
        .def("erase", &SetWrapper<T>::erase)
        .def("clear", &SetWrapper<T>::clear)
        .def("contains", &SetWrapper<T>::contains)
        .def("data", &SetWrapper<T>::getData)
        .def("find", &SetWrapper<T>::find)
        .def("__len__", &SetWrapper<T>::size)
        .def("__iter__", [](SetWrapper<T> &s) { return py::make_iterator(s.begin(), s.end()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_set(py::module &m, const std::string &type) {
    py::class_<SetWrapper<T>>(m, ("Set" + type).c_str())
        .def(py::init<>())
        .def(py::init<const std::set<T>&>())
        .def("size", &SetWrapper<T>::size)
        .def("empty", &SetWrapper<T>::empty)
        .def("insert", &SetWrapper<T>::insert)
        .def("erase", &SetWrapper<T>::erase)
        .def("clear", &SetWrapper<T>::clear)
        .def("contains", &SetWrapper<T>::contains)
        .def("data", &SetWrapper<T>::getData)
        .def("find", &SetWrapper<T>::find)
        .def("__len__", &SetWrapper<T>::size)
        .def("__iter__", [](SetWrapper<T> &s) { return py::make_iterator(s.begin(), s.end()); },
             py::keep_alive<0, 1>());
}

template <typename Key, typename T>
void bind_map_wrapper(py::module &m) {
    py::class_<MapWrapper<Key, T>>(m, "Map")
        .def(py::init<>())
        .def(py::init<const std::map<Key, T>&>())
        .def("size", &MapWrapper<Key, T>::size)
        .def("empty", &MapWrapper<Key, T>::empty)
        .def("clear", &MapWrapper<Key, T>::clear)
        .def("insert", &MapWrapper<Key, T>::insert)
        .def("erase", &MapWrapper<Key, T>::erase)
        .def("at", &MapWrapper<Key, T>::at)
        .def("contains", &MapWrapper<Key, T>::contains)
        .def("data", &MapWrapper<Key, T>::getData)
        .def("items", &MapWrapper<Key, T>::items)
        .def("find", &MapWrapper<Key, T>::find)
        .def("__len__", &MapWrapper<Key, T>::size)
        .def("__setitem__", &MapWrapper<Key, T>::setItem)
        .def("__getitem__", &MapWrapper<Key, T>::getItem)
        .def("__delitem__", &MapWrapper<Key, T>::deleteItem)
        .def("__contains__", &MapWrapper<Key, T>::contains)
        .def("__iter__", [](MapWrapper<Key, T> &m) { return py::make_iterator(m.begin(), m.end()); },
             py::keep_alive<0, 1>());
}

template <typename Key, typename T>
void bind_map(py::module &m, const std::string &key_type, const std::string &value_type) {
    py::class_<MapWrapper<Key, T>>(m, ("Map" + key_type + value_type).c_str())
        .def(py::init<>())
        .def(py::init<const std::map<Key, T>&>())
        .def("size", &MapWrapper<Key, T>::size)
        .def("empty", &MapWrapper<Key, T>::empty)
        .def("clear", &MapWrapper<Key, T>::clear)
        .def("insert", &MapWrapper<Key, T>::insert)
        .def("erase", &MapWrapper<Key, T>::erase)
        .def("at", &MapWrapper<Key, T>::at)
        .def("contains", &MapWrapper<Key, T>::contains)
        .def("data", &MapWrapper<Key, T>::getData)
        .def("items", &MapWrapper<Key, T>::items)
        .def("find", &MapWrapper<Key, T>::find)
        .def("__len__", &MapWrapper<Key, T>::size)
        .def("__setitem__", &MapWrapper<Key, T>::setItem)
        .def("__getitem__", &MapWrapper<Key, T>::getItem)
        .def("__delitem__", &MapWrapper<Key, T>::deleteItem)
        .def("__contains__", &MapWrapper<Key, T>::contains)
        .def("__iter__", [](MapWrapper<Key, T> &m) { return py::make_iterator(m.begin(), m.end()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_unordered_set_wrapper(py::module& m) {
    using Wrapper = UnorderedSetWrapper<T>;
    std::string class_name = "UnorderedSet";

    py::class_<Wrapper>(m, class_name.c_str())
        .def(py::init<>())
        .def(py::init<const typename Wrapper::SetType&>())
        .def("size", &Wrapper::size)
        .def("max_size", &Wrapper::max_size)
        .def("empty", &Wrapper::empty)
        .def("clear", &Wrapper::clear)
        .def("insert", &Wrapper::insert)
        .def("erase", &Wrapper::erase)
        .def("count", &Wrapper::count)
        .def("contains", &Wrapper::contains)
        .def("bucket_count", &Wrapper::bucket_count)
        .def("bucket_size", &Wrapper::bucket_size)
        .def("bucket", &Wrapper::bucket)
        .def("load_factor", &Wrapper::load_factor)
        .def("max_load_factor", &Wrapper::max_load_factor)
        .def("rehash", &Wrapper::rehash)
        .def("reserve", &Wrapper::reserve)
        .def("to_list", &Wrapper::to_list)
        .def("find", &Wrapper::find)
        .def("__iter__", [](Wrapper &s) { return py::make_iterator(s.begin(), s.end()); }, py::keep_alive<0, 1>())
        .def("__len__", &Wrapper::size);
}

template <typename T>
void bind_unordered_set(py::module& m, const std::string& type) {
    using Wrapper = UnorderedSetWrapper<T>;
    std::string class_name = "UnorderedSet" + type;

    py::class_<Wrapper>(m, class_name.c_str())
        .def(py::init<>())
        .def(py::init<const typename Wrapper::SetType&>())
        .def("size", &Wrapper::size)
        .def("max_size", &Wrapper::max_size)
        .def("empty", &Wrapper::empty)
        .def("clear", &Wrapper::clear)
        .def("insert", &Wrapper::insert)
        .def("erase", &Wrapper::erase)
        .def("count", &Wrapper::count)
        .def("contains", &Wrapper::contains)
        .def("bucket_count", &Wrapper::bucket_count)
        .def("bucket_size", &Wrapper::bucket_size)
        .def("bucket", &Wrapper::bucket)
        .def("load_factor", &Wrapper::load_factor)
        .def("max_load_factor", &Wrapper::max_load_factor)
        .def("rehash", &Wrapper::rehash)
        .def("reserve", &Wrapper::reserve)
        .def("to_list", &Wrapper::to_list)
        .def("find", &Wrapper::find)
        .def("__iter__", [](Wrapper &s) { return py::make_iterator(s.begin(), s.end()); }, py::keep_alive<0, 1>())
        .def("__len__", &Wrapper::size);
}

template <typename Key, typename T>
void bind_unordered_map(py::module& m, const std::string& key_type, const std::string& value_type) {
    py::class_<UnorderedMapWrapper<Key, T>>(m, ("UnorderedMap" + key_type + value_type).c_str())
        .def(py::init<>())
        .def("at", &UnorderedMapWrapper<Key, T>::at)
        .def("__getitem__", &UnorderedMapWrapper<Key, T>::operator[])
        .def("insert", &UnorderedMapWrapper<Key, T>::insert)
        .def("erase", &UnorderedMapWrapper<Key, T>::erase)
        .def("clear", &UnorderedMapWrapper<Key, T>::clear)
        .def("contains", &UnorderedMapWrapper<Key, T>::contains)
        .def("find", &UnorderedMapWrapper<Key, T>::find)
        .def("bucket_count", &UnorderedMapWrapper<Key, T>::bucket_count)
        .def("bucket_size", &UnorderedMapWrapper<Key, T>::bucket_size)
        .def("bucket", &UnorderedMapWrapper<Key, T>::bucket)
        .def("load_factor", &UnorderedMapWrapper<Key, T>::load_factor)
        .def("max_load_factor", &UnorderedMapWrapper<Key, T>::max_load_factor)
        .def("rehash", &UnorderedMapWrapper<Key, T>::rehash)
        .def("reserve", &UnorderedMapWrapper<Key, T>::reserve)
        .def("data", &UnorderedMapWrapper<Key, T>::getData)
        .def("__len__", &UnorderedMapWrapper<Key, T>::size)
        .def("__setitem__", &UnorderedMapWrapper<Key, T>::setItem)
        .def("__getitem__", &UnorderedMapWrapper<Key, T>::getItem)
        .def("__delitem__", &UnorderedMapWrapper<Key, T>::deleteItem)
        .def("__contains__", &UnorderedMapWrapper<Key, T>::contains)
        .def("__iter__", [](UnorderedMapWrapper<Key, T> &m) { return py::make_iterator(m.begin(), m.end()); },
             py::keep_alive<0, 1>());
}

template <typename T>
void bind_queue_wrapper(py::module &m) {
    py::class_<QueueWrapper<T>>(m, "Queue")
        .def(py::init<>())
        .def("push", &QueueWrapper<T>::push)
        .def("pop", &QueueWrapper<T>::pop)
        .def("front", &QueueWrapper<T>::front)
        .def("empty", &QueueWrapper<T>::empty)
        .def("size", &QueueWrapper<T>::size)
        .def("print", &QueueWrapper<T>::print);
}

template <typename T>
void bind_queue(py::module &m, const std::string &type) {
    py::class_<QueueWrapper<T>>(m, ("Queue" + type).c_str())
        .def(py::init<>())
        .def("push", &QueueWrapper<T>::push)
        .def("pop", &QueueWrapper<T>::pop)
        .def("front", &QueueWrapper<T>::front)
        .def("empty", &QueueWrapper<T>::empty)
        .def("size", &QueueWrapper<T>::size)
        .def("print", &QueueWrapper<T>::print);
}

template <typename T>
void bind_stack_wrapper(py::module &m) {
    py::class_<StackWrapper<T>>(m, "Stack")
        .def(py::init<>())
        .def("push", &StackWrapper<T>::push)
        .def("pop", &StackWrapper<T>::pop)
        .def("top", &StackWrapper<T>::top)
        .def("empty", &StackWrapper<T>::empty)
        .def("size", &StackWrapper<T>::size)
        .def("print", &StackWrapper<T>::print);
}

template <typename T>
void bind_stack(py::module &m, const std::string &type) {
    py::class_<StackWrapper<T>>(m, ("Stack" + type).c_str())
        .def(py::init<>())
        .def("push", &StackWrapper<T>::push)
        .def("pop", &StackWrapper<T>::pop)
        .def("top", &StackWrapper<T>::top)
        .def("empty", &StackWrapper<T>::empty)
        .def("size", &StackWrapper<T>::size)
        .def("print", &StackWrapper<T>::print);
}