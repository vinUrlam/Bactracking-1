class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        L = len(num)
        ans = set()
        
        def backtrack(i, total, last, expr):
            if i == L:
                if total == target:
                    ans.add(expr)
                return
            
            for j in range(i, L):
                n = int(num[i:j+1]) # '1' or '12' or '123'
                if i == 0:
                    backtrack(j+1, n, n, str(n))
                else:
                    backtrack(j+1, total + n, n, expr + '+' + str(n))
                    backtrack(j+1, total - n, -n, expr + '-' + str(n))
                    backtrack(j+1, total - last + last * n, last * n, expr + '*' + str(n))
                if n == 0:
                    break
                    
        backtrack(0, 0, 0, '')
        return list(ans)