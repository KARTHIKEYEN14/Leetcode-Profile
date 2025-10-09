class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        res = []
        i = 0
        while(i<len(matrix[0])):
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            res.append(arr)
            arr = []
            i+=1
        return res
        