# Check if array is sorted in non-decreasing order
# Approach: Compare each element with its previous element
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isSorted(self, arr) -> bool:
        # Traverse from second element
        for i in range(1, len(arr)):
            
            # If current element is smaller than previous → not sorted
            if arr[i] < arr[i - 1]:
                return False
        
        # If no violation found → sorted
        return True


# 🔷 Take input from user
arr = list(map(int, input("Enter elements separated by space: ").split()))

# 🔷 Create object
obj = Solution()

# 🔷 Call function and print result
if obj.isSorted(arr):
    print("Array is sorted")
else:
    print("Array is NOT sorted")