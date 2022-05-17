
# TODO: comentario
# FIXME: erro

while True:
    # TODO: nome de variavel com letra maiscula 
    #       nome_de_variavel, NOME_DE_VARIAVEL
    #       incluir nome da variabel commands
    Comando = input('Digite o comando para movimentar o robô: ')

    # TODO: incluir nome da variavel como orientação (Inglês)
    x=0; y=0; ori= "N"
    i=0

    # TODO: nome da variavel deve ser em inglês
    posicao = ("N","E","S","W")

    print(f"\n({x},{y},{ori})")

    # TODO: incluir nome da variavel "chart" como "command"
    for char in Comando:
        # TODO: talvez fazer dessa forma -> if char in ['M', 'R', 'L']:

        if char == "M" or char == "R" or char == "L":
            # TODO: if char == 'M':
            #           if ori == 'N':
            if char == "M" and ori == "N":
                if y==4:
                    # TODO: incluir validação em uma função para vefiricar se o robo saira do terreno
                    print ("O próximo movimento fará o robô sair do terreno. Sua movimentação foi travada.")
                    break
            
                y = y + 1
            
            elif char == "M" and ori == "S":
                if y==0:
                    print ("O próximo movimento fará o robô sair do terreno. Sua movimentação foi travada.")
                    break
            
                y=y-1
            
            elif char == "M" and ori == "E":
                if x==4:
                    print ("O próximo movimento fará o robô sair do terreno. Sua movimentação foi travada.")
                    break
            
                x=x+1
            
            elif char == "M" and ori == "W":
                if x==0:
                    print ("O próximo movimento fará o robô sair do terreno. Sua movimentação foi travada.")
                    break
            
                x=x-1

            if char == "R":
                i=i+1

            elif char == "L":
                i=i-1

            i = i % 4
            ori = posicao[i]

            print (f"({x},{y},{ori})")
