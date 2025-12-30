#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>
#include "data.h"
#include "algorithms.h"

namespace py = pybind11;

PYBIND11_MODULE(labneura, m) {
    bind_sorting(m);
    bind_graph(m);
    bind_tensor(m);
    bind_avl<int, int>(m, "Int", "Int");
    bind_avl<int, float>(m, "Int", "Float");
    bind_avl<int, double>(m, "Int", "Double");
    bind_avl<int, std::string>(m, "Int", "String");

    bind_avl<float, int>(m, "Float", "Int");
    bind_avl<float, float>(m, "Float", "Float");
    bind_avl<float, double>(m, "Float", "Double");
    bind_avl<float, std::string>(m, "Float", "String");

    bind_avl<double, int>(m, "Double", "Int");
    bind_avl<double, float>(m, "Double", "Float");
    bind_avl<double, double>(m, "Double", "Double");
    bind_avl<double, std::string>(m, "Double", "String");

    bind_avl<std::string, int>(m, "String", "Int");
    bind_avl<std::string, float>(m, "String", "Float");
    bind_avl<std::string, double>(m, "String", "Double");
    bind_avl<std::string, std::string>(m, "String", "String");

    bind_vector_wrapper<py::object>(m);
    bind_vector<int>(m, "Int");
    bind_vector<float>(m, "Float");
    bind_vector<double>(m, "Double");
    bind_vector<std::string>(m, "String");
    
    bind_deque_wrapper<py::object>(m);
    bind_deque<int>(m, "Int");
    bind_deque<float>(m, "Float");
    bind_deque<double>(m, "Double");
    bind_deque<std::string>(m, "String");
    
    bind_list_wrapper<py::object>(m);
    bind_list<int>(m, "Int");
    bind_list<float>(m, "Float");
    bind_list<double>(m, "Double");
    bind_list<std::string>(m, "String");

    bind_forward_list_wrapper<py::object>(m);
    bind_forward_list<int>(m, "Int");
    bind_forward_list<float>(m, "Float");
    bind_forward_list<double>(m, "Double");
    bind_forward_list<std::string>(m, "String");

    bind_set_wrapper<py::object>(m);
    bind_set<int>(m, "Int");
    bind_set<float>(m, "Float");
    bind_set<double>(m, "Double");
    bind_set<std::string>(m, "String");

    bind_map_wrapper<py::object, py::object>(m);

    bind_map<int, int>(m, "Int", "Int");
    bind_map<int, float>(m, "Int", "Float");
    bind_map<int, double>(m, "Int", "Double");
    bind_map<int, std::string>(m, "Int", "String");

    // Float combinations
    bind_map<float, int>(m, "Float", "Int");
    bind_map<float, float>(m, "Float", "Float");
    bind_map<float, double>(m, "Float", "Double");
    bind_map<float, std::string>(m, "Float", "String");

    // Double combinations
    bind_map<double, int>(m, "Double", "Int");
    bind_map<double, float>(m, "Double", "Float");
    bind_map<double, double>(m, "Double", "Double");
    bind_map<double, std::string>(m, "Double", "String");

    // String combinations
    bind_map<std::string, int>(m, "String", "Int");
    bind_map<std::string, float>(m, "String", "Float");
    bind_map<std::string, double>(m, "String", "Double");
    bind_map<std::string, std::string>(m, "String", "String");

    bind_unordered_set<int>(m, "Int");
    bind_unordered_set<float>(m, "Float");
    bind_unordered_set<double>(m, "Double");
    bind_unordered_set<std::string>(m, "String");

    bind_unordered_map<int, int>(m, "Int", "Int");
    bind_unordered_map<int, float>(m, "Int", "Float");
    bind_unordered_map<int, double>(m, "Int", "Double");
    bind_unordered_map<int, std::string>(m, "Int", "String");
    
    bind_unordered_map<float, int>(m, "Float", "Int");
    bind_unordered_map<float, float>(m, "Float", "Float");
    bind_unordered_map<float, double>(m, "Float", "Double");
    bind_unordered_map<float, std::string>(m, "Float", "String");

    bind_unordered_map<double, int>(m, "Double", "Int");
    bind_unordered_map<double, float>(m, "Double", "Float");
    bind_unordered_map<double, double>(m, "Double", "Double");
    bind_unordered_map<double, std::string>(m, "Double", "String");

    bind_unordered_map<std::string, int>(m, "String", "Int");
    bind_unordered_map<std::string, float>(m, "String", "Float");
    bind_unordered_map<std::string, double>(m, "String", "Double");
    bind_unordered_map<std::string, std::string>(m, "String", "String");

    bind_stack_wrapper<py::object>(m);
    bind_stack<int>(m, "Int");
    bind_stack<float>(m, "Float");
    bind_stack<double>(m, "Double");
    bind_stack<std::string>(m, "String");
    bind_queue_wrapper<py::object>(m);
    bind_queue<int>(m, "Int");
    bind_queue<float>(m, "Float");
    bind_queue<double>(m, "Double");
    bind_queue<std::string>(m, "String");
}