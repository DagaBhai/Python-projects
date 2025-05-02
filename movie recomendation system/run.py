import streamlit as st
import streamlit.components.v1 as components
import pickle
import requests

movies = pickle.load(open('movie recomendation system/movies_list.pkl', 'rb'))
similarity = pickle.load(open("movie recomendation system/similarity.pkl", 'rb'))
movies_list = movies['title'].values

if 'selected_movie' not in st.session_state:
    st.session_state.selected_movie = movies_list[0]

st.header('Movie Recommendation System')

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=7e4b636e12f4a8277173702840ec1afb&language=en-US'
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

def main():
    imageCarouselComponent = components.declare_component("image-carousel-component", path="movie recommendation system/frontend/public")
    movie_ids = [1632, 299536, 17455, 2830, 429422, 9722, 13972, 240, 155, 598, 914, 255709, 572154]
    imageUrls = [fetch_poster(movie_id) for movie_id in movie_ids]
    clicked_url = imageCarouselComponent(imageUrls=imageUrls, height=200)
    clicked_index = imageUrls.index(clicked_url) if clicked_url in imageUrls else None

    if clicked_index is not None:
        clicked_id = movie_ids[clicked_index]
        clicked_movie_title = movies[movies['id'] == clicked_id]['title'].values[0]
        st.session_state.selected_movie = clicked_movie_title

    movie_selected = st.selectbox(
        'Select the movie',
        movies_list,
        index=movies_list.tolist().index(st.session_state.selected_movie) if st.session_state.selected_movie in movies_list else 0
    )

    if movie_selected != st.session_state.selected_movie:
        st.session_state.selected_movie = movie_selected

    movie_to_recommend = st.session_state.selected_movie

    if st.button("Show Recommend") or clicked_index is not None:
        movie_names, movie_poster = recommend(movie_to_recommend)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(movie_names[0])
            st.image(movie_poster[0])
        with col2:
            st.text(movie_names[1])
            st.image(movie_poster[1])
        with col3:
            st.text(movie_names[2])
            st.image(movie_poster[2])
        with col4:
            st.text(movie_names[3])
            st.image(movie_poster[3])
        with col5:
            st.text(movie_names[4])
            st.image(movie_poster[4])

if __name__ == "__main__":
    main()
