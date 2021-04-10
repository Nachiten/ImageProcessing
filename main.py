from PIL import Image
import numpy



def printearColor(color):
    if color == 'R':
        printearMatriz(0)
    if color == 'G':
        printearMatriz(1)
    if color == 'B':
        printearMatriz(2)


def printearNuevaMatriz():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            print(nuevaMatriz[unaFila][unaColumna], end=" ")
        print("")


def printearMatriz(elemento):
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            elementoElegido = numpy_array[unaFila][unaColumna][elemento]
            print(elementoElegido, end=" ")
            if elementoElegido < 10:
                print("  ", end="")
            elif elementoElegido < 100:
                print(" ", end="")
        print("")


def modificarMatrizEnIndex(indexFuncion, limite):
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            if indexFuncion == 3:  # YELLOW
                if numpy_array[unaFila][unaColumna][0] >= limite \
                        and numpy_array[unaFila][unaColumna][1] >= limite \
                        and numpy_array[unaFila][unaColumna][2] <= 50:
                    nuevaMatriz[unaFila][unaColumna] = 1

            elif indexFuncion == 4:  # PINK
                if numpy_array[unaFila][unaColumna][0] >= limite \
                        and numpy_array[unaFila][unaColumna][1] <= 50 \
                        and numpy_array[unaFila][unaColumna][2] >= limite:
                    nuevaMatriz[unaFila][unaColumna] = 1

            elif indexFuncion == 5:  # CYAN
                if numpy_array[unaFila][unaColumna][0] <= 50 \
                        and numpy_array[unaFila][unaColumna][1] >= limite \
                        and numpy_array[unaFila][unaColumna][2] >= limite:
                    nuevaMatriz[unaFila][unaColumna] = 1

            elif indexFuncion == 6:  # WHITE
                if numpy_array[unaFila][unaColumna][0] >= 250 \
                        and numpy_array[unaFila][unaColumna][1] >= 250 \
                        and numpy_array[unaFila][unaColumna][2] >= 250:
                    nuevaMatriz[unaFila][unaColumna] = 1

            elif indexFuncion == 7:  # BLACK
                if numpy_array[unaFila][unaColumna][0] <= 7 \
                        and numpy_array[unaFila][unaColumna][1] <= 7 \
                        and numpy_array[unaFila][unaColumna][2] <= 7:
                    nuevaMatriz[unaFila][unaColumna] = 1
            else:
                valoresNoPosibles = [0, 1, 2]
                valoresNoPosibles.remove(indexFuncion)

                if numpy_array[unaFila][unaColumna][indexFuncion] >= limite \
                        and numpy_array[unaFila][unaColumna][valoresNoPosibles[0]] <= 50 \
                        and numpy_array[unaFila][unaColumna][valoresNoPosibles[1]] <= 50:
                    nuevaMatriz[unaFila][unaColumna] = 1
                else:
                    nuevaMatriz[unaFila][unaColumna] = 0


def transformarMatriz(indexFuncion, limite):
    if indexFuncion == 0:
        colorFuncion = 'R'
    elif indexFuncion == 1:
        colorFuncion = 'G'
    elif indexFuncion == 2:
        colorFuncion = 'BLU'
    elif indexFuncion == 3:
        colorFuncion = 'Y'
    elif indexFuncion == 4:
        colorFuncion = 'P'
    elif indexFuncion == 5:
        colorFuncion = 'C'
    elif indexFuncion == 6:
        colorFuncion = 'W'
    elif indexFuncion == 7:
        colorFuncion = 'BLA'
    else:
        colorFuncion = 'R'

    modificarMatrizEnIndex(index, limite)

    return colorFuncion


def vecinosDe(fila, columna):
    vecinosActuales = []

    for unaFila in range(fila - 1, fila + 2):
        for unaColumna in range(columna - 1, columna + 2):
            if unaFila == fila and unaColumna == columna:
                continue
            if nuevaMatriz[unaFila][unaColumna] == 1:
                vecinosActuales.append((unaFila, unaColumna))

    # print("Los vecinos de: " + str((fila, columna)) + " son " + str(vecinosActuales))
    return vecinosActuales


def marcarYEscanearDesdePixel(unaFila, unaColumna):
    nuevaMatriz[unaFila][unaColumna] = 0
    vecinosDePixel = vecinosDe(unaFila, unaColumna)

    if len(vecinosDePixel) != 0:
        for (unaFila, unaColumna) in vecinosDePixel:
            marcarYEscanearDesdePixel(unaFila, unaColumna)


# 1 - Encontrar un punto
# 2 - Marcarlo como vacio
# 3 - Encontrar todos los vecinos
# 4 - Repetir desde paso 2 con cada uno de los vecinos
def hayAlgunCluster():
    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            if nuevaMatriz[unaFila][unaColumna] == 1:
                # print("Encontre el pixel: " + str((unaFila, unaColumna)))
                marcarYEscanearDesdePixel(unaFila, unaColumna)
                nuevaMatriz[unaFila][unaColumna] = 2
                return True
    return False


def contarClusters():
    cantidadClustersActual = 0

    for unaFila in range(0, height):
        for unaColumna in range(0, width):
            if nuevaMatriz[unaFila][unaColumna] == 2:
                cantidadClustersActual += 1

    return cantidadClustersActual


image = Image.open('D:\Escritorio\ImagenPrueba.PNG')
width, height = image.size

for index in range(0, 8):
    numpy_array = numpy.array(image)
    nuevaMatriz = [[0 for _ in range(width)] for _ in range(height)]

    color = transformarMatriz(index, 200)

    while hayAlgunCluster():
        pass

    cantidadClusters = contarClusters()

    print("Hay una cantidad de: " + str(cantidadClusters) + " clusters de color: " + color + " en la imagen.")

# Answers

# Blanco:	4
# Negro:	4

# Rojo: 3 R
# Verde: 1 G
# Azul: 12 B

# Amarillo: 9 Y
# Cyan: 4 C
# Rosa: 4 P
