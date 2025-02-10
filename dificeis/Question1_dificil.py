class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.memo = {}  # Memoização (semelhante ao cache do Knapsack)
        self.res = float('-inf')  # Inicializa com um valor muito baixo

        def dfs(node):
            if not node:
                return 0
            
            if node in self.memo:  # Verifica se já calculamos esse nó (evita recomputação)
                return self.memo[node]
            
            left_max = max(0, dfs(node.left))  # Como no Knapsack, "incluir ou não"
            right_max = max(0, dfs(node.right))

            # Atualiza o maior caminho possível (similar à escolha ótima no Knapsack)
            self.res = max(self.res, node.val + left_max + right_max)

            # Armazena o resultado no cache (Knapsack Memoization)
            self.memo[node] = node.val + max(left_max, right_max)
            return self.memo[node]

        dfs(root)
        return self.res
