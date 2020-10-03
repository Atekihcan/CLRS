# Selection Sort
def SelectionSort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex] and j != minIndex:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]


# Test
import random
num_failed = 0
total_tests = 100
for i in range(total_tests):
    length = random.randint(2, 50)
    lst = [random.randint(0, 100) for _ in range(length)]
    SelectionSort(lst)

    # Check if list has been sorted
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            num_failed += 1
            print(f"Test #{i:<2}: List is not sorted")
            break
    if num_failed > 0:
        break

if num_failed > 0:
    print(f"\nFailed")
else:
    print(f"Passed {total_tests}/{total_tests} tests")
