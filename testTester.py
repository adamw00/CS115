def hi(L,k):
    amd = True
    for i in range(len(L)):
        if not amd: break
        for d in range(0,k):
            if L[i]>L[i+d]:
                amd = False
                break
    return amd
