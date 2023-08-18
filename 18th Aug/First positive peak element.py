#peak element refers to the element that is greater than the neighboring elements
# for the given 1D array, find the find first positive peak element

#Method 1 - Linear Search Method
arr = [20, 32, 15, 100, 65]
for i in range(len(arr)):
    if (i == 0 or arr[i-1] < arr[i]) and (i == len(arr)-1 or arr[i] > arr[i-1]):
        print("First peak element is ", arr[i])
        break

#Method 2 - Binary search Method

def find_peak_element(arr, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None

s = []
k = int(input("Enter the array size: "))
print("Enter the elements of the array: ")
for _ in range(k):
    s.append(int(input()))

peak_element = find_peak_element(s, 0, len(s) - 1)

if peak_element is not None:
    print("The first peak element is:", peak_element)
else:
    print("No peak element found in the array.")
