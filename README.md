# Movies Recommendation System

A movie recommendation web app built with Python and Streamlit. It recommends movies based on similarity scores and displays posters using the TMDB API. The app includes both a standard recommendation view and an improved recommendation model that ranks results using a weighted rating strategy.

## Demo

- Hugging Face Space: https://huggingface.co/spaces/alyalsayed/movie_recommendation_system
- Kaggle Notebook: https://www.kaggle.com/code/alyalsayed/movies-recommender-system-with-deployment

## Features

- Movie search and selection from a large movie dataset
- Cosine similarity-based recommendations
- Improved recommendation filtering using vote count and vote average
- Poster fetching from TMDB
- Interactive UI powered by Streamlit
- Easy setup with a requirements file

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- Python-dotenv
- TMDB API

## Project Structure

```text
Movies-Recommendation-System/
├── app.py
├── utils.py
├── requirements.txt
├── .gitignore
├── .gitattributes
├── src/
│   ├── movies_df.pkl
│   └── cosine_sim.pkl
├── Notebooks/
└── README.md
```

## How It Works

1. The app loads a precomputed movie dataset and cosine similarity matrix from `src/`.
2. A user selects a movie from the dropdown.
3. The system computes similar movies and returns the top recommendations.
4. The app fetches each movie poster from TMDB and displays it in the UI.
5. An improved recommendation option applies a weighted rating formula to prioritize popular and highly rated movies.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/alyalsayed/Movies-Recommendation-System.git
cd Movies-Recommendation-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure TMDB API key

Create a `.env` file in the project root and add your TMDB API key:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

You can get a free API key from: https://www.themoviedb.org/settings/api

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## Usage

- Select a movie from the dropdown.
- Click `Show Recommendation` to view the top related movies.
- Click `Show Improved Recommendations` to see refined recommendations using a weighted-score approach.

## Notes

- The app depends on the precomputed pickle files in `src/` to avoid rebuilding the recommendation model each time.
- Movie poster images require a valid TMDB API key.
- If no TMDB key is configured, poster retrieval may fail or return empty results.

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## Author

Aly Alsayed
