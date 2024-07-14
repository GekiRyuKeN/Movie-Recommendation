import pickle
import streamlit as st
import requests
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import gdown

file_id = '1Mto4Lh6bQzLl76c3KO3B5w8slGVlHb3o'
url = f'https://drive.google.com/uc?id={file_id}'
destination = 'similarity.pkl'

if not os.path.exists(destination):
    # Download the file if it doesn't exist
    gdown.download(url, destination, quiet=False)
# Setting the Page Configuration
img = Image.open('./images/favicon.png')
st.set_page_config(page_title='Movie Recommender Engine', page_icon=img, layout="centered", initial_sidebar_state="expanded")

# Function to fetch movie posters
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit app header with image
col1, col2 = st.columns([3, 4])
with col1:
    st.markdown(
        """
        <h1 style='text-align: center; color:#A0CFD3; font-family: Monospace;'>Movie Recommender System</h1>
        """
        , unsafe_allow_html=True)
with col2:
    st.image('./images/index2.jpg', width=400)

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# About section
st.header('About Movie Recommender System')
st.markdown("""
Recommendation systems are used to predict the preferences or ratings that a user would give to a product. There are several types of recommendation systems, each serving different purposes:

1. **Collaborative Filtering**:
   - Collaborative filtering methods are based on collecting and analyzing information on user behaviors, activities, or preferences and predicting what users will like based on their similarity to other users.
   - ![Collaborative Filtering](https://miro.medium.com/v2/resize:fit:828/format:webp/1*Z8p9PAqx2dFfEn76B6juAw.png)

2. **Content-Based Filtering**:
   - Content-based filtering recommends items based on a comparison between the content of the items and a user profile.
   - ![Content-Based Filtering](https://cdn.sanity.io/images/oaglaatp/production/a2fc251dcb1ad9ce9b8a82b182c6186d5caba036-1200x800.png?w=1200&h=800&auto=format)

3. **Hybrid Recommender Systems**:
   - Hybrid recommender systems combine multiple recommendation techniques to overcome the limitations of individual methods and provide more accurate recommendations.
   - ![Hybrid Recommender Systems](https://editor.analyticsvidhya.com/uploads/18877873191_5z9o9XrN8QCkcVMYwxPHEQ.png)

4. **Matrix Factorization**:
   - Matrix factorization methods decompose user-item interaction matrices into lower-dimensional matrices and use them to predict missing values.
   - ![Matrix Factorization](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*b4M7o7W8bfRRxdMxtFoVBQ.png)

5. **Context-Aware Recommendation**:
   - Context-aware recommendation systems take into account various contextual information such as time, location, and device to provide more personalized recommendations.
   - ![Context-Aware Recommendation](https://pub.mdpi-res.com/applsci/applsci-07-01211/article_deploy/html/images/applsci-07-01211-g008.png?1569707004)

### How It Works:
- Select a movie from the dropdown list or type its name.
- Click on "Show Recommendation" to see similar movies based on the selected movie.


### Accuracy Metrics:
- **Correlation Matrix:**
""")
st.image("images/Corelation.jpeg", caption="Correlation Matrix")


# Dropdown for selecting a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(
            f"""
            <div style='background-color:#a873b0; padding:10px; text-align:center; border-radius:8px;'>
                {recommended_movie_names[0]}
                <br>
                <img src="{recommended_movie_posters[0]}" alt="{recommended_movie_names[0]}" style="width:100%; border-radius:8px;">
            </div>
            """
            , unsafe_allow_html=True)
    with col2:
        st.markdown(
            f"""
            <div style='background-color:#a873b0; padding:10px; text-align:center; border-radius:8px;'>
                {recommended_movie_names[1]}
                <br>
                <img src="{recommended_movie_posters[1]}" alt="{recommended_movie_names[1]}" style="width:100%; border-radius:8px;">
            </div>
            """
            , unsafe_allow_html=True)
    with col3:
        st.markdown(
            f"""
            <div style='background-color:#a873b0; padding:10px; text-align:center; border-radius:8px;'>
                {recommended_movie_names[2]}
                <br>
                <img src="{recommended_movie_posters[2]}" alt="{recommended_movie_names[2]}" style="width:100%; border-radius:8px;">
            </div>
            """
            , unsafe_allow_html=True)
    with col4:
        st.markdown(
            f"""
            <div style='background-color:#a873b0; padding:10px; text-align:center; border-radius:8px;'>
                {recommended_movie_names[3]}
                <br>
                <img src="{recommended_movie_posters[3]}" alt="{recommended_movie_names[3]}" style="width:100%; border-radius:8px;">
            </div>
            """
            , unsafe_allow_html=True)
    with col5:
        st.markdown(
            f"""
            <div style='background-color:#a873b0; padding:10px; text-align:center; border-radius:8px;'>
                {recommended_movie_names[4]}
                <br>
                <img src="{recommended_movie_posters[4]}" alt="{recommended_movie_names[4]}" style="width:100%; border-radius:8px;">
            </div>
            """
            , unsafe_allow_html=True)
