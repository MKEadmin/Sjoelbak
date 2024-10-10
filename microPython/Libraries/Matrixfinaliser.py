import dotMatrix_6x6 as m
import MatrixHelp as hlp

#listOfChars is a list of dot_matrix chars
#returns a matrix with all the characters
def setCompleteList( listOfChars ):
    allCharacters = []
    if len(listOfChars) == 0:
        return allCharacters
    y = 0
    while y < len(listOfChars[0]):
        line = []
        for c in listOfChars:
            line = line + list(c[y])
        allCharacters.append(list(line))
        y = y + 1            
    return allCharacters

def get_sentence(text):
    list_in_sentence = []
    for char in text:
        list_in_sentence.append(m.getMatrix(char))   
    return list_in_sentence  
    
#width of the first matrix is leadingf
def verticalAppendMatrix(verticalMatrixList):
    if len(verticalMatrixList) == 0:
        return []
    maxWidth = 0
    for m in verticalMatrixList:
        if len(m) > maxWidth:
            maxWidth = len(m)
    maxWidth = 32
    matrix = hlp.resizeMatrix(verticalMatrixList[0], maxWidth, center = True)
    for m in verticalMatrixList[1:]:
        matrix3 = hlp.resizeMatrix(m, maxWidth, center = True)
    
if __name__ == "__main__":
    text = """Hallo
Dit is een test
"""
    listText = text.split("\n")
    matrix = []
    for txt in listText:
        list_in_sentence = get_sentence(txt)
        matrix.append(setCompleteList(list_in_sentence))
    #new_matrix =hlp.make_upside_down(matrix)
    matrix = verticalAppendMatrix(matrix)
    #hlp.terminal_display(matrix)
