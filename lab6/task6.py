import numpy as np

def rdCSV(csv_file):
    with open(csv_file) as file:
        pre_res = []
        res = []
        nd_row = []
        csv_string = file.read()
        csv_string = csv_string.split("\n")
        for row in csv_string:
            pre_res.append(eval(row))
        for i in range(0, len(pre_res[0])):
            for j in range(0, len(pre_res[0])):
                nd_row.append(pre_res[j][i])
            res.append(nd_row)
            nd_row = []
    return res

def mMyMatrix(matrix):
    new_row = []
    arr_matrix = []
    for k in range(0, len(matrix)):
        for i in range(0, len(matrix[k])):
            for j in range(0, len(matrix[k])):
                if (matrix[k][i] < matrix[k][j]):
                    new_row.append(1)
                elif (matrix[k][i] == matrix[k][j]):
                    new_row.append(0.5)
                elif (matrix[k][i] > matrix[k][j]):
                    new_row.append(0)
        arr_matrix.append(new_row)
        new_row = []
    return arr_matrix

def mfMatrix(matrixs):
    fMatrix = []
    for i in range(0, len(matrixs[0])):
        sum = 0
        for k in range(0, len(matrixs)):
            sum += matrixs[k][i]
        fMatrix.append(sum/len(matrixs))
    return fMatrix


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def mKMatrix(fMatrix, k = [1/3, 1/3, 1/3]):
    kMatrix = list(split(fMatrix, len(k)))
    n = len(kMatrix[0])
    kP = np.ones(n) / n
    kN = None
    while True:
        y = np.matmul(kMatrix, kP)
        lbd = np.matmul(np.ones(n), y)
        kN = (1 / lbd) * y
        diff = abs(kN - kP)
        max = diff.max()
        if max <= 0.001:
            break
        else:
            kP = kN
    return np.around(kN, 3)

def task(csvString):
    res1 = readCSV(csvString)
    res2 = mMyMatrix(res1)
    res3 = mfMatrix(res2)
    res4 = mKMatrix(res3)
    return res4
    
print(task("./task6_data.csv"))