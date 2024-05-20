from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Função para ler o conteúdo do arquivo .txt
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()  # Ler todo o conteúdo do arquivo como um único texto
    return text

# Lendo texto de um arquivo .txt
file_path = 'seu_arquivo.txt'  # Substitua pelo caminho correto do arquivo
text = read_text_from_file(file_path)

# Gerando a WordCloud
wordcloud = WordCloud(width=800, height=400).generate(text)

# Configurações de exibição
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# Salvar a imagem no diretório local
plt.savefig('wordcloud.png', format='png')
plt.close()  # Fecha a figura para evitar consumo de memória
