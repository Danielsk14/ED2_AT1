import random
import time
import sys

#cria um vetor com base no tamanho e no tipo escolhido pelo usuário.
def gerar_vetor(tamanho, tipo_geracao):
    #Aqui verifico se o tamanho é negativo. Não faz sentido criar um vetor assim, então paro.
    if tamanho < 0:
        print("Erro: O tamanho do vetor não pode ser negativo.")
        return None

    #Agora verifico o tipo do vetor que o usuário quer.
    if tipo_geracao == 'c':  #Se for 'c', significa que o vetor deve ser crescente.
        return list(range(1, tamanho + 1))  #Gero uma lista de números de 1 até o tamanho desejado.
    elif tipo_geracao == 'd':  #Se for 'd', o vetor deve ser decrescente.
        return list(range(tamanho, 0, -1))  #Uso range invertido para gerar do maior para o menor.
    elif tipo_geracao == 'r':  #Se for 'r', o vetor é aleatório.
        return [random.randint(0, 32000) for contador in range(tamanho)]  #Uso randint para números aleatórios.
    else:
        #Se o tipo for inválido, mostro um erro para ajudar o usuário.
        print("Erro: Tipo de geração inválido. Use 'c', 'd' ou 'r'.")
        return None

#Insertion Sort
#O Insertion Sort funciona como organizar cartas na mão: começamos com o primeiro elemento "ordenado"
#e, a cada passo, inserimos o próximo elemento na posição correta dentro da parte já ordenada.
def insertion_sort(vetor):
    comparacoes = 0  #Usado para contar quantas comparações o algoritmo faz.
    for i in range(1, len(vetor)):  #Percorro o vetor a partir do segundo elemento.
        chave = vetor[i]  #Elemento que quero posicionar corretamente.
        j = i - 1  #Começo comparando com o elemento anterior.
        while j >= 0 and vetor[j] > chave:  #Se o elemento anterior for maior, movo ele para frente.
            vetor[j + 1] = vetor[j]
            j -= 1
            comparacoes += 1  #Conto cada comparação feita.
        vetor[j + 1] = chave  #Coloco a chave na posição correta.
    return vetor, comparacoes  #Retorno o vetor ordenado e o total de comparações.

#Complexidade:
#Melhor caso: O(n) (vetor já ordenado).
#Pior caso: O(n^2) (vetor em ordem reversa).


#Selection Sort
#O Selection Sort encontra o menor elemento no vetor e o coloca na primeira posição.
#Depois encontra o próximo menor e o coloca na segunda posição, e assim por diante.
def selection_sort(vetor):
    comparacoes = 0  #Usado para contar comparações.
    for i in range(len(vetor)):  #Para cada posição no vetor:
        indice_minimo = i  #Assumo que o menor elemento está na posição atual.
        for j in range(i + 1, len(vetor)):  #Procuro o menor elemento no restante do vetor.
            comparacoes += 1  #Registro cada comparação feita.
            if vetor[j] < vetor[indice_minimo]:  #Se encontro um menor, atualizo o índice.
                indice_minimo = j
        #Troco o menor elemento encontrado com o elemento atual.
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]
    return vetor, comparacoes  #Retorno o vetor ordenado e o número de comparações.

#Complexidade:
#Melhor caso e pior caso: O(n^2).
#Isso acontece porque o algoritmo sempre percorre todo o vetor para encontrar o menor elemento.


#Bubble Sort
#Ele percorre o vetor repetidamente, comparando pares de elementos adjacentes e trocando-os se estiverem fora de ordem.
def bubble_sort(vetor):
    comparacoes = 0  #Usado para contar quantas comparações são feitas.
    n = len(vetor)  #Tamanho do vetor.
    for i in range(n):  #Faço n passagens no vetor.
        for j in range(0, n - i - 1):  #Comparo apenas até os elementos ainda não ordenados.
            comparacoes += 1
            if vetor[j] > vetor[j + 1]:  #Se estiverem fora de ordem, troco os dois elementos.
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor, comparacoes  #Retorno o vetor ordenado e o número de comparações.

#Complexidade:
#Melhor caso: O(n) (vetor já ordenado).
#Pior caso: O(n^2).

