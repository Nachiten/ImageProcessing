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


def modificarMatrizEnIndex(index, limite):
    for unaFila in range(0, height):
        for unaColumna in range(0, width):

            # 0 = r
            # 1 = g
            # 2 = b
            # 3 = y

            if index == 3:
                if numpy_array[unaFila][unaColumna][0] >= limite \
                        and numpy_array[unaFila][unaColumna][1] >= limite\
                        and numpy_array[unaFila][unaColumna][2] <= 50:
                    nuevaMatriz[unaFila][unaColumna] = 1
            else:
                valoresNoPosibles = [0, 1, 2]
                valoresNoPosibles.remove(index)

                if numpy_array[unaFila][unaColumna][index] >= limite \
                        and numpy_array[unaFila][unaColumna][valoresNoPosibles[0]] <= 50 \
                        and numpy_array[unaFila][unaColumna][valoresNoPosibles[1]] <= 50:
                    nuevaMatriz[unaFila][unaColumna] = 1
                else:
                    nuevaMatriz[unaFila][unaColumna] = 0


def transformarMatriz(colorActual, limite):
    if colorActual == 'R':
        modificarMatrizEnIndex(0, limite)

    if colorActual == 'G':
        modificarMatrizEnIndex(1, limite)

    if colorActual == 'B':
        modificarMatrizEnIndex(2, limite)

    if colorActual == 'Y':
        modificarMatrizEnIndex(3, limite)


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

for index in range(0, 4):
    numpy_array = numpy.array(image)
    nuevaMatriz = [[0 for _ in range(width)] for _ in range(height)]

    if index == 0:
        color = 'R'
    elif index == 1:
        color = 'G'
    elif index == 2:
        color = 'B'
    elif index == 3:
        color = 'Y'
    else:
        color = 'R'

    transformarMatriz(color, 200)

    while hayAlgunCluster():
        pass

    cantidadClusters = contarClusters()

    print("Hay una cantidad de: " + str(cantidadClusters) + " clusters de color: " + color + " en la imagen.")


# Answers
# Amarillo: 9
# Rojo: 3
# Cyan: 3
# Verde: 1
# Rosa: 4
# Azul: 12
# Blanco:	4
# Negro:	4
