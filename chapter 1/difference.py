def difference(list1, list2):
    result = []

    # Pick elements of list1 that are not in list2
    for i in range(len(list1)):
        found = False
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                found = True
                break
        if not found and list1[i] not in result:
            result.append(list1[i])
    
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

print("Difference (list1 - list2):", difference(list1, list2))








