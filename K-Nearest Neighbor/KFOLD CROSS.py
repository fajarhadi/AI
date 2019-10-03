import pandas as pd
import statistics as st
import numpy as np

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

kfold = 20
JdataTiapPartisi = int(barisTrain / kfold);

partisi = [[[0 for p in range(JdataTiapPartisi)] for q in range(kfold)] for r in range(kolomTrain)];

x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[0][j][k] = dataTrain['X1'][x + 1];
        x=x+1;
x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[1][j][k] = dataTrain['X2'][x + 1];
        x = x + 1;
x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[2][j][k] = dataTrain['X3'][x + 1];
        x = x + 1;
x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[3][j][k] = dataTrain['X4'][x + 1];
        x = x + 1;
x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[4][j][k] = dataTrain['X5'][x + 1];
        x = x + 1;
x = 0;
for j in range(kfold):
    for k in range(JdataTiapPartisi):
        partisi[5][j][k] = dataTrain['Y'][x + 1];
        x = x + 1;

print('kfold  =  ',kfold);
print('jumlah kolom Train  =  ',kolomTrain);
print('jumlah data tiap partisi  =  ', JdataTiapPartisi);


nilai_K = 1
kebenaran = 0;

for nilai_K in range(1, 21, 1):
    for i in range(kfold):
        anggapDataTest = [[0 for p in range(JdataTiapPartisi)] for q in range(kolomTrain)];
        for k in range(kolomTrain):
            for l in range(JdataTiapPartisi):
                anggapDataTest[k][l] = partisi[k][i][l];

        j = i;
        for k in range(kolomTrain):
            for j in range(j, kfold - 1, 1):
                for l in range(JdataTiapPartisi):
                    partisi[k][j][l] = partisi[k][j + 1][l];

        anggapDataTrain = [[0 for p in range((JdataTiapPartisi * kfold) - JdataTiapPartisi)] for q in
                           range(kolomTrain)];
        v = 0;
        for s in range(kolomTrain):
            for t in range(kfold - 1):
                for u in range(JdataTiapPartisi):
                    anggapDataTrain[s][v] = partisi[s][t][u];
                    v = v + 1;
            v = 0;

        euclideanDistance = [
            [[0 for p in range((JdataTiapPartisi * kfold) - JdataTiapPartisi)] for q in range(JdataTiapPartisi)] for r
            in range(2)];

        for k in range(JdataTiapPartisi):
            for l in range((JdataTiapPartisi * kfold) - JdataTiapPartisi):
                euclideanDistance[0][k][l] = np.sqrt((anggapDataTrain[0][l] - anggapDataTest[0][k]) ** 2 +
                                                  (anggapDataTrain[1][l] - anggapDataTest[1][k]) ** 2 +
                                                  (anggapDataTrain[2][l] - anggapDataTest[2][k]) ** 2 +
                                                  (anggapDataTrain[3][l] - anggapDataTest[3][k]) ** 2 +
                                                  (anggapDataTrain[4][l] - anggapDataTest[4][k]) ** 2);
                euclideanDistance[1][k][l] = anggapDataTrain[5][l];

        kosong = [0 for p in range(2)];
        for k in range(JdataTiapPartisi):
            for m in range((JdataTiapPartisi * kfold) - JdataTiapPartisi):
                for l in range(((JdataTiapPartisi * kfold) - JdataTiapPartisi) - 2, -1, -1):
                    if euclideanDistance[0][k][l + 1] < euclideanDistance[0][k][l]:
                        kosong[0] = euclideanDistance[0][k][l]
                        euclideanDistance[0][k][l] = euclideanDistance[0][k][l + 1];
                        euclideanDistance[0][k][l + 1] = kosong[0]
                        kosong[1] = euclideanDistance[1][k][l]
                        euclideanDistance[1][k][l] = euclideanDistance[1][k][l + 1];
                        euclideanDistance[1][k][l + 1] = kosong[1]

        nol = 0;
        satu = 0;
        dua = 0;
        tiga = 0;
        dummyTestY = [0 for p in range(JdataTiapPartisi)]
        for l in range(JdataTiapPartisi):
            for m in range(nilai_K):
                # print(euclideanDistance[1][l][m]);
                if euclideanDistance[1][l][m] == 0:
                    nol = nol + 1;
                elif euclideanDistance[1][l][m] == 1:
                    satu = satu + 1;
                elif euclideanDistance[1][l][m] == 2:
                    dua = dua + 1;
                else:
                    tiga = tiga + 1;
            if nol > satu and nol > dua and nol > tiga:
                dummyTestY[l] = 0;
            elif satu > nol and satu > dua and satu > tiga:
                dummyTestY[l] = 1;
            elif dua > nol and dua > satu and dua > tiga:
                dummyTestY[l] = 2;
            else:
                dummyTestY[l] = 3;
            satu = 0;
            nol = 0;
            dua = 0;
            tiga = 0;
        bener = 0
        for l in range(JdataTiapPartisi):
            if dummyTestY[l] == anggapDataTest[5][l]:
                bener = bener + 1;
        kebenaran = kebenaran + bener;

        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[0][j][k] = dataTrain['X1'][x + 1];
                x = x + 1;
        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[1][j][k] = dataTrain['X2'][x + 1];
                x = x + 1;
        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[2][j][k] = dataTrain['X3'][x + 1];
                x = x + 1;
        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[3][j][k] = dataTrain['X4'][x + 1];
                x = x + 1;
        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[4][j][k] = dataTrain['X5'][x + 1];
                x = x + 1;
        x = 0;
        for j in range(kfold):
            for k in range(JdataTiapPartisi):
                partisi[5][j][k] = dataTrain['Y'][x + 1];
                x = x + 1;

    akurasi = kebenaran / (kfold * JdataTiapPartisi);
    print('akurasi untuk K = ',nilai_K,' adalah     :   ',akurasi);
    akurasi = 0;
    kebenaran = 0;
    benar = 0;
