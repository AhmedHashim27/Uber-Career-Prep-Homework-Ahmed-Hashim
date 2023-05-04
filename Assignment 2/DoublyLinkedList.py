struct Node {
    int data;
    Node* prev;
    Node* next;
};

Node* insertAtFront(Node* head, int val) {
    Node* newNode = new Node;
    newNode->data = val;
    newNode->prev = nullptr;
    newNode->next = head;
    if (head != nullptr) {
        head->prev = newNode;
    }
    return newNode;
}

void insertAtBack(Node* head, int val) {
    Node* newNode = new Node;
    newNode->data = val;
    newNode->prev = nullptr;
    newNode->next = nullptr;
    if (head == nullptr) {
        head = newNode;
    } else {
        Node* curr = head;
        while (curr->next != nullptr) {
            curr = curr->next;
        }
        curr->next = newNode;
        newNode->prev = curr;
    }
}

void insertAfter(Node* head, int val, Node* loc) {
    if (loc == nullptr) {
        return;
    }
    Node* newNode = new Node;
    newNode->data = val;
    newNode->prev = loc;
    newNode->next = loc->next;
    if (loc->next != nullptr) {
        loc->next->prev = newNode;
    }
    loc->next = newNode;
}

Node* deleteFront(Node* head) {
    if (head == nullptr) {
        return nullptr;
    }
    Node* newHead = head->next;
    if (newHead != nullptr) {
        newHead->prev = nullptr;
    }
    delete head;
    return newHead;
}

void deleteBack(Node* head) {
    if (head == nullptr) {
        return;
    }
    if (head->next == nullptr) {
        delete head;
        head = nullptr;
        return;
    }
    Node* curr = head;
    while (curr->next != nullptr) {
        curr = curr->next;
    }
    curr->prev->next = nullptr;
    delete curr;
}

Node* deleteNode(Node* head, Node* loc) {
    if (loc == nullptr) {
        return head;
    }
    if (loc->prev != nullptr) {
        loc->prev->next = loc->next;
    } else {
        head = loc->next;
    }
    if (loc->next != nullptr) {
        loc->next->prev = loc->prev;
    }
    delete loc;
    return head;
}

int length(Node* head) {
    int count = 0;
    Node* curr = head;
    while (curr != nullptr) {
        count++;
        curr = curr->next;
    }
    return count;
}

Node* reverseIterative(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr != nullptr) {
        Node* next = curr->next;
        curr->next = prev;
        curr->prev = next;
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
    curr->prev = next;
    return reverseRecursiveHelper(next, curr);
}

Node* reverseRecursive(Node* head) {
    return reverseRecursiveHelper(head, nullptr);
}
