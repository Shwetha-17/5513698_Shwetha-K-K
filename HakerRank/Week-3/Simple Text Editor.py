# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
s = ""
stack = []
for _ in range(q):
    op = input().split()
    if op[0] == '1':
        stack.append(s)
        s += op[1]
    elif op[0] == '2':
        stack.append(s)
        s = s[:-int(op[1])]
    elif op[0] == '3':
        print(s[int(op[1])-1])
    else:
        s = stack.pop()
