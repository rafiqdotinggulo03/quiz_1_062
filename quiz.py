class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flat_matrix = [element for row in self.matrix for element in row]
        min_value = min(flat_matrix)
        max_value = max(flat_matrix)
        return min_value, max_value

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(transposed_matrix)

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result_matrix = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*other.matrix)] for row_a in self.matrix]
        return Matrix(result_matrix)

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("The matrices must have the same dimensions.")
        result_matrix = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.matrix, other.matrix)]
        return Matrix(result_matrix)


if __name__ == "__main__":
    # Matrix A
    matrix_a = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    # Create Matrix object
    a = Matrix(matrix_a)

    # 1. Menghitung elemen terbesar dan terkecil
    min_value, max_value = a.find_min_max()
    print("Nilai Minimum:", min_value)
    print("Nilai Maksimum:", max_value)

    # 2. Transpose matrix
    t = a.transpose()
    print("Transpose matrix:")
    for row in t.matrix:
        print(row)

    # 3. Menghitung perkalian matrix A dan T
    product = a.multiply(t)
    print("Hasil perkalian matrix (t) dan (a): ")
    for row in product.matrix:
        print(row)

    # 4. Menghitung penjumlahan matrix T dan A
    sum_result = t.add(a)
    print("Hasil penjumlahan matrix (t) dan (a):")
    for row in sum_result.matrix:
        print(row)