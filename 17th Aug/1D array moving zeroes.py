"""size = int(input("Enter the size of the array: "))
m = []
z = []
print("Enter the elements")
for i in range(size):
    m.append(int(input()))
for i in m:
    if i == 0:
        z.append(i)
        m.remove(i)
m += z
print(m)
"""

size = int(input("Enter the size of the array: "))
m = []
print("Enter the elements")
for i in range(size):
    m.append(int(input()))
pos = 0
for i in range(size):
    if m[i] != 0:
        m[pos] = m[i]
        pos += 1
while pos < size:
    m[pos] = 0
    pos += 1
print(m)
