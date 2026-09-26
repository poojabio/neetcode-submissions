class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)-1):
            maxima = max(arr[i::])
            if arr[i] == maxima:
                arr[i] = max(arr[(i+1)::])
            else:
                arr[i] = maxima
        arr[-1] = -1
        return arr

            