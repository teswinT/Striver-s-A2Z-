# mergesort

class Solution():
    def merge(self,arr,low,mid,high):
        temp = []
        left,right = low,mid+1 # left is leftpointer and right is rightpointer

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        

        


    def mergesort(self, arr, low, high):

        if low >= high: # base case
            return None
        mid = (low + high)//2

        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid+1, high)
        self.merge(arr, low, mid, high)


arr = [2,3,1,4,5]
print(arr)

sol = Solution()
sol.mergesort(arr,0,len(arr)-1)

print(arr)
