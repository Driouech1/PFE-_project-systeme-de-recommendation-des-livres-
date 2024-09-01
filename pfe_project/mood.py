import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load the dataset from your desktop
final_df = pd.read_csv('C:/Users/hajar/Desktop/final_df.csv')
data=final_df.sample(10000)

def get_recommendations(title, genre, word2vec_model):
    # Combine title and genre into one text
    text = title + ' ' + genre
    # Tokenize text
    tokens = text.split()
    # Get average vector for tokens
    vectors = [word2vec_model.wv[token] for token in tokens if token in word2vec_model.wv]
    if len(vectors) == 0:
        return None
    avg_vector = sum(vectors) / len(vectors)

    # Calculate cosine similarity with all other books
    similarities = []
    recommended_titles = set()  # Set to store titles of recommended books
    for idx, row in data.iterrows():
        other_vectors = [word2vec_model.wv[token] for token in row['Book-Title'].split() if token in word2vec_model.wv]
        if len(other_vectors) > 0:
            other_avg_vector = sum(other_vectors) / len(other_vectors)
            similarity = cosine_similarity([avg_vector], [other_avg_vector])[0][0]
            similarities.append((row, similarity))

    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Get top 10 unique recommendations
    recommendations = []
    for book, sim in similarities:
        if book['Book-Title'] not in recommended_titles and book['Book-Rating'] > 5:
            recommendations.append(book.to_dict())
            recommended_titles.add(book['Book-Title'])
        if len(recommendations) >= 10:
            break


    return recommendations
