def quicksort(arr, left, right):
    # Base case: If the array has one or zero elements, it is already sorted
    if left >= right:
        return 0

    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)

    # Number of comparisons is the size of the subarray minus 1
    comparisons = right - left

    # Recursively sort the left and right subarrays
    comparisons += quicksort(arr, left, pivot_index - 1)
    comparisons += quicksort(arr, pivot_index + 1, right)

    return comparisons

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    return i - 1

def quicksort_with_comparisons(arr):
    return quicksort(arr, 0, len(arr) - 1)

# Read the input array from the file
with open('./QuickSort.txt') as f:
    input_array = [int(line.strip()) for line in f]

# Calculate the total number of comparisons
total_comparisons = quicksort_with_comparisons(input_array)

# Print the total number of comparisons
print(total_comparisons)



# Reading the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def quicksort(arr, start, end):
    if start >= end:
        return 0

    pivot_index = end
    pivot = arr[pivot_index]

    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    pivot_index = start
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    comparisons = (end - start)
    comparisons += quicksort(arr, start, i - 2)
    comparisons += quicksort(arr, i, end)

    return comparisons

file_path = './QuickSort.txt'
array = read_file(file_path)
total_comparisons = quicksort(array, 0, len(array) - 1)
print(f"Total number of comparisons: {total_comparisons}")

# Reading the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def median_of_three(arr, start, mid, end):
    a = arr[start]
    b = arr[mid]
    c = arr[end]
    
    if (a <= b <= c) or (c <= b <= a):
        return mid
    elif (b <= a <= c) or (c <= a <= b):
        return start
    else:
        return end

def quicksort(arr, start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2
    pivot_index = median_of_three(arr, start, mid, end)
    pivot = arr[pivot_index]

    # Move pivot to the start of the array
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    pivot_index = start
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    comparisons = (end - start)
    comparisons += quicksort(arr, start, i - 2)
    comparisons += quicksort(arr, i, end)

    return comparisons

file_path = './QuickSort.txt'
array = read_file(file_path)
total_comparisons = quicksort(array, 0, len(array) - 1)
print(f"Total number of comparisons: {total_comparisons}")
