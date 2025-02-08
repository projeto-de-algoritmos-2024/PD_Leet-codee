class Solution:
    def numTrees(self, n):
        # Tabela DP semelhante ao Knapsack 0/1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Casos base: 1 árvore vazia e 1 árvore com um nó
        
        # Preenchendo a tabela (parecido com a abordagem iterativa do Knapsack)
        for nodes in xrange(2, n + 1): 
            for root in xrange(1, nodes + 1):
                left = root - 1
                right = nodes - root
                dp[nodes] += dp[left] * dp[right]  # Combinação dos valores
        
        return dp[n]