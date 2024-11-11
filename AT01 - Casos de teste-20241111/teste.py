import time
import random

# Função para geração do vetor conforme o tipo de ordenação
def gerar_vetor(tamanho, tipo):
    if tipo == 'c':
        return list(range(1, tamanho + 1))
    elif tipo == 'd':
        return list(range(tamanho, 0, -1))
    elif tipo == 'r':
        return [random.randint(0, 32000) for _ in range(tamanho)]

# Funções de ordenação com contagem de comparações
def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1 if j >= 0 else 0
        arr[j + 1] = key
    return arr, comparisons

def selection_sort(arr):
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons

def bubble_sort(arr):
    comparisons = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons

def merge_sort(arr):
    comparisons = [0]  # Usando lista para mutabilidade

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr, comparisons[0]
    mid = len(arr) // 2
    left, _ = merge_sort(arr[:mid])
    right, _ = merge_sort(arr[mid:])
    return merge(left, right), comparisons[0]

def quick_sort(arr):
    comparisons = [0]  # Usando lista para mutabilidade

    def _quick_sort(items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        comparisons[0] += len(items) - 1
        return _quick_sort(left) + middle + _quick_sort(right)

    return _quick_sort(arr), comparisons[0]

def heap_sort(arr):
    comparisons = [0]  # Usando lista para mutabilidade

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest] < arr[left]:
            largest = left
            comparisons[0] += 1
        if right < n and arr[largest] < arr[right]:
            largest = right
            comparisons[0] += 1
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr, comparisons[0]

# Função para executar e medir o tempo e comparações dos métodos de ordenação
def executar_ordenacoes(vetor):
    metodos = {
        'insertionSort': insertion_sort,
        'selectionSort': selection_sort,
        'bubbleSort': bubble_sort,
        'mergeSort': merge_sort,
        'quickSort': quick_sort,
        'heapSort': heap_sort
    }
    
    resultados = []
    for nome, func in metodos.items():
        vetor_copia = vetor.copy()
        inicio = time.time()
        ordenado, comparacoes = func(vetor_copia)
        tempo = (time.time() - inicio) * 1000  # Tempo em milissegundos
        resultados.append((nome, ordenado, comparacoes, tempo))
    
    return resultados

# Função principal para ler o arquivo de entrada, executar as ordenações e salvar o resultado
def main(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as f:
        tamanho = int(f.readline().strip())
        tipo = f.readline().strip()
    
    vetor = gerar_vetor(tamanho, tipo)
    resultados = executar_ordenacoes(vetor)
    
    with open(arquivo_saida, 'w') as f:
        for nome, ordenado, comparacoes, tempo in resultados:
            f.write(f"{nome}: {' '.join(map(str, ordenado))}, {comparacoes} comp, {tempo:.2f} ms\n")



