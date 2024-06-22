# Movie-Recommendation
This repository contains the code for a Movie Recommendation System. The system recommends movies based on their content using a machine learning model. The recommendation is made using a combination of movie overview and genre information.

Features
* Content-Based Filtering: Recommends movies based on the similarity of their content.
* Interactive UI: Built with Streamlit, allowing users to select movies and get recommendations interactively.
* Pre-trained Model: Utilizes a pre-trained Nearest Neighbors model for quick and efficient recommendations.

Dataset
The dataset used contains the following columns:

* id: Unique identifier for each movie.
* title: Title of the movie.
* genre: Genres associated with the movie.
* original_language: Language in which the movie was originally released.
* overview: A brief summary of the movie.
* popularity: Popularity score of the movie.
* release_date: Release date of the movie.
* vote_average: Average vote score.
* vote_count: Number of votes.

How It Works
* Data Preprocessing: The dataset is preprocessed to create a combined tags column containing both the overview and genres of the movies.
* Vectorization: The tags column is vectorized using CountVectorizer to create a feature matrix.
* Similarity Calculation: Cosine similarity is computed between the feature vectors of the movies.
* Model Training: A Nearest Neighbors model is trained using the similarity matrix.
* Recommendation: For a given movie, the system finds and returns movies with the highest similarity scores.
Setup and Installation
Clone the repository:

bash
1 Copy code
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
Install dependencies:

bash
2 Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
3 Copy code
streamlit run app.py
File Structure
app.py: The main Streamlit app file.
movies_list.pkl: Pickled DataFrame containing movie data.
nearest_neighbors.pkl: Pickled Nearest Neighbors model.
count_vectorizer.pkl: Pickled CountVectorizer model.
vector.pkl: Pickled feature matrix.
requirements.txt: List of dependencies.
Usage
Select a Movie: Choose a movie from the dropdown menu.
Get Recommendations: Click the "Recommend" button to see a list of recommended movies along with their posters.
Contributions
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.

