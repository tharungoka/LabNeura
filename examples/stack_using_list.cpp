#include <iostream>

class Node {
    public:
        int data;
        Node* next;
        Node(int dat): data(dat),next(nullptr) {}
};

class Stack {
    Node* head;
    int top;
    public:
        Stack():head(nullptr),top(-1) {}
        void push(int data) {
            Node* node = new Node(data);
            node->next = head;
            head = node;
            top+=1;
        }
        void pop() { 
            if (head) {
                head = head->next;
                top-=1;
            }
        }
        int peek() {
            return head->data;
        }
};

int main() {
    Stack stack = Stack();
    stack.push(2);
    stack.push(3);
    stack.pop();
}