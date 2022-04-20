while True:
    Comando = input('Digite o comando para movimentar o robô: ')

    x=0; y=0; ori= "N"
    i=0
    posicao = ("N","E","S","W")

    print (f"\n({x},{y},{ori})")
    
    for char in Comando:
        if char == "M" or char == "R" or char == "L":
            if char == "M" and ori == "N":
                if y==4:
                    print ("O próximo movimento fará o robô sair do terreno. Sua movimentação foi travada.")
                    break
                y=y+1
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

            i=i%4
            ori = posicao[i]

            print (f"({x},{y},{ori})")
