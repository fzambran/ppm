def main():
    lista = [11, 13, 5, 12, 8]

    print('Lista original: ', lista)
    print('\n')
    insertion_sort(lista)
    print('Lista ordenada: ', lista)    

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key
        
main()