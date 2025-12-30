#pragma once
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "algorithms/sorting.h"
#include "algorithms/graph.h"
#include "algorithms/avl.h"

namespace py=pybind11;

template <typename Key, typename Value>
void bind_avl(py::module& m, const std::string& key_type, const std::string& value_type) {
    std::string class_name = "AVL" + key_type + value_type;
    py::class_<AVL<Key, Value>>(m, class_name.c_str())
        .def(py::init<>())
        .def("insert", &AVL<Key, Value>::insert)
        .def("remove", &AVL<Key, Value>::remove)
        .def("find", &AVL<Key, Value>::find)
        .def("__setitem__", &AVL<Key, Value>::insert)
        .def("__getitem__", &AVL<Key, Value>::find)
        .def("__delitem__", &AVL<Key, Value>::remove);
        // .def("search", &AVLTree<Key, Value>::search);
}

void bind_sorting(py::module &m) {
    py::class_<Sorting>(m, "Sorting")
        .def(py::init<std::vector<int>>())
        .def("selection", &Sorting::selection)
        .def("insertion", &Sorting::insertion)
        .def("bubble", &Sorting::bubble)
        .def("merge", &Sorting::merge)
        .def("quick", &Sorting::quick)
        .def_property("data", &Sorting::getData, &Sorting::setData)
        .def_property_readonly("no_timesteps", &Sorting::getTimeSteps)
        .def_property_readonly("no_swaps", &Sorting::getSwaps)
        .def_property_readonly("no_recursive_calls", &Sorting::getRecursiveCalls);
}

void bind_graph(py::module &m) {
    py::class_<Graph>(m, "Graph")
        .def(py::init<int>())
        .def("addEdge", &Graph::addEdge)
        .def("displayGraph", &Graph::displayGraph);
}