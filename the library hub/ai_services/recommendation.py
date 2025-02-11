import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, books_df):
        self.books_df = books_df
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(
            self.books_df['keywords'] + ' ' + 
            self.books_df['title'] + ' ' + 
            self.books_df['author']
        )

    def recommend_books(self, book_title, n_recommendations=5):
        idx = self.books_df[self.books_df['title'] == book_title].index[0]
        sim_scores = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()
        top_indices = sim_scores.argsort()[-n_recommendations-1:-1][::-1]
        return self.books_df.iloc[top_indices]
