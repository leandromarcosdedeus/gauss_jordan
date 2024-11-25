#exemplo gpt
import numpy as np

def gauss_jordan(mat):
    """
    Aplica o método de Gauss-Jordan e imprime cada passo da redução.
    
    Args:
        mat (numpy.ndarray): Matriz aumentada do sistema de equações.
        
    Returns:
        numpy.ndarray: Matriz resultante após a redução.
    """
    # Obtendo as dimensões da matriz
    rows, cols = mat.shape

    print("Matriz inicial:")
    print(mat)
    print("-" * 50)
    
    # Loop para cada linha
    for i in range(rows):
        # Verifica se o pivô é zero e troca as linhas se necessário
        if mat[i, i] == 0:
            for k in range(i + 1, rows):
                if mat[k, i] != 0:
                    mat[[i, k]] = mat[[k, i]]  # Troca as linhas
                    print(f"Troca de linha {i+1} com linha {k+1}:")
                    print(mat)
                    print("-" * 50)
                    break

        # Normaliza o pivô para 1
        pivot = mat[i, i]
        if pivot != 0:
            mat[i] = mat[i] / pivot
            print(f"Normalizando linha {i+1} (dividindo por {pivot}):")
            print(mat)
            print("-" * 50)

        # Elimina os elementos acima e abaixo do pivô
        for j in range(rows):
            if j != i:
                factor = mat[j, i]
                mat[j] -= factor * mat[i]
                print(f"Eliminando elemento na posição ({j+1},{i+1}) usando linha {i+1}:")
                print(mat)
                print("-" * 50)

    return mat

# Exemplo de uso
# Matriz aumentada (sistema de equações: Ax = b)
A = np.array([
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
], dtype=float)

resultado = gauss_jordan(A)

# Resultado final
print("Matriz escalonada reduzida:")
print(resultado)

# Soluções do sistema
solucoes = resultado[:, -1]
print("Soluções do sistema:")
print(solucoes)
