![Image](https://github.com/user-attachments/assets/498f818b-2103-46f1-8d63-7738f5baad27)
# 🎬Movie Recommender System
A content-based movie recommendation system designed to suggest movies similar to a user’s choice by analyzing multiple facets of movie data, including plot overviews, genres, keywords, cast, and crew. This system leverages natural language processing techniques, vectorization, and cosine similarity to find meaningful connections between movies.

## How it works
Combines movie data: merges two datasets — one with movie info and another with cast and crew details.

Processes text:  cleans and prepares the movie descriptions, genres, cast, and keywords by breaking them down into meaningful parts and simplifying words.

Builds a ‘tags’ field: All important movie details are combined into one searchable text field.

Turns text into numbers: Using a technique vectorization, it converts this text into numbers so the computer can compare movies.

Finds similarities: measures how alike movies are by calculating the similarity between these number vectors.

Recommends movies: When you pick a movie, it shows the top movies most similar to it.

Shows movie posters:fetches posters from The Movie Database (TMDb) API to make recommendations more visual and engaging.

Interactive app: The whole system runs in a clean, easy-to-use web app built with Streamlit.

