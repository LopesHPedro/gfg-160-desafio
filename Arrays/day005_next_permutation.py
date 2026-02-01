"""
Objetivo: = Reorganizar os dígitos para formar o próximo número maior possível
Complexidade: Tempo O(N), Espaço O(1).
"""
class Solution:
    def nextPermutation(self, arr):
        pivo = -1
        last = len(arr) - 1

        for i in range(last, 0, -1):
            if arr[i - 1] < arr[i]:
                pivo = i - 1
                break

        if pivo == -1:
            arr.reverse()
            return arr

        for i in range(last, pivo, -1):
            if arr[i] > arr[pivo]:
                arr[pivo], arr[i] = arr[i], arr[pivo]
                break

        start =  pivo + 1
        end = last
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        return arr

if __name__ == '__main__':
    obj = Solution()
    arr1 = [1, 2, 3, 6, 5, 4]
    arr2 = [1, 2 ,3, 4, 5, 6]
    print(obj.nextPermutation(arr1))
    print(obj.nextPermutation(arr2))
