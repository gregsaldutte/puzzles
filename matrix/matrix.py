class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self):
        row_index = len(self.matrix_string.split("\n"))
        row_list = []
        for i in range(row_index):
            row_list.append(self.matrix_string.split("\n")[i].split())
        return(row_list)    

    def column(self):
        row_index = len(self.matrix_string.split("\n"))
        column_index = len(self.matrix_string.split("\n")[0].split())
        column_list = []
        
        for j in range(row_index):
            col_element = self.matrix_string.split("\n")[j]
            for i in range(column_index):
                if j==0:
                    column_list.append([col_element.split()[i]])
                else:
                    column_list[i].append(col_element.split()[i])
        return(column_list)
    
Matrix_trial = '''9 8 7
5 3 2
6 6 7'''

my_matrix = Matrix(Matrix_trial)

print(my_matrix.row())
print(my_matrix.column())
                    
