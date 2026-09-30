porog = float(input())
n = int(input())

error = 0
high = 0
list = []

for i in range(n):
    x = input()
    if x == 'error':
        error += 1
    else:
        x = float(x)
        list.append(x)
        if porog < x:
            high += 1



print(n)
print(error)
print(high)
print(f'{max(list):.1f}')
print(f'{sum(list)/len(list):.1f}')
