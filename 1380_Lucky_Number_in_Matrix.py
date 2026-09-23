class Solution:
    def luckyNumbers(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        mini = []
        maxi = []

        # Minimum of every row
        for i in range(n):
            temp = matrix[i][0]

            for j in range(m):
                temp = min(temp, matrix[i][j])

            mini.append(temp)

        # Maximum of every column
        for i in range(m):
            temp = matrix[0][i]

            for j in range(n):
                temp = max(temp, matrix[j][i])

            maxi.append(temp)

        # Find common elements
        ans = []

        for i in range(len(mini)):
            for j in range(len(maxi)):
                if mini[i] == maxi[j]:
                    ans.append(mini[i])

        return ans
