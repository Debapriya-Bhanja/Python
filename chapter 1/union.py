def union(list1, list2):
    result = []  
    
    # Add all elements of list1
    for i in range(len(list1)):
        if list1[i] not in result:   # Avoid duplicates
            result.append(list1[i])
    
    # Add elements of list2 if not already present
    for j in range(len(list2)):
        if list2[j] not in result:
            result.append(list2[j])
    
    return result


# Example usage
list1 = []
list2 = []

n1 = int(input("Enter number of elements in list1: "))
for i in range(n1):
    val = int(input(f"Enter element {i+1} for list1: "))
    list1.append(val)

n2 = int(input("Enter number of elements in list2: "))
for i in range(n2):
    val = int(input(f"Enter element {i+1} for list2: "))
    list2.append(val)

print("Union of lists:", union(list1, list2))
