"""
Objetivo: = Rotacionar o array para a esquerda.
Complexidade: Tempo O(N), Espaço O(1).
"""

class Solution:
    def reverse_custom(self, arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start +=1
            end -= 1

    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        self.reverse_custom(arr,0, d-1)
        self.reverse_custom(arr, d, n-1)
        arr.reverse()
        return arr

if __name__ == '__main__':
    obj = Solution()
    arr = [1, 2, 3, 4, 5]
    d = 2
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    d2 = 3
    print(obj.rotateArr(arr, d))
    print(obj.rotateArr(arr2, d2))
