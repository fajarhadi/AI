import pandas
import statistics
import numpy


data = pandas.read_csv(r'E:\MATKUL\AI\FuzzyLogic\DataTugas2.csv',
                       index_col= 0, sep='\s*,\s*', header=0, encoding='ascii', engine='python');

baris, kolom= 100, 5;
matrix = [[0 for y in range(kolom)] for z in range(baris)]
hasil = []

saveP=data['Pendapatan']
minP = min(saveP)
maxP = max(saveP)
avgP = numpy.round_(statistics.mean(saveP),2)
stdP = numpy.round_(statistics.stdev(saveP),2)
minzP = avgP - stdP
plusP = avgP + stdP

saveH=data['Hutang']
minH = min(saveH)
maxH = max(saveH)
avgH = numpy.round_(statistics.mean(saveH),2)
stdH = numpy.round_(statistics.stdev(saveH),2)
minzH = avgH - stdH
plusH = avgH + stdH

for i in range(saveP.count()):
    matrix[i][0] = saveP[i+1];
for i in range(saveH.count()):
    matrix[i][1] = saveH[i+1];

derajatP = [[0 for b in range(3)] for c in range(100)];
derajatH = [[0 for e in range(3)] for f in range(100)];

#FUZIFIKASI
for i in range(saveP.count()):
    if saveP[i+1] <= minzP:
        derajatP[i][0] = 1
        derajatP[i][1] = 0
        derajatP[i][2] = 0
    elif saveP[i+1] <= avgP:
        derajatP[i][0] = (avgP-saveP[i+1])/(avgP-minzP)
        derajatP[i][1] = (saveP[i+1]-minzP)/(avgP-minzP)
        derajatP[i][2] = 0
    elif saveP[i+1] <= plusP:
        derajatP[i][0] = 0
        derajatP[i][1] = (plusP-saveP[i+1])/(plusP-avgP)
        derajatP[i][2] = (saveP[i+1]-avgP)/(plusP-avgP)
    else:
        derajatP[i][0] = 0
        derajatP[i][1] = 0
        derajatP[i][2] = 1

for i in range(saveH.count()):
    if saveH[i+1] <= minzH:
        derajatH[i][0] = 1
        derajatH[i][1] = 0
        derajatH[i][2] = 0
    elif saveH[i+1] <= avgH:
        derajatH[i][0] = (avgH-saveH[i+1])/(avgH-minzH)
        derajatH[i][1] = (saveH[i+1]-minzH)/(avgH-minzH)
        derajatH[i][2] = 0
    elif saveH[i+1] <= plusH:
        derajatH[i][0] = 0
        derajatH[i][1] = (plusH-saveH[i+1])/(plusH-avgH)
        derajatH[i][2] = (saveH[i+1]-avgH)/(plusH-avgH)
    else:
        derajatH[i][0] = 0
        derajatH[i][1] = 0
        derajatH[i][2] = 1

#DEFUZIFIKASI
for i in range(100):
    if derajatP[i][0] >= 0.5:
        matrix[i][2] = 'RENDAH'
    elif derajatP[i][1] >= 0.48:
        matrix[i][2] = 'SEDANG'
    else:
        matrix[i][2] = 'TINGGI'

for i in range(100):
    if derajatH[i][2] >= 0.5:
        matrix[i][3] = 'TINGGI'
    elif derajatH[i][1] >= 0.48:
        matrix[i][3] = 'SEDANG'
    else:
        matrix[i][3] = 'RENDAH'

#INFERENSI
for i in range(100):
    if (matrix[i][2]=='RENDAH' and matrix[i][3]=='TINGGI') or (matrix[i][2]=='SEDANG' and matrix[i][3]=='TINGGI'):
        matrix[i][4] = 'YA'
    else:
        matrix[i][4] = 'TIDAK'

#OUTPUT
for i in range(100):
    print(matrix[i][:])
    
o=0

for i in range(100):
    if matrix[i][4]=='YA':
        #hasil.append([i+1])
        print(i+1)
#data=pandas.DataFrame({'No' : hasil})
#data.to_csv('TebakanTugas2.csv', index=False)