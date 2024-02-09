from collections import defaultdict

def processar_dataset(emd):
    # Abrir o arquivo para leitura
    
    with open(emd, 'r') as arquivo:
        # Ignorar a primeira linha (cabeçalho)
        next(arquivo)
        linhas = arquivo.readlines()
        
    # Inicializar estruturas de dados para armazenar as informações
    modalidades = set() #conjunto de modalidades onde não aparecem repetições
    total_atletas = 0
    aptos = 0
    inaptos = 0
    distribuicao_idade = defaultdict(int)

    # Processar cada linha do arquivo
    for linha in linhas:
        # Dividir a linha em partes usando a vírgula como delimitador
        partes = linha.strip().split(',')
        nome = partes[3] + ' ' + partes[4]
        idade = int(partes[5])
        modalidade = partes[8]
        aptidao = partes[12]

        # Atualizar a lista de modalidades
        modalidades.add(modalidade)

        # Atualizar contadores de aptidão
        if aptidao == 'true':
            aptos += 1
        elif aptidao == 'false':
            inaptos += 1

        # Atualizar distribuição de idade
        faixa_etaria = idade // 5 * 5  # Calcula o intervalo de 5 anos
        distribuicao_idade[faixa_etaria] += 1 

        total_atletas += 1

    # Ordenar a lista de modalidades alfabeticamente
    modalidades_ordenadas = sorted(modalidades)

    # Calcular percentagens de aptidão
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = (inaptos / total_atletas) * 100

    # Exibir resultados
    print("Lista ordenada alfabeticamente das modalidades desportivas:")
    for modalidade in modalidades_ordenadas:
        print(modalidade)
    
    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print("Aptos: {:.2f}%".format(percentagem_aptos))
    print("Inaptos: {:.2f}%".format(percentagem_inaptos))
    
    print("\nDistribuição de atletas por escalão etário:")
    for faixa_etaria, quantidade in sorted(distribuicao_idade.items()):
        print("[{}-{}]: {}".format(faixa_etaria, faixa_etaria + 4, quantidade))

# Chamada da função para processar o dataset
processar_dataset('emd.csv')  # Substitua 'dataset.txt' pelo nome do seu arquivo de dados
