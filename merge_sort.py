# mergesort

class Solution():
    def merge(self,arr,low,mid,high):
        temp = []
        left_pointer = low #pointer of the left part
        right_pointer = mid+1 # pointer of the right part

        
        while left_pointer <= mid and right_pointer <= high:
            if left_pointer < right_pointer:
                temp.append(arr[left_pointer])
                left_pointer += 1
            else:
                temp.append(arr[right_pointer])
                right_pointer += 1

        


    def mergesort(self, arr, low, high):

        if low >= high: # base case
            return None
        
        mid = (low + high)//2

        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid+1, high)
        self.merge(arr, low, mid, high)
