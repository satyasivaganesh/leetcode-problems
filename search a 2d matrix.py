   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=0
        for i in matrix:
            if target in i:
                c=1
        if c==1:
            return 1
        return 0
