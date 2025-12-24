import sys
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            n_list.append(self.items[-1])
            self.items.pop()
        except IndexError:
            n_list.append('-1')

    def top(self):
        try:
            n_list.append(self.items[-1])
        except IndexError:
            n_list.append('-1')

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) == 0:
            n_list.append('1')
        else:
            n_list.append('0')

n_list = []
n = int(sys.stdin.readline().rstrip())
stack = Stack()
for i in range(n):
    data = sys.stdin.readline().strip().split()
    order = data[0]
    
    if order == '1':
        stack.push(data[1])
    elif order == '2':
        stack.pop()
    elif order == '3':
        stack.__len__()
        n_list.append(stack.__len__())
    elif order == '4':
        stack.isEmpty()
    elif order == '5':
        stack.top()
    else:
        pass

for j in range(len(n_list)):
    print(n_list[j])