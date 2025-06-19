# --- 1. Função que retorna números ímpares ---
def filtrar_impares(lista):
    return [num for num in lista if num % 2 != 0]

# --- 2. Função que retorna números primos ---
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if eh_primo(num)]

# --- 3. Elementos presentes apenas em uma das listas ---
def elementos_exclusivos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

# --- 4. Segundo maior valor da lista ---
def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    if len(lista_unica) >= 2:
        return lista_unica[1]
    return None

# --- 5. Ordenar lista de tuplas pelo nome ---
def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda pessoa: pessoa[0].lower())

# --- 6. Identificar e tratar outliers ---
import pandas as pd

def tratar_outliers_desvio(df, coluna):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    limite_inferior = media - 3 * desvio
    limite_superior = media + 3 * desvio
    return df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]

def tratar_outliers_quartil(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]

# --- 7. Concatenar DataFrames ---
def exemplo_concat():
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})
    concat_linhas = pd.concat([df1, df2], axis=0)
    concat_colunas = pd.concat([df1, df2], axis=1)
    return concat_linhas, concat_colunas

# --- 8. Ler CSV e exibir primeiras linhas ---
def ler_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    print(df.head())
    return df

# --- 9. Selecionar coluna e filtrar ---
def filtrar_coluna(df, coluna, condicao):
    return df[df[coluna] > condicao]

# --- 10. Lidar com NaN ---
def lidar_com_nan(df):
    print("Valores ausentes por coluna:")
    print(df.isnull().sum())
    df_sem_nan = df.dropna()
    df_preenchido = df.fillna(0)
    return df_sem_nan, df_preenchido

# --- EXEMPLOS DE USO ---
# Testando funções básicas
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
pessoas = [('Carlos', 30), ('Ana', 25), ('Bruno', 40)]

print("Ímpares:", filtrar_impares(lista_numeros))
print("Primos:", filtrar_primos(lista_numeros))
print("Exclusivos:", elementos_exclusivos(lista1, lista2))
print("Segundo maior:", segundo_maior(lista_numeros))
print("Ordenado por nome:", ordenar_por_nome(pessoas))

# Testando pandas
df_exemplo = pd.DataFrame({'idade': [25, 30, 29, 1000, 27, 26]})
print("\nTratar outliers (desvio padrão):")
print(tratar_outliers_desvio(df_exemplo, 'idade'))

print("\nTratar outliers (quartil):")
print(tratar_outliers_quartil(df_exemplo, 'idade'))

concat_linhas, concat_colunas = exemplo_concat()
print("\nConcat linhas:")
print(concat_linhas)

print("\nConcat colunas:")
print(concat_colunas)
