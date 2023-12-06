def square_matrix_simple(matrix=[]):
     if(matrix):
        return ([[y*y for y in x] for x in matrix])
#       return [list(map(lambda x: x**2, row)) for row in matrix]
 
