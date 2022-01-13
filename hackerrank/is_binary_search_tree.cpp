// https://www.hackerrank.com/challenges/is-binary-search-tree

#include<algorithm>

struct Node {
    int data;
    Node* left;
    Node* right;
};

struct Triplet {
    bool bst;
    int min;
    int max;
};

Triplet checkBstAll(Node* root) {
    int min = root->data;
    int max = root->data;
    if (root->left) {
        auto left = checkBstAll(root->left);
        min = std::min(left.min, min);
        max = std::max(left.max, max);
        if (!left.bst)
            return {false, min, max};
        if (left.max >= root->data)
            return {false, min, max};
    }
    if (root->right) {
        auto right = checkBstAll(root->right);
        min = std::min(right.min, min);
        max = std::max(right.max, max);
        if (!right.bst)
            return {false, min, max};
        if (right.min <= root->data)
            return {false, min, max};
    }
    return {true, min, max};
}

bool checkBST(Node* root) {
    return checkBstAll(root).bst;
}

int main() {
    Node case11 = {1, nullptr, nullptr};
    Node case14 = {4, nullptr, nullptr};
    Node case15 = {5, &case11, &case14};
    Node case16 = {6, nullptr, nullptr};
    Node case12 = {2, &case16, nullptr};
    Node case13 = {3, &case15, &case12};
    
    Node* case1 = &case13;

    Node case21 = {1, nullptr, nullptr};
    Node case22r = {2, nullptr, nullptr};
    Node case22 = {2, &case21, &case22r};

    Node* case2 = &case22;

    if (checkBST(case1))
        return -1;
    if (checkBST(case2))
        return -2;
}
