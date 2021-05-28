def spiralOrder(matrix):
    rowstart = 0
    rowstop = len(matrix) - 1
    colstart = 0
    for i in range(rowstop+1):
        colstop = len(matrix[i]) - 1
    result = []
    dr = 0
    while rowstart <= rowstop and colstart <= colstop:
        if dr == 0:
            for i in range(colstart, colstop + 1):
                result.append(matrix[rowstart][i])
            rowstart += 1
            dr=1
        elif dr ==1:
            for i in range(rowstart, rowstop + 1):
                result.append(matrix[i][colstop])
            colstop -= 1
            dr = 2
        elif dr ==2:

            for i in range(colstop, colstart - 1, -1):
                result.append(matrix[rowstop][i])
            rowstop -= 1
            dr = 3
        elif dr ==3:

            for i in range(rowstop, rowstart - 1, -1):
                result.append(matrix[i][colstart])
            colstart += 1
            dr = 0

    return result


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = spiralOrder(matrix)
    print(result)


main()
