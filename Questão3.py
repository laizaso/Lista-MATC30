import random

def gcbrMedian(gcbrContagem, gcbrD):
    gcbrAcumulado = 0
    if gcbrD % 2 == 1:
        gcbrMeio = gcbrD // 2 + 1
        for gcbrI in range(201):
            gcbrAcumulado += gcbrContagem[gcbrI]
            if gcbrAcumulado >= gcbrMeio:
                return gcbrI
    else:
        gcbrPrimeiro = gcbrD // 2
        gcbrSegundo = gcbrPrimeiro + 1
        gcbrMed1 = None
        gcbrMed2 = None
        for gcbrI in range(201):
            gcbrAcumulado += gcbrContagem[gcbrI]
            if gcbrMed1 is None and gcbrAcumulado >= gcbrPrimeiro:
                gcbrMed1 = gcbrI
            if gcbrAcumulado >= gcbrSegundo:
                gcbrMed2 = gcbrI
                break
        return (gcbrMed1 + gcbrMed2) / 2

def gcbrActivityNotifications(gcbrExpenditure, gcbrD):
    gcbrNotificacoes = 0
    gcbrContagem = [0] * 201  
    for gcbrI in range(gcbrD):
        gcbrContagem[gcbrExpenditure[gcbrI]] += 1

    for gcbrI in range(gcbrD, len(gcbrExpenditure)):
        gcbrMediana = gcbrMedian(gcbrContagem, gcbrD)
        if gcbrExpenditure[gcbrI] >= 2 * gcbrMediana:
            gcbrNotificacoes += 1

        gcbrContagem[gcbrExpenditure[gcbrI - gcbrD]] -= 1
        gcbrContagem[gcbrExpenditure[gcbrI]] += 1

    return gcbrNotificacoes

def gcbrGerarDados(gcbrN, gcbrMaxVal=200):
    return [random.randint(0, gcbrMaxVal) for _ in range(gcbrN)]

def gcbrMain():
    gcbrN, gcbrD = 9, 5
    gcbrGastos = [2, 3, 4, 2, 3, 6, 8, 4, 5]  
    gcbrResultado = gcbrActivityNotifications(gcbrGastos, gcbrD)
    print("Notificações:", gcbrResultado)

if __name__ == '__main__':
    gcbrMain()
