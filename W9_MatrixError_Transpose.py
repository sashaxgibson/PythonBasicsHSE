from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:

    def __init__(self, listoflists):
        tstlist = []
        for i in listoflists:
            templist = []
            for j in i:
                templist.append(j)
            tstlist.append(templist)
        self.obj_list = tstlist

    def __str__(self):
        uni_lst = []
        for i in self.obj_list:
            uni_lst.append('\t'.join(map(str, i)))
        return '\n'.join(map(str, uni_lst))

    def size(self):
        return len(self.obj_list), len(self.obj_list[0])

    def __add__(self, second_mtrx):
        if self.size() == second_mtrx.size():
            result_mtrx = []
            for i in range(len(self.obj_list)):
                result_line = []
                for j in range(len(self.obj_list[0])):
                    x1 = self.obj_list[i][j]
                    x2 = second_mtrx.obj_list[i][j]
                    result_line.append(x1 + x2)
                result_mtrx.append(result_line)
            return Matrix(result_mtrx)
        else:
            raise MatrixError(self, second_mtrx)
        return Matrix(m1, m2)

    def __mul__(self, mnozh):
        new_matrix = []
        for i in range(len(self.obj_list)):
            new_matrix_line = []
            for j in range(len(self.obj_list[0])):
                xij = self.obj_list[i][j] * mnozh
                new_matrix_line.append(xij)
            new_matrix.append(new_matrix_line)
        return Matrix(new_matrix)

    __rmul__ = __mul__

#exec(stdin.read())

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)

m2 = Matrix([[0, 1, 0], [20, 0, -1]])
try:
    m = m1 + m2
    print('WA\n' + str(m))
except MatrixError as e:
    print(e.matrix1)
    print(e.matrix2)
