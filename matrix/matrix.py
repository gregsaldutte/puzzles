class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row_index = len(self.matrix_string.split("\n"))
        row_list = []
        for i in range(row_index):
            row_list.append([ int(x) for x in self.matrix_string.split("\n")[i].split()])
        
        return(row_list[index-1])    

    def column(self, index):
        row_index = len(self.matrix_string.split("\n"))
        column_index = len(self.matrix_string.split("\n")[0].split())
        column_list = []
        
        for j in range(row_index):
            col_element = self.matrix_string.split("\n")[j]
            for i in range(column_index):
                if j==0:
                    column_list.append([int(col_element.split()[i])])
                else:
                    column_list[i].append(int(col_element.split()[i]))                 
        return(column_list[index-1])
    

                    
