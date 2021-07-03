
"""implementation of stack"""

def create_stack():
    stack = []
    return stack

def stack_empty(stack):
    if len(stack) == 0:
        return True
    return False

def push(stack, value):
    stack.append(value)

def delet(stack):
    if stack_empty(stack):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
print(stack)
delet(stack)
delet(stack)
print(stack)