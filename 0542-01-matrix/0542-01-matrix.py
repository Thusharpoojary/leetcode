class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r=len(mat)
        c=len(mat[0])

        ans=[[-1]*c for _ in range(r)]

        q=deque()

        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    q.append((i,j))
                    ans[i][j]=mat[i][j]
        
        direction=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            ro,co=q.popleft()

            for dr,dc in direction:
                nr=dr+ro
                nc=dc+co
                if 0 <= nr < r and 0 <= nc < c and ans[nr][nc] == -1:
                    ans[nr][nc] = ans[ro][co] + 1
                    q.append((nr, nc))
        return ans


        