#Merge Sort
#O Merge Sort é um algoritmo baseado no conceito de "dividir e conquistar".
#Ele divide o vetor em dois subvetores menores, ordena cada um recursivamente e, depois, intercala os dois subvetores.
def merge_sort(vetor):
    comparacoes = [0]  #Lista para contar comparações (é mutável, então pode ser alterada internamente).

    #Função auxiliar para intercalar dois subvetores ordenados.
    def intercalar(esquerda, direita):
        resultado = []  #Lista onde armazeno os elementos intercalados.
        i = j = 0  #Índices para percorrer os subvetores.
        while i < len(esquerda) and j < len(direita):  #Enquanto houver elementos em ambos os subvetores:
            comparacoes[0] += 1  #Cada comparação entre elementos é contada aqui.
            if esquerda[i] < direita[j]:  #Se o elemento da esquerda for menor, adiciono ele.
                resultado.append(esquerda[i])
                i += 1
            else:  #Caso contrário, adiciono o elemento da direita.
                resultado.append(direita[j])
                j += 1
        #Adiciono os elementos restantes de cada subvetor (se houver).
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    if len(vetor) <= 1:  #Se o vetor tem apenas um elemento, já está ordenado.
        return vetor, comparacoes[0]
    meio = len(vetor) // 2  #Divido o vetor ao meio.
    esquerda, _ = merge_sort(vetor[:meio])  #Ordeno recursivamente a primeira metade.
    direita, _ = merge_sort(vetor[meio:])  #Ordeno recursivamente a segunda metade.
    vetor_ordenado = intercalar(esquerda, direita)  #Intercalo as duas metades ordenadas.
    return vetor_ordenado, comparacoes[0]  #Retorno o vetor ordenado e o total de comparações.

#Complexidade:
#Melhor caso e pior caso: O(n log n).


#Quick Sort
#O Quick Sort é outro algoritmo de "dividir e conquistar".
#Ele escolhe um elemento como pivô e particiona o vetor em torno desse pivô.
#Os elementos menores que o pivô ficam à esquerda, e os maiores ficam à direita.
def quick_sort(vetor):
    comparacoes = [0]  #Lista para contar comparações.

    #Função auxiliar que particiona o vetor em torno do pivô.
    def particionar(baixo, alto):
        pivo = vetor[alto]  #Escolho o último elemento como pivô.
        i = baixo - 1  #i separa os elementos menores que o pivô dos maiores.
        for j in range(baixo, alto):  #Percorro o vetor de baixo até alto-1.
            comparacoes[0] += 1  #Cada comparação entre elementos é contada aqui.
            if vetor[j] < pivo:  #Se o elemento for menor que o pivô:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]  #Troco os elementos para manter a divisão.
        vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]  #Coloco o pivô na posição correta.
        return i + 1  #Retorno o índice onde o pivô foi colocado.

    #Função recursiva para aplicar o Quick Sort.
    def quick_sort_recursivo(baixo, alto):
        if baixo < alto:  #Condição de parada: vetor com um único elemento já está ordenado.
            pi = particionar(baixo, alto)  #Particiono o vetor e obtenho a posição do pivô.
            quick_sort_recursivo(baixo, pi - 1)  #Ordeno os elementos antes do pivô.
            quick_sort_recursivo(pi + 1, alto)  #Ordeno os elementos depois do pivô.

    quick_sort_recursivo(0, len(vetor) - 1)  #Chamada inicial.
    return vetor, comparacoes[0]  #Retorno o vetor ordenado e o total de comparações.

#Complexidade:
#Melhor caso: O(n log n).
#Pior caso: O(n^2)


