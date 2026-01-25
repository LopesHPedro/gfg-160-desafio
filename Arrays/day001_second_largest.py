"""
Objetivo: Encontrar o segundo maior elemento de um array.
Nota: Retorna -1 se não existir. Complexidade O(N).
"""

class Solution:
	def getSecondLargest(self, arr):
		
		if len(arr) < 2:
			return -1

		largest = max(arr)
		second_largest = -1 

		for ele in arr:
			if ele > second_largest and ele < largest:
				second_largest = ele
				
		return second_largest

if __name__ == "__main__":
	
	sol = Solution()

	# Caso de teste 1
	arr1 = [12, 35, 1, 10, 34, 1]
	print(f'Input: {arr1}')
	print(f'Output: {sol.getSecondLargest(arr1)}')

	# Caso de teste 2
	arr2 = [10, 10, 10]
	print(f'Input: {arr2}')
	print(f'Output: {sol.getSecondLargest(arr2)}')