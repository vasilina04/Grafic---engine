class Matrix:
    def __init__(self, matrix: [float], mul):
        self.matrix = matrix
        self.mul = mul

    def determinant(self):
        width = len(self.matrix)
        height = len(self.matrix[0])
        if width != height:
            return "Erorr wrong"
        if width == 1:
            return self.mul * self.matrix[0][0]
        else:
            sign = -1
            answer = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(self.matrix[j][k])
                    m.append(buff)
                sign *= -1
                answer = answer + self.mul * Matrix.determinant(m, sign * (self.matrix[0][i]))
        return answer

test_matrix = [[3,2,-3],[7,-1,0],[2,-4,5]]
mul = 1

print(Matrix.determinant(test_matrix, mul))