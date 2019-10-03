import pandas as pd
import statistics as st
import numpy as np
import xlsxwriter

# from sklearn.model_selection import KFold


dataTrain = pd.read_csv(r'E:\MATKUL\AI\KNNQ\DataTrain_Tugas3_AI.csv',
                            index_col=0, sep='\s*,\s*', header=0, encoding='ascii', engine='python');

barisTrain, kolomTrain = np.size(dataTrain['X1']), 6;
matrixTrain = [[0 for y in range(barisTrain)] for z in range(kolomTrain)];

for i in range(barisTrain):
    matrixTrain[0][i] = dataTrain['X1'][i + 1];
for i in range(barisTrain):
    matrixTrain[1][i] = dataTrain['X2'][i + 1];
for i in range(barisTrain):
    matrixTrain[2][i] = dataTrain['X3'][i + 1];
for i in range(barisTrain):
    matrixTrain[3][i] = dataTrain['X4'][i + 1];
for i in range(barisTrain):
    matrixTrain[4][i] = dataTrain['X5'][i + 1];
for i in range(barisTrain):
    matrixTrain[5][i] = dataTrain['Y'][i + 1];

dataTest = pd.read_csv(r'E:\MATKUL\AI\KNNQ\DataTest_Tugas3_AI.csv',
                           index_col=0, sep='\s*,\s*', header=0, encoding='ascii', engine='python');

barisTest, kolomTest = np.size(dataTest['X1']), 6;
matrixTest = [[0 for y in range(barisTest)] for z in range(kolomTest)];

for i in range(barisTest):
    matrixTest[0][i] = dataTest['X1'][i + 1];
for i in range(barisTest):
    matrixTest[1][i] = dataTest['X2'][i + 1];
for i in range(barisTest):
    matrixTest[2][i] = dataTest['X3'][i + 1];
for i in range(barisTest):
    matrixTest[3][i] = dataTest['X4'][i + 1];
for i in range(barisTest):
    matrixTest[4][i] = dataTest['X5'][i + 1];
# for i in range(barisTest) :
#    matrixTrain[i][5] = dataTest['Y'][i+1];

# print(size(dataTrain['X1']));

euclideanDistance = [[[0 for p in range(barisTrain)] for q in range(barisTest)] for r in range(2)];

for i in range(barisTest):
    for j in range(barisTrain):
        euclideanDistance[0][i][j] = np.sqrt((matrixTrain[0][j] - matrixTest[0][i]) ** 2 +
                                          (matrixTrain[1][j] - matrixTest[1][i]) ** 2 +
                                          (matrixTrain[2][j] - matrixTest[2][i]) ** 2 +
                                          (matrixTrain[3][j] - matrixTest[3][i]) ** 2 +
                                          (matrixTrain[4][j] - matrixTest[4][i]) ** 2);
        euclideanDistance[1][i][j] = matrixTrain[5][j];

kosong = [0 for p in range(2)];
for i in range(barisTest):
    for k in range(barisTrain):
        for j in range(barisTrain-2, -1, -1):
            if euclideanDistance[0][i][j + 1] < euclideanDistance[0][i][j]:
                kosong[0] = euclideanDistance[0][i][j]
                euclideanDistance[0][i][j] = euclideanDistance[0][i][j + 1];
                euclideanDistance[0][i][j + 1] = kosong[0]
                kosong[1] = euclideanDistance[1][i][j]
                euclideanDistance[1][i][j] = euclideanDistance[1][i][j + 1];
                euclideanDistance[1][i][j + 1] = kosong[1]


nol = 0;
satu = 0;
dua = 0;
tiga = 0;
k = 5;
for i in range(barisTest):
    for j in range(k):
        if euclideanDistance[1][i][j] == 0:
            nol = nol + 1 ;
        elif euclideanDistance[1][i][j] == 1:
            satu = satu + 1 ;
        elif euclideanDistance[1][i][j] == 2:
            dua = dua + 1 ;
        elif euclideanDistance[1][i][j] == 3:
            tiga = tiga + 1;
    if nol>satu and nol>dua and nol>tiga:
        matrixTest[5][i] = 0;
    elif satu>nol and satu>dua and satu>tiga:
        matrixTest[5][i] = 1;
    elif dua > nol and dua > satu and dua > tiga:
        matrixTest[5][i] = 2;
    else :
        matrixTest[5][i] = 3;
    satu = 0;
    nol = 0;
    dua= 0;
    tiga = 0;


workbook = xlsxwriter.Workbook('prediksi data test KNN.xlsx')
worksheet = workbook.add_worksheet()

row=0;

for col, data in enumerate(matrixTest):
    worksheet.write_column(row, col, data)

workbook.close()