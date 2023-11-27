#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


class Node {
public:
	int value;
	Node* next;
	Node* prev;
};

class LinkedList {
private:
	Node* head;
	int length;
public:
	LinkedList() {
		head = nullptr;
		length = 0;
	}

	int get(int index) {
		Node* data = find(index);
		return data->value;
	}

	void insert(int value, int index) {
		Node* newNode = new Node();
		newNode->value = value;
		if (index == 0) {
			newNode->prev = nullptr;
			newNode->next = head;
			head = newNode;
		}
		else {
			Node* oldNode = find(index - 1);
			newNode->next = oldNode->next;
			oldNode->next = newNode;
			newNode->prev = oldNode;
		}
		length++;
	}


	void remove(int index) {
		if (index == 0) {
			head = head->next;
		}
		else {
			Node* prev = find(index - 1);
			Node* removed = prev->next;
			prev->next = removed->next;
		}
		length--;
	}

	int getLength() {
		return length;
	}

private:
	Node* find(int index) {
		Node* current = head;
		int i = 0;
		while (i != index) {
			current = current->next;
			i++;
		}
		return current;
	}
};


class ArrayList {
private:
	int* arr;
	int length;
	int capacity;
public:
	ArrayList() {
		int capacity = 2;
		arr = new int[capacity];
		length = 0;
	}

	void add(int value) {
		if (length == capacity) {
			expand();
		}
		arr[length] = value;
		length++;
	}

	void remove(int index) {
		for (int i = index + 1; i < length; i++) {
			arr[i - 1] = arr[i];
		}
		length--;
	}

	int get(int index) {
		return arr[index];
	}

	int getLength() {
		return length;
	}

private:
	void expand() {
		capacity *= 2;
		int* newArr = new int[capacity];
		for (int i = 0; i <= length; i++) {
			newArr[i] = arr[i];
		}
		delete[] arr;
		arr = newArr;
	}
};


class NodeS {
public:
	string value;
	NodeS* next;
};

class Stack {
private:
	NodeS* top;
public:
	Stack() {
		top = nullptr;
	}

	void push(string value) {
		NodeS* newNode = new NodeS;
		newNode->value = value;
		newNode->next = top;
		top = newNode;
	}

	void pop() {
		if (!isEmpty()) {
			NodeS* temp = top;
			top = top->next;
			delete temp;
		}
	}

	string peek() {
		if (!isEmpty()) {
			return top->value;
		}
		else {
			return "";
		}
	}

	bool isEmpty() {
		return top == nullptr;
	}
};

bool isOperator(string ch) {
	return ch == "+" || ch == "-" || ch == "*" || ch == "/" || ch == "^";
}

bool isFunction(string ch) {
	return ch == "cos" || ch == "sin";
}

int isSkobka(string ch) {
	if (ch == "(") {
		return 1;
	}
	if (ch == ")") {
		return 2;
	}
}

int getPrecedence(string op) {
	if (op == "+" || op == "-") {
		return 1;
	}
	else if (op == "*" || op == "/") {
		return 2;
	}
	else if (op == "^") {
		return 3;
	}
	return 0;
}

vector<string> substrings(string str) {
	vector<string> substrings;
	istringstream iss(str);

	string substring;
	while (iss >> substring) {
		substrings.push_back(substring);
	}
	return substrings;
}

string infixToPostfix(vector<string> infix) {
	Stack stack;
	string postfix;

	for (string ch : infix) {
		if (!isOperator(ch) and isSkobka(ch) != 1 and isSkobka(ch) != 2 and !isFunction(ch)) {
			postfix += ch;
		}
		else if (isFunction(ch)) {
			stack.push(ch);
		}
		else if (getPrecedence(ch) != 0) {
			while (getPrecedence(stack.peek()) >= getPrecedence(ch)) {
				postfix += stack.peek();
				stack.pop();
			}
			stack.push(ch);
		}
		else if (isSkobka(ch) == 1) {
			stack.push(ch);
		}
		else if (isSkobka(ch) == 2) {
			while (isSkobka(stack.peek()) != 1) {
				if (isOperator(stack.peek())) {
					postfix += stack.peek();
					stack.pop();
				}
				if (stack.isEmpty()) {
					cout << "Missed (" << endl;
				}
			}
			stack.pop();
			if (isFunction(stack.peek())) {
				postfix += stack.peek();
				stack.pop();
			}
		}
	}
	while (!stack.isEmpty()) {
		if (isOperator(stack.peek())) {
			postfix += stack.peek();
		}
		stack.pop();
	}
	return postfix;
}

void main() {
	cout << "Work of linked list: " << endl;
	LinkedList list;
	list.insert(1, 0);
	list.insert(2, 1);
	list.insert(3, 2);
	list.insert(34, 3);
	list.insert(5, 4);
	list.insert(7, 1);
	for (int i = 0; i < list.getLength(); i++) {
		cout << list.get(i) << " ";
	}
	cout << endl;
	cout << "length: " << list.getLength() << endl;
	list.remove(0);
	for (int i = 0; i < list.getLength(); i++) {
		cout << list.get(i) << " ";
	}
	cout << endl;
	cout << "length after removing: " << list.getLength() << endl << endl;;


	cout << "Work of array list: " << endl;
	ArrayList arr;
	arr.add(12);
	arr.add(34);
	arr.add(56);
	arr.add(78);
	for (int i = 0; i < arr.getLength(); i++) {
		cout << arr.get(i) << " ";
	}
	cout << endl;
	cout << "length: " << arr.getLength() << endl;

	arr.remove(1);
	for (int i = 0; i < arr.getLength(); i++) {
		cout << arr.get(i) << " ";
	}

	cout << endl << "length after removing: " << arr.getLength() << endl << endl;

	cout << "Algorithm realized by stack: " << endl;
	string infix = "sin ( 4 * 5 ^ 44 )";
	string postfix = infixToPostfix(substrings(infix));
	cout << "Infix expression: " << infix << endl;
	cout << "Postfix expression: " << postfix << endl;
}
