"""
Objetivo: = Inverter um array de inteiros.
Nota: Modifique o array 'no lugar'(in place).
Complexidade: Tempo O(N), Espaço O(1).
"""

class Solution:
    def reverseArray(self, arr):
        start = 0
        end = len(arr) - 1
        for i in range(len(arr)//2):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

if __name__ == '__main__':
    obj = Solution()
    arr = [1, 4, 3, 2, 6, 5]
    print(obj.reverseArray(arr))
