import sys
sys.path.append('../Libraries')
import dotMatrix

"""
    kamberg 1.0
"""

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

#framebuffer is an instance of frameBuf
def setByteArray(framebuffer, allCharacters):
    yMax = len(allCharacters)
    if yMax == 0:
        return
    xMax = len(allCharacters[0])
    
    for y in range(yMax):
        for x in range(len(allCharacters[y])):
            framebuffer.pixel(x,y, allCharacters[y][x])
        
                
#list of elements to convert to matrix
def elementsToMatrix(ls):
    matrix = []
    for element in ls:
        matrix.append(dotMatrix.getMatrix(element))
    return matrix 
 
if __name__ == "__main__":
    print(elementsToMatrix(('1', '2', '3' )))
    
    listOfChars1 = []
    listOfChars1.append(dotMatrix.ONE)
    listOfChars1.append(dotMatrix.CC_TOP)
    listOfChars1.append(dotMatrix.SEVEN)
    
    listOfChars2 = []
    listOfChars2.append(dotMatrix.ONE)
    listOfChars2.append(dotMatrix.CC_BTTM)
    listOfChars2.append(dotMatrix.SEVEN)
    #print(listOfChars2)
    #print(listOfChars1)
    dotMatrix.printMatrix(setCompleteList(listOfChars1))
    dotMatrix.printMatrix(setCompleteList(listOfChars2))