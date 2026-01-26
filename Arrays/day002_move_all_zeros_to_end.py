"""
Objetivo: Mover zeros para o final mantendo a ordem dos nao-zeros.
Complexidade: Tempo O(N), Espaco O(1).
"""

class Solution:
    def pushZerosToEnd(self, arr):
        posi = 0
        
        # Passo 1: Move todos os nao-zeros para frente
        for ele in arr:
            if ele != 0:
                arr[posi] = ele
                posi += 1
        
        # Passo 2: Preenche o restante com zeros
        for i in range(posi, len(arr)):
            arr[i] = 0
            
        return arr

if __name__ == '__main__':
    obj = Solution()
    
    # Caso 1: Padrao
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(f"Input: [1, 2, 0, 4, 3, 0, 5, 0]")
    print(f"Output: {obj.pushZerosToEnd(arr)}") # Esperado: [1, 2, 4, 3, 5, 0, 0, 0]

    # Caso 2: Apenas zeros
    arr2 = [0, 0, 0]
    print(f"Input: [0, 0, 0]")
    print(f"Output: {obj.pushZerosToEnd(arr2)}") # Esperado: [0, 0, 0]
