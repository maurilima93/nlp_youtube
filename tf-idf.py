import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        documents = file.readlines()
    return [doc.strip() for doc in documents]

file_path = 'seu_arquivo.txt' 
documents = read_text_from_file(file_path)

# TF-IDF calc
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Transformando a matriz TF-IDF em DataFrame para visualização
feature_names = vectorizer.get_feature_names_out()
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Criando e salvando um heatmap do TF-IDF
plt.figure(figsize=(10, 8))
sns.heatmap(df_tfidf, annot=True, cbar=False, cmap="viridis")
plt.title("TF-IDF Heatmap")
plt.xlabel("Features")
plt.ylabel("Documents")
plt.savefig('tfidf_heatmap.png', format='png', dpi=300)
plt.close()  # Fecha a figura para liberar memória
