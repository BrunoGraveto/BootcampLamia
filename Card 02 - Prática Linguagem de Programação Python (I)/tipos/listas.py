# Criando as listas
nums = [1, 2, 3]
print("Tipo: " + str(type(nums)))

# Adicionando
nums.append(3)
nums.append(4)
nums.append(5)
print('Tamanho da lista: ' + str(len(nums)))

# Alterando
nums[3] = 100

# Inserindo em algum index
nums.insert(0, -1)

# Imprimindo
print("Lista:" + str(nums))

print(f"Ultimo: {nums[6]}") 
print(f"Ultimo: {nums[-1]}") 
print(f"Antepenultimo: {nums[-2]}") 