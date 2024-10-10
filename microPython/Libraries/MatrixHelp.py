#this function is for the Header
def _printHeader(width, leadingSpace = 2):
    print(f" {' ' * leadingSpace}", end="")
    for x in range(width):
            print(f"{x//10}" if x % 10 == 0 else " ", end="")
    print()
    print(f"O{' ' * leadingSpace}", end="")
    for x in range(width):
        print(f"{x%10}", end="")
    print()
    print(" " + " " * leadingSpace, end="")
    for x in range(width):
        print(f"-", end="")
    print()

#Getting the hight of the matrix
def _getWidtHeiht(matrix):
    return len(matrix[0]),len(matrix)

#Numbering the rows
def _rowNumbering(row):
    print(f"{row//10}", end="")
    print(f"{row%10}|", end="")
    
#Print to the Terminal
def terminal_display(matrix):
    width,height = _getWidtHeiht(matrix)
    _printHeader(width)
    
    for y in range(height):
        _rowNumbering(y)
        for x in range(width):
            print(" " if matrix[y][x] == 0 else "x", end="")
        print()

#Make the matrix upside down and return a new list
def make_upside_down(matrix):
    new_matrix = copyMatrix(matrix)
    new_matrix.reverse()
    for row in new_matrix:
        row.reverse()
    return new_matrix

def copyMatrix(matrix):
    newMatrix = []
    for row in matrix:
        newMatrix += [list(row)]
    return newMatrix
    
def resizeMatrix(matrix, maxWidth, fillCharacter = 0, center = True):
    newMatrix = []
    for row in matrix:
        newRow = []
        for idx, element in enumerate(row):
            if idx < maxWidth:
                newRow.append(element)
        while idx < maxWidth:
            newRow.append(fillCharacter)
            idx += 1
        print(idx)
        newMatrix.append(newRow)
    return newMatrix

if __name__ == "__main__":
    letter =(
        (0, 0, 0, 0, 0, 0, 0,),
        (0, 0, 0, 0, 0, 0, 0,),
        (1, 0, 0, 0, 0, 1, 0,),
        (1, 0, 0, 0, 0, 1, 0,),
        (0, 1, 0, 0, 1, 0, 0,),
        (0, 0, 1, 1, 0, 0, 0,),
        )
    matrix = resizeMatrix(letter, 32, center = True)
    
    #matrix = make_upside_down(letter)
    terminal_display(matrix)

    