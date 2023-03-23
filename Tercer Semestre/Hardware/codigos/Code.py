def Code(sTxT, nKey)
    sMsg = ''
    for xE in sTxt:
        nXOR = ord(xE) ^ nKey
        nLSB = nXOR & 0x0F
        nMSB = nXOR >> 0x04
        nAux = nLSB << 4 | nMSB
        sMsg += chr(nAux)

    return nAux

print(Code('O', 19))
