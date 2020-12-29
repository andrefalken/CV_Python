def sair(var):
    return (var == 'sair')

def numPos(num):
	return (int(num) > 0)
	
valores = '';

while (sair):
	var = input('Digite um número ou "sair" para Sair: ')    
	if sair(var):
		break
	elif numPos(var):
		valores = valores+' '+var
    
print(valores)