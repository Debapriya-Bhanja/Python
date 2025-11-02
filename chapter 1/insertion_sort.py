# Insertion Sort 
def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]      # current element
        j = i - 1
        # shift larger elements to the right
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j = j-1 
        L[j+1] = key    # place key at correct position

# Input from user
n = int(input("Enter number of elements: "))
L = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    L.append(val)   # using append for input

print("Original List:", L)
insertion_sort(L)
print("Sorted List:", L)