#Heap Sort
def heap_sort(vetor):
    comparacoes = 0  #Usado para contar comparações.

    #Função auxiliar para ajustar a estrutura do heap.
    def aux_heap(n, i, comparacoes):
        maior = i  #Assumo que a raiz (índice `i`) é o maior elemento.
        esquerda = 2 * i + 1  #Índice do filho esquerdo.
        direita = 2 * i + 2  #Índice do filho direito.

        #Verifico se o filho esquerdo existe e é maior que a raiz.
        if esquerda < n and vetor[i] < vetor[esquerda]:
            maior = esquerda
            comparacoes += 1

        #Verifico se o filho direito existe e é maior que o maior atual.
        if direita < n and vetor[maior] < vetor[direita]:
            maior = direita
            comparacoes += 1

        #Se o maior elemento não é a raiz, troco e ajusto o heap recursivamente.
        if maior != i:
            vetor[i], vetor[maior] = vetor[maior], vetor[i]
            comparacoes = aux_heap(n, maior, comparacoes)
        return comparacoes

    n = len(vetor)
    for i in range(n // 2 - 1, -1, -1):  #Construo o heap.
        comparacoes = aux_heap(n, i, comparacoes)
    for i in range(n - 1, 0, -1):  #Extraio os elementos do heap, um por um.
        vetor[i], vetor[0] = vetor[0], vetor[i]
        comparacoes = aux_heap(i, 0, comparacoes)
    return vetor, comparacoes

#Complexidade:
#Melhor caso e pior caso: O(n log n).

#Counting Sort -  é diferente porque ele não faz comparações.    (Espero que não tenha problema isso '-')
def counting_sort(vetor):
    if not vetor:  #Se o vetor estiver vazio, não preciso fazer nada.
        return vetor, 0

    max_valor = max(vetor)  #Encontro o maior valor no vetor.
    contagem = [0] * (max_valor + 1)  #Crio uma lista para contar a frequência de cada número.

    for num in vetor:  #Conto cada número no vetor.
        contagem[num] += 1

    indice = 0
    for valor, qtd in enumerate(contagem):  #Recrio o vetor com base na contagem.
        for contador in range(qtd):
            vetor[indice] = valor
            indice += 1

    return vetor, 0  #Counting Sort não faz comparações.
#Usa a contagem de frequência, ideal para inteiros em intervalos pequenos.

#executar qualquer algoritmo de ordenação e medir o tempo de execução.
def executar_ordenacao(vetor, algoritmo):
    copia_vetor = vetor.copy()  #Faço uma cópia para preservar o vetor original.
    inicio = time.perf_counter()  #Inicio a medição do tempo.
    if algoritmo == "insertionSort":
        copia_vetor, comparacoes = insertion_sort(copia_vetor)
    elif algoritmo == "selectionSort":
        copia_vetor, comparacoes = selection_sort(copia_vetor)
    elif algoritmo == "bubbleSort":
        copia_vetor, comparacoes = bubble_sort(copia_vetor)
    elif algoritmo == "mergeSort":
        copia_vetor, comparacoes = merge_sort(copia_vetor)
    elif algoritmo == "quickSort":
        copia_vetor, comparacoes = quick_sort(copia_vetor)
    elif algoritmo == "heapSort":
        copia_vetor, comparacoes = heap_sort(copia_vetor)
    elif algoritmo == "countingSort":
        copia_vetor, comparacoes = counting_sort(copia_vetor)
    fim = time.perf_counter()  #Termino a medição do tempo.
    tempo = (fim - inicio) * 1000  #Converto o tempo para milissegundos.
    return copia_vetor, tempo, comparacoes

#processar os arquivos de entrada e saída.
def processar_arquivos(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, "r") as entrada:  #Abro o arquivo de entrada para leitura.
            linhas = entrada.readlines()
            if len(linhas) < 2:
                print("Erro: Arquivo de entrada está vazio ou incompleto.")
                return
            try:
                tamanho = int(linhas[0].strip())
                tipo_geracao = linhas[1].strip()
                if tamanho < 0:
                    print("Erro: O tamanho do vetor não pode ser negativo.")
                    return
                if tipo_geracao not in {'c', 'd', 'r'}:
                    print("Erro: Tipo de geração inválido. Use 'c', 'd' ou 'r'.")
                    return
            except ValueError as ve:
                print("Erro ao processar o arquivo de entrada:", ve)
                return

        vetor = gerar_vetor(tamanho, tipo_geracao)
        if vetor is None:
            return

        algoritmos = ["insertionSort", "selectionSort", "bubbleSort", "mergeSort", "quickSort", "heapSort", "countingSort"]

        with open(arquivo_saida, "w") as saida:  #Abro o arquivo de saída para gravar os resultados.
            for algoritmo in algoritmos:
                vetor_ordenado, tempo, comparacoes = executar_ordenacao(vetor, algoritmo)
                saida.write(f"{algoritmo}: {vetor_ordenado}\n")
                saida.write(f"Comparações: {comparacoes}, Tempo: {tempo:.2f} ms\n\n")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#Verifico se os argumentos foram passados corretamente.
if len(sys.argv) != 3:
    print("Uso correto: python nome_do_programa.py [arquivo de entrada] [arquivo de saída]")
else:
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    processar_arquivos(arquivo_entrada, arquivo_saida)
    print("Processamento concluído! Resultados salvos no arquivo de saída.")