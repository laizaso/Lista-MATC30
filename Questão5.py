from collections import defaultdict

def gcbrSimilarPair(gcbrN, gcbrK, gcbrEdges):
    gcbrTree = defaultdict(list)
    gcbrTemPai = [False] * (gcbrN + 1)

    for gcbrPai, gcbrFilho in gcbrEdges:
        gcbrTree[gcbrPai].append(gcbrFilho)
        gcbrTemPai[gcbrFilho] = True

    gcbrRaiz = -1
    for gcbrI in range(1, gcbrN + 1):
        if not gcbrTemPai[gcbrI]:
            gcbrRaiz = gcbrI
            break

    gcbrResultado = 0
    gcbrCaminho = []

    def gcbrDFS(gcbrNo):
        nonlocal gcbrResultado
        for gcbrAncestral in gcbrCaminho:
            if abs(gcbrAncestral - gcbrNo) <= gcbrK:
                gcbrResultado += 1
        gcbrCaminho.append(gcbrNo)
        for gcbrFilho in gcbrTree[gcbrNo]:
            gcbrDFS(gcbrFilho)
        gcbrCaminho.pop()

    gcbrDFS(gcbrRaiz)
    return gcbrResultado

gcbrN = 5
gcbrK = 2
gcbrEdges = [(3, 2), (3, 1), (1, 4), (1, 5)]

print(gcbrSimilarPair(gcbrN, gcbrK, gcbrEdges)) 