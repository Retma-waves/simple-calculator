num_1 = float(input('first number: '))
op = input('operator: ')
num_2 = float(input('second number: '))
if op == '+':
    ans = num_1 + num_2
    print(ans)
elif op == '-':
    ans = num_1 - num_2
    print(ans)
elif op == '/':
    ans = num_1 / num_2
    print(ans)
elif op == '*':
    ans = num_1 * num_2
    print(ans)
else:
    print('This is just a simple calculator')
