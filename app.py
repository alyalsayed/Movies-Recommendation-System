import streamlit as st
import pickle
import pandas
from utils import fetch_poster, recommend, improved_recommendations

st.header('Movie Recommender System Using Machine Learning')
# Load movies_df
with open('src/movies_df.pkl', 'rb') as f:
    movies = pickle.load(f)

# Load cosine_sim
with open('src/cosine_sim.pkl', 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie,movies,similarity)
    num_cols = 5
    num_recommendations = 10

    col_list = st.columns(num_cols)

    for i in range(num_recommendations):
        col_index = i % num_cols
        with col_list[col_index]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])

if st.button('Show Improved Recommendations'):
    recommendations = improved_recommendations(selected_movie,movies,similarity)
    
    if recommendations is not None:
        recommended_movie_ids = recommendations['id'].tolist()
        recommended_movie_names = recommendations['title'].tolist()
        recommended_movie_posters = []
        
        for movie_id in recommended_movie_ids:
            recommended_movie_posters.append(fetch_poster(movie_id))

        num_recommendations = len(recommended_movie_ids)
        num_cols = 5
        
        # Calculate the number of rows needed
        num_rows = (num_recommendations + num_cols - 1) // num_cols

        for row in range(num_rows):
            col_list = st.columns(num_cols)
            start_index = row * num_cols
            end_index = min((row + 1) * num_cols, num_recommendations)
            
            for i in range(start_index, end_index):
                with col_list[i - start_index]:
                    st.text(recommended_movie_names[i])
                    st.image(recommended_movie_posters[i])
