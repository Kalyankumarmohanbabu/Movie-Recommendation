import streamlit as st
import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer

# Load the data and model
with open('D:\\Movie Recommendation\\movies_list.pkl', 'rb') as f:
    new_data = pickle.load(f)
with open('D:\\Movie Recommendation\\nearest_neighbors.pkl', 'rb') as f:
    nn = pickle.load(f)
with open('D:\\Movie Recommendation\\count_vectorizer.pkl', 'rb') as f:
    cv = pickle.load(f)
with open('D:\\Movie Recommendation\\vector.pkl', 'rb') as f:
    vector = pickle.load(f)

# Function to recommend movies
def recommend(movie_title):
    # Case insensitive search for the movie title
    movie_title = movie_title.lower()
    titles = new_data['title'].str.lower()

    if movie_title not in titles.values:
        return [("Movie not found in the dataset.", "")]

    index = titles[titles == movie_title].index[0]
    distances, indices = nn.kneighbors([vector[index]], n_neighbors=6)
    recommendations = [(new_data.iloc[i].title, '') for i in indices[0] if i != index]  # Skip the first movie (itself)
    return recommendations

# Streamlit app
st.title('Movie Recommendation System')

movie_list = new_data['title'].values
selected_movie = st.selectbox('Select a movie:', movie_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.write('Recommended movies:')
    for title, image_url in recommendations:
        st.write(f"**{title}**")
        if image_url:
            st.image(image_url, use_column_width=True)
