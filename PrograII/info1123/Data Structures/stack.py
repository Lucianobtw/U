# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# print(stack.pop())
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

try:
    print(stack.pop())
except IndexError:
    print("Stack is empty")
except:
    print("Something else went wrong")

# the use of try-except will catch
# the IndexError exception and allow us
# to continue the program execution
