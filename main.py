pip install -U numpy


import numpy as np
Data = np.zeros((5,8), int)
Data[0][0] = 0
Data[0][1] = 100
Data[0][2] = 200
Data[0][3] = 300
Data[0][4] = 400
Data[0][5] = 500
Data[0][6] = 600
Data[0][7] = 700
Data[1][0] = 0
Data[1][1] = 10
Data[1][2] = 20
Data[1][3] = 30
Data[1][4] = 38
Data[1][5] = 43
Data[1][6] = 49
Data[1][7] = 52
Data[2][0] = 0
Data[2][1] = 13
Data[2][2] = 25
Data[2][3] = 37
Data[2][4] = 47
Data[2][5] = 55
Data[2][6] = 61
Data[2][7] = 66
Data[3][0] = 0
Data[3][1] = 6
Data[3][2] = 13
Data[3][3] = 20
Data[3][4] = 27
Data[3][5] = 33
Data[3][6] = 38
Data[3][7] = 41
Data[4][0] = 0
Data[4][1] = 24
Data[4][2] = 36
Data[4][3] = 42
Data[4][4] = 46
Data[4][5] = 48
Data[4][6] = 48
Data[4][7] = 49

Data[0][0] = 0
Data[0][1] = 100
Data[0][2] = 200
Data[0][3] = 300
Data[0][4] = 400
Data[0][5] = 500
Data[0][6] = 600
Data[0][7] = 700
Data[1][0] = 0
Data[1][1] = 10
Data[1][2] = 20
Data[1][3] = 30
Data[1][4] = 38
Data[1][5] = 43
Data[1][6] = 49
Data[1][7] = 52
Data[2][0] = 0
Data[2][1] = 13
Data[2][2] = 25
Data[2][3] = 37
Data[2][4] = 47
Data[2][5] = 55
Data[2][6] = 61
Data[2][7] = 66
Data[3][0] = 0
Data[3][1] = 6
Data[3][2] = 13
Data[3][3] = 20
Data[3][4] = 27
Data[3][5] = 33
Data[3][6] = 38
Data[3][7] = 41
Data[4][0] = 0
Data[4][1] = 24
Data[4][2] = 36
Data[4][3] = 42
Data[4][4] = 46
Data[4][5] = 48
Data[4][6] = 48
Data[4][7] = 49

F = np.zeros((4, 8), int)
F[3] = Data[4]
for row in [3, 2]:
    for col in range (8):
        f = np.zeros(8)
        x_prev = 100 * col
        for run in range(col+1):
            u = x_prev - run*100
            ind = int(u/100)
            w = Data[row][ind]
            f[run] = w + F[row][run]
        F[row-1][col] = np.amax(f)
for row in [1]:
    for col in range (8):
        f = np.zeros(8)
        x_prev = 700
        for run in range(col+1):
            u = x_prev - run*100
            ind = int(u/100)
            w = Data[row][ind]
            f[run] = w + F[row][run]
            # print(F[row][run])
        F[row-1][col] = np.amax(f)
print(F[row][run])
print(w)

print (F)