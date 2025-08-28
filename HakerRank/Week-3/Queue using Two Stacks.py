# Enter your code here. Read input from STDIN. Print output to STDOUT
# Queue using two stacks
stack1 = []  # For enqueue
stack2 = []  # For dequeue

def enqueue(x):
    stack1.append(x)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    stack2.pop()

def print_front():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    print(stack2[-1])


q = int(input()) 
for _ in range(q):
    query = input().split()
    if query[0] == '1':
        enqueue(int(query[1]))
    elif query[0] == '2':
        dequeue()
    elif query[0] == '3':
        print_front()
