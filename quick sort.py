# quick sort

class Solution():
    def partition(self, arr, low, pivot, high):

        
        temp = []

        
        pointer = low
        while pointer <= high:
            if arr[pivot] >= arr[pointer]:
                
                temp.append(arr[pointer])
                
            pointer += 1



        new_pos_pivot = low + len(temp) - 1 # new position of the pivot in the altered array
        


        
        pointer = low
        while pointer <= high:
            if arr[pivot] < arr[pointer]:
                
                temp.append(arr[pointer])
                
            pointer += 1


        
        for i in range(low, high+1):
            arr[i] = temp[i - low]
       
        self.quicksort(arr,low,new_pos_pivot - 1)
        self.quicksort(arr,new_pos_pivot + 1, high)





    def quicksort(self, arr, low, high):

        if low >= high:
            return 

        self.partition(arr, low, high, high)





arr = [1,0,4,2,3,2]
print(arr)

sol = Solution()
sol.quicksort(arr, 0, len(arr)-1)

print(arr)

        
