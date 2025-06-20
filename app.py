import pickle
import streamlit as st
import requests

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    poster_path = data.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Image"

def recommend_movies(movie_title: str, movies_df, similarity_matrix, num_recommendations=5):
    try:
        idx = movies_df[movies_df['title'] == movie_title].index[0]
    except IndexError:
        return [], []

    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended_titles = []
    recommended_posters = []

    for i, _ in similarity_scores[1:num_recommendations+1]:
        movie_id = movies_df.iloc[i]['movie_id']
        recommended_titles.append(movies_df.iloc[i]['title'])
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters

def main():
    st.set_page_config(page_title="Movie Recommender", layout="wide")

    st.markdown(
        """
        <style>
        body {
            background-color: #e6dbf2;
            color: black;
        }
        .stApp {
            background-color: #e6dbf2;
        }
        h1 {
            color: white !important;
            background-color: #a084ca;
            padding: 20px;
            border-radius: 10px;
        }
        .stSidebar > div:first-child {
            background-color: #f0e6ff;
            padding: 20px;
        }
        .about-header {
            color: black !important;
            font-size: 22px;
            font-weight: bold;
        }
        .movie-sticker {
            position: fixed;
            top: 10px;
            right: 10px;
            width: 80px;
            z-index: 999;
        }
        </style>
        <img src="https://cdn-icons-png.flaticon.com/512/744/744465.png" class="movie-sticker">
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
    st.markdown("> *“Cinema is a mirror by which we often see ourselves.”* – Alejandro González Iñárritu")
    st.markdown("---")

    
    st.sidebar.markdown('<div class="about-header">👩‍💻 About Me</div>', unsafe_allow_html=True)
    st.sidebar.write("""
        Sara Oraib, strong passion for data-driven problem solving.  
        My expertise lies in data analysis, machine learning, deep learning, and natural language processing (NLP).  
        I enjoy turning raw data into actionable insights and building intelligent systems that learn and adapt.
    """)


    st.sidebar.markdown('<div class="about-header">📱 Connect With Me</div>', unsafe_allow_html=True)
    st.sidebar.markdown("""
    [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/sara.oraib)  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sara-oraib)  
    [![Facebook](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/saraoraib6)
    """)

    
    movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

    movie_titles = movies['title'].values
    selected_movie = st.selectbox("🎥 Type or select a movie:", movie_titles)

    if st.button("🎯 Show Recommendations"):
        names, posters = recommend_movies(selected_movie, movies, similarity)
        if names:
            st.subheader("✨ Recommended Movies")
            cols = st.columns(len(names))
            for col, name, poster in zip(cols, names, posters):
                col.image(poster, use_column_width=True)
                col.caption(name)
        else:
            st.warning("No recommendations found. Please try a different movie.")

if __name__ == "__main__":
    main()
