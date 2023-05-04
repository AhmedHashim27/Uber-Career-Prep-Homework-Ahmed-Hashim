struct Node {
    int data;
    Node* next;
};

Node* insertAtFront(Node* head, int val) {
    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = head;
    return newNode;
}

void insertAtBack(Node* head, int val) {
    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = nullptr;
    Node* curr = head;
    while (curr->next != nullptr) {
        curr = curr->next;
    }
    curr->next = newNode;
}

void insertAfter(Node* head, int val, Node* loc) {
    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = loc->next;
    loc->next = newNode;
}

Node* deleteFront(Node* head) {
    Node* newHead = head->next;
    delete head;
    return newHead;
}

void deleteBack(Node* head) {
    Node* curr = head;
    while (curr->next->next != nullptr) {
        curr = curr->next;
    }
    delete curr->next;
    curr->next = nullptr;
}

Node* deleteNode(Node* head, Node* loc) {
    if (head == loc) {
        return deleteFront(head);
    }
    Node* curr = head;
    while (curr->next != loc) {
        curr = curr->next;
    }
    curr->next = loc->next;
    delete loc;
    return head;
}

int length(Node* head) {
    int len = 0;
    Node* curr = head;
    while (curr != nullptr) {
        len++;
        curr = curr->next;
    }
    return len;
}

Node* reverseIterative(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr != nullptr) {
        Node* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

Node* reverseRecursiveHelper(Node* curr, Node* prev) {
    if (curr == nullptr) {
        return prev;
    }
    Node* next = curr->next;
    curr->next = prev;
    return reverseRecursiveHelper(next, curr);
}

Node* reverseRecursive(Node* head) {
    return reverseRecursiveHelper(head, nullptr);
}
