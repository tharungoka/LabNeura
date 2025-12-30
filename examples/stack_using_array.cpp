#include <iostream>
#include <vector>

class Stack {
    std::vector<int> stack;
    public:
        void push(int data) {
            stack.push_back(data);
        }
        int pop() {
            if (stack.size()) {
                int temp = stack.back();
                stack.pop_back();
                return temp;
            }
            return -1;
        }
        int top() {
            if (stack.size())
                return stack.size()-1;
            return -1;
        }
        int peek() {
            if (stack.size())
                return stack.back();
            return -1;
        }
};

int main() {
    Stack stack = Stack();
    stack.push(2);
    stack.pop();
    std::cout << stack.top() << std::endl;
}