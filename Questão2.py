import random

def gcbrInsertionSort(gcbrArr):
    gcbrDeslocamentos = 0
    gcbrN = len(gcbrArr)
    for gcbrI in range(1, gcbrN):
        gcbrChave = gcbrArr[gcbrI]
        gcbrJ = gcbrI - 1
        while gcbrJ >= 0 and gcbrArr[gcbrJ] > gcbrChave:
            gcbrArr[gcbrJ + 1] = gcbrArr[gcbrJ]
            gcbrDeslocamentos += 1
            gcbrJ -= 1
        gcbrArr[gcbrJ + 1] = gcbrChave
    return gcbrDeslocamentos

def gcbrGenerateRandomArray(gcbrSize, gcbrMinVal=1, gcbrMaxVal=100):
    return [random.randint(gcbrMinVal, gcbrMaxVal) for _ in range(gcbrSize)]

def gcbrMain():
    gcbrT = 2
    gcbrCasos = [
        [1, 1, 1, 2, 2],
        [2, 1, 3, 1, 2]
    ]

    for gcbrCaso in gcbrCasos:
        gcbrArr = gcbrCaso[:]
        gcbrResultado = gcbrInsertionSort(gcbrArr)
        print(gcbrResultado)

if __name__ == '__main__':
    gcbrMain()
