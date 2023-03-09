import string
from collections import Counter

def analisar_texto(arquivo):
    # Abre o arquivo especificado
    with open(arquivo, 'r') as f:
        texto = f.read().lower() # Lê o conteúdo do arquivo em minúsculas
    
    # Remove pontuações e quebras de linha do texto
    for c in string.punctuation + '\n':
        texto = texto.replace(c, ' ')
    
    # Divide o texto em palavras e conta o número total de palavras
    palavras = texto.split()
    num_palavras = len(palavras)
    
    # Divide o texto em frases e conta o número total de frases
    frases = texto.split('.')
    num_frases = len(frases)
    
    # Conta o número de ocorrências de cada palavra e identifica as palavras mais frequentes
    contagem_palavras = Counter(palavras)
    palavras_freq = contagem_palavras.most_common(5) # Retorna as 5 palavras mais frequentes
    
    # Imprime as informações obtidas
    print(f"O texto contém {num_palavras} palavras e {num_frases} frases.")
    print("As palavras mais frequentes são:")
    for palavra, frequencia in palavras_freq:
        print(f"{palavra}: {frequencia}")

# Chama a função analisar_texto passando o nome do arquivo
analisar_texto('arquivo.txt')
