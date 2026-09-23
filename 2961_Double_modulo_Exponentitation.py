class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []

        for i in range(len(variables)):
            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            d = variables[i][3]

            first = pow(a, b, 10)
            res = pow(first, c, d)

            if res == target:
                ans.append(i)

        return ans
        
