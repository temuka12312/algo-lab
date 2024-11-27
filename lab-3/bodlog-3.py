class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def merge(self, array, left, mid, right):
        left_len = mid - left + 1
        right_len = right - mid

        left_array = array[left:left + left_len]
        right_array = array[mid + 1:mid + 1 + right_len]

        i = 0 
        j = 0 
        k = left 

        while i < left_len and j < right_len:
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < left_len:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < right_len:
            array[k] = right_array[j]
            j += 1
            k += 1

    def mergeSort(self, array, left, right):
        if left < right:
            mid = (left + right) // 2

            self.mergeSort(array, left, mid)
            self.mergeSort(array, mid + 1, right)

            self.merge(array, left, mid, right)
