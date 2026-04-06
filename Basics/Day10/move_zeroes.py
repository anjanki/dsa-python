# Take input for size of array
n = int(input("Enter number of elements: "))

# Initialize list with zeros
L = [0 for i in range(n)]

# Pointer for placing non-zero elements
j = 0

# Take elements as input
for i in range(n):
    a = int(input("Enter element: "))
    
    # If element is not zero, place it in list
    if a != 0:
        L[j] = a
        j += 1

# Print final list
print("Output array:")
for i in L:
    print(i, end=" ")