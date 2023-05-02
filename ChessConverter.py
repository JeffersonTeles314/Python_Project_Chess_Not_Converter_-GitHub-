
def read_TXT():
    return

def Write_TXT(strtxt,nometxt):
    FINAL_FILE = open(str(title)+".txt", "x")
    for linha in textlist:
        FINAL_FILE.write(linha)
    FINAL_FILE.close()

def convertstr(var_vig):
    var_vig = str(input("Pgn: ")) 
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
