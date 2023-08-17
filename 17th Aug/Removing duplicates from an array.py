#removing duplicates from the array in an efficient way

s = int(input("Enter the size of array: "))
a = []
print("Enter the elements of the array: ")
for i in range(s):
    a.append(int(input()))
for i in range(s):
    for j in range(i+1, s):
        if a[i] == a[j]:
            for k in range(j, s):
                a[k] = a[k+1]
            s -= 1
            j -= 1

print(a)
