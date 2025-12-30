#include <iostream>

class Node {
    public:
        int data;
        Node* prev;
        Node* next;
        Node(int dat):data(dat),prev(nullptr),next(nullptr) {}
};

class Queue {
    public:
        Node* front;
        Node* rear;
        Queue():front(nullptr),rear(nullptr) {}
        void enqueue(int data) {
            Node* newData = new Node(data);
            if (front==nullptr && rear == nullptr) {
                front = newNode;
                rear = newNode;
                front->next = rear;
                read->prev = front;
            }
            else {
                newNode->prev = rear->prev;
                rear->next = newNode;
                rear = newNode;
            }
        }
        int dequeue() {
            Node* toBeDeleted = front;
            front = front->next;

        }
}