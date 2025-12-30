#pragma once

#include <memory>
#include <algorithm>

template <typename Key, typename Value>
class AVL {
    private:
        size_t size;
        struct Node {
            Key key;
            Value data;
            int height;
            std::shared_ptr<Node> left;
            std::shared_ptr<Node> right;

            Node(Key key, Value value): key(key), data(value), left(nullptr), right(nullptr), height(1) {}
        };

        std::shared_ptr<Node> root;

        int getHeight(std::shared_ptr<Node> n){
            return n ? n->height : 0;
        }

        int getBalanceFactor(std::shared_ptr<Node> n) {
            return n ? (getHeight(n->left)-getHeight(n->right)) : 0;
        }

        std::shared_ptr<Node> rightRotate(std::shared_ptr<Node> y) {
            std::shared_ptr<Node> x = y->left;
            std::shared_ptr<Node> T2 = x->right;

            x->right = y;
            y->left = T2;

            y->height = 1 + std::max(getHeight(y->left), getHeight(y->right));
            x->height = 1 + std::max(getHeight(x->left), getHeight(y->right));

            return x;
        }

        std::shared_ptr<Node> leftRotate(std::shared_ptr<Node> x) {
            std::shared_ptr<Node> y = x->right;
            std::shared_ptr<Node> T2 = y->left;

            y->left = x;
            x->right = T2;

            y->height = 1 + std::max(getHeight(y->left), getHeight(y->right));
            x->height = 1 + std::max(getHeight(x->left), getHeight(y->right));

            return y;
        }

        std::shared_ptr<Node> balanceTree(std::shared_ptr<Node> node, Key key) {
            int balanceFactor = getBalanceFactor(node);

            if (balanceFactor > 1 && key < node->left->key) {
                return rightRotate(node);
            }

            else if (balanceFactor < -1 && key > node->right->key) {
                return leftRotate(node);
            }

            else if (balanceFactor > 1 && key > node->left->key) {
                node->left = leftRotate(node->left);
                return rightRotate(node);
            }

            else if (balanceFactor < -1 && key < node->left->key) {
                node->right = rightRotate(node->right);
                return leftRotate(node);
            }

            else {
                return node;
            }
        }
        std::shared_ptr<Node> insertNode(std::shared_ptr<Node> node, Key key, Value value) {
            if (!node) {
                return std::make_shared<Node>(key, value);
            }

            if (key < node->key) {
                node->left = insertNode(node->left, key, value);
            }
            else if (key > node->key) {
                node->right = insertNode(node->right, key, value);
            }
            else {
                return node;
            }

            node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
            
            size += 1;
            return balanceTree(node, key);
        }

        std::shared_ptr<Node> minValueNode(std::shared_ptr<Node> node) {
            std::shared_ptr<Node> current = node;
            while(!current->left) {
                current = current->left;
            }
            return current;
        }

        std::shared_ptr<Node> deleteNode(std::shared_ptr<Node> node, Key key) {
            if (!node) {
                return node;
            }

            if (key < node->key) {
                node->left = deleteNode(node->left, key);
            }
            else if (key > node->key) {
                node->right = deleteNode(node->right, key);
            }
            else {
                if (!node->left || !node->right) {
                    std::shared_ptr<Node> temp = node->left ? node->left : node->right;
                    if (!temp) {
                        node = nullptr;
                    }
                    else {
                        *node = *temp;
                    }
                }
                else {
                    std::shared_ptr<Node> temp = minValueNode(node->right);
                    node->data = temp->data;
                    node->key = temp->key;
                    node->right = deleteNode(node->right, temp->key);
                }
            }

            if (!node) {
                return node;
            }

            node->height = 1 + std::max(getHeight(node->left), getHeight(node->right));
            
            return balanceTree(node, key);
        }

        Value findValue(std::shared_ptr<Node> node, Key key) {
            std::shared_ptr<Node> temp = node;
            while(node) {
                if (node->key < key) {
                    node = node->right;
                }
                else if (node->key > key) {
                    node = node->left;
                }
                else {
                    return node->data;
                }
            }
            throw std::out_of_range("Key not found in dict!");
        }
    public:
        AVL() : root(nullptr) {}
        void insert(Key key, Value value) {
            root = insertNode(root, key, value);
        }
        void remove(Key key) {
            root = deleteNode(root, key);
        }
        Value find(Key key) {
            return findValue(root, key);
        }
        
        Value at(const Key& key) { return find(key); }
        Value& operator[](const Key& key) { return find(key); }
        
};