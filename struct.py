from dataclasses import dataclass

# Using a normal list to make a stack
print("Hello World")

stack = []

# append replace push
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack ', stack)

# pop() fucntion to pop
print('\n elements from the stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Implementing a custom stack and nodes
class CustomNode:
    def __init__(self, input) -> None:
        self.data = input
        self.next = None
    
    
class CustomStack:
    def __init__(self):
        self.head = None
        
    # isEmpty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Push puts an item on the stack
    def push(self, data):
        # Case 1: Stack is empty
        newNode = CustomNode(data)
        if self.is_empty():
            self.head = newNode
        # Case 2: Stack is non-empty
        else:
            newNode.next = self.head
            self.head = newNode

    # Pop
    def pop(self):
        # Case 1: Stack is empty
        if self.is_empty():
            return None
        # Case 2: Stack is non-empty
        else:
            popped_node = self.head
            self.head = self.head.next
            return popped_node.data
    
    # Peek
    def peek(self):
        peek_node = self.head.data
        return peek_node
    
    # Count
    def count(self):
        num_stack_items = 0
        temp_node = self.head
        while temp_node is not None:
            num_stack_items += 1
            temp_node = temp_node.next
        return num_stack_items
    
    # Print
    def print(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

print("Making new custom Stack object")    
test_stack = CustomStack()

print("Pushing a, 1, and 'Hello' to the stack")
test_stack.push('a')
test_stack.push(1)
test_stack.push("Hello")
print("The count of the stack is ", test_stack.count())

print("Printing Stack")
test_stack.print()

print("Popped: {0} from the stack".format(test_stack.pop()))
print("Peeking at the top of the stack: ", test_stack.peek())

print("Is the stack empty: ", test_stack.is_empty())

    