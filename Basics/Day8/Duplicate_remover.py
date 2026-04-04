#Implemented an optimized solution to remove duplicate elements
#  from a sorted array using the Two Pointer technique. 
# The approach leverages the sorted nature of the array to
#  efficiently eliminate duplicates in-place while preserving 
# order. Achieves O(n) time complexity and O(1) auxiliary space
class Solution:
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return []

        i = 0  # pointer for unique elements

        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        return arr[:i+1]


# 🔷 Give input
arr = [2, 2, 2, 3, 4, 4]

# 🔷 Create object
obj = Solution()

# 🔷 Call function
result = obj.removeDuplicates(arr)

# 🔷 Print output
print("Unique elements:", result)