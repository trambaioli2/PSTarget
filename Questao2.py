def letraA(palavra): #Cria a função para teste
    cont = 0 #inicia o contador
    lista = ['a', 'ã', 'á', 'à', 'â', 'A', 'Á', 'Ã', 'Â', 'À'] #lista com os possíveiscaracteres relacionados à letra "a"
    for i in palavra: #i assume cada letra da palavra informada
        if i in lista: #se a letra atul está na lista o contador recebe +1
            cont+=1
    return cont

n = letraA(input()) #n recebe o número de aparições da letra a na palavra informada pelo usuario
if n == 0: print('A palavra não contém a letra "a"') #se n é 0 então não existe "a" na palavra
else: print('A letra "a" aparece '+str(n)+' vezes')