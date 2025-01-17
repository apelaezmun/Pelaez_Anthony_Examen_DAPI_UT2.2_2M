def OrdenarLista(lista):
    lista = nums.sort()
    with open('ListaOrdenada.txt', 'w') as file:
        file.write(nums)
    return 

nums = [1, 3, 5, 2, 4]
print(OrdenarLista(nums))