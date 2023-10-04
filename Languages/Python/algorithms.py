# Popular sorting algorithms implemented in Python

# Bubble Sort

class Bubblez:
    """_summary_
    Attributes:
        arr (list): This is the array that will be sorted
    Methods:
        swap: This is a method that swaps two elements in an array
        bubble_sort: This is the method that bubble sorts the array
    Time and space complexity:
        time complexity: O(n^2)
        space complexity: O(1)
    Returns:
        list: This is the sorted array
    """

    def __init__(self, arr):
        """_summary_
        Args:
            arr (list): This is the array that will be sorted
        Returns:
            None
        Time and space complexity:
            time complexity: O(1)
            space complexity: O(1)
        """
        self.arr = arr

    def swap(self, i, j):
        """_summary_
        Args:
            i (int): index of first element to be swapped
            j (int): index of second element to be swapped
        Returns:
            None
        Time and space complexity:
            time complexity: O(1)
            space complexity: O(1)
        """
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def bubble_sort(self):
        """_summary_
        Args:
            None
        Returns:
            list: This is the sorted array
        Time and space complexity:
            time complexity: O(n^2)
            space complexity: O(1)
        """
        for i in range(len(self.arr)):  # This is the outer loop
            for j in range(len(self.arr) - 1):  # This is the inner loop
                if self.arr[j] > self.arr[j+1]:  # This is the comparison
                    self.swap(j, j+1)  # This is the swap6
        return self.arr  # This is the sorted array


# Test Cases
arr = [5, 4, 3, 2, 1]
arr2 = [1,5,2,4,4,5,100,21,1,2]

bubble = Bubblez(arr)
print(bubble.bubble_sort())

bubble2 = Bubblez(arr2)
print(bubble2.bubble_sort())


