import BigMatrixDisplay as display
import BigMatrixPoints as points
import BigMatrixHoleDetection as detection

if __name__ == "__main__":
    display.clear()
    while True:
        holes = detection.generateStonesInHoles()
        points.add(holes[0], holes[1], holes[2], holes[3])
        pointsTotaal, aantalInVakken, lastAdded = points.puntenTotaal()
        display.show(lastAdded, pointsTotaal)
        