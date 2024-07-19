#placa do times
gols_time_a = input(" Informe o Gols do time A: ")
gols_time_b = input(" Informe o Gols do time B: ")
gols_time_c = input(" Informe o Gols do time C: ")
gols_time_d = input(" Informe o Gols do time D: ")

#penalte em caso de empate
penaltis_time_a = None # inicializar com None
penaltis_time_b = None
penaltis_time_c = None
penaltis_time_d = None 

#verificando empate e penaltes
if gols_time_a == gols_time_b:
    penaltis_time_a = int(input(" Informe o penaltis do timer A: "))
    penaltis_time_b = int(input(" Informe o penaltis do timer B: "))

if gols_time_c == gols_time_d:
    penaltis_time_c = int(input(" Informe o penaltis do time C: "))
    penaltis_time_d = int(input(" Informe o penaltis do timer D: ")) 

    #Definido o vencedor
    vencedor1 = None #inicializar com None
    vencedor2 = None

    #Analizando o resultado
    if gols_time_a > gols_time_b:
        vencedor1 = "Time A"

    elif gols_time_b > gols_time_a:
     vencedor1 = "Time B"

    else: # Empate no tempo normal
     if penaltis_time_a > penaltis_time_b:
        vencedor1 = "Time A"

    if gols_time_c > gols_time_d:
     vencedor2 = "Time C"

    elif gols_time_d > gols_time_c:
     vencedor2 = "Time D"

    else:  # Empate no tempo normal
     if penaltis_time_c > penaltis_time_d:
        vencedor2 = "Time C"

     elif penaltis_time_d > penaltis_time_c:
        vencedor2 = "Time D"

        # Mensagem Final com os Vencedores
    if vencedor1 is not None and vencedor2 is not None:
     print(f"Os times {vencedor1} e {vencedor2} estão na grande final!")
    else:
     print("Erro: Não foi possível determinar os vencedores. Verifique os dados inseridos.")
