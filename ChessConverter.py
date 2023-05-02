var_vig = str(input("Pgn: ")) 
#Rei 
if 'R' in var_vig: 
    var_vig = var_vig.replace('R', 'K') 
#Rainha 
if 'D' in var_vig: 
    var_vig = var_vig.replace('D', 'Q') 
#Torre 
if 'T' in var_vig: 
    var_vig = var_vig.replace('T', 'R') 
#Bispo 
#Cavalo 
if 'C' in var_vig: 
    var_vig = var_vig.replace('C', 'N') 
print(var_vig)
