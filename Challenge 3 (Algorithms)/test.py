import fileinput

for line in fileinput.input():
    print('line : ', [int(s) for s in line.split()])

# print(fileinput.input())

print('test1')