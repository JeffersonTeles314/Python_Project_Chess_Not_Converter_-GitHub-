# Abrir Aquivo para Ler - lo

def read_TXT():
    with open("chesstxt.txt", "r", encoding="utf8") as FINAL_FILE:
        dfsd = FINAL_FILE.readline()
        return dfsd

def Write_TXT(inputtxt):
    with open("chesstxt.txt", "a", encoding="utf8") as FINAL_FILE:
        FINAL_FILE.write("\n"+inputtxt)

def convertstr(var_vig):
    # Peão

    # Rei
    if 'R' in var_vig: 
        var_vig = var_vig.replace('R', 'K') 
    # Rainha 
    if 'D' in var_vig: 
        var_vig = var_vig.replace('D', 'Q') 
    # Torre 
    if 'T' in var_vig: 
        var_vig = var_vig.replace('T', 'R') 
    # Bispo
        # Não Necessário
    # Cavalo 
    if 'C' in var_vig: 
        var_vig = var_vig.replace('C', 'N') 
    return var_vig

var1 = read_TXT()
var1 = convertstr(var1)
Write_TXT(var1)